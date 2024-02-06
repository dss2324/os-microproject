#function to calculate average waiting time and average turnaround time
def avg_wt_tat(data):
    for dct in data:
        dct['tat'] = dct['ct'] - dct['at']
        dct['wt'] = dct['tat'] - dct['bt']
    tot_wt = tot_tat = 0
    for dct in data:
        tot_wt += dct['wt']
        tot_tat += dct['tat']
    ln = len(data)
    return {'avg_tat': tot_tat/ln, 'avg_wt': tot_wt/ln}

#function for fcfs algorithm
def first_come_first_serve(data):
    #create list arrival_time with elements [arrival_time,process_id,index]
    arrival_time = []
    indx = 0
    for i in data:
        arrival_time.append([i['at'], i['id'], indx])
        indx += 1
    #sort processes based on arrival time
    arrival_time.sort()
    curr_time = 0
    #iterate through processes sorted by arrival time
    for val in arrival_time:
        #if process arrive after current time wait for it to arrive
        if data[val[2]]['at'] > curr_time:
            curr_time += data[val[2]]['at'] - curr_time
        #update completion time for the current process based on burst time
        curr_time += data[val[2]]['bt']
        data[val[2]]['ct'] = curr_time
    return data

#use to represent and store information about process
data = [{'id': '1', 'at': 0, 'bt': 3},
        {'id': '2', 'at': 1, 'bt': 6}, {
    'id': '3', 'at': 4, 'bt': 4},
    {'id': '4', 'at': 6, 'bt': 2}]

#function to calculate round robin
def round_robin(data, tq):
    #list to store processes with [arrival_time,burst_time,index]
    rr = []
    indx = 0
    curr_time = 0
    flag = True
    for dct in data:
        rr.append([dct['at'], dct['bt'], indx])
        indx += 1
    #main loop until all process are completed
    while flag:
        for i in range(len(rr)):
            bt = rr[i][1]
            
            #check if the process is ready to execute and has burst time remaining
            if bt != 0 and rr[i][0] < curr_time or curr_time == 0:
                #if burst time is greater than time quantm
                if bt > tq:
                    rr[i][1] -= tq  #if process still has burst time remaining after time quantm it's adde back to the end of queue with updated burst time
                    curr_time += tq
                else:
                    rr[i][1] = 0
                    curr_time += bt
                    data[rr[i][2]]['ct'] = curr_time
        #check if all  processes are completed
        flg = True
        for i in rr:
            if not i[1] == 0:
                flg = False
        if flg:
            flag = False
    return data

#function to calculate sjf
def shortest_job_first(data):
    #list to store processes with burst time arrival time index
    sjf = []
    indx = 0
    curr_time = 0
    for dct in data:
        sjf.append([dct['bt'], dct['at'], indx])
        indx += 1
    #sort processes based on burst time
    sjf.sort()
    #main loop until all processes are completed
    while sjf:
        for val in sjf:
            #check if the process is ready to execute based on arrival time
            if val[1] <= curr_time:
                curr_time += data[val[2]]['bt']
                data[val[2]]['ct'] = curr_time #update the completion time based on burst time
                sjf.remove(val)
    return data


