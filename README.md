# REAL-TIME-PROJECT
# Climate Data Visualiser

The **Climate Data Visualiser** is a Python application that provides visualizations of climate data such as temperature, humidity, wind speed, and pressure over time. It supports various types of graphs, including Line plots, Bar charts, Scatter plots, Histograms, and Pie charts for better data visualization and analysis.

## Features
- **Line Plot**: Displays the trend of temperature over time.

## Requirements
- Python 3.7+
- pandas
- matplotlib
- seaborn

## Installation
1. Clone the repository or download the files.
   ```bash
   git clone https://github.com/Svignesh16/climate-data-visualiser.git
   cd climate-data-visualiser
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Ensure you have a CSV file containing the climate data.

2. Run the script to generate visualizations:
   ```bash
   python climate_data_visualiser.py
   ```
3. The script will generate the following graphs:
   - line plot

## File Structure
- **climate_data_visualiser.py**: The main script that loads the data and generates the graphs.
- **Climate Data.csv**: Example CSV file containing climate data.
- **README.md**: Documentation for the project.

## Example Output
1. **Line Plot**: Mean Temperature Trend  
   ![Line Plot](example_line_plot.png)

## Data Format
The input data should be in CSV format with the following columns:
- `date`: The date of the record (YYYY-MM-DD format).
- `meantemp`: The mean temperature (in Celsius).
- `humidity`: The humidity percentage.
- `wind_speed`: The wind speed (in km/h).
- `meanpressure`: The mean atmospheric pressure (in hPa).

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your improvements.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author
Created by [Svignesh16](https://github.com/Svignesh16)
