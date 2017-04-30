#!/bin/sh
echo "Installing WYSIWYG Tensorflow GUI"
sudo apt-get install python
echo "Done."
echo "Python installed."
sudo apt-get install python-pip
echo "pip installed"
echo "installing numPy"
sudo pip install numpy
echo "Done."
echo "adding kivy to apt repo"
sudo add-apt-repository ppa:kivy-team/kivy
echo "installing kivy"
pip install cython
sudo pip install kivy
sudo apt-get install python-kivy
echo "Done."
echo "installing kivy examples"
sudo apt-get install python-kivy-examples
clear
echo "Done."
