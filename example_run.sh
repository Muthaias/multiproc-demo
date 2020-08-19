# Generisk beskrivning:
#  * num_procs: Antalet process som process-poolen får använda under körning
#  * file_glob_x: En filsökväg som får innehålla wildcards (*) för att matcha filer
# python parallel_search.py <num_procs> <file_glob_0> ... <file_glob_N>
python parallel_search.py 2 data/*.txt