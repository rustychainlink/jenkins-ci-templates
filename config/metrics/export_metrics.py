import os, io
from dataclasses import dataclass, asdict
from typing import List

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

def get_list_of_processes(count:int=0) -> List[ProcessMetrics]:

    # Extract data from source
    TOP_10_CPU_HOGS=f"ps aux --sort -pcpu | head -n{1+count}"
    stdout=os.popen(TOP_10_CPU_HOGS).read()
    
    PROCESS_LIST:List[ProcessMetrics]=[]

    # Parse data
    with io.StringIO(stdout) as buffer:
        for line in buffer.readlines():
            PROCESS_LIST.append(
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

    return PROCESS_LIST

print([asdict(process) for process in get_list_of_processes(5)])
