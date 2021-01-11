#!/bin/bash
sudo apt update -y
sudo apt install git golang-go libolm-dev -y
git clone https://github.com/tulir/gomuks.git
cd gomuks
go build
sudo cp gomuks /bin
cd ..
gomuks
