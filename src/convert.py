import glob
import os
import shutil

import numpy as np
import supervisely as sly
from cv2 import connectedComponents
from dataset_tools.convert import unpack_if_archive
from supervisely.io.fs import (
    file_exists,
    get_file_ext,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
)
from tqdm import tqdm

import src.settings as s


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # Possible structure for bbox case. Feel free to modify as you needs.

    dataset_path = "/home/alex/DATASETS/IMAGES/RGBD-SOD"
    images_folder = "RGB"
    masks_folder = "GT"
    depth_folder = "depths"
    batch_size = 30
    group_tag_name = "im_id"
    mask_ext = ".png"

    def create_ann(image_path):
        labels = []

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        if ds_name == "train":
            subfolder_value = "COME-8K"
        else:
            subfolder_value = image_path.split("/")[-3]

        im_id_value = get_file_name(image_path)
        if ds_name == "test":
            im_id_value = subfolder_value + "_" + im_id_value
        group_id = sly.Tag(tag_id, value=im_id_value)

        subfolder = sly.Tag(tag_subfolder, value=subfolder_value)

        mask_path = image_path.replace(image_path.split("/")[-2] + "/", masks_folder + "/")
        mask_path = mask_path.replace(get_file_ext(image_path), mask_ext)
        ann_np = sly.imaging.image.read(mask_path)[:, :, 0]
        mask_height = ann_np.shape[0]
        mask_wight = ann_np.shape[1]

        if img_height != mask_height or img_wight != mask_wight:
            return sly.Annotation(img_size=(img_height, img_wight), img_tags=[group_id, subfolder])

        if len(np.unique(ann_np)) > 1:
            obj_mask = ann_np == 255
            curr_bitmap = sly.Bitmap(obj_mask)
            curr_label = sly.Label(curr_bitmap, obj_class)
            labels.append(curr_label)

        return sly.Annotation(
            img_size=(img_height, img_wight), labels=labels, img_tags=[group_id, subfolder]
        )

    obj_class = sly.ObjClass("salient object", sly.Bitmap)
    tag_subfolder = sly.TagMeta("source_dataset", sly.TagValueType.ANY_STRING)
    tag_id = sly.TagMeta(group_tag_name, sly.TagValueType.ANY_STRING)
    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=[obj_class], tag_metas=[tag_subfolder, tag_id])
    api.project.update_meta(project.id, meta.to_json())
    api.project.images_grouping(id=project.id, enable=True, tag_name=group_tag_name)

    for ds_name in os.listdir(dataset_path):
        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

        ds_path = os.path.join(dataset_path, ds_name)

        if ds_name == "train":
            images_pathes = glob.glob(ds_path + "/RGB/*.jpg")
            depths_path = glob.glob(ds_path + "/depths/*.png")
        else:
            images_pathes = glob.glob(ds_path + "/*/RGB/*.jpg")
            depths_path = glob.glob(ds_path + "/*/depths/*.png")

        for curr_images_path in [images_pathes, depths_path]:
            progress = sly.Progress("Create dataset {}".format(ds_name), len(images_pathes))

            for img_pathes_batch in sly.batched(curr_images_path, batch_size=batch_size):
                if ds_name == "train":
                    img_names_batch = [
                        get_file_name_with_ext(im_path) for im_path in img_pathes_batch
                    ]

                else:
                    img_names_batch = [
                        im_path.split("/")[-3] + "_" + get_file_name_with_ext(im_path)
                        for im_path in img_pathes_batch
                    ]

                img_infos = api.image.upload_paths(dataset.id, img_names_batch, img_pathes_batch)
                img_ids = [im_info.id for im_info in img_infos]

                anns = [create_ann(image_path) for image_path in img_pathes_batch]
                api.annotation.upload_anns(img_ids, anns)

                progress.iters_done_report(len(img_names_batch))
