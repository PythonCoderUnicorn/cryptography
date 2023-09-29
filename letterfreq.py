
# letter frequencies for Cryptanalysis 

import collections
import string

print("""
 #####################################
 ##                                 ##
 ##      LETTER FREQUENCIES         ##
 ##                                 ##
 #####################################
""")

# word = "BUUBDL UIF FOFNZ JO UIF FWFOJOH"

word = input("Enter cipher (no spaces): ").strip()

c = collections.Counter(word)

# print(c )

most_common = c.most_common(5)[0][:2]
print(f"most common: {most_common}")

most_common5 = c.most_common(5)
print(f"5 most common letters: {most_common5}")

least_common = c.most_common()[-1][:]
print(f"least common letter: {least_common} \n")




