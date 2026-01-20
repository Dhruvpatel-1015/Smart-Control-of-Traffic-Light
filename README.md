🚦 Smart Control of Traffic Light Using YOLOv8
📌 Overview

This project implements an AI-based intelligent traffic signal control system using YOLOv8 object detection to dynamically manage traffic lights based on real-time vehicle density. Unlike traditional fixed-timer traffic signals, this system adapts green light duration according to traffic congestion, improving road efficiency and reducing unnecessary waiting time.

The model is trained on a custom-annotated dataset consisting of traffic images, where vehicles such as cars, buses, trucks, and bikes were manually labeled and used to train a YOLOv8 detection model.

🎯 Objectives

Detect vehicles in real-time using deep learning
Count vehicles per lane dynamically
Allocate green signal duration based on traffic density
Reduce congestion and idle waiting time at intersections

🧠 Technologies Used

Python
YOLOv8 (Ultralytics)
OpenCV
PyTorch
NumPy

🏗 Project Structure
Smart-Control-of-Traffic-Light/
│── models/
│   └── best.pt
│
│── notebooks/
│   └── training.ipynb
│
│── src/
│   ├── detect.py
│   ├── traffic_controller.py
│   └── utils.py
│
│── sample_data/
│   └── test.jpg
│
│── results/
│   └── output_samples/
│
│── README.md
│── requirements.txt
│── .gitignore

⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/Dhruvpatel-1015/Smart-Control-of-Traffic-Light.git
cd Smart-Control-of-Traffic-Light

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ How to Run
🔹 Run Vehicle Detection
python src/detect.py

🔹 Run Traffic Signal Logic
python src/traffic_controller.py

📊 Features

Custom dataset annotation and training pipeline
Real-time vehicle detection
Lane-wise traffic density estimation
Dynamic green light duration control
Modular and scalable project structure

🧪 Dataset

The dataset used in this project was custom collected and manually annotated.
Due to privacy and ownership constraints, it is not publicly shared, but the training pipeline is fully reproducible.

🚀 Results

Successfully detected multiple vehicle classes in real-time
Demonstrated adaptive signal timing based on traffic density
Reduced idle signal time in simulated scenarios

🔮 Future Enhancements

Multi-camera intersection support
Emergency vehicle prioritization
Edge-device deployment (Jetson Nano / Raspberry Pi)
Web dashboard for real-time monitoring

👨‍💻 Author
Dhruv Patel
Computer Science Graduate | AI & Computer Vision Enthusiast
GitHub: https://github.com/Dhruvpatel-1015

📄 License
This project is licensed under the MIT License.