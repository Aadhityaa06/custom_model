# custom_model.py
To run a custom .h5 model in raspberry pi 
sudo chmod 777 *
sudo ./dependency.sh  

#install Tensorflow Lite
pip3 install https://github.com/google-coral/pycoral/releases/download/release-frogfish/tflite_runtime-2.5.0-cp37-cp37m-linux_armv7l.whl


#copy h5 custom model 
wget https://github.com/oleksandr-g-rock/create-image-classification-for-recognizing-persons-animals-others/raw/main/animall_person_other_v2_fine_tuned.h5
#run script
python3 classify_picamera_with_live_time_custom_model.py
