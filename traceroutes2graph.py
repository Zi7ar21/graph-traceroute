import graphviz
import re
from os import listdir

unknown_counter = 1

def open_traceroute(filename):
	global unknown_counter

	with open(filename, 'r') as file:
		tracert = file.read()

	lines = tracert.splitlines()[1:]

	line_number = 0

	_hops = []

	for line in lines:
		match = re.findall(r'\(([\d\.]+)\)', line)
		if match:
			_hops.append(match)
		else:
			_hops.append(["*"+str(unknown_counter)])
			unknown_counter += 1
			continue

		line_number += 1

	print(_hops)


	return _hops

def generate_graph(output_filename, traceroute_filenames):
	dot = graphviz.Digraph('G', filename='mytraceroute.gv', comment='super duper traceroute')

	print(dot)

	for traceroute_filename in traceroute_filenames:
		hops = open_traceroute(traceroute_filename)

		for i in range(len(hops) - 1):

			hops_left = 0

			for hop in (hops[i:]):
				#print(hop)
				if (hop[0])[0] != '*':
					hops_left += 1

			if(hops_left <= 0):
				continue

			current_hop = hops[i]
			next_hop = hops[i + 1]

			for src in current_hop:
				for dst in next_hop:
					dot.node(src)
					dot.node(dst)
					dot.edge(src, dst)

	dot.save()

def main():
	generate_graph("./mytraceroute.gv", ["./out/"+f for f in listdir("./out/")])

if __name__ == "__main__":
	main()
