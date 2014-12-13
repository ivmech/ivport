IVPORT
======

Raspberry Pi Camera Module Multiplexer

IVPORT which is the first Raspberry Pi (also Raspberry Pi B+ and ODROID-W compatible) Camera Module multiplexer is designed to make possible connecting more than one camera module to Raspberry Pi.  Multiplexing can be controlled by 3pins for 4 camera modules, 5 pins for 8 camera modules and 9 pins for 16 camera modules with using GPIO.

![alt ivport](https://raw.githubusercontent.com/ivmech/ivport/master/images/ivport_01.jpg)

Ivport has 5 FFC (flexible flat cable) connectors that make possible to connect more than one Camera Module to Raspberry Pi board. 3 of them are placed to top side of Ivport and 2 of them are placed to bottom side of Ivport.

Ivport's headers are shipped separated because stackable option may not be preferred and extra high pins may exists problems.

It is needed to cut 2x18 Long Pin Female header into two pieces with one of them 2x13 and other 2x3. 2X13 Long Pin Female header should be soldered as shown like above picture (“Ivport” and “Ivmech” labels and “Input Socket” should be on top when it is attached to Raspberry Pi board).

There are pinout configuration jumpers on Ivport's both sides. They make possible to connect Ivport's each other with stackable headers. Also they are used to configure Ivport's pinouts if predefined pins have been already using for other purpose.

There are 4 pair jumpers coded as A, B, C, D. One pair of these jumpers should be soldered with determining from below table before Ivport is used. Each coded jumpers are placed boards both sides. Therefore if “Enable 1 → Pin 11” and “Enable 2 → Pin 12” option was chosen therefore “A” labelled jumpers should be soldered.

![alt ivport](https://raw.githubusercontent.com/ivmech/ivport/master/images/ivport_02.jpg)

After headers and jumpers are soldered, Camera Module can be attached to Ivport with using its flexible flat cable to preferred connector. Also one more flexible flat cable (same as Camera Module's) needed for connection between “Raspberry Pi Camera Input” and “Ivport Input”. After flexible flat cable connection, Ivport can be attached to Raspberry Pi's GPIO headers.

![alt ivport](https://raw.githubusercontent.com/ivmech/ivport/master/images/ivport_03.jpg)
