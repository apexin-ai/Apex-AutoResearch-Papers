#!/bin/bash
PID=569344
RESDIR=/root/autodl-tmp/exp006/results_stratified_irt
LOGFILE=/root/autodl-tmp/exp006/stratified_irt_schemeB.log
MARKER=/root/autodl-tmp/exp006/results_stratified_irt/_DONE_MARKER

while ps -p $PID > /dev/null 2>&1; do
    sleep 60
done

# Process finished - write marker with timestamp
echo "DONE at $(date)" > $MARKER
echo "Exit code of wait: $?" >> $MARKER
echo "--- Last 20 lines of log ---" >> $MARKER
tail -20 $LOGFILE >> $MARKER
echo "--- JSON files ---" >> $MARKER
find $RESDIR -name "*.json" -type f >> $MARKER
echo "--- Directory listing ---" >> $MARKER
ls -laR $RESDIR >> $MARKER
