#!/bin/bash

# Installazione startday
sudo ln -s /usr/bin/startday ./bash/startday.sh
chown $USER:$USER /usr/bin/startday

# Installazione score
sudo ln -s /usr/bin/score ./bash/score.sh
chown $USER:$USER /usr/bin/score

# Installazione startday
sudo ln -s /usr/bin/report ./bash/report.sh
chown $USER:$USER /usr/bin/report

echo "Installation completed"
