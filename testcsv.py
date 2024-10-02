
import csv
# Definisci i nomi delle colonne e i valori ordinati
column_names = ["nodes_number",	"max_capacity", "num_edges", "source node",
                "sink node", "experiments", "mean_time_fifo", "std_time_fifo",
                "max_flow_list_fifo", "mean_time_sapa", "std_time_sapa",
                "max_flow_list_sapa"]

data = [("A", 1, 2,3,4,5,6,7,8,9, 10, 11)]

# Specifica il nome del file CSV da creare
csv_file_name = "multi_column_values.csv"

# Scrivi l'intestazione solo se il file è vuoto
try:
    with open(csv_file_name, mode='x', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(column_names)
except FileExistsError:
    pass  # Il file esiste già, quindi non scrivere l'intestazione


# Scrivi nel file CSV
with open(csv_file_name, mode='a', newline='') as file:

    writer = csv.writer(file)

    # Scrivi l'intestazione (nomi delle colonne)
    writer.writerow(column_names)

    # Scrivi i valori
    writer.writerows(data)

print(f"CSV file '{csv_file_name}' created successfully.")