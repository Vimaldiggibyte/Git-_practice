import csv

def load_data(filepath):
    with open(filepath, newline='') as f:
        return list(csv.DictReader(f))

def save_data(data, filepath):
    if not data:
        return
    with open(filepath, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
def remove_nulls(data):
    clean = [row for row in data if row['customer'] and row['amount']]
    print(f"After removing nulls: {len(clean)} rows")
    return clean

def main():
    data = load_data('data/sales_data.csv')
    print(f"Loaded {len(data)} rows")

    data = remove_nulls(data)        # ← new line

    save_data(data, 'data/clean_sales.csv')
    print("Saved to data/clean_sales.csv")

if __name__ == '__main__':
    main()