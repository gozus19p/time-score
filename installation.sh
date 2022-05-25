#!/bin/bash

# Installazione startday
sudo ln -s ./bash/startday.sh /usr/bin/startday
chown $USER:$USER /usr/bin/startday

# Installazione score
sudo ln -s ./bash/score.sh /usr/bin/score
chown $USER:$USER /usr/bin/score

# Installazione startday
sudo ln -s ./bash/report.sh /usr/bin/report
chown $USER:$USER /usr/bin/report

echo "Installation completed"
