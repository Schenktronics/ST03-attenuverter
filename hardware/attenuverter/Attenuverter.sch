EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "Attenuverter"
Date "2020-04-17"
Rev "1.0"
Comp "Nathan Schenk"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Connector:AudioJack2_SwitchT J1
U 1 1 5DDBE5A8
P 1650 1550
F 0 "J1" H 1471 1529 50  0000 R CNN
F 1 "AudioJack2_SwitchT" H 1682 1784 50  0001 C CNN
F 2 "_NTSFootprints:Jack_3.5mm_QingPu_WQP-PJ398SM_Vertical_CenterHole_OvalPads" H 1650 1550 50  0001 C CNN
F 3 "~" H 1650 1550 50  0001 C CNN
	1    1650 1550
	1    0    0    1   
$EndComp
$Comp
L Connector:AudioJack2_SwitchT J2
U 1 1 5DDC157E
P 4350 1650
F 0 "J2" H 4170 1629 50  0000 R CNN
F 1 "AudioJack2_SwitchT" H 4382 1884 50  0001 C CNN
F 2 "_NTSFootprints:Jack_3.5mm_QingPu_WQP-PJ398SM_Vertical_CenterHole_OvalPads" H 4350 1650 50  0001 C CNN
F 3 "~" H 4350 1650 50  0001 C CNN
	1    4350 1650
	-1   0    0    1   
$EndComp
$Comp
L Amplifier_Operational:TL084 U1
U 5 1 5DDC382F
P 8600 4000
F 0 "U1" H 8558 4046 50  0000 L CNN
F 1 "TL084" H 8558 3955 50  0000 L CNN
F 2 "Housings_SOIC:SOIC-14_3.9x8.7mm_Pitch1.27mm" H 8550 4100 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/tl081.pdf" H 8650 4200 50  0001 C CNN
	5    8600 4000
	1    0    0    -1  
$EndComp
$Comp
L Amplifier_Operational:TL084 U1
U 1 1 5DDC644A
P 3350 1650
F 0 "U1" H 3500 1550 50  0000 C CNN
F 1 "TL084" H 3450 1450 50  0000 C CNN
F 2 "Housings_SOIC:SOIC-14_3.9x8.7mm_Pitch1.27mm" H 3300 1750 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/tl081.pdf" H 3400 1850 50  0001 C CNN
	1    3350 1650
	1    0    0    1   
$EndComp
$Comp
L Device:R R1
U 1 1 5DDC84D9
P 3350 1350
F 0 "R1" V 3143 1350 50  0000 C CNN
F 1 "100k" V 3234 1350 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 3280 1350 50  0001 C CNN
F 3 "~" H 3350 1350 50  0001 C CNN
	1    3350 1350
	0    1    1    0   
$EndComp
$Comp
L Device:R_POT RV1
U 1 1 5DDC8C46
P 2250 1850
F 0 "RV1" H 2181 1896 50  0000 R CNN
F 1 "100k" H 2181 1805 50  0000 R CNN
F 2 "_NTSFootprints:Potentiometer_Alps_RK09L_Plated_Mount_Holes" H 2250 1850 50  0001 C CNN
F 3 "~" H 2250 1850 50  0001 C CNN
	1    2250 1850
	1    0    0    -1  
$EndComp
$Comp
L Device:R R2
U 1 1 5DDCBD7B
P 2800 1550
F 0 "R2" V 2593 1550 50  0000 C CNN
F 1 "100k" V 2684 1550 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 2730 1550 50  0001 C CNN
F 3 "~" H 2800 1550 50  0001 C CNN
	1    2800 1550
	0    1    1    0   
$EndComp
$Comp
L Device:R R4
U 1 1 5DDCC3E4
P 2500 1700
F 0 "R4" H 2430 1654 50  0000 R CNN
F 1 "100k" H 2430 1745 50  0000 R CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 2430 1700 50  0001 C CNN
F 3 "~" H 2500 1700 50  0001 C CNN
	1    2500 1700
	-1   0    0    1   
$EndComp
$Comp
L Device:R R5
U 1 1 5DDCD4C4
P 2500 2000
F 0 "R5" H 2430 1954 50  0000 R CNN
F 1 "100k" H 2430 2045 50  0000 R CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 2430 2000 50  0001 C CNN
F 3 "~" H 2500 2000 50  0001 C CNN
	1    2500 2000
	-1   0    0    1   
$EndComp
Wire Wire Line
	2400 1850 2500 1850
Connection ~ 2500 1850
Wire Wire Line
	1850 1550 2250 1550
Wire Wire Line
	2650 1550 2500 1550
Connection ~ 2500 1550
Wire Wire Line
	2950 1550 3000 1550
Wire Wire Line
	3200 1350 3000 1350
Wire Wire Line
	3000 1350 3000 1550
Connection ~ 3000 1550
Wire Wire Line
	3000 1550 3050 1550
Wire Wire Line
	3500 1350 3650 1350
Wire Wire Line
	3650 1350 3650 1650
Wire Wire Line
	2500 2150 3050 2150
Wire Wire Line
	2250 1700 2250 1550
Connection ~ 2250 1550
Wire Wire Line
	2250 1550 2500 1550
Wire Wire Line
	2500 2150 2250 2150
Wire Wire Line
	2250 2150 2250 2000
Connection ~ 2500 2150
Wire Wire Line
	1850 1650 1850 2150
Wire Wire Line
	1850 2150 2250 2150
Connection ~ 2250 2150
$Comp
L Device:R R3
U 1 1 5DDDB57A
P 3900 1650
F 0 "R3" V 3693 1650 50  0000 C CNN
F 1 "100" V 3784 1650 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 3830 1650 50  0001 C CNN
F 3 "~" H 3900 1650 50  0001 C CNN
	1    3900 1650
	0    1    1    0   
$EndComp
Wire Wire Line
	3650 1650 3750 1650
Connection ~ 3650 1650
Wire Wire Line
	4050 1650 4150 1650
$Comp
L power:GND #PWR0101
U 1 1 5DDDC16D
P 3050 2150
F 0 "#PWR0101" H 3050 1900 50  0001 C CNN
F 1 "GND" H 3055 1977 50  0000 C CNN
F 2 "" H 3050 2150 50  0001 C CNN
F 3 "" H 3050 2150 50  0001 C CNN
	1    3050 2150
	1    0    0    -1  
$EndComp
Connection ~ 3050 2150
Wire Wire Line
	4150 2150 4150 1750
$Comp
L Device:C C1
U 1 1 5DDDD497
P 3350 1000
F 0 "C1" V 3098 1000 50  0000 C CNN
F 1 "10pF" V 3189 1000 50  0000 C CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 3388 850 50  0001 C CNN
F 3 "~" H 3350 1000 50  0001 C CNN
	1    3350 1000
	0    1    1    0   
$EndComp
Wire Wire Line
	3200 1000 3000 1000
Wire Wire Line
	3000 1000 3000 1350
Connection ~ 3000 1350
Wire Wire Line
	3650 1350 3650 1000
Wire Wire Line
	3650 1000 3500 1000
Connection ~ 3650 1350
$Comp
L Reference_Voltage:LM4040DBZ-5 U2
U 1 1 5DDDE922
P 9500 4200
F 0 "U2" V 9550 4400 50  0000 R CNN
F 1 "LM4040DBZ-5" V 9450 4850 50  0000 R CNN
F 2 "TO_SOT_Packages_SMD:SOT-23" H 9500 4000 50  0001 C CIN
F 3 "http://www.ti.com/lit/ds/symlink/lm4040-n.pdf" H 9500 4200 50  0001 C CIN
	1    9500 4200
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR0102
U 1 1 5DDE574E
P 9500 4350
F 0 "#PWR0102" H 9500 4100 50  0001 C CNN
F 1 "GND" H 9505 4177 50  0000 C CNN
F 2 "" H 9500 4350 50  0001 C CNN
F 3 "" H 9500 4350 50  0001 C CNN
	1    9500 4350
	1    0    0    -1  
$EndComp
$Comp
L Device:R R11
U 1 1 5DDE5F57
P 9500 3800
F 0 "R11" H 9430 3754 50  0000 R CNN
F 1 "1k" H 9430 3845 50  0000 R CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 9430 3800 50  0001 C CNN
F 3 "~" H 9500 3800 50  0001 C CNN
	1    9500 3800
	-1   0    0    1   
$EndComp
Wire Wire Line
	3050 2150 4150 2150
$Comp
L power:+12V #PWR0103
U 1 1 5DDE6CAE
P 8500 5150
F 0 "#PWR0103" H 8500 5000 50  0001 C CNN
F 1 "+12V" H 8515 5323 50  0000 C CNN
F 2 "" H 8500 5150 50  0001 C CNN
F 3 "" H 8500 5150 50  0001 C CNN
	1    8500 5150
	1    0    0    -1  
$EndComp
$Comp
L power:-12V #PWR0104
U 1 1 5DDE7EAC
P 8500 5850
F 0 "#PWR0104" H 8500 5950 50  0001 C CNN
F 1 "-12V" H 8515 6023 50  0000 C CNN
F 2 "" H 8500 5850 50  0001 C CNN
F 3 "" H 8500 5850 50  0001 C CNN
	1    8500 5850
	-1   0    0    1   
$EndComp
$Comp
L power:+12V #PWR0105
U 1 1 5DDE88E7
P 9500 3650
F 0 "#PWR0105" H 9500 3500 50  0001 C CNN
F 1 "+12V" H 9515 3823 50  0000 C CNN
F 2 "" H 9500 3650 50  0001 C CNN
F 3 "" H 9500 3650 50  0001 C CNN
	1    9500 3650
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0106
U 1 1 5DDE97B1
P 9900 3650
F 0 "#PWR0106" H 9900 3500 50  0001 C CNN
F 1 "+5V" H 9915 3823 50  0000 C CNN
F 2 "" H 9900 3650 50  0001 C CNN
F 3 "" H 9900 3650 50  0001 C CNN
	1    9900 3650
	1    0    0    -1  
$EndComp
$Comp
L Device:C C4
U 1 1 5DDEC2A5
P 9900 4200
F 0 "C4" H 10015 4246 50  0000 L CNN
F 1 "100nF" H 10015 4155 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 9938 4050 50  0001 C CNN
F 3 "~" H 9900 4200 50  0001 C CNN
	1    9900 4200
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0107
U 1 1 5DDED6CC
P 9900 4350
F 0 "#PWR0107" H 9900 4100 50  0001 C CNN
F 1 "GND" H 9905 4177 50  0000 C CNN
F 2 "" H 9900 4350 50  0001 C CNN
F 3 "" H 9900 4350 50  0001 C CNN
	1    9900 4350
	1    0    0    -1  
$EndComp
Wire Wire Line
	9500 4050 9500 4000
Wire Wire Line
	9900 4050 9900 4000
Wire Wire Line
	9500 4000 9900 4000
Connection ~ 9500 4000
Wire Wire Line
	9500 4000 9500 3950
Connection ~ 9900 4000
Wire Wire Line
	9900 4000 9900 3650
$Comp
L power:+5V #PWR0108
U 1 1 5DDF41AE
P 1850 1450
F 0 "#PWR0108" H 1850 1300 50  0001 C CNN
F 1 "+5V" V 1865 1578 50  0000 L CNN
F 2 "" H 1850 1450 50  0001 C CNN
F 3 "" H 1850 1450 50  0001 C CNN
	1    1850 1450
	0    1    1    0   
$EndComp
NoConn ~ 4150 1550
$Comp
L Connector:AudioJack2_SwitchT J3
U 1 1 5DE125C4
P 1650 3050
F 0 "J3" H 1471 3029 50  0000 R CNN
F 1 "AudioJack2_SwitchT" H 1682 3284 50  0001 C CNN
F 2 "_NTSFootprints:Jack_3.5mm_QingPu_WQP-PJ398SM_Vertical_CenterHole_OvalPads" H 1650 3050 50  0001 C CNN
F 3 "~" H 1650 3050 50  0001 C CNN
	1    1650 3050
	1    0    0    1   
$EndComp
$Comp
L Connector:AudioJack2_SwitchT J4
U 1 1 5DE125CA
P 4350 3150
F 0 "J4" H 4170 3129 50  0000 R CNN
F 1 "AudioJack2_SwitchT" H 4382 3384 50  0001 C CNN
F 2 "_NTSFootprints:Jack_3.5mm_QingPu_WQP-PJ398SM_Vertical_CenterHole_OvalPads" H 4350 3150 50  0001 C CNN
F 3 "~" H 4350 3150 50  0001 C CNN
	1    4350 3150
	-1   0    0    1   
$EndComp
$Comp
L Amplifier_Operational:TL084 U1
U 2 1 5DE125D0
P 3350 3150
F 0 "U1" H 3500 3050 50  0000 C CNN
F 1 "TL084" H 3450 2950 50  0000 C CNN
F 2 "Housings_SOIC:SOIC-14_3.9x8.7mm_Pitch1.27mm" H 3300 3250 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/tl081.pdf" H 3400 3350 50  0001 C CNN
	2    3350 3150
	1    0    0    1   
$EndComp
$Comp
L Device:R R6
U 1 1 5DE125D6
P 3350 2850
F 0 "R6" V 3143 2850 50  0000 C CNN
F 1 "100k" V 3234 2850 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 3280 2850 50  0001 C CNN
F 3 "~" H 3350 2850 50  0001 C CNN
	1    3350 2850
	0    1    1    0   
$EndComp
$Comp
L Device:R_POT RV2
U 1 1 5DE125DC
P 2250 3350
F 0 "RV2" H 2181 3396 50  0000 R CNN
F 1 "100k" H 2181 3305 50  0000 R CNN
F 2 "_NTSFootprints:Potentiometer_Alps_RK09L_Plated_Mount_Holes" H 2250 3350 50  0001 C CNN
F 3 "~" H 2250 3350 50  0001 C CNN
	1    2250 3350
	1    0    0    -1  
$EndComp
$Comp
L Device:R R7
U 1 1 5DE125E2
P 2800 3050
F 0 "R7" V 2593 3050 50  0000 C CNN
F 1 "100k" V 2684 3050 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 2730 3050 50  0001 C CNN
F 3 "~" H 2800 3050 50  0001 C CNN
	1    2800 3050
	0    1    1    0   
$EndComp
$Comp
L Device:R R9
U 1 1 5DE125E8
P 2500 3200
F 0 "R9" H 2430 3154 50  0000 R CNN
F 1 "100k" H 2430 3245 50  0000 R CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 2430 3200 50  0001 C CNN
F 3 "~" H 2500 3200 50  0001 C CNN
	1    2500 3200
	-1   0    0    1   
$EndComp
$Comp
L Device:R R10
U 1 1 5DE125EE
P 2500 3500
F 0 "R10" H 2430 3454 50  0000 R CNN
F 1 "100k" H 2430 3545 50  0000 R CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 2430 3500 50  0001 C CNN
F 3 "~" H 2500 3500 50  0001 C CNN
	1    2500 3500
	-1   0    0    1   
$EndComp
Wire Wire Line
	2400 3350 2500 3350
Connection ~ 2500 3350
Wire Wire Line
	1850 3050 2250 3050
Wire Wire Line
	2650 3050 2500 3050
Connection ~ 2500 3050
Wire Wire Line
	2950 3050 3000 3050
Wire Wire Line
	3200 2850 3000 2850
Wire Wire Line
	3000 2850 3000 3050
Connection ~ 3000 3050
Wire Wire Line
	3000 3050 3050 3050
Wire Wire Line
	3500 2850 3650 2850
Wire Wire Line
	3650 2850 3650 3150
Wire Wire Line
	2500 3650 3050 3650
Wire Wire Line
	2250 3200 2250 3050
Connection ~ 2250 3050
Wire Wire Line
	2250 3050 2500 3050
Wire Wire Line
	2500 3650 2250 3650
Wire Wire Line
	2250 3650 2250 3500
Connection ~ 2500 3650
Wire Wire Line
	1850 3150 1850 3650
Wire Wire Line
	1850 3650 2250 3650
Connection ~ 2250 3650
$Comp
L Device:R R8
U 1 1 5DE1260B
P 3900 3150
F 0 "R8" V 3693 3150 50  0000 C CNN
F 1 "100" V 3784 3150 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 3830 3150 50  0001 C CNN
F 3 "~" H 3900 3150 50  0001 C CNN
	1    3900 3150
	0    1    1    0   
$EndComp
Wire Wire Line
	3650 3150 3750 3150
Connection ~ 3650 3150
Wire Wire Line
	4050 3150 4150 3150
$Comp
L power:GND #PWR0109
U 1 1 5DE12614
P 3050 3650
F 0 "#PWR0109" H 3050 3400 50  0001 C CNN
F 1 "GND" H 3055 3477 50  0000 C CNN
F 2 "" H 3050 3650 50  0001 C CNN
F 3 "" H 3050 3650 50  0001 C CNN
	1    3050 3650
	1    0    0    -1  
$EndComp
Connection ~ 3050 3650
Wire Wire Line
	4150 3650 4150 3250
$Comp
L Device:C C2
U 1 1 5DE1261C
P 3350 2500
F 0 "C2" V 3098 2500 50  0000 C CNN
F 1 "10pF" V 3189 2500 50  0000 C CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 3388 2350 50  0001 C CNN
F 3 "~" H 3350 2500 50  0001 C CNN
	1    3350 2500
	0    1    1    0   
$EndComp
Wire Wire Line
	3200 2500 3000 2500
Wire Wire Line
	3000 2500 3000 2850
Connection ~ 3000 2850
Wire Wire Line
	3650 2850 3650 2500
Wire Wire Line
	3650 2500 3500 2500
Connection ~ 3650 2850
Wire Wire Line
	3050 3650 4150 3650
$Comp
L power:+5V #PWR0110
U 1 1 5DE12629
P 1850 2950
F 0 "#PWR0110" H 1850 2800 50  0001 C CNN
F 1 "+5V" V 1865 3078 50  0000 L CNN
F 2 "" H 1850 2950 50  0001 C CNN
F 3 "" H 1850 2950 50  0001 C CNN
	1    1850 2950
	0    1    1    0   
$EndComp
NoConn ~ 4150 3050
$Comp
L Connector:AudioJack2_SwitchT J5
U 1 1 5DE41412
P 1650 4550
F 0 "J5" H 1471 4529 50  0000 R CNN
F 1 "AudioJack2_SwitchT" H 1682 4784 50  0001 C CNN
F 2 "_NTSFootprints:Jack_3.5mm_QingPu_WQP-PJ398SM_Vertical_CenterHole_OvalPads" H 1650 4550 50  0001 C CNN
F 3 "~" H 1650 4550 50  0001 C CNN
	1    1650 4550
	1    0    0    1   
$EndComp
$Comp
L Connector:AudioJack2_SwitchT J6
U 1 1 5DE41418
P 4350 4650
F 0 "J6" H 4170 4629 50  0000 R CNN
F 1 "AudioJack2_SwitchT" H 4382 4884 50  0001 C CNN
F 2 "_NTSFootprints:Jack_3.5mm_QingPu_WQP-PJ398SM_Vertical_CenterHole_OvalPads" H 4350 4650 50  0001 C CNN
F 3 "~" H 4350 4650 50  0001 C CNN
	1    4350 4650
	-1   0    0    1   
$EndComp
$Comp
L Amplifier_Operational:TL084 U1
U 3 1 5DE4141E
P 3350 4650
F 0 "U1" H 3500 4550 50  0000 C CNN
F 1 "TL084" H 3450 4450 50  0000 C CNN
F 2 "Housings_SOIC:SOIC-14_3.9x8.7mm_Pitch1.27mm" H 3300 4750 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/tl081.pdf" H 3400 4850 50  0001 C CNN
	3    3350 4650
	1    0    0    1   
$EndComp
$Comp
L Device:R R12
U 1 1 5DE41424
P 3350 4350
F 0 "R12" V 3143 4350 50  0000 C CNN
F 1 "100k" V 3234 4350 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 3280 4350 50  0001 C CNN
F 3 "~" H 3350 4350 50  0001 C CNN
	1    3350 4350
	0    1    1    0   
$EndComp
$Comp
L Device:R_POT RV3
U 1 1 5DE4142A
P 2250 4850
F 0 "RV3" H 2181 4896 50  0000 R CNN
F 1 "100k" H 2181 4805 50  0000 R CNN
F 2 "_NTSFootprints:Potentiometer_Alps_RK09L_Plated_Mount_Holes" H 2250 4850 50  0001 C CNN
F 3 "~" H 2250 4850 50  0001 C CNN
	1    2250 4850
	1    0    0    -1  
$EndComp
$Comp
L Device:R R13
U 1 1 5DE41430
P 2800 4550
F 0 "R13" V 2593 4550 50  0000 C CNN
F 1 "100k" V 2684 4550 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 2730 4550 50  0001 C CNN
F 3 "~" H 2800 4550 50  0001 C CNN
	1    2800 4550
	0    1    1    0   
$EndComp
$Comp
L Device:R R15
U 1 1 5DE41436
P 2500 4700
F 0 "R15" H 2430 4654 50  0000 R CNN
F 1 "100k" H 2430 4745 50  0000 R CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 2430 4700 50  0001 C CNN
F 3 "~" H 2500 4700 50  0001 C CNN
	1    2500 4700
	-1   0    0    1   
$EndComp
$Comp
L Device:R R16
U 1 1 5DE4143C
P 2500 5000
F 0 "R16" H 2430 4954 50  0000 R CNN
F 1 "100k" H 2430 5045 50  0000 R CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 2430 5000 50  0001 C CNN
F 3 "~" H 2500 5000 50  0001 C CNN
	1    2500 5000
	-1   0    0    1   
$EndComp
Wire Wire Line
	2400 4850 2500 4850
Connection ~ 2500 4850
Wire Wire Line
	1850 4550 2250 4550
Wire Wire Line
	2650 4550 2500 4550
Connection ~ 2500 4550
Wire Wire Line
	2950 4550 3000 4550
Wire Wire Line
	3200 4350 3000 4350
Wire Wire Line
	3000 4350 3000 4550
Connection ~ 3000 4550
Wire Wire Line
	3000 4550 3050 4550
Wire Wire Line
	3500 4350 3650 4350
Wire Wire Line
	3650 4350 3650 4650
Wire Wire Line
	2500 5150 3050 5150
Wire Wire Line
	2250 4700 2250 4550
Connection ~ 2250 4550
Wire Wire Line
	2250 4550 2500 4550
Wire Wire Line
	2500 5150 2250 5150
Wire Wire Line
	2250 5150 2250 5000
Connection ~ 2500 5150
Wire Wire Line
	1850 4650 1850 5150
Wire Wire Line
	1850 5150 2250 5150
Connection ~ 2250 5150
$Comp
L Device:R R14
U 1 1 5DE41459
P 3900 4650
F 0 "R14" V 3693 4650 50  0000 C CNN
F 1 "100" V 3784 4650 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 3830 4650 50  0001 C CNN
F 3 "~" H 3900 4650 50  0001 C CNN
	1    3900 4650
	0    1    1    0   
$EndComp
Wire Wire Line
	3650 4650 3750 4650
Connection ~ 3650 4650
Wire Wire Line
	4050 4650 4150 4650
$Comp
L power:GND #PWR0111
U 1 1 5DE41462
P 3050 5150
F 0 "#PWR0111" H 3050 4900 50  0001 C CNN
F 1 "GND" H 3055 4977 50  0000 C CNN
F 2 "" H 3050 5150 50  0001 C CNN
F 3 "" H 3050 5150 50  0001 C CNN
	1    3050 5150
	1    0    0    -1  
$EndComp
Connection ~ 3050 5150
Wire Wire Line
	4150 5150 4150 4750
$Comp
L Device:C C3
U 1 1 5DE4146A
P 3350 4000
F 0 "C3" V 3098 4000 50  0000 C CNN
F 1 "10pF" V 3189 4000 50  0000 C CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 3388 3850 50  0001 C CNN
F 3 "~" H 3350 4000 50  0001 C CNN
	1    3350 4000
	0    1    1    0   
$EndComp
Wire Wire Line
	3200 4000 3000 4000
Wire Wire Line
	3000 4000 3000 4350
Connection ~ 3000 4350
Wire Wire Line
	3650 4350 3650 4000
Wire Wire Line
	3650 4000 3500 4000
Connection ~ 3650 4350
Wire Wire Line
	3050 5150 4150 5150
$Comp
L power:+5V #PWR0112
U 1 1 5DE41477
P 1850 4450
F 0 "#PWR0112" H 1850 4300 50  0001 C CNN
F 1 "+5V" V 1865 4578 50  0000 L CNN
F 2 "" H 1850 4450 50  0001 C CNN
F 3 "" H 1850 4450 50  0001 C CNN
	1    1850 4450
	0    1    1    0   
$EndComp
NoConn ~ 4150 4550
$Comp
L Connector:AudioJack2_SwitchT J8
U 1 1 5DE4CCB5
P 1650 6050
F 0 "J8" H 1471 6029 50  0000 R CNN
F 1 "AudioJack2_SwitchT" H 1682 6284 50  0001 C CNN
F 2 "_NTSFootprints:Jack_3.5mm_QingPu_WQP-PJ398SM_Vertical_CenterHole_OvalPads" H 1650 6050 50  0001 C CNN
F 3 "~" H 1650 6050 50  0001 C CNN
	1    1650 6050
	1    0    0    1   
$EndComp
$Comp
L Connector:AudioJack2_SwitchT J9
U 1 1 5DE4CCBB
P 4350 6150
F 0 "J9" H 4170 6129 50  0000 R CNN
F 1 "AudioJack2_SwitchT" H 4382 6384 50  0001 C CNN
F 2 "_NTSFootprints:Jack_3.5mm_QingPu_WQP-PJ398SM_Vertical_CenterHole_OvalPads" H 4350 6150 50  0001 C CNN
F 3 "~" H 4350 6150 50  0001 C CNN
	1    4350 6150
	-1   0    0    1   
$EndComp
$Comp
L Amplifier_Operational:TL084 U1
U 4 1 5DE4CCC1
P 3350 6150
F 0 "U1" H 3500 6050 50  0000 C CNN
F 1 "TL084" H 3450 5950 50  0000 C CNN
F 2 "Housings_SOIC:SOIC-14_3.9x8.7mm_Pitch1.27mm" H 3300 6250 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/tl081.pdf" H 3400 6350 50  0001 C CNN
	4    3350 6150
	1    0    0    1   
$EndComp
$Comp
L Device:R R17
U 1 1 5DE4CCC7
P 3350 5850
F 0 "R17" V 3143 5850 50  0000 C CNN
F 1 "100k" V 3234 5850 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 3280 5850 50  0001 C CNN
F 3 "~" H 3350 5850 50  0001 C CNN
	1    3350 5850
	0    1    1    0   
$EndComp
$Comp
L Device:R_POT RV4
U 1 1 5DE4CCCD
P 2250 6350
F 0 "RV4" H 2181 6396 50  0000 R CNN
F 1 "100k" H 2181 6305 50  0000 R CNN
F 2 "_NTSFootprints:Potentiometer_Alps_RK09L_Plated_Mount_Holes" H 2250 6350 50  0001 C CNN
F 3 "~" H 2250 6350 50  0001 C CNN
	1    2250 6350
	1    0    0    -1  
$EndComp
$Comp
L Device:R R18
U 1 1 5DE4CCD3
P 2800 6050
F 0 "R18" V 2593 6050 50  0000 C CNN
F 1 "100k" V 2684 6050 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 2730 6050 50  0001 C CNN
F 3 "~" H 2800 6050 50  0001 C CNN
	1    2800 6050
	0    1    1    0   
$EndComp
$Comp
L Device:R R20
U 1 1 5DE4CCD9
P 2500 6200
F 0 "R20" H 2430 6154 50  0000 R CNN
F 1 "100k" H 2430 6245 50  0000 R CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 2430 6200 50  0001 C CNN
F 3 "~" H 2500 6200 50  0001 C CNN
	1    2500 6200
	-1   0    0    1   
$EndComp
$Comp
L Device:R R21
U 1 1 5DE4CCDF
P 2500 6500
F 0 "R21" H 2430 6454 50  0000 R CNN
F 1 "100k" H 2430 6545 50  0000 R CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 2430 6500 50  0001 C CNN
F 3 "~" H 2500 6500 50  0001 C CNN
	1    2500 6500
	-1   0    0    1   
$EndComp
Wire Wire Line
	2400 6350 2500 6350
Connection ~ 2500 6350
Wire Wire Line
	1850 6050 2250 6050
Wire Wire Line
	2650 6050 2500 6050
Connection ~ 2500 6050
Wire Wire Line
	2950 6050 3000 6050
Wire Wire Line
	3200 5850 3000 5850
Wire Wire Line
	3000 5850 3000 6050
Connection ~ 3000 6050
Wire Wire Line
	3000 6050 3050 6050
Wire Wire Line
	3500 5850 3650 5850
Wire Wire Line
	3650 5850 3650 6150
Wire Wire Line
	2500 6650 3050 6650
Wire Wire Line
	2250 6200 2250 6050
Connection ~ 2250 6050
Wire Wire Line
	2250 6050 2500 6050
Wire Wire Line
	2500 6650 2250 6650
Wire Wire Line
	2250 6650 2250 6500
Connection ~ 2500 6650
Wire Wire Line
	1850 6150 1850 6650
Wire Wire Line
	1850 6650 2250 6650
Connection ~ 2250 6650
$Comp
L Device:R R19
U 1 1 5DE4CCFC
P 3900 6150
F 0 "R19" V 3693 6150 50  0000 C CNN
F 1 "100" V 3784 6150 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 3830 6150 50  0001 C CNN
F 3 "~" H 3900 6150 50  0001 C CNN
	1    3900 6150
	0    1    1    0   
$EndComp
Wire Wire Line
	3650 6150 3750 6150
Connection ~ 3650 6150
Wire Wire Line
	4050 6150 4150 6150
$Comp
L power:GND #PWR0113
U 1 1 5DE4CD05
P 3050 6650
F 0 "#PWR0113" H 3050 6400 50  0001 C CNN
F 1 "GND" H 3055 6477 50  0000 C CNN
F 2 "" H 3050 6650 50  0001 C CNN
F 3 "" H 3050 6650 50  0001 C CNN
	1    3050 6650
	1    0    0    -1  
$EndComp
Connection ~ 3050 6650
Wire Wire Line
	4150 6650 4150 6250
$Comp
L Device:C C7
U 1 1 5DE4CD0D
P 3350 5500
F 0 "C7" V 3098 5500 50  0000 C CNN
F 1 "10pF" V 3189 5500 50  0000 C CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 3388 5350 50  0001 C CNN
F 3 "~" H 3350 5500 50  0001 C CNN
	1    3350 5500
	0    1    1    0   
$EndComp
Wire Wire Line
	3200 5500 3000 5500
Wire Wire Line
	3000 5500 3000 5850
Connection ~ 3000 5850
Wire Wire Line
	3650 5850 3650 5500
Wire Wire Line
	3650 5500 3500 5500
Connection ~ 3650 5850
Wire Wire Line
	3050 6650 4150 6650
$Comp
L power:+5V #PWR0114
U 1 1 5DE4CD1A
P 1850 5950
F 0 "#PWR0114" H 1850 5800 50  0001 C CNN
F 1 "+5V" V 1865 6078 50  0000 L CNN
F 2 "" H 1850 5950 50  0001 C CNN
F 3 "" H 1850 5950 50  0001 C CNN
	1    1850 5950
	0    1    1    0   
$EndComp
NoConn ~ 4150 6050
$Comp
L power:PWR_FLAG #FLG0101
U 1 1 5DE56B76
P 10200 -500
F 0 "#FLG0101" H 10200 -425 50  0001 C CNN
F 1 "PWR_FLAG" H 10200 -327 50  0000 C CNN
F 2 "" H 10200 -500 50  0001 C CNN
F 3 "~" H 10200 -500 50  0001 C CNN
	1    10200 -500
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0115
U 1 1 5DE56EA7
P 10200 -500
F 0 "#PWR0115" H 10200 -750 50  0001 C CNN
F 1 "GND" H 10205 -673 50  0000 C CNN
F 2 "" H 10200 -500 50  0001 C CNN
F 3 "" H 10200 -500 50  0001 C CNN
	1    10200 -500
	1    0    0    -1  
$EndComp
$Comp
L power:+12V #PWR0116
U 1 1 5DE576F1
P 10500 -500
F 0 "#PWR0116" H 10500 -650 50  0001 C CNN
F 1 "+12V" H 10515 -327 50  0000 C CNN
F 2 "" H 10500 -500 50  0001 C CNN
F 3 "" H 10500 -500 50  0001 C CNN
	1    10500 -500
	1    0    0    -1  
$EndComp
$Comp
L power:-12V #PWR0117
U 1 1 5DE58A68
P 10850 -500
F 0 "#PWR0117" H 10850 -400 50  0001 C CNN
F 1 "-12V" H 10865 -327 50  0000 C CNN
F 2 "" H 10850 -500 50  0001 C CNN
F 3 "" H 10850 -500 50  0001 C CNN
	1    10850 -500
	-1   0    0    1   
$EndComp
$Comp
L power:PWR_FLAG #FLG0102
U 1 1 5DE5F233
P 10850 -500
F 0 "#FLG0102" H 10850 -425 50  0001 C CNN
F 1 "PWR_FLAG" H 10850 -327 50  0000 C CNN
F 2 "" H 10850 -500 50  0001 C CNN
F 3 "~" H 10850 -500 50  0001 C CNN
	1    10850 -500
	1    0    0    -1  
$EndComp
$Comp
L power:PWR_FLAG #FLG0103
U 1 1 5DE627B2
P 10500 -500
F 0 "#FLG0103" H 10500 -425 50  0001 C CNN
F 1 "PWR_FLAG" H 10500 -327 50  0000 C CNN
F 2 "" H 10500 -500 50  0001 C CNN
F 3 "~" H 10500 -500 50  0001 C CNN
	1    10500 -500
	-1   0    0    1   
$EndComp
$Comp
L power:+5V #PWR0118
U 1 1 5DE6AB00
P 9900 -500
F 0 "#PWR0118" H 9900 -650 50  0001 C CNN
F 1 "+5V" H 9915 -327 50  0000 C CNN
F 2 "" H 9900 -500 50  0001 C CNN
F 3 "" H 9900 -500 50  0001 C CNN
	1    9900 -500
	1    0    0    -1  
$EndComp
$Comp
L power:PWR_FLAG #FLG0104
U 1 1 5DE6BBBF
P 9900 -500
F 0 "#FLG0104" H 9900 -425 50  0001 C CNN
F 1 "PWR_FLAG" H 9900 -327 50  0000 C CNN
F 2 "" H 9900 -500 50  0001 C CNN
F 3 "~" H 9900 -500 50  0001 C CNN
	1    9900 -500
	-1   0    0    1   
$EndComp
$Comp
L Device:C C6
U 1 1 5DE6C020
P 8500 5300
F 0 "C6" H 8615 5346 50  0000 L CNN
F 1 "100nF" H 8615 5255 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 8538 5150 50  0001 C CNN
F 3 "~" H 8500 5300 50  0001 C CNN
	1    8500 5300
	1    0    0    -1  
$EndComp
$Comp
L Device:C C9
U 1 1 5DE6C70A
P 8500 5700
F 0 "C9" H 8615 5746 50  0000 L CNN
F 1 "100nF" H 8615 5655 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 8538 5550 50  0001 C CNN
F 3 "~" H 8500 5700 50  0001 C CNN
	1    8500 5700
	1    0    0    -1  
$EndComp
$Comp
L Device:C C5
U 1 1 5DE6CBA1
P 8000 5300
F 0 "C5" H 8115 5346 50  0000 L CNN
F 1 "10uF" H 8115 5255 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 8038 5150 50  0001 C CNN
F 3 "~" H 8000 5300 50  0001 C CNN
	1    8000 5300
	1    0    0    -1  
$EndComp
$Comp
L Device:C C8
U 1 1 5DE6D066
P 8000 5700
F 0 "C8" H 8115 5746 50  0000 L CNN
F 1 "10uF" H 8115 5655 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 8038 5550 50  0001 C CNN
F 3 "~" H 8000 5700 50  0001 C CNN
	1    8000 5700
	1    0    0    -1  
$EndComp
$Comp
L power:+12V #PWR0119
U 1 1 5DE78F46
P 8500 3700
F 0 "#PWR0119" H 8500 3550 50  0001 C CNN
F 1 "+12V" H 8515 3873 50  0000 C CNN
F 2 "" H 8500 3700 50  0001 C CNN
F 3 "" H 8500 3700 50  0001 C CNN
	1    8500 3700
	1    0    0    -1  
$EndComp
$Comp
L power:-12V #PWR0120
U 1 1 5DE7947E
P 8500 4300
F 0 "#PWR0120" H 8500 4400 50  0001 C CNN
F 1 "-12V" H 8515 4473 50  0000 C CNN
F 2 "" H 8500 4300 50  0001 C CNN
F 3 "" H 8500 4300 50  0001 C CNN
	1    8500 4300
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR0121
U 1 1 5DE7EC1C
P 8600 5500
F 0 "#PWR0121" H 8600 5250 50  0001 C CNN
F 1 "GND" V 8605 5372 50  0000 R CNN
F 2 "" H 8600 5500 50  0001 C CNN
F 3 "" H 8600 5500 50  0001 C CNN
	1    8600 5500
	0    -1   -1   0   
$EndComp
Wire Wire Line
	8600 5500 8500 5500
Wire Wire Line
	8000 5500 8000 5450
Wire Wire Line
	8000 5500 8000 5550
Connection ~ 8000 5500
Wire Wire Line
	8500 5450 8500 5500
Connection ~ 8500 5500
Wire Wire Line
	8500 5500 8000 5500
Wire Wire Line
	8500 5500 8500 5550
Wire Wire Line
	8000 5150 8500 5150
Connection ~ 8500 5150
Wire Wire Line
	8000 5850 8500 5850
Connection ~ 8500 5850
$Comp
L Connector_Generic:Conn_02x05_Odd_Even J7
U 1 1 5DEE03C1
P 10250 5500
F 0 "J7" H 10300 5167 50  0000 C CNN
F 1 "Conn_02x05_Odd_Even" H 10300 5166 50  0001 C CNN
F 2 "_NTSFootprints:PinHeader_2x05_P2.54mm_Vertical_Shrouded" H 10250 5500 50  0001 C CNN
F 3 "~" H 10250 5500 50  0001 C CNN
	1    10250 5500
	1    0    0    1   
$EndComp
$Comp
L Device:Polyfuse F1
U 1 1 5DEE1C21
P 9900 5300
F 0 "F1" V 9767 5300 50  0000 C CNN
F 1 "Polyfuse" V 9766 5300 50  0001 C CNN
F 2 "Fuse_Holders_and_Fuses:Fuse_SMD1206_HandSoldering" H 9950 5100 50  0001 L CNN
F 3 "~" H 9900 5300 50  0001 C CNN
	1    9900 5300
	0    1    1    0   
$EndComp
$Comp
L Device:D D1
U 1 1 5DEE30D1
P 9500 5350
F 0 "D1" V 9500 5429 50  0000 L CNN
F 1 "D" V 9545 5429 50  0001 L CNN
F 2 "Diodes_SMD:D_SMA_Handsoldering" H 9500 5350 50  0001 C CNN
F 3 "~" H 9500 5350 50  0001 C CNN
	1    9500 5350
	0    1    1    0   
$EndComp
$Comp
L Device:Polyfuse F2
U 1 1 5DEE3B0B
P 9900 5700
F 0 "F2" V 9767 5700 50  0000 C CNN
F 1 "Polyfuse" V 9766 5700 50  0001 C CNN
F 2 "Fuse_Holders_and_Fuses:Fuse_SMD1206_HandSoldering" H 9950 5500 50  0001 L CNN
F 3 "~" H 9900 5700 50  0001 C CNN
	1    9900 5700
	0    1    1    0   
$EndComp
$Comp
L Device:D D2
U 1 1 5DEE4BF9
P 9500 5650
F 0 "D2" V 9500 5729 50  0000 L CNN
F 1 "D" V 9545 5729 50  0001 L CNN
F 2 "Diodes_SMD:D_SMA_Handsoldering" H 9500 5650 50  0001 C CNN
F 3 "~" H 9500 5650 50  0001 C CNN
	1    9500 5650
	0    1    1    0   
$EndComp
Wire Wire Line
	10050 5400 10050 5500
Wire Wire Line
	10050 5500 10050 5600
Connection ~ 10050 5500
Wire Wire Line
	10550 5600 10050 5600
Connection ~ 10050 5600
Wire Wire Line
	10550 5500 10050 5500
Wire Wire Line
	10550 5400 10050 5400
Connection ~ 10050 5400
Wire Wire Line
	10550 5300 10050 5300
Connection ~ 10050 5300
Wire Wire Line
	10550 5700 10050 5700
Connection ~ 10050 5700
Wire Wire Line
	9750 5300 9750 5200
Wire Wire Line
	9750 5200 9500 5200
Wire Wire Line
	9500 5800 9750 5800
Wire Wire Line
	9750 5800 9750 5700
$Comp
L power:GND #PWR0122
U 1 1 5DF0A4AA
P 9500 5500
F 0 "#PWR0122" H 9500 5250 50  0001 C CNN
F 1 "GND" V 9505 5372 50  0000 R CNN
F 2 "" H 9500 5500 50  0001 C CNN
F 3 "" H 9500 5500 50  0001 C CNN
	1    9500 5500
	0    1    1    0   
$EndComp
Connection ~ 9500 5500
$Comp
L power:+12V #PWR0123
U 1 1 5DF0A999
P 9500 5200
F 0 "#PWR0123" H 9500 5050 50  0001 C CNN
F 1 "+12V" H 9515 5373 50  0000 C CNN
F 2 "" H 9500 5200 50  0001 C CNN
F 3 "" H 9500 5200 50  0001 C CNN
	1    9500 5200
	1    0    0    -1  
$EndComp
Connection ~ 9500 5200
$Comp
L power:-12V #PWR0124
U 1 1 5DF0B0FC
P 9500 5800
F 0 "#PWR0124" H 9500 5900 50  0001 C CNN
F 1 "-12V" H 9515 5973 50  0000 C CNN
F 2 "" H 9500 5800 50  0001 C CNN
F 3 "" H 9500 5800 50  0001 C CNN
	1    9500 5800
	-1   0    0    1   
$EndComp
Connection ~ 9500 5800
Wire Wire Line
	2500 6350 3050 6350
Wire Wire Line
	3050 6350 3050 6250
Wire Wire Line
	2500 4850 3050 4850
Wire Wire Line
	3050 4850 3050 4750
Wire Wire Line
	2500 3350 3050 3350
Wire Wire Line
	3050 3350 3050 3250
Wire Wire Line
	2500 1850 3050 1850
Wire Wire Line
	3050 1850 3050 1750
Wire Wire Line
	10050 5500 9500 5500
$EndSCHEMATC
