import argparse

def filtrator (args):
     with open(f"{args['output_file_prefix']}_passed.fastq", "w") as passed_read:
        if args['save_filtered']:  
            with open(f"{args['output_file_prefix']}_failed.fastq", "w") as failed_read:
                with open(args['input_fastq'], "r") as fastq_file:
		#reading fastq string-by-string 
                    while True:
                        seq_name = fastq_file.readline()
                        seq = fastq_file.readline()
                        seq_length = len(seq[:-1])
                        string_3 = fastq_file.readline()
                        quality = fastq_file.readline()
                        if seq_name == "":
                            break
		#gc fraction calculation 
                        gc_amount = seq.count("C") + seq.count("G")
                        gc_fraction = gc_amount / seq_length * 100
                        if not args['gc_bounds'][0] <= gc_fraction <= args['gc_bounds'][1]:
                            failed_read.write(seq_name)
                            failed_read.write(seq)
                            failed_read.write(string_3)
                            failed_read.write(quality)
                            continue 
                  #length bounds range      
                        if not args['length_bounds'][0] <= seq_length <= args['length_bounds'][1]:
                            failed_read.write(seq_name)
                            failed_read.write(seq)
                            failed_read.write(string_3)
                            failed_read.write(quality)
                            continue 
		#quality counter check 

                        quality_counter = 0
                        for item in quality[:-1]:
                            quality_counter+=int(ord(item))
                            mean_quality = quality_counter/seq_length

                        if args['quality_threshold'] >= mean_quality:
                            failed_read.write(seq_name)
                            failed_read.write(seq)
                            failed_read.write(string_3)
                            failed_read.write(quality)
                            continue
		#if all tests are passed, write to fastq_passed 
                        passed_read.write(seq_name)
                        passed_read.write(seq)
                        passed_read.write(string_3)
                        passed_read.write(quality)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_fastq', metavar="input_fastq.fastq", help='A fastq file to filter')
    parser.add_argument('--output_file_prefix', help='A named string argument', default='')
    parser.add_argument('--gc_bounds', type=int, nargs=2,
                        metavar=('start', 'end'),
                        help='Values for upper and lower boundary for preferred GC-content', default=[0,100]
                       )
    parser.add_argument('--length_bounds',  type=int, nargs=2, metavar=('start', 'end'), help='Length interval for reads', default = [0,2**32])
    parser.add_argument('--quality_threshold',  type=int, help='Threshold for quality', default = 0)
    parser.add_argument('--save_filtered', help='Boolean argument, save filtered reads of not', default=False, action="store_true")
    args = vars(parser.parse_args())
    filtrator(args) 
main()
