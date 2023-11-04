import os, io
from dataclasses import dataclass, asdict
from typing import List, Dict
from prometheus_client import start_http_server, Info
import time

CPU_HOG_COUNT:int=5
PROMETHEUS_PORT:int=8000
EXPORT_RATE:int=1 #Hz


@dataclass
class ProcessMetrics:
    user:str=''
    pid:str=''
    cpu:str=''
    mem:str=''
    vsz:str=''
    rss:str=''
    tty:str=''
    stat:str=''
    start:str=''
    time:str=''
    command:str=''


def get_list_of_processes(n:int=0) -> List[ProcessMetrics]:

    # Extract data from source
    TOP_n_CPU_HOGS=f"ps aux --sort -pcpu | head -n{1+n}"
    stdout=os.popen(TOP_n_CPU_HOGS).read()
    
    process_list:List[ProcessMetrics]=[]

    # Parse data
    with io.StringIO(stdout) as buffer:
        for line in buffer.readlines():
            process_list.append(
                ProcessMetrics(
                    user=line.split()[0],
                    pid=line.split()[1],
                    cpu=line.split()[2],
                    mem=line.split()[3],
                    vsz=line.split()[4],
                    rss=line.split()[5],
                    tty=line.split()[6],
                    stat=line.split()[7],
                    start=line.split()[8],
                    time=line.split()[9],
                    command=' '.join(line.split()[10:]),
                )
            )

    return process_list


if __name__=="__main__":

    # prepare info metrics, launch exporter service
    process_info_metric_list = [Info(f"process_cpu_hog_{i}", '') for i in range(CPU_HOG_COUNT)]
    start_http_server(PROMETHEUS_PORT)

    while True:

        # gather process data
        top_cpu_hogs_list:List[ProcessMetrics]=\
                [asdict(process) for process in get_list_of_processes(CPU_HOG_COUNT+1)][1:]

        # export process data
        for metric_obj, process_info in zip(process_info_metric_list, top_cpu_hogs_list):
            metric_obj.info(process_info)

        time.sleep(1/float(EXPORT_RATE))
