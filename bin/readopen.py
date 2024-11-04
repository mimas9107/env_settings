import sys
n_argv = len(sys.argv)
print(""" 
      usage: readopen.py [filename]
      """ if n_argv < 2 else "")

if (n_argv != 1): # filename存在於 [1] ~ [n_argv-1]
    for file in sys.argv[1:]:

        try:
            fop=open(file,"r")
            # do something...
            buf=fop.readlines()

            result=[chr(int(e)) for e in buf]
            print("".join(result))

            fop.close()

        except FileNotFoundError:
            print(f"There is no {file} exists.")

            pass