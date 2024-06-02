The authors create the **RGB-D Salient Object Detection Dataset** (RGB-D SOD), which aims to detect and segment objects that visually attract the most human interest from a pair of color and depth images. The dataset lies between Object Detection and Semantic Segmentation. Each sample is a pair of color (RGB) and depth images.

## Salient object detection problem

Salient object detection, mimicking human visual perception to identify the most prominent objects within a scene, has found extensive application across diverse computer vision tasks. With the emergence of depth sensors, capturing depth maps has become more accessible, thereby providing supplementary spatial data that can significantly enhance the accuracy of salient object detection. Despite the development of numerous RGB-D based models for salient object detection boasting promising results in recent years, there persists a gap in understanding the intricacies of these models and the inherent challenges within this field.

Salient object detection serves the purpose of identifying the most visually striking objects within a given scene, playing a pivotal role across a spectrum of real-world applications. These applications span stereo matching, image comprehension, co-saliency detection, action recognition, video segmentation, semantic segmentation, medical imaging, object tracking, person re-identification, camouflaged object detection, and image retrieval, among others. Despite notable advancements in salient object detection in recent years, challenges persist, particularly when confronted with complex backgrounds or fluctuating lighting conditions within scenes. One effective strategy to address these challenges involves leveraging depth maps, which offer supplementary spatial information to conventional RGB images and have become more readily accessible thanks to the widespread availability of depth sensors. Recently, RGB-D based salient object detection has gained increasing attention, and various methods have been developed.

<img src="https://github.com/dataset-ninja/rgbd-sod/assets/120389559/f5bde388-a2eb-49c8-93c2-33d8266cf8db" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">RGB-D based salient object prediction on a sample image using two classical models: DCMC and SE, and seven state-of-the-art deep models: D3 Net, SSF, A2dele, S2 MA, ICNet, JL-DCF, and UC-Net</span>

## Dataset creation

With the rapid development of RGB-D based salient object detection, various datasets have been constructed over the past several years. The authors
summarized nine popular RGB-D datasets.

| No. | Dataset           | Year | Pub.    | Size  | # Obj. Types | Sensor                   | Resolution                |
|-----|-------------------|------|---------|-------|--------------|--------------------------|---------------------------|
| 1   | STERE [139]       | 2012 | CVPR    | 1000  | ∼One         | Internet Stereo camera + sift flow | [251 − 1200] × [222 − 900] |
| 2   | GIT [47]          | 2013 | BMVC    | 80    | Multiple     | Home environment Microsoft Kinect  | 640 × 480                 |
| 3   | DES [49]          | 2014 | ICIMCS  | 135   | One          | Indoor Microsoft Kinect             | 640 × 480                 |
| 4   | NLPR [51]         | 2014 | ECCV    | 1000  | Multiple     | Indoor/outdoor Microsoft Kinect     | 640 × 480, 480 × 640      |
| 5   | LFSD [140]        | 2014 | CVPR    | 100   | One          | Indoor/outdoor Lytro Illum camera  | 360 × 360                 |
| 6   | NJUD [56]         | 2014 | ICIP    | 1985  | ∼One         | Movie/Internet/photo FujiW3 camera + optical flow | [231 − 1213] × [274 − 828] |
| 7   | SSD [85]          | 2017 | ICCVW   | 80    | Multiple     | Movies Sun’s optical flow           | 960 × 1080                |
| 8   | DUT-RGBD [137]    | 2019 | ICCV    | 1200  | Multiple     | Indoor/outdoor —                    | 400 × 600                 |
| 9   | SIP [38]          | 2020 | TNNLS   | 929   | Multiple     | Person in the wild Huawei Mate10    | 992 × 744                 |


* **STERE**. The authors collected 1250 stereo-scopic images from [Flickr](http://www.flickr.com/), [NVIDIA 3D Vision Live](http://photos.3dvisionlive
.com/), and the [Stereoscopic Image Gallery](http://www.stereophotography.com/). The most salient objects in each image were annotated by three users. All annotated images were then sorted based on the overlapping salient regions and the top 1000 images were selected to construct the ﬁnal dataset.
This was the ﬁrst collection of stereoscopic images in this ﬁeld.

* **GIT** consists of 80 color and depth images, collected using a mobile-manipulator robot in a real-world home environment. Each image is annotated
based on pixel-level segmentation of its objects.

* **DES** consists of 135 indoor RGB-D images, taken by Kinect at a resolution of 640 × 640. When collecting this dataset, three users were asked to label the salient object in each image, and overlapping labeled areas were regarded as the ground truth.

* **NLPR** consists of 1000 RGB images and corresponding depth maps, obtained by a standard Microsoft Kinect. This dataset includes a series of outdoor and indoor locations, e.g., offices, supermarkets, campuses, streets, and so on.

* **LFSD** includes 100 light ﬁelds collected using a Lytro light ﬁeld camera, and consists of 60 indoor and 40 outdoor scenes. To label this dataset, three individuals were asked to manually segment salient regions; the segmented results were deemed ground truth when the overlap of the three results was over 90%.

* **NJUD** consists of 1985 stereo image pairs, collected from the Internet, 3D movies, and photographs taken by a Fuji W3 stereo camera.

* **SSD** was constructed using three stereo movies and includes indoor and outdoor scenes. It includes 80 samples; each image has resolution of 960 × 1080.

* **DUT-RGBD** consists of 800 indoor and 400 outdoor scenes with corresponding depth images. This dataset provides several challenging factors: multiple and transparent objects, complex backgrounds, similar foregrounds to backgrounds, and low-intensity environments. 

* **SIP** consists of 929 annotated high-resolution images, with multiple salient persons in each image. In this dataset, depth maps were captured using a smart phone (Huawei Mate10). This dataset covers diverse scenes and various challenging factors, and is annotated with pixel-level ground truth.

<img src="https://github.com/dataset-ninja/rgbd-sod/assets/120389559/1c769e23-3bb7-47f5-b995-97f99b41498e" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">Examples of RGB images, depth maps, and annotations from RGB-D datasets.</span>


