# 📊 Course Progress EDA & Visualizations
# Author: Shubhanshu Kumar (Final Version)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import Tk, filedialog

# ------------------------------
# 1️⃣ Select & Load Dataset
# ------------------------------
Tk().withdraw()  # Hide the small Tkinter window
file_path = filedialog.askopenfilename(
    title="Select the Course Progress CSV File",
    filetypes=[("CSV Files", "*.csv")]
)

if not file_path:
    raise FileNotFoundError("No file selected. Please choose a CSV file.")

df = pd.read_csv(file_path)

# ------------------------------
# 2️⃣ Data Cleaning
# ------------------------------
df.rename(columns={
    'Modules con': 'Modules Completed',
    'total Module': 'Total Modules',
    '%': 'Completion (%)'
}, inplace=True)

df['Modules Completed'] = df['Modules Completed'].astype(int)

sns.set(style="whitegrid")

# ------------------------------
# 3️⃣ Bar Chart: Modules Completed per User
# ------------------------------
plt.figure(figsize=(10,6))
sns.barplot(
    data=df.sort_values(by="Modules Completed", ascending=False),
    x='Name', 
    y='Modules Completed',
    hue='Course Name',
    palette="viridis",
    dodge=False
)
plt.title("Modules Completed per User", fontsize=16, weight='bold')
plt.xlabel("User Name")
plt.ylabel("Modules Completed")
plt.xticks(rotation=45)
plt.legend(title="Course Name")
plt.show()

# ------------------------------
# 4️⃣ Column Chart: Average Completion per Course
# ------------------------------
plt.figure(figsize=(10,6))
sns.barplot(
    data=df,
    x='Course Name',
    y='Completion (%)',
    hue='Course Name',
    palette="coolwarm",
    legend=False
)
plt.title("Average Completion (%) by Course", fontsize=16, weight='bold')
plt.xlabel("Course Name")
plt.ylabel("Average Completion (%)")
plt.xticks(rotation=45)
plt.show()

# ------------------------------
# 5️⃣ Pie Chart: Status Distribution
# ------------------------------
status_counts = df['Status'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(
    status_counts,
    labels=status_counts.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=sns.color_palette("Set2"),
    wedgeprops={'edgecolor': 'white'}
)
plt.title("Course Status Distribution", fontsize=16, weight='bold')
plt.show()

# ------------------------------
# 6️⃣ Histogram: Completion Percentage
# ------------------------------
plt.figure(figsize=(8,5))
sns.histplot(df['Completion (%)'], bins=5, kde=True, color='skyblue')
plt.title("Distribution of Course Completion (%)", fontsize=16, weight='bold')
plt.xlabel("Completion Percentage")
plt.ylabel("Number of Students")
plt.show()

# ------------------------------
# 7️⃣ Boxplot: Completion % by Status
# ------------------------------
plt.figure(figsize=(8,5))
sns.boxplot(
    data=df,
    x='Status',
    y='Completion (%)',
    palette="pastel"
)
plt.title("Completion (%) by Status", fontsize=16, weight='bold')
plt.show()

# ------------------------------
# 8️⃣ Heatmap: Correlation
# ------------------------------
plt.figure(figsize=(6,4))
sns.heatmap(
    df[['Modules Completed', 'Total Modules', 'Completion (%)']].corr(),
    annot=True,
    cmap="YlGnBu",
    fmt=".2f"
)
plt.title("Correlation Heatmap", fontsize=14, weight='bold')
plt.show()
# KPI values
average_progress = 54.00
total_dropouts = 7

# Text to save
kpi_text = f"Average Progress: {average_progress:.2f}%\nTotal Dropouts: {total_dropouts}"

# Save file in current folder
with open("kpis.txt.in", "w") as file:
    file.write(kpi_text)

print("File saved as kpis.txt.in")
