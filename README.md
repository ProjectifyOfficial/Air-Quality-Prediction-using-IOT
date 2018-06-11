# Air Quality Prediction using IOT
Detecting Pollution Levels and giving information to Mobile and recording the values in the form of Spread Sheets.
## Getting Started
  This project attempts to build an efficient system which identifies highly polluted areas in less time.A drone is built with sensors like NO2, CO2, O2 etc, a micro controller and GPS. This drone is powered by lithium batteries and can be controlled remotely. The Central Pollution Control Board (CPCB) has set some standard concentration of gases that are present in a non-polluted environment. The drone flies around the city. For every 2 minutes the drone senses the concentration of gases and calculates whether the air is polluted or not. If it is polluted then GPS records the location. These values are sent to cloud or administrator via internet. Later a strict action can be taken by the Ministry.  This project also showed that a single cost effective system can efficiently identify polluted areas and also involves less human intervention involved with the traditional systems.

### Requirements 

* [Rawsberry Pi](http://amzn.in/h76Ptk2)
* [GAS SENSOR](http://amzn.in/aSMVMk1)
* [LIPO Batteries for Drone](http://amzn.in/dyLMOJ1) - runs maximum 1 hour 
* [Drone] crafted by own from youtube tutorials 
* check the rest of the requirements like API etc in Documents folder

### Building Drone with components

![Drone](https://user-images.githubusercontent.com/35171449/41200774-ddcde1da-6cc8-11e8-8500-5fbfd95666d6.png)

### Configuring Application
![putty config](https://user-images.githubusercontent.com/35171449/41200797-0e200994-6cc9-11e8-8e3b-057298ebf944.PNG)

### Result
![output screen1](https://user-images.githubusercontent.com/35171449/41200857-fd76d270-6cc9-11e8-81d8-e4b8bf090e8a.PNG)
![output screen3](https://user-images.githubusercontent.com/35171449/41200808-3dd93ffc-6cc9-11e8-81f2-d24f11a543b7.PNG)
![output screen4](https://user-images.githubusercontent.com/35171449/41200813-5c88028a-6cc9-11e8-8a6e-a979e7a5c269.PNG)
![spreadsheet](https://user-images.githubusercontent.com/35171449/41200829-9aafbb7a-6cc9-11e8-9c16-f9a5dd6206c1.PNG)

### References
* [1] WSN Based Air Pollution Monitoring System, International Journal of Science and Engineering Applications (IJSEA), Amol R. Kasar, Dnyandeo S. Khemnar, Nagesh P. Tembhurnikar, 2016
* [2] Zigbee Based Wireless Air Pollution Monitoring System Using Low Cost and Energy Efficient Sensors, International Journal of Engineering Trends and Technology (IJETT) – Volume 10 Number 9 Mr.Vasim K. Ustad , Prof.A.S.Mali, Mr.SuhasS.Kibile - Apr 2015
* [3] Using Social Media to Detect Outdoor Air Pollution and Monitor Air Quality Index (AQI) , PLoS ONE , Jiang W, Wang Y, Tsou M-H, Fu X, 2015
* [4] Sensor Deployment for Air Pollution Monitoring Using Public Transportation System, Evolutionary Computation (CEC), 2012 IEEE Congress on, 1.James J.Q. Yu, Victor O.K. Li, Albert Y.S. Lam, 2013 
* [5] Real Time Wireless Air Pollution Monitoring system. ICTACT Journal on Communication Technology, Prasad, Raja Vara and Baig, M Z and Mishra, R K and P, Rajalakshmi and Desai, U B and Merchant, 2011
* [6] Roger S Pressman,Software Engineering: A Practitioners Approach, 7th Edition Hardcover, 2014
