# Data Analysis: Osteoporosis Risk Prediction

## Description
This repository contains dashboards and reports with data related to osteoporosis risk prediction. Osteoporosis is a health condition that weakens bones, making them brittle and more likely to break. The objective of this project is to use data analysis techniques to predict the risk of osteoporosis in patients based on different variables, such as age, bone mineral density, medical history, among others.


## Repository Structure
- `data/`: Folder containing data sets used in the analysis.
- `converter.py`: Python script for converting data in .csv to .json, to run the script just run the command `python convert.py`
- `docs/`: Folder contains additional documentation
- `PYTHON.md` - Installing and configuring Python on your local machine
- `NETXJS.md` - Installing nodejs to run the front-end in netxjs
- `bone-vision-api/`: Folder with Python API for analyzing osteoporosis data
- `bone-vision-frontend/`: Visually displaying data


## Data set
The dataset provides comprehensive information on the health factors that influence the development of osteoporosis, including demographic details, lifestyle choices, medical history, and bone health indicators. The goal is to facilitate research into osteoporosis prediction by enabling machine learning models to identify at-risk individuals. Analysis of factors such as age, sex, hormonal changes and lifestyle habits can help improve osteoporosis management and prevention strategies.


## Requirements 

* [Python](PYTHON) - Installation and configuration
* [NEXTJS] - Installation and configuration


## Getting Started

#### Backend

Navigate to the `bone-vision-api` directory of the project.

1 - Once the dependencies are installed, start the backend server by running:

```bash
uvicorn main:app --reload
``` 

The backend server should now be running on `http://127.0.0.1:8000`.





## Contribution

Contributions to this repository are welcome. If you would like to contribute fixes, improvements, or new analysis, please follow the project's contribution guidelines and open a pull request.


## License
This project is distributed under the [MIT](LICENSE).