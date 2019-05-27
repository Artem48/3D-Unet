# 3D U-Net Convolution Neural Network with Keras

## Background
Originally designed after [this paper](http://lmb.informatik.uni-freiburg.de/Publications/2016/CABR16/cicek16miccai.pdf) on 
volumetric segmentation with a 3D U-Net.
The code was written to be trained using the 
[BRATS](http://www.med.upenn.edu/sbia/brats2017.html) data set for brain tumors, but it can
be easily modified to be used in other 3D applications. 

## Tutorial using BRATS Data
### Training
1. Download the BRATS 2018 data by following the steps outlined on the [BRATS 2018 competition page](https://www.med.upenn.edu/sbia/brats2018/registration.html).
Place the unzipped folders in the
```brats/data/original``` folder.
2. Install Python 3 and dependencies: 
```
nibabel,
keras,
pytables,
nilearn,
SimpleITK,
nipype
```
(nipype is required for preprocessing only) 

3. Install [ANTs N4BiasFieldCorrection](https://github.com/stnava/ANTs/releases) and add the location of the ANTs 
binaries to the PATH environmental variable.

4. Add the repository directory to the ```PYTONPATH``` system variable:
```
$ export PYTHONPATH=${PWD}:$PYTHONPATH
```
5. Convert the data to nifti format and perform image wise normalization and correction:

cd into the brats subdirectory:
```
$ cd brats
```
Import the conversion function and run the preprocessing:
```
$ python
>>> from preprocess import convert_brats_data
>>> convert_brats_data("data/original", "data/preprocessed")
```
6. Run the training:

To run training using the original UNet model:
```
$ python train.py
```

To run training using an improved UNet model (recommended): 
```
$ python train_isensee2017.py
```
**If you run out of memory during training:** try setting 
```config['patch_shape`] = (64, 64, 64)``` for starters. 
Also, read the "Configuration" notes at the bottom of this page.

### Write prediction images from the validation data
In the training above, part of the data was held out for validation purposes. 
To write the predicted label maps to file:
```
$ python predict.py
```
The predictions will be written in the ```prediction``` folder along with the input data and ground truth labels for 
comparison.

### Configuration
Changing the configuration dictionary in the [train.py](brats/train.py) or the 
[train_isensee2017.py](brats/train_isensee2017.py) scripts, makes it easy to test out different model and
training configurations.
I would recommend trying out the Isensee et al. model first and then modifying the parameters until you have satisfactory 
results. 
If you are running out of memory, try training using ```(64, 64, 64)``` shaped patches. 
Reducing the "batch_size" and "validation_batch_size" parameters will also reduce the amount of memory required for 
training as smaller batch sizes feed smaller chunks of data to the CNN. 
If the batch size is reduced down to 1 and it still you are still running 
out of memory, you could also try changing the patch size to ```(32, 32, 32)```. 
Keep in mind, though, that a smaller patch sizes may not perform as well as larger patch sizes.

## Using this code on other 3D datasets
If you want to train a 3D UNet on a different set of data, you can copy either the [train.py](brats/train.py) or the 
[train_isensee2017.py](brats/train_isensee2017.py) scripts and modify them to 
read in your data rather than the preprocessed BRATS data that they are currently setup to train on.

## Pretrained model on Brats2018+[TCGA_LGG](https://drive.google.com/file/d/1-1MfNj5AUcGGw2qT8iM_8s7xgLBqOWpR/view?usp=sharing) datasets.
[Pretrained model](https://drive.google.com/file/d/1MKm64YHXs04EJp5AV1dq66-_oV-5Ns5W/view?usp=sharing)
