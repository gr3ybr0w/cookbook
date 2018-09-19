# Deploying Multiple Models Using TF Serving

1. Make a models.config file. This will tell the server where the model files are held and what endpoints they should use.
Under ```C:\Users\th3182\Documents\temp\models\ukpred2``` lives the folders exporterd from our TF model an example would be ```1536593993```
these folders contain the ```saved_model.pb``` the ```assests``` folder and the ```variables``` folder needed to server a model. 

```
model_config_list: {

  config: {
    name: "model",
    base_path: "/models/my_models/ukpred2",
    model_platform: "tensorflow"
  },
  config: {
    name: "model2",
    base_path: "/models/my_models/ukpred3",
    model_platform: "tensorflow"
  }
}
```


2. Install docker

3. ```docker pull tensorflow/serving:nightly```

4. Here wer are going to start the server inside a docker container. The first part of the command specifies the
local port and the containers port.
Then we mount our local folder location to a point created inside the docker container. This is done with out two
model folder locations. Following this we mount the config file. Finally we start specify the container to load
with a switch that points to our config file


```
docker run -p 8501:8501
--mount type=bind,source=C:\Users\th3182\Documents\temp\models\ukpred2,target=/models/my_models/ukpred2
--mount type=bind,source=C:\Users\th3182\Documents\temp\models\ukpred3,target=/models/my_models/ukpred3
--mount type=bind,source=C:\Users\th3182\Documents\temp\models.config,target=/models/models.config
-t tensorflow/serving:nightly --model_config_file=/models/models.config
```
