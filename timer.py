import time, argparse, subprocess

# Set up the parser to take in the command/options
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('file_name', metavar='<file_name>',
                    help='The file to output the result to')
parser.add_argument('cmd', metavar='<cmd>',
                    help='The command to run (and time)')
parser.add_argument('-args', dest='dash_args', nargs='*',
                    help='Extra args to add to the command')
args = parser.parse_args()

# Run the process and calculate how long it takes
start_time = time.clock()
if args.dash_args:
    subprocess.call([args.cmd] + ['-{0}'.format(option) for option in args.dash_args])
else:
    subprocess.call(args.cmd)
end_time = time.clock()
deltaT = end_time - start_time

# Write to file
f = open(args.file_name, 'w')
f.write("{0}".format(deltaT))
f.close()
