#!/bin/bash
cd ~/Sites/sgdialer/docs
sphinx-apidoc --full -H "sgdialer" -A "Michael Andrew" -V "1.0" -R "RC1" -o . ../src
make clean
make html