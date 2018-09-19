# Installing TensorFlow on a Windows server with a GPU

## Install Anaconda

1. Download anaconda installer

```https://www.anaconda.com/download/```

2. Updating conda

2.1 Open you Anaconda Prompt from the start menu.

2.2 Navigate to the anaconda directory

2.3 ```$ conda update conda```

2.4  ```$ conda upgrade --all```


## Install CUDA Toolkit 9.0
https://developer.nvidia.com/cuda-downloads

3.1 Download for Windows Server 2016 and all of the patches

## Install cuDNN 7.0.5 for CUDA 9.0
https://developer.nvidia.com/rdp/cudnn-download
login: 
pass: 

4.1 Extract files

4.2 ```cd cuDNN/bin```

4.3 copy ```cudnn*.dll``` to ```C:\Program files\NVIDIA GPU Computing Toolkit\CUDA\9.2\bin```


##  Create virtual env

https://conda.io/docs/_downloads/conda-cheatsheet.pdf

5.1 Start anaconda prompt

5.2 ```$ conda create -n tf19 anaconda python=3.6```

5.3 ```$ activate tf19```

5.4 ```$ conda install nb_conda```

5.5 ```$ conda install -c anaconda msgpack-python```

## Install TensorFlow 1.9 GPU version

5.1 ```$ pip install --ignore-installed --upgrade tensorflow-gpu```

5.2 Test the install has worked correctly

5.2.1 ```$ python```

5.2.2 ```>>> import tensorflow as tf```

5.2.3 ```>>> tf.__version__```

5.2.4 ```>>> hello=tf.constant("hello world")```

5.2.5 ```>>> with tf.Session() as sess:```

```....print(sess.run(hello))```


## Setup Jupyter notebook server
7.1 In a new anaconda prompt

```$ jupyter notebook --generate-config```

7.2 $ jupyter notebook password

Password used: ???
This creates a file in ```C:\Users\{your username}\.jupyter\```

called ```jupyter_notebook_config.json``` This contains a hash that you will need later


8 Set up config
8.1 in the folder ```C:\Users\{your username}\.jupyter\```

is a file called ```jupyter_notebook_config.py```

Open this with and editor and add these lines

```
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.password = '{hash made earlier}'
c.NotebookApp.port = 8888
```

## Start Jupyter lab
Inside a anaconda prompt activate the enviroment you made earlier then run

```$ jupyter lab```

This will give you a URL that you can now use to log into jupyter lab on your local computer


TESTING GPU in powershell
```PS C:\Program Files\NVIDIA Corporation\NVSMI> .\nvidia-smi.exe```
