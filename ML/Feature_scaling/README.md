Feature scaling is a method used to standardize the range of independent variables or features of data.
In data processing, it is also known as data normalization and is generally performed during the data preprocessing step.


# Motivation 

Since the range of values of raw data varies widely, in some machine learning algorithms, objective functions will not work
properly without normalization. For example, the majority of classifiers calculate the distance between two points by the
Euclidean distance. If one of the features has a broad range of values, the distance will be governed by this particular
feature. Therefore, the range of all features should be normalized so that each feature contributes approximately
proportionately to the final distance.

Another reason why feature scaling is applied is that gradient descent converges much faster with feature scaling than without it.


# Methods

## Rescaling (min-max normalization)
Also known as min-max scaling or min-max normalisation, is the simplest method and consists in rescaling the range of
features to scale the range in [0, 1] or [−1, 1]. Selecting the target range depends on the nature of the data.
The general formula is given as:

![rescaling_min_max_normalization](https://user-images.githubusercontent.com/8236737/42682844-91ba78d8-8683-11e8-9aa3-2b0448d2033d.jpg)

where x and an original value, x' is the normalized value. for example, suppose that we have the students weight data,
and the students wights sapne [160 pounds, 200 pounds]. To rescale this data, we first subtract 160 from each
students weight and deivide theresult by 40 (the difference between the max and min weights).

## Mean normalization
![mean_normalization](https://user-images.githubusercontent.com/8236737/42683333-f220300e-8684-11e8-83a6-118edb8e4bdc.jpg)

where x is an original value, x' is the normalized value.

## Standardization
In machine learning, we can handle various types of data, e.g. audion signals and pixel values for image data, and this
data can include multiple dimensions. Feature standardization makes the values of each feature in the data have zero-mean
(when subtracting the mean in the numerator) and unit-variance. This method is widely used for normalization is widely
used for normalization in many machine learning algorithms (e.g support vector machines, logistic regression,
and artifical neural networks). The general method of calculation is to determine the distribution mean and standard deviation
for each feature. Next we subtract the mean from each feature. Then we divide the values (mean is already subtracted) of
each feature by is by its standard deviation.

![standardization](https://user-images.githubusercontent.com/8236737/42683760-232b5704-8686-11e8-8509-0def67aac43c.jpg)


## Scaling to unit length
Another option that is widely used in machine-learning is to scale the components of a feature vector such that the
complete vector has length one. This usually means dividing each component by the Euclidean length of the vector:

![scaling_to_unit_length](https://user-images.githubusercontent.com/8236737/42684982-a14c093c-8689-11e8-823c-6661899727c8.jpg)

In some applications (e.g. Histogram features) it can be more practical to use the L1 norm (i.e. Manhattan Distance,
City-Block Length or Taxicab Geometry) of the feature vector. This is especially important if in the following
learning steps the Scalar Metric is used as a distance measure.


This information comes from
https://wikimedia.org/api/rest_v1/media/math/render/svg/358923abc154221bb5022fc329061f6fc4dcc69f
