import datetime
import csv
import matplotlib.pyplot as plt

class calculationsRecord:
    def __init__(self, date, amount, category, unit, source):
        self.date = datetime.datetime.strptime(date, '%Y-%m-%d')
        self.amount = amount
        self.category = category
        self.unit = unit
        self.source = source
    
    def __repr__(self):
        return f"calculationsRecord(date={self.date}, amount={self.amount}, category='{self.category}', unit='{self.unit}', source='{self.source}')"

class CompanyData:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def load_data(self, file_path):
        self._load_csv(file_path)

    def _load_csv(self, file_path):
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                record = calculationsRecord(row['date'], float(row['amount']), row['category'], row['unit'], row['source'])
                self.add_record(record)

    def get_summary(self):
        summary = {}
        for record in self.records:
            if record.category not in summary:
                summary[record.category] = 0
            summary[record.category] += record.amount
        return summary

    def __repr__(self):
        return f"CompanyData(records={self.records})"

class DataVisualizer:
    @staticmethod
    def plot_calculations_trend(company_data):
        dates = [record.date for record in company_data.records]
        amounts = [record.amount for record in company_data.records]

        plt.plot(dates, amounts, marker='o')
        plt.title('Calculations Trend')
        plt.xlabel('Date')
        plt.ylabel('Amount')
        plt.show()

# Example usage:
if __name__ == "__main__":
    company_data = CompanyData()
    # Load data from a CSV file (change the file path as needed)
    company_data.load_data('climate_Data.csv')
    
    # Print the summary of amounts by category
    summary = company_data.get_summary()
    print("Amounts Summary by Category:", summary)
    
    # Plot the calculations trend
    DataVisualizer.plot_calculations_trend(company_data)