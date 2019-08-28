# pytorch-deep-image-matting
This repository includes the non-official pytorch implementation of [deep image matting](http://openaccess.thecvf.com/content_cvpr_2017/papers/Xu_Deep_Image_Matting_CVPR_2017_paper.pdf).

## Performance
|model       |SAD |MSE  |Grad|Conn| link |
|------------|----|-----|----|----| ---- |
|paper-stage1|54.6|0.017|36.7|55.3|      |
|my-stage1   |57.1|0.017|36.1|58.3|      |
* Training batch=1, images=43100, epochs=12.
* Test maxSize=1600.


## Updates
* 2019.08.24: Fix cv2.dilate and cv2.erode iterations is set default = 1 and set triamp dilate and erode as the test 1k tirmap (k_size:2-5, iterations:5-15). Get [Stage1-SAD=57.1]().
* 2019.07.05: Training with refine stage, fixed encoder-decoder. Get [Stage2-SAD=57.7](https://github.com/huochaitiantang/pytorch-deep-image-matting/releases/download/v1.2/stage2_norm_balance_sad_57.9.pth).
* 2019.06.23: Training with alpha loss and composite loss. Get [Stage1-SAD=58.7](https://github.com/huochaitiantang/pytorch-deep-image-matting/releases/download/v1.2/stage1_norm_balance_sad_58.7.pth).
* 2019.06.17: Training trimap generated by erode as well as dialte to balance the 0 and 1 value. Get [Stage0-SAD=62.0](https://github.com/huochaitiantang/pytorch-deep-image-matting/releases/download/v1.2/stage0_norm_balance_sad_62.0.pth).
* 2019.04.22: Input image is normalized by mean=[0.485, 0.456, 0.406] and std=[0.229, 0.224, 0.225] and fix crop error. Get [Stage0-SAD=69.1](https://github.com/huochaitiantang/pytorch-deep-image-matting/releases/download/v1.1/stage0_norm_e12_sad_69.1.pth).
* 2018.12.14: Initial. Get [Stage0-SAD=72.9](https://github.com/huochaitiantang/pytorch-deep-image-matting/releases/download/v1.0/my_stage0_sad_72.9.pth). 

## Installation
* Python 2.7.12 or 3.6.5
* Pytorch 0.4.0 or 1.0.0
* OpenCV 3.4.3

## Demo
Download our model to the  `./model` and run the following command. Then the predict alpha mattes will locate in the folder `./result/example/pred`.

    python core/demo.py

## Training
### Adobe-Deep-Image-Matting-Dataset
Please concat author for available.
### MSCOCO-2017-Train-Dataset
[Download](http://images.cocodataset.org/zips/train2017.zip)
### PASCAL-VOC-2012 
[Download](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar)
### Composite-Dataset 
Run the following command and the composite training and test dataset will locate in `Combined_Dataset/Training_set/comp` and `Combined_Dataset/Test_set/comp`, `Combined_Dataset` is the extracted folder of Adobe-Deep-Image-Matting-Dataset

    python tools/composite.py

### Pretrained-Model
Run the following command and the pretrained model will locate in `./model/vgg_state_dict.pth`

    python tools/chg_model.py

### Start Training
Run the following command and start the training

    bash train.sh

## Test
Run the following command and start the test of Adobe-1k-Composite-Dataset

    bash deploy.sh

## Evaluation
Plead eval with [official Matlab Code](https://docs.google.com/uc?export=download&id=1euP9WmWve3c7EgOwRqgHfnp2H8NXH3OM). and get the SAD, MSE, Grad Conn.

### Visualization
Running model is Stage1-SAD=57.1, please click to view whole images.

| Image | Trimap | Pred-Alpha | GT-Alpha |
|---|---|---|---|
|![image](https://github.com/huochaitiantang/pytorch-deep-image-matting/blob/master/result/example/image/boy-1518482_1920_12.png) |![image](https://github.com/huochaitiantang/pytorch-deep-image-matting/blob/master/result/example/trimap/boy-1518482_1920_12.png) |![image](https://github.com/huochaitiantang/pytorch-deep-image-matting/blob/master/result/example/pred/boy-1518482_1920_12.png) |![image](https://github.com/huochaitiantang/pytorch-deep-image-matting/blob/master/result/example/alpha/boy-1518482_1920_12.png)
|![image](https://github.com/huochaitiantang/pytorch-deep-image-matting/blob/master/result/example/image/dandelion-1335575_1920_1.png) |![image](https://github.com/huochaitiantang/pytorch-deep-image-matting/blob/master/result/example/trimap/dandelion-1335575_1920_1.png) |![image](https://github.com/huochaitiantang/pytorch-deep-image-matting/blob/master/result/example/pred/dandelion-1335575_1920_1.png) |![image](https://github.com/huochaitiantang/pytorch-deep-image-matting/blob/master/result/example/alpha/dandelion-1335575_1920_1.png)
|![image](https://github.com/huochaitiantang/pytorch-deep-image-matting/blob/master/result/example/image/light-bulb-376930_1920_11.png) |![image](https://github.com/huochaitiantang/pytorch-deep-image-matting/blob/master/result/example/trimap/light-bulb-376930_1920_11.png) |![image](https://github.com/huochaitiantang/pytorch-deep-image-matting/blob/master/result/example/pred/light-bulb-376930_1920_11.png) |![image](https://github.com/huochaitiantang/pytorch-deep-image-matting/blob/master/result/example/alpha/light-bulb-376930_1920_11.png)
|![image](https://github.com/huochaitiantang/pytorch-deep-image-matting/blob/master/result/example/image/sieve-641426_1920_1.png) |![image](https://github.com/huochaitiantang/pytorch-deep-image-matting/blob/master/result/example/trimap/sieve-641426_1920_1.png) |![image](https://github.com/huochaitiantang/pytorch-deep-image-matting/blob/master/result/example/pred/sieve-641426_1920_1.png) |![image](https://github.com/huochaitiantang/pytorch-deep-image-matting/blob/master/result/example/alpha/sieve-641426_1920_1.png)
|![image](https://github.com/huochaitiantang/pytorch-deep-image-matting/blob/master/result/example/image/spring-289527_1920_15.png) |![image](https://github.com/huochaitiantang/pytorch-deep-image-matting/blob/master/result/example/trimap/spring-289527_1920_15.png) |![image](https://github.com/huochaitiantang/pytorch-deep-image-matting/blob/master/result/example/pred/spring-289527_1920_15.png) |![image](https://github.com/huochaitiantang/pytorch-deep-image-matting/blob/master/result/example/alpha/spring-289527_1920_15.png)
