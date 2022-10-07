
#Function for iterative function calling until exit is printed
def action():
    task=input('Enter the task:')
    if task=='exit':
        return
    myMain(task)
    action()

#Function which makes reverse complement starin for RNA or for DNA
def reverse_complement(seq):
    if any ((i in 'Uu') for i in seq):  #if there are some U, it should be RNA                   
        return ''.join([RNA_Complement[nuc] for nuc in seq]) [::-1] 
    else: 
        return ''.join([DNA_Complement[nuc] for nuc in seq]) [::-1]

#Function which makes complement starin for RNA or for DNA
def complement(seq):
    if any ((i in 'Uu') for i in seq):
        return ''.join([RNA_Complement[nuc] for nuc in seq])
    else: 
        return ''.join([DNA_Complement[nuc] for nuc in seq])

#Function for transcription
def transcribe(seq):
    return (''.join([DNA2RNA[nuc] for nuc in seq])) [::-1]

#Function for reverse
def func_reverse_seq(seq):
    return ''.join([str(item) for item in seq])[::-1]


    
# takes sequence and send it to the corresponding functions 
##if there are no restriction
def myMain(task):
    seq=input('Enter the sequence:')
    if any ((i not in 'ATGCUatgcu') for i in seq): #for non-nucleotide symbols 
        print ("Not a nucleic acid")
        return
    elif any ((i in 'tT') for i in seq) and  any ((i in 'uU') for i in seq): # if U and T are in same sequence 
        print ('You mixed up RNA and DNA nucleotides')
        return
    elif task=='transcribe' and any ((i in 'Uu') for i in seq): #if for transcription U is used 
        print ("transcription is possible for DNA, not for RNA")
        return
    else: 
        seq=list(seq)
        return print(what2do[task](seq)) 

def exit():
    return

#Dictionary for complementary DNA sequence
DNA_Complement = {
    'A':'T', 
    'T': 'A', 
    'G':'C', 
    'C':'G', 
    'a':'t', 
    't': 'a', 
    'g':'c', 
    'c':'g'
} 
#Dictionary for complementary RNA sequence
RNA_Complement = {
    'A':'U',
    'U': 'A',
    'G':'C', 
    'C':'G', 
    'a':'u', 
    'u': 'a', 
    'g':'c', 
    'c':'g'
} 

#Dictionary for functions calling

what2do = {
    'transcribe': transcribe, 
    'reverse': func_reverse_seq, 
    'complement':complement, 
    'reverse complement':reverse_complement,
    'exit':exit
}

#Sictionary for transcription

DNA2RNA = {
    'A':'U', 
    'T': 'A', 
    'G':'C', 
    'C':'G', 
    'a':'u', 
    't': 'a',
    'g':'c',
    'c':'g'
}


action() #to start the party!
