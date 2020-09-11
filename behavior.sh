#!/bin/sh

xterm -title "Radar Module" -e "source ~/.bashrc; roslaunch ti_mmwave_rospkg 1843_multi_3d_0.launch"&

sleep 5 

xterm -title "Microdoppler" -e "source ~/.bashrc; cd catkin_py_ws/src/micro_doppler_pkg/scripts/; python micro_doppler_m.py"&

sleep 5 

xterm -title "CNN Node" -e "source ~/.bashrc; cd catkin_py_ws/src/ti-mmwave-mds-cnn/scripts/; python3 mds_cnn_node.py"
