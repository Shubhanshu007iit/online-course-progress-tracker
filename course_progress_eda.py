
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import Tk, filedialog

Tk().withdraw()
file_path = filedialog.askopenfilename(title="Select Course Progress CSV", filetypes=[("CSV Files", "*.csv")])
if not file_path:
    raise FileNotFoundError("No file selected.")

df = pd.read_csv(file_path)
df.columns = df.columns.str.strip()
if '%' in df.columns:
    df.rename(columns={'%': 'Completion (%)'}, inplace=True)

print("\nUser Progress (%):")
print(df[['Name', 'Completion (%)']].to_string(index=False))

plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Name', y='Completion (%)', palette="Blues_d")
plt.title("Completion Percentage per User")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

def category(p):
    if p >= 80: return 'High'
    elif p >= 50: return 'Medium'
    return 'Low'

df['Category'] = df['Completion (%)'].apply(category)
counts = df['Category'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140,
        colors=sns.color_palette("Set2"), wedgeprops={'edgecolor': 'white'})
plt.title("Completion Categories")
plt.show()

avg = df['Completion (%)'].mean()
dropouts = (df['Status'].str.lower() == 'dropped').sum()
print(f"\nAverage Progress: {avg:.2f}%")
print(f"Total Dropouts: {dropouts}")

with open("kpis.txt", "w") as f:
    f.write(f"Average Progress: {avg:.2f}%\nTotal Dropouts: {dropouts}")

print("KPI metrics saved to kpis.txt")

