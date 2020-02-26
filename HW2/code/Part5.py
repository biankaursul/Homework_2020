import matplotlib.pyplot as plt
import string
Char = []
for i in range(ord('A'), ord('N')):
    Char.append(chr(i))
Char.remove('I')
files = [f'../data/part5/{char}.geneBodyCoverage.r' for char in Char]

coverage = {}
for char,file in zip(Char,files):
    f = open(file,"r")
    raw_read = f.read()
    coverage[char] = [float(i) for i in raw_read.split()[2].rstrip(')').lstrip('c(').split(',')]   

fig, ax = plt.subplots(3,4, figsize = (20,15))
for (i,item) in enumerate(coverage):
    ax.ravel()[i].plot(coverage[item])
    ax.ravel()[i].set_title(item)
    ax.ravel()[i].set_xlabel("Gene Body Percentile (5'-3')")
    ax.ravel()[i].set_ylabel("Coverage")
plt.tight_layout()
plt.savefig("Part5 Output")
