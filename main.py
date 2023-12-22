import dispy, random, time, socket

def compute(n):
    time.sleep(n)
    host = socket.gethostname()
    return (host, n)

try:
    cluster = dispy.JobCluster(compute, nodes=['raspLabo2.local', 'raspLabo3.local', 'raspLabo4.local'], ip_addr='172.20.10.8')
    jobs = []

    for i in range(20):
        job = cluster.submit(random.randint(5,20))
        job.id = i
        print('submitted job %s' % (job.id))
        jobs.append(job)

    cluster.stats()
    print('waiting for jobs to complete')

    for job in jobs:
        host, n = job() 
        print('%s executed job %s at %s with %s' % (host, job.id, job.start_time, n))

    cluster.print_status()
except KeyboardInterrupt:
    cluster.close()
    exit()