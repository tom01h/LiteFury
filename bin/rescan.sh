#!/bin/sh
echo 1 | sudo tee /sys/bus/pci/devices/0000\:0$1\:00.0/remove
echo 1 | sudo tee /sys/bus/pci/rescan
