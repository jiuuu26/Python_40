import psutil

#cpu 속도
cpu=psutil.cpu_freq()
print(cpu)

#cpu 물리코어 수
cpu_core=psutil.cpu_count(logical=False)
print(cpu_core)

#메모리 정보
memory = psutil.virtual_memory()
print(memory)

#디스크 정보
disk=psutil.disk_partitions()
print(disk)

#네트워크 통해 보내고 받은 데이터량
net=psutil.net_io_counters()
print(net)