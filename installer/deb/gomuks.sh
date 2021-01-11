#!/bin/bash
sudo apt update -y
sudo apt install git -y
sudo apt install golang-go -y
sudo apt install libolm-dev -y
git clone https://github.com/tulir/gomuks.git
cd gomuks
go build
sudo cp gomuks /bin
cd ..
gomuks
