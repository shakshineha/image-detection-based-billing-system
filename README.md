# Billing using image detection

This paper aims at putting forward the idea of image-based billing system. In many C-shops it
is often seen that billing of products is done manually. Also, establishing billing systems like Optical code
readers (OCR) prove to be quite expensive and thus cannot is not preferred to be used by all the shops.
Thus, in this paper we are proposing an edge computing-based technique which will help the shops use a
faster and more accurate billing system. The proposed model will not only detects the object accurately, but
based on its size it can also differentiate among the price, meaning that if there are two versions of the same
product, one of small size( of price x) and the other of larger size( of price 2x) then it will successfully
recognize them and add the price to the billing system accordingly.


## Libraries to be installed:

For this project to install them use the following pip commands:

- pip install tensorflow-gpu==1.15.2
- pip install opencv-python
- pip3 install keras
- pip3 install imageai --upgrade
- pip install -U Flask

Incase imageAI does not install directly, the following method can be used.
pip install https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.2/imageai-2.0.2-py3-none-any.whl

For full reference:
https://medium.com/@guymodscientist/image-prediction-with-10-lines-of-code-3266f4039c7a

### This project has been trained on a model named model90.h5. The model can be downloaded from this link

https://drive.google.com/drive/folders/1ZexrvUSFj9U35EDm5jf0Jy4wtYobdmd2?usp=sharing 

It is trained on the dataset of 14 objects which are:

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




