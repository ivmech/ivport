#! /bin/bash

output_file="out_%d.jpg"
height="480"
width="640"

test -x ./ivportfastcamd || exit 0

case "$1" in
  start)
        ./ivportfastcamd -w $width -h $height -o $output_file &
        ;;
  stop)
        pkill ivportfastcamd
        ;;

  restart)
        pkill ivportfastcamd
        ./ivportfastcamd -w $width -h $height -o $output_file &
        ;;

  pid)
        if [[ -n $(pgrep ivportfastcamd) ]]; then
                echo "Raspberry Pi Ivport Camera Module Fast Capture Daemon is at" `pgrep ivportfastcamd`
        else
                echo "Raspberry Pi Ivport Camera Module Fast Capture Daemon is Not Running"
        fi
        ;;

  capture)
        kill -s USR1 `pgrep ivportfastcamd`
        ;;
  *)
        echo "Usage: ivport_fast {start|stop|restart|pid|capture}"
        exit 1
        ;;
esac
exit 0
