#!/bin/bash
apt-get update && apt-get install -y python-pip
pip install -r /mnt/extra-addons/requirements.txt
odoo