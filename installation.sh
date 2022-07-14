#!/bin/bash

project_dir=/home/manuel/PersonalProjects/time-score

# Installazione startday
sudo ln -s $project_dir/bash/startday.sh /usr/bin/startday
chown $USER:$USER /usr/bin/startday

# Installazione score
sudo ln -s $project_dir/bash/score.sh /usr/bin/score
chown $USER:$USER /usr/bin/score
chmod +x /usr/bin/score

# Installazione startday
sudo ln -s $project_dir/bash/report.sh /usr/bin/report
chown $USER:$USER /usr/bin/report
chmod +x /usr/bin/report

# Installazione work status
sudo ln -s $project_dir/bash/workstatus.sh /usr/bin/workstatus
chown $USER:$USER /usr/bin/workstatus
chmod +x /usr/bin/workstatus

echo "Installation completed"
