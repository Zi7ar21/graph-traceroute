import traceroutes
#import traceroutes2graph

priority_highest = False

output_directory = "./out"

targets = [
]

def main():
	traceroutes.traceroutes(targets, ["-i", "enp4s0"]+["-I", "-q", "10"], output_directory+'/', threads=10, realtime=priority_highest)

if __name__ == "__main__":
	main()
