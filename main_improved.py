from FIFO_improved import MaxFlow
from problem_generator_improved import DirectedGraph,generate_random_graph
from SAPA import MaxFlowSAPA
import time
from numpy import mean,std
from res import build_residual_graph
import csv

def algoritmo_lanciato_in_loop(ver, edg, wei, experiment_rep):
    source = 0
    sink = ver - 1

    # ver = int(input("Insert the number of nodes:"))
    # edg = float(input("Insert the number of edges:"))
    # wei = int(input("Insert the max capacity of the graph edges:"))

    graph = generate_random_graph(ver,edg,wei)
    # for edge in graph.getEdges():
    #     print(edge)

    time_rep_fifo = []
    max_flow_list_fifo = []

    time_rep_sapa = []
    max_flow_list_sapa = []


    for i in range(experiment_rep):
        start = time.time()
        maxFlow = MaxFlow(graph, source, sink)
        max_flow_list_fifo.append(maxFlow.FIFOPushRelabel())
        end = time.time()
        time_rep_fifo.append(end-start)
    mean_time_fifo = mean(time_rep_fifo)
    std_time_fifo = std(time_rep_fifo)
    print(time_rep_fifo)
    print(f"mean time FIFO: {mean_time_fifo}")
    print(f"std time FIFO: {std_time_fifo}")
    print(f"max flow FIFO: {max_flow_list_fifo}")

    for i in range(experiment_rep):
        start = time.time()
        maxFlow = MaxFlowSAPA(graph,source,sink)
        flow = maxFlow.shortest_augmenting_path()
        max_flow_list_sapa.append(sum(flow[0]))
        end = time.time()
        time_rep_sapa.append(end-start)
    mean_time_sapa = mean(time_rep_sapa)
    print(time_rep_sapa)
    std_time_sapa = std(time_rep_sapa)
    print(f"mean time SAPA: {mean_time_sapa}")
    print(f"std time SAPA: {std_time_sapa}")
    print(f"max flow SAPA: {max_flow_list_sapa}")

    # Define the column name and the ordered list of values
    column_name = "Values"
    ordered_values = []

    # Definisci i nomi delle colonne e i valori ordinati
    column_names = ["nodes_number", "max_capacity", "num_edges", "source node",
                    "sink node", "experiments", "mean_time_fifo", "std_time_fifo",
                    "max_flow_list_fifo", "mean_time_sapa", "std_time_sapa",
                    "max_flow_list_sapa"]

    data = [(ver, wei, edg, source,
             sink, experiment_rep, mean_time_fifo, std_time_fifo,
             max_flow_list_fifo, mean_time_sapa, std_time_sapa, max_flow_list_sapa)]

    # Specifica il nome del file CSV da creare
    csv_file_name = "risultati_esperimenti_progettoV2.csv"

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

        # Scrivi i valori
        writer.writerows(data)

    print(f"CSV file '{csv_file_name}' created successfully.")




if __name__ == "__main__":
    for vertici in [1000,2000,4000,8000,16000]:
        for pesi in [100, 150, 200, 250, 300, 350, 400, 450, 500]:
            algoritmo_lanciato_in_loop(vertici, vertici*2, pesi, 5)
            print(f"Eseguito test con {vertici} pesi {pesi}")