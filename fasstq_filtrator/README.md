#### The script filtrator.py takes *.fastq files and filter reads according to specified thresholds. 

**Flags**: \
*--input_fastq* path to .fastq file which you want to filter  !Required! \
*--output_file_prefix* prefix to files, which would collect filtered reads. File with passed reads ends \
with "_passed.fastq", failed reads are collected in "_failed.fastq". !Requred! \
*--gc_bounds* GC-fraction interval (in per cent). Specify both bounds. Default = [0,100] \
*--length_bounds* Read length interval. Specify both bounds. Dafault = [0,2**32] \
*--quality_threshold* Mean quality threhold for a read.  Deafult = 0\
*--save_filtered* If you want to save filtered reads. Default=False 
