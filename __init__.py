
from subprocess import Popen, PIPE

def subprocess_cmd(dr,cmd1,cmd2):
    p1 = Popen(cmd1.split(),stdout=PIPE,cwd=dr)
    p2 = Popen(cmd2.split(),stdin=p1.stdout,stdout=PIPE,cwd=dr)
    p1.stdout.close()
    return p2.communicate()[0]

subprocess_cmd('/Users/mbp-2017/Desktop/Repositories/REST_API/webserver/app','open -a Terminal','flask run')
subprocess_cmd('/Users/mbp-2017/Desktop/Repositories/REST_API/client','open -a Terminal','npm run serve')
