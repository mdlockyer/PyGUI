from subprocess import PIPE, Popen
command: str = 'fbs freeze'
process = Popen(args=command, stdout=PIPE, shell=True)
output: str = process.communicate()[0].decode("utf-8")
print('\n' + output)
