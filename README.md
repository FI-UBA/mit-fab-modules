# MIT Fab Modules

http://academy.kaziunas.com/tutorials/install_fab_modules.php

https://kokompe.cba.mit.edu/

https://www.youtube.com/watch?v=jkLJI8L7TUs

https://www.youtube.com/watch?v=jOm9CLx93GY


# Building Docker Image

```bash
docker buildx build -t fabmodules .
```

# Running

```bash
docker run -it --rm -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=${DISPLAY} --net=host --ipc=host 
--privileged fabmodules:latest /bin/bash
```

# Changing Serial Port

This must be done inside the docker container, so possibly you need to recreate the docker image.

## To find out the correct serial port path:
Go to the terminal and type:

```bash
setserial -g /dev/ttyS[0123]
```

You will get a listing of serial ports with the port / path displayed first: the correct path should have a number listed.

For example:

```bash
fab@laser-cpu:~/Desktop/fabmodules$ setserial -g /dev/ttyS[0123]
/dev/ttyS0, UART: 16550A, Port: 0x03f8, IRQ: 4
/dev/ttyS1, UART: unknown, Port: 0x02f8, IRQ: 3
/dev/ttyS2, UART: unknown, Port: 0x03e8, IRQ: 4
/dev/ttyS3, UART: unknown, Port: 0x02e8, IRQ: 3
```

## Change the Path for Serial Connections:

```bash
sudo nano /usr/local/bin/fab_send
```

In Nano:
1. The file will open - edit all of the lines that say port="/dev/ttyUSB0".
2. Change each "/dev/ttyUSB0" to your serial port.
3. Save changes:
    * Press [control]+O to save the file
    * press [control]+X to exit the editor.

Then you should be in business. Relaunch the fab modules and try to send a file to the machine.

## To Open the Fab Modules - type:

```bash
fab
```
