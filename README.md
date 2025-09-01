# Security-Camera-Analysis-BriefCam-Collaboration.
A Python-based system for real-time object detection and tracking using a Raspberry Pi camera and a Windows server.
The Raspberry Pi captures and streams images via sockets, while the server processes them with OpenCV and stores the results in CSV format.

Features:

-Capture images directly from Raspberry Pi camera

-Send image data to a Windows machine using sockets

-Detect and track objects/faces with OpenCV

-Store results in structured CSV files

-Works even with low-performance hardware (Raspberry Pi)

-Tech Stack


Language: Python 3

Core Libraries: OpenCV, numpy, pandas, imutils, Pillow, socket

Hardware: Raspberry Pi (Linux) + Windows PC

Development Environments: PyCharm, Thonny


📂 Project Structure
Security-Camera-Analysis-BriefCam/
│
├── raspberry/        # Raspberry Pi side
│   └── capture.py
│
├── server/           # Windows side
│   ├── receive.py
│   ├── detect.py
│   └── save_csv.py
│
├── models/           # Pre-trained models (if applicable)
│
└── README.md

Installation
# Clone repository
git clone https://github.com/hiEester/Security-Camera-Analysis-BriefCam.git
cd Security-Camera-Analysis-BriefCam

# Install dependencies
pip install -r requirements.txt

Usage
On Raspberry Pi (image capture & send):
python raspberry/capture.py

On Windows PC (receive & detect)
python server/receive.py
python server/detect.py

Results will be saved into CSV files for analysis.
