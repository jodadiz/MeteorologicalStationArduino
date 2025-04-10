# Meteorological Station using Arduino Development Board

## Description

This project involves building a meteorological station using an Arduino development board and various sensors to measure temperature, humidity, and luminance (via a photoresistor). The system collects data from these sensors and displays it through both additional hardware (LCD screen and LEDs) and a graphical interface on a computer.

The project utilizes **pthreads** to handle parallel processing, ensuring that tasks are synchronized efficiently. Sensor data is sent via the serial port to the computer, where it is shown through a graphical interface built with **WxPython**. The interface also generates real-time graphs to visualize the collected data.

### Key Features
- **Sensor Integration**: Collects temperature, humidity, and luminance data using specialized sensors.
- **Parallel Processing**: Uses pthreads to ensure that sensor data collection and processing occur concurrently and efficiently.
- **Graphical Interface**: Built using WxPython, the interface displays the collected data and generates graphs for easy visualization.
- **Hardware Interface**: Data is displayed on an LCD screen and with LEDs for a more qualitative representation of the measurements.

## Objectives
- Measure temperature, humidity, and luminance using specific sensors.
- Use pthreads for parallel and synchronized task execution in the microcontroller.
- Design and build the necessary circuit for a functional meteorological station.
- Display the collected data both on additional hardware (LCD screen, LEDs) and a graphical interface.
- Send sensor data to the computer via the serial port, where it is displayed and saved using the graphical interface.
- Generate real-time graphs from the data collected.
