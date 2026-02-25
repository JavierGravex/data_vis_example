# CoBiVa Data Visualization Project
### About CoBiVa
The CoBiVa (Corpus Bilingüe del Valle) documents the Spanish and English spoken in South Texas, specifically in the Rio Grande Valley. This digital oral corpus provides material for multiple linguistic analyses of local language varieties and subsequent comparisons with other varieties.

### Project Overview
This project provides an interactive data visualization suite built with Python, Pandas, and Plotly. The goal is to transform raw sociolinguistic data into intuitive, interactive maps of bilingual identity.


### Key Visualizations
Demographic Sunburst Chart: A multi-layered look at the participant pool, categorized by Birth Country, Gender, and Education level.

https://github.com/user-attachments/assets/d060771b-1963-45c5-954f-f59389f338ff

Linguistic Balance Pyramid: A mirrored bar chart comparing years of Spanish vs. English experience for each participant.

https://github.com/user-attachments/assets/78e3db97-bb0b-42c4-a7c3-6ad07d0e61c4

Language Dominance Scatter Plot: A 2D mapping of language experience that identifies "Balanced Bilinguals" vs. language-dominant individuals, with bubble sizes representing participant age to visualize generational shifts.

https://github.com/user-attachments/assets/26d14a96-340b-4552-a573-809ee0895b6a

## Getting Started
### Prerequisites
Python 3.8+

### A browser to view the interactive charts

### Installation
Clone or download this repository to your local machine.

Navigate to the project folder in your terminal:

``cd data_vis_example``
### Activate your Virtual Environment:
- Windows:
``.\venv\Scripts\activate``

- Install dependencies:
``pip install -r requirements.txt``

### Project Structure

- Example_01.ipynb: The primary Jupyter Notebook containing the data processing and all interactive visualizations.

- datavis_test.csv: The sanitized dataset used for the analysis (re-formatted for research purposes).

- requirements.txt: List of Python dependencies (Pandas, Plotly, Dash).

- .gitignore: Configured to exclude virtual environments and temporary system files.

### Usage
- Open Example_01.ipynb in VS Code or Jupyter.

- Run all cells to generate the interactive Plotly figures.

- Hover over data points in the Language Dominance Graph to see specific participant metadata (ID, Birth Country, Education).

# References:
- https://dash.plotly.com/dash-core-components
- https://dash.gallery/Portal/
- https://plotly.com/python-api-reference/plotly.express.html
- https://plotly.com/python/

