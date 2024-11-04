import pandas as pd
class Process:
    def __init__(self, PID, arrivalTime, burstTime):
        self.PID = PID
        self.arrivalTime = arrivalTime
        self.burstTime = burstTime
        self.waitingTime = 0
        self.remainingTime = burstTime
        self.completeTime = 0
        self.turnAroundTime = 0
        self.startTime = arrivalTime


def fcfs(processes): #a. first come first serve
    time = 0
    queue = []
    running = None
    finishedJob = 0
    
    while finishedJob < len(processes):
        for process in processes:
            if process.arrivalTime == time:
                if running is not None:
                    queue.append(process)
                else:
                    running = process
                
        if running is not None:
            if len(queue) > 0:
                lowest = running
                for q in queue:
                    if q.arrivalTime < lowest.arrivalTime and q.remainingTime > 0:
                        lowest = q
                if lowest is not running:
                    queue.remove(lowest)
                    queue.append(running)
                    running = lowest
        else:
            if len(queue) > 0:
                lowest = None
                for q in queue:
                    if lowest is None:
                        if q.remainingTime > 0:
                            lowest = q
                    else:
                        if q.arrivalTime < lowest.arrivalTime and q.remainingTime > 0:
                            lowest = q
                if lowest is not None:
                    queue.remove(lowest)
                    running = lowest

        if running is not None:
            running.remainingTime -= 1
            running.turnAroundTime += 1
            if running.remainingTime == 0:
                finishedJob += 1
                running.completeTime = time
                running = None
        
        for q in queue:
            q.waitingTime += 1
            q.turnAroundTime += 1
        time += 1
    return processes

def sjfNone(processes): #b. Shortest Job First (None preemptive)
    time = 0
    queue = []
    running = None
    finishedJob = 0
    
    while finishedJob < len(processes):
        for process in processes:
            if process.arrivalTime == time:
                if running is not None:
                    queue.append(process)
                else:
                    running = process
                
        if running is None:
            if len(queue) > 0:
                lowest = None
                for q in queue:
                    if lowest is None:
                        if q.remainingTime > 0:
                            lowest = q
                    else:
                        if q.remainingTime < lowest.remainingTime and q.remainingTime > 0:
                            lowest = q
                if lowest is not None:
                    queue.remove(lowest)
                    running = lowest

        if running is not None:
            running.remainingTime -= 1
            running.turnAroundTime += 1
            if running.remainingTime == 0:
                finishedJob += 1
                running.completeTime = time
                running = None
        
        for q in queue:
            q.waitingTime += 1
            q.turnAroundTime += 1
        time += 1
    return processes

def sjf(processes): #c. Shortest Job First (preemptive)
    time = 0
    queue = []
    running = None
    finishedJob = 0
    
    while finishedJob < len(processes):
        for process in processes:
            if process.arrivalTime == time:
                if running is not None:
                    queue.append(process)
                else:
                    running = process
                
        if running is not None:
            if len(queue) > 0:
                lowest = running
                for q in queue:
                    if q.remainingTime < lowest.remainingTime and q.remainingTime > 0:
                        lowest = q
                if lowest is not running:
                    queue.remove(lowest)
                    queue.append(running)
                    running = lowest
        else:
            if len(queue) > 0:
                lowest = None
                for q in queue:
                    if lowest is None:
                        if q.remainingTime > 0:
                            lowest = q
                    else:
                        if q.remainingTime < lowest.remainingTime and q.remainingTime > 0:
                            lowest = q
                if lowest is not None:
                    queue.remove(lowest)
                    running = lowest

        if running is not None:
            running.remainingTime -= 1
            running.turnAroundTime += 1
            if running.remainingTime == 0:
                finishedJob += 1
                running.completeTime = time
                running = None
        
        for q in queue:
            q.waitingTime += 1
            q.turnAroundTime += 1
        time += 1
    return processes

def ljf(processes): #d. Longest Job First (preemptive)
    time = 0
    queue = []
    running = None
    finishedJob = 0
    
    while finishedJob < len(processes):
        for process in processes:
            if process.arrivalTime == time:
                if running is not None:
                    queue.append(process)
                else:
                    running = process
                
        if running is not None:
            if len(queue) > 0:
                highest = running
                for q in queue:
                    if q.remainingTime > highest.remainingTime and q.remainingTime > 0:
                        highest = q
                if highest is not running:
                    queue.remove(highest)
                    queue.append(running)
                    running = highest
        else:
            if len(queue) > 0:
                highest = None
                for q in queue:
                    if highest is None:
                        if q.remainingTime > 0:
                            highest = q
                    else:
                        if q.remainingTime > highest.remainingTime and q.remainingTime > 0:
                            highest = q
                if highest is not None:
                    queue.remove(highest)
                    running = highest

        if running is not None:
            running.remainingTime -= 1
            running.turnAroundTime += 1
            if running.remainingTime == 0:
                finishedJob += 1
                running.completeTime = time
                running = None
        
        for q in queue:
            q.waitingTime += 1
            q.turnAroundTime += 1
        time += 1
    return processes

def roundRobin(processes, quantumTime): #Round Robin (Quantum time = 12)
    counter = quantumTime
    time = 0
    queue = []
    running = None
    finishedJob = 0
    
    while finishedJob < len(processes):    
        nextInLine = None
        if counter == 0:
            if running is not None:
                running.startTime = time
                nextInLine = running
                running = None
            counter = quantumTime
            
        for process in processes:
            if process.arrivalTime == time:
                if running is not None:
                    queue.append(process)
                else:
                    running = process
                
        if running is not None:
            if len(queue) > 0:
                lowest = running
                for q in queue:
                    if q.startTime < lowest.startTime and q.remainingTime > 0:
                        lowest = q
                if lowest is not running:
                    queue.remove(lowest)
                    queue.append(running)
                    running = lowest
        else:
            if len(queue) > 0:
                lowest = None
                for q in queue:
                    if lowest is None:
                        if q.remainingTime > 0:
                            lowest = q
                    else:
                        if q.startTime < lowest.startTime and q.remainingTime > 0:
                            lowest = q
                if lowest is not None:
                    queue.remove(lowest)
                    running = lowest
                    
        if nextInLine is not None:
            queue.append(nextInLine)

        if running is not None:
            running.remainingTime -= 1
            running.turnAroundTime += 1
            if running.remainingTime == 0:
                finishedJob += 1
                running.completeTime = time
                running = None
                counter = quantumTime + 1
        
        counter -= 1
        
        for q in queue:
            if q.remainingTime > 0:
                q.waitingTime += 1
                q.turnAroundTime += 1
        
        time += 1
    return processes