# 📊 Online Course Progress Tracker
https://github.com/Shubhanshu007iit/online-course-progress-tracker

A Python-based project to track and visualize online course progress from a dataset (`kpis.txt.in`).  
It generates charts, KPIs, and saves results for easy performance monitoring.

---

## 📌 Features
- **Progress Table**: Shows each user's completion percentage
- **Bar Chart**: Completion percentage per user
- **Pie Chart**: Completion categories (High, Medium, Low)
- **KPIs**: Average progress and total dropouts
- **Image Exports**: All charts saved in `images/` folder

---

## 📂 Project Structure
online-course-progress-tracker/
│
├── course_progress_eda.py # Main Python script
├── kpis.txt.in # Dataset file
├── requirements.txt # Dependencies
├── images/ # Generated charts
└── README.md # Documentation

## 🛠️ Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/online-course-progress-tracker.git
   cd online-course-progress-tracker
    ▶️ Usage
Run the script:
python course_progress_eda.py
The script will:
Load kpis.txt.in
Display and save charts to the images/ folder
Save KPIs to kpis_output.tx4. Commit new file.
### **5️⃣ Add `kpis.txt.in`*
kpis.txt.in

dataset:
```csv
UserID,Name,Course Name,Modules con,total Module,%,Status
1,Ram,Python101,10,10,60,InProgress
2,Alice,Datascience102,8,10,100,Completed
3,Malan,ML103,6,10,80,Dropout
4,Jack,Financial Economics104,6,10,20,InProgress
5,Nova,Fsd105,5,10,40,Dropout
6,Bob,Data Analytics106,4,10,30,InProgress
7,Prince,Mathematics107,3,10,70,Completed
8,Sam,English108,1,10,50,Dropout
9,Stokes,Ai109,8.7,10,10,InProgress
10,Ben,Computer Science110,7.5,10,90,Completed
