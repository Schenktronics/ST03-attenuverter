# Bill of Materials — Attenuverter v1.0

A machine-readable copy is in [BOM.csv](BOM.csv). The original spreadsheet is [Attenuverter/attenuverter BOM.xlsx](<../Attenuverter/attenuverter BOM.xlsx>).

All the resistors, capacitors, diodes, fuses and chips are surface-mount parts on the back of the board. The resistors and capacitors are 0805 size. Parts marked "or equivalent" can be swapped for any part with the same value, package and pinout.

The **Easy Build Kit** includes a PCB with every surface-mount part below already soldered and tested — you only need to source the through-hole parts.

## Surface-mount parts (back of the board)

| Qty | Reference | Part | Manufacturer / Part No. | Notes |
|----:|-----------|------|--------------------------|-------|
| 1 | U1 | Quad JFET op-amp, SOIC-14 | Texas Instruments TL074CDR, or equivalent | [Datasheet](https://www.ti.com/lit/ds/symlink/tl074.pdf). The schematic says TL084; the TL084 and TL074 have the same pinout, and either one works. |
| 1 | U2 | 5.0 V shunt voltage reference, SOT-23-3 | Microchip LM4040DYM3-5.0-TR, or equivalent | The schematic uses TI's LM4040 in the DBZ package: [datasheet](https://www.ti.com/lit/ds/symlink/lm4040.pdf). An equivalent must have the cathode on pin 1 and the anode on pin 2. Sets the +5 V that unplugged inputs receive. |
| 16 | R1, R2, R4, R5, R6, R7, R9, R10, R12, R13, R15, R16, R17, R18, R20, R21 | Resistor, 100 kΩ, 1%, 0805 | Yageo RC0805FR-07100KL, or equivalent | |
| 13 | R3, R8, R11, R14, R19, R22–R29 | Resistor, 1 kΩ, 1%, 0805 | Yageo RC0805FR-071KL, or equivalent | R3, R8, R14 and R19 are the output resistors, one per channel. R11 feeds the 5 V reference. R22–R29 are part of the input protection. |
| 4 | C1, C2, C3, C7 | Capacitor, 10 pF, 50 V, C0G/NP0, 0805 | Yageo CC0805JRNPO9BN100, or equivalent | |
| 3 | C4, C6, C9 | Capacitor, 100 nF, 25 V, X7R, 0805 | AVX 08053C104KAT2A, or equivalent | |
| 2 | C5, C8 | Capacitor, 10 µF, 25 V, X5R, 0805 | Taiyo Yuden TMK212BBJ106KG-T, or equivalent | |
| 2 | D1, D2 | Diode, 1 A, 300 V, SMA | ON Semiconductor MRA4003T3G, or equivalent | Reverse-power protection. The cathode (stripe) end matters. |
| 9 | D3–D11 | Diode, 1N4148, SOD-323, 75 V, 150 mA | Diodes Incorporated 1N4148WS-7-F, or equivalent | [Datasheet](https://datasheet.octopart.com/1N4148WS-7-F-Diodes-Inc.-datasheet-7284054.pdf). Input protection. The cathode (stripe) end matters. |
| 2 | F1, F2 | Resettable fuse (PTC), 200 mA hold, 30 V, 1206 | Bel Fuse 0ZCJ0020FF2E, or equivalent | Either way round |

## Through-hole parts

| Qty | Reference | Part | Manufacturer / Part No. | Notes |
|----:|-----------|------|--------------------------|-------|
| 1 | J7 | Shrouded pin header, 2 × 5, 2.54 mm, vertical | On Shore Technology 302-S101, or equivalent | Eurorack power connector. Fits on the back. |
| 8 | J1–J6, J8, J9 | 3.5 mm mono switched jack, vertical PCB mount, with nut | QingPu WQP-PJ398SM or WQP518MA, or equivalent. Either one works. CUI MJ-3507 also works, with a ground wire. | [Datasheet / product page](http://www.qingpu-electronics.com/en/products/WQP-PJ398SM-362.html). The inputs use the switched contact for the +5 V normal. The footprint also takes the CUI MJ-3507 ([datasheet](https://www.cuidevices.com/product/resource/mj-3507.pdf)), which is on Mouser: its tip and switch pins go into the board, and its sleeve lug needs a short wire to the jack's square ground pad. |
| 4 | RV1–RV4 | Potentiometer, 100 kΩ linear, 9 mm, center detent, bushingless, 25 mm flat (D) shaft, with board-lock lugs | Bourns PTV09A-4225F-B104, or equivalent | [Datasheet](https://www.bourns.com/docs/Product-Datasheets/PTV09.pdf). The center detent marks zero. There's no threaded bushing or nut: the pots are held by the PCB. An equivalent must fit the 9 mm footprint (3 pins in a row, 2 mounting lugs) and pass through the 7 mm panel hole. |
| 4 | — | Knob, for 6 mm shaft | Davies Molding 1221-J, or equivalent | An equivalent must fit the pot's D shaft. |
| 1 | — | Main PCB, 30 × 100 mm, 2-layer, 1.6 mm FR4 | Schenktronics | Gerbers: [AttenuverterGerbers.zip](../Attenuverter/AttenuverterGerbers.zip) |
| 1 | — | Faceplate, 6HP (30 × 128.5 mm), 1.6 mm aluminium PCB | Schenktronics | Gerbers: [AttenuverterFaceplateGerbers.zip](../AttenuverterFaceplate/AttenuverterFaceplateGerbers.zip). Single-sided, so it can also be made in FR4. |
| 1 | — | Eurorack power cable, 10-pin to 16-pin | | Red stripe marks −12 V. |

## Not included

| Qty | Part | Notes |
|----:|------|-------|
| 4 | M3 rack screws | Supplied with most Eurorack cases. Two, in diagonally opposite corners, will hold the module. |

## Ordering the parts

There's a [Mouser project](https://www.mouser.com/ProjectManager/ProjectDetail.aspx?AccessID=490ed0ce39) with the parts for building from bare PCBs. Mouser doesn't stock QingPu jacks, so the project uses CUI MJ-3507 jacks instead. They fit the board, but each one needs a ground wire: see the note in Step 6 of the [assembly guide](assembly-guide.md#step-6--solder-the-pots-and-jacks).
