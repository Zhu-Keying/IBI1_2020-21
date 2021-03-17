#use numpy to calculate the average lengths.
import numpy as np
gene_lengths=np.array([9410,394141,4442,105338,19149,76779,126550,36296,842,15981])
exon_counts=([51,1142,42,216,25,650,32533,57,1,523])
a=np.true_divide(gene_lengths,exon_counts)
#use order "sorted" to rearrange the turn
print(sorted(a))
# use matplotlib to draw
import matplotlib.pyplot as plt
n=10
score=a
plt.boxplot(score,vert=True,whis=1.5,patch_artist=True)
plt.show()
