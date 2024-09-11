#!/bin/bash
set -e

./run.py --config_file configs/cluster.cfg --start persist --username ubuntu
./run.py --config_file configs/cluster.cfg --start tso nodepool  --username ubuntu
sleep 1s
./run.py --config_file configs/cluster.cfg --start cpo  --username ubuntu
./run.py --config_file configs/cluster.cfg --start load  --username ubuntu 
./run.py --config_file configs/cluster.cfg —stop load  --username ubuntu 
./run.py --config_file configs/cluster.cfg —remove load   --username ubuntu 
sleep 1s
./run.py --config_file configs/cluster.cfg --start load  --username ubuntu
./run.py --config_file configs/cluster.cfg —stop load  --username ubuntu
./run.py --config_file configs/cluster.cfg —remove load   --username ubuntu
sleep 1s
./run.py --config_file configs/cluster.cfg --start load  --username ubuntu
./run.py --config_file configs/cluster.cfg —stop load  --username ubuntu
./run.py --config_file configs/cluster.cfg —remove load   --username ubuntu
sleep 1s
./run.py --config_file configs/cluster.cfg --start client --username ubuntu
sleep 30s
./run.py --config_file configs/cluster.cfg —log client --username ubuntu



