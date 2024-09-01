import subprocess
from random import shuffle
from multiprocessing import Pool

def traceroute(target, arguments, output_filename, realtime=False):
	output_file = open(output_filename, "w")

	arguments = ["traceroute"]+arguments+[str(target)]

	if(realtime):
		arguments = ["nice", "--999", "chrt", "99"]+arguments

	print(arguments)

	p = subprocess.Popen(arguments, stdout=output_file)

	p.wait()

	output_file.close()

def traceroutes(targets, arguments, output_prefix, randomize=True, threads=1, realtime=False):
	if(randomize):
		shuffle(targets)

	#for _target in targets:
	#	traceroute(_target, arguments, output_prefix+_target, realtime)

	with Pool(threads) as pool:
		pool.starmap(traceroute, [(_target, arguments, output_prefix+_target+".txt", realtime) for _target in targets])
