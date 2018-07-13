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





This information comes from
https://wikimedia.org/api/rest_v1/media/math/render/svg/358923abc154221bb5022fc329061f6fc4dcc69f
