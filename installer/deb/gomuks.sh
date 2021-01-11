#!/bin/bash
sudo apt update -y
echo "
"
sudo apt install git -y
echo "
"
sudo apt install golang-go -y
echo "
"
sudo apt install libolm-dev -y
echo "
"
git clone https://github.com/tulir/gomuks.git
echo "
"
cd gomuks
echo "
"
go build
echo "
"
sudo cp gomuks /bin
echo "
"
cd ..
gomuks
