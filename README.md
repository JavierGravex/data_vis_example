# Data Visualization Dashboard
This project is an interactive web application built with Python, Dash, and Plotly. It allows users to visualize participant demographics using a dynamic Sunburst chart.

## Getting Started
Prerequisites
Ensure you have Python 3.8+ installed on your machine.

## Installation
1: Clone or Download this repository to your local machine.

2: Open your terminal (or VS Code terminal) and navigate to the project folder.

3: Install the required libraries using the following command:

```Bash
pip install -r requirements.txt
```

Project Structure
```
main.py The core script containing the Dash layout and logic.
```
```
datavis_test.csv The dataset (must be in the same folder as main.py).
```
```
requirements.txt: List of dependencies (pandas, dash, plotly).
```
## Running the App
Run the script from your terminal:

```Bash
python main.py
```
Once the script starts, you will see a message: Dash is running on http://127.0.0.1:8050/ (Or somthing similar)

Click the link or copy-paste it into your browser to view the dashboard.

## How It Works
The dashboard is divided into three main components:

1. Data Processing
Using Pandas, we load the CSV file into a "DataFrame." This acts like a high-performance spreadsheet that Python can manipulate instantly.

2. Interactive Layout
The interface consists of:

Dropdown Menu: Allows you to switch between different data hierarchies (e.g., viewing by Country first vs. Gender first).

Sunburst Chart: An interactive Plotly graph that expands and shrinks as you click on different segments.

3. The Callback (The "Logic")
The app uses a Callback function. This is a listener that detects when a user changes the dropdown selection. It automatically recalculates the chart hierarchy and updates the display without needing to refresh the page.
