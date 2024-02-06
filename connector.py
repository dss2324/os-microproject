from algorithms import *
import second_screen
import json
#dictionary mapping algorithm identifiers to their corresponding functions
algos = {
    '1': first_come_first_serve,
    '2': shortest_job_first,
    '3': round_robin 
}


def main():
    #reading process data fom data.json
    with open('data.json', "r") as read_file:
        data = json.load(read_file)
    #reading the selected algorithm identifier from f1.txt
    f = open('fl.txt')
    txt = next(f)
    txt = txt.strip('\n')
    #if the selected algorithm is round robin,read time quantm from f1.txt
    if txt == '3':
        tq = next(f)
    f.close()
    #applying the selected algorithm to the data
    if txt == '3':
        res = algos[txt](data, int(tq))
    else:
        res = algos[txt](data)
    #calculating average turnaround and waiting time 
    avg = avg_wt_tat(res)
    #writing the modified data bback to data.json
    data_f = open('data.json', 'w')
    data_f.write(json.dumps(res))
    data_f.close()
    #returning calculate avg turnaround and waiting time
    return avg

#here data.json serves as central data storage file that maintain 
#the state of processes both as input for scheduling algorithm and as ouput after
#their execution
