#!/bin/bash

#run this script via: bash run_test.sh

#run the unit tests
nosetests --with-coverage html test_futurefish.py

#run the PEP8 checker
pycodestyle data_processing.py test_futurefish.py
