#!/bin/bash
sudo apt install git
git clone https://github.com/tulir/gomuks.git
cd gomuks
go build
sudo cp gomuks /bin
