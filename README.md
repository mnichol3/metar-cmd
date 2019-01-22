# metar-cmd
A simple tool to fetch &amp; display METARs from NOAA's Aviation Weather Center
## Getting Started
### Prerequisites

- Python 2.7
- Anaconda (optional)

### Usage
The script takes US airport ICAO codes as arguments. Although ICAO codes are capitalized (i.e., KDCA), argument capitalization 
does not matter (Acceptable inputs: kdca; KDCA; kDcA; etc...). For example:

```
python metar-cmd.py kbwi kdca kiad
```

will display:

```
---------------------------------------------------------------------------------------
KBWI 222054Z 14003KT 10SM SCT160 BKN250 M01/M17 A3062 RMK AO2 SLP370 T10061167 56020
---------------------------------------------------------------------------------------
KDCA 222052Z 17005KT 10SM FEW150 BKN230 00/M15 A3064 RMK AO2 SLP373 T00001150 56025
---------------------------------------------------------------------------------------
KIAD 222052Z 17005KT 10SM FEW220 BKN250 M01/M16 A3060 RMK AO2 SLP367 T10061156 56024
---------------------------------------------------------------------------------------
Updating in: 5:00
```

The script updates the METARs every 5 minutes, and displayes a running timer counting down the minutes and seconds until the next
update in the lower left corner. In order to not display the update timer, enter `-t` as the first argument. For example:

```
python metar-cmd.py -t kbwi kdca kiad
```

yields:

```
---------------------------------------------------------------------------------------
KBWI 222054Z 14003KT 10SM SCT160 BKN250 M01/M17 A3062 RMK AO2 SLP370 T10061167 56020
---------------------------------------------------------------------------------------
KDCA 222052Z 17005KT 10SM FEW150 BKN230 00/M15 A3064 RMK AO2 SLP373 T00001150 56025
---------------------------------------------------------------------------------------
KIAD 222052Z 17005KT 10SM FEW220 BKN250 M01/M16 A3060 RMK AO2 SLP367 T10061156 56024
---------------------------------------------------------------------------------------
```

The script will still update the METARs even though the timer is not shown.



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

