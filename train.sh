#/bin/bash

ROOT=/home/liuliang/Desktop/pytorch-deep-image-matting
DATA_ROOT=/home/liuliang/Desktop/matting_data

python core/train.py \
	--crop_h=512 \
	--crop_w=512 \
	--size_h=480 \
	--size_w=480 \
	--imgDir=$DATA_ROOT/train/image \
	--alphaDir=$DATA_ROOT/train/alpha \
	--fgDir=$DATA_ROOT/train/fg \
	--bgDir=$DATA_ROOT/train/bg \
	--saveDir=$ROOT/model/input_480_stage3 \
	--batchSize=3 \
	--nEpochs=40 \
	--step=-1 \
	--lr=0.00001 \
	--wl_weight=0.5 \
	--threads=4 \
	--printFreq=10 \
	--ckptSaveFreq=1 \
	--cuda \
        --stage=3 \
        --arch=vgg16 \
        --resume=model/input_480_stage3/ckpt_e3.pth
        #--pretrain=model/ckpt-resnet50-19c8e357.pth
        #--pretrain=model/vgg_state_dict.pth
