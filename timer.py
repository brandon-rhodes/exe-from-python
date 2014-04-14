import time, argparse, subprocess

# Set up the parser to take in the command/options
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('file_name', type=str, metavar='<file_name>',
                    help='The file to output the result to')
parser.add_argument('cmd', type=str, metavar='<cmd>',
                    help='The command to run (and time)')
# @TODO: Fix line below, extra args don't currently work
parser.add_argument('extra_args', type=str, metavar='<extra_args>', nargs='*',
                    help='Extra args to add to the command')
args = parser.parse_args()

# Run the process and calculate how long it takes
start_time = time.clock()
if args.extra_args:
    subprocess.call([args.cmd] + [option for option in args.extra_args])
else:
    subprocess.call(args.cmd)
end_time = time.clock()
deltaT = end_time - start_time

# Write to file
f = open(args.file_name, 'w')
f.write("{0}".format(deltaT))
f.close()
