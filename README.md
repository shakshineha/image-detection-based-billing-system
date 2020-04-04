# image-detection-based-billing-system
This is a complete python based project( with GUI) for billing system on the basis of image detection.
This project aims at putting forward the idea of image-based billing system. In many C-shops it is often seen that billing of products is done manually. Also, establishing billing systems like Optical code readers (OCR) prove to be quite expensive and thus cannot is not preferred to be used by all the shops. Thus, with the help of this project we are proposing an edge computing-based technique which will help the shops use a faster and more accurate billing system. The proposed model will not only detects the object accurately, but based on its size it can also differentiate among the price, meaning that if there are two versions of the same product, one of small size( of price x) and the other of larger size( of price 2x) then it will successfully recognize them and add the price to the billing system accordingly.

This whole project is python based and to operate it cerain libraries need to installed, which are as follows:

1. Tensorflow
2. OpenCV
3. Keras
4. ImageAI
5. Flask

For this project to install them use the following pip commands:

pip install tensorflow-gpu==1.15.2
pip install opencv-python
pip3 install keras
pip3 install imageai --upgrade
pip install -U Flask

This project has been trained on a model named model90.h5. It is trained on the dataset of 14 objects which are:

1. biscuit_big
2. biscuit_small
3. coco_oil
4. feviqwik
5.hand_Wash
6. maggi
7. masala
8. odomos
9. pasta
10. rollon
11. sanitizer
12. shampoo_pouch
13. sunscreen
14. table_salt

