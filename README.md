# 🎥 YouTube Content Intelligence

An end-to-end Data Analytics project that collects, cleans, and analyzes YouTube video data from AI-focused content creators.

The project demonstrates a complete data analytics workflow using Python, including web scraping, data preprocessing, feature engineering, and exploratory data analysis (EDA).

---

# 📌 Project Objectives

The objectives of this project are to:

- Collect YouTube video information from multiple AI channels
- Build a structured dataset using Python
- Clean and preprocess the collected data
- Perform exploratory data analysis (EDA)
- Discover meaningful insights from video performance

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- yt-dlp
- Jupyter Notebook
- Git
- GitHub

---

# 📂 Project Structure

```
youtube-content-intelligence
│
├── data
│   ├── raw
│   └── cleaned
│
├── notebooks
│   ├── 01_data_cleaning.ipynb
│   └── 02_eda.ipynb
│
├── scraper
│   ├── config.py
│   ├── scrape_videos.py
│   └── main.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 📊 Dataset

The dataset contains YouTube video information collected from multiple AI-related YouTube channels.

### Features

- Channel Name
- Video Title
- Video URL
- Views
- Likes
- Comments
- Upload Date
- Video Duration
- Description
- Thumbnail
- Channel Subscribers
- Tags

### Engineered Features

- Duration (Minutes)
- Engagement Rate
- Upload Year
- Title Length
- Description Length
- Tag Count

---

# 🧹 Data Cleaning

The preprocessing process included:

- Handling missing values
- Removing duplicate records
- Creating new analytical features
- Standardizing data types
- Preparing the dataset for analysis

---

# 📈 Exploratory Data Analysis

The analysis answers several business questions, including:

- How are video views distributed?
- Does video duration affect popularity?
- Is there a relationship between views and likes?
- Do higher views generate more comments?
- Which videos receive the highest number of views?
- Which variables are strongly correlated?

Visualizations include:

- Distribution of Views
- Distribution of Video Duration
- Distribution of Engagement Rate
- Views vs Likes
- Views vs Comments
- Duration vs Views
- Correlation Heatmap
- Top 10 Most Viewed Videos
- Top 10 Most Engaging Videos

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/fizaabbas0345-png/youtube-content-intelligence.git
```

Move into the project folder:

```bash
cd youtube-content-intelligence
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Scraper

```bash
python scraper/main.py
```

---

# 📌 Project Status

- ✅ Web Scraping
- ✅ Data Cleaning
- ✅ Exploratory Data Analysis

---

# 👩‍💻 Author

**Fiza Abbas**

GitHub:
https://github.com/fizaabbas0345-png