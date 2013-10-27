#!/bin/bash
clear
echo "pygame 1.9.1 or higher is required. Download and install the"
echo "appropriate binary from http://www.pygame.org/download.shtml"
echo "before continuing."
echo ""
echo Installing dependencies...
echo ""
pip install sphinx
pip install docutils
pip install jinja2
pip install pygments
pip install xmltodict
echo ""
read -p "Press [Enter] key to exit..."