import subprocess

# subprocess.call(["Test2.py","1","2"], shell=True)
# rez = subprocess.run(["Test2.py","1","2"], shell=True)
# process = subprocess.Popen(["Test2.py","1","2"], shell=True)
# print("HERE")
# data = process.communicate()
# print(data)

# cmd = 'python3 Test2.py'
#
# p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
# out, err = p.communicate()
# print(out)
# result = out.split('\n')
# for lin in result:
#     if not lin.startswith('#'):
#         print(lin)
# import subprocess
# import sys
# p = subprocess.Popen([sys.executable, 'Test2.py', 'argzzz1', 'argzzz2'],shell=True)
# out, err = p.communicate()
# print(out)
import subprocess

# p = subprocess.run("Test2.py", shell=True)
# for i in range(5):
k = 0
while True:
    # subprocess.run("Test2.py",input=b'foo\n'+bytes(k)+b'\n', shell=True)
    subprocess.run("python3 Test2.py",universal_newlines=True, input="foo\n"+str(k)+"\n", shell=True)
    k += 1
