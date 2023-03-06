def dnaSynthesis(templateStrand):
    for i in templateStrand:
        if i != 'G' and i != 'T' and i != 'A' and i != 'C':
            print("Not a valid nucleotide sequence.", end = "")
            break
    print(" 5' ")
    for i in templateStrand:
        if i == 'A':
            print('T', end = "")
        if i == 'G':
            print('C', end = "")
        if i == 'C':
            print('G', end = "")
        if i == 'T':
            print('A', end = "")
    print("3' ", end = " ")
    
def transcribe(dnaTemplateStrand):
    print (" 5'", end = " ")
    for i in dnaTemplateStrand:
        if i != 'G' and i != 'T' and i != 'A' and i != 'C':
            print("Not a valid nucleotide sequence.", end = "")
            break
        if i == 'A':
            print('U', end = "")
        if i == 'G':
            print('C', end = "")
        if i == 'C':
            print('G', end = "")
        if i == 'T':
            print('A', end = "")
    
    print(" 3' ", end = " ")



def translate(mrnastrand):
    Phe = ['UUU', 'UUC']
    Leu = ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG']
    Ile = ['AUU', 'AUC', 'AUA']
    Met = ['AUG']
    Val = ['GUU', 'GUC', 'GUA', 'GUG']
    Ser = ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC']
    Pro = ['CCU', 'CCC', 'CCA', 'CCG']
    Thr = ['ACU', 'ACC', 'ACA', 'ACG']
    Ala = ['GCU', 'GCC', 'GCA', 'GCG']
    Tyr = ['UAU', 'UAC']
    Stop = ['UAA', 'UAG', 'UGA']
    His = ['CAU', 'CAC']
    Gin = ['CAA', 'CAG']
    Asn = ['AAU', 'AAC']
    Lys = ['AAA', 'AAG']
    Asp = ['GAU', 'GAC']
    Glu = ['GAA', 'GAG']
    Cys = ['UGU', 'UGC']
    Trp = ['UGG']
    Arg = ['CGU', 'CGC', 'CGA', 'CGG', 'AGA','AGG']
    Gly = ['GGU', 'GGC', 'GGA', 'GGG']
    codonchart = Phe + Leu + Ile + Met + Val + Ser + Pro + Thr + Ala + Tyr + Stop + His + Gin + Asn + Lys + Asp + Glu + Cys + Trp + Arg + Gly


    newtemp = []
    for i in range(0, len(mrnastrand),3):
        newtemp.append(mrnastrand[i:i+3])

    if (len(mrnastrand) % 3 != 0):
        print('Not a valid nucleotide sequence. Make sure all of your codons are complete!')

    for x in newtemp:
        if x in Phe:
            print('Phe', end = '-')
        if x in Leu:
            print('Leu', end = '-')
        if x in Ile:
            print('Ile', end = '-')
        if x in Met:
            print('Met', end = '-')
        if x in Val:
            print('Val', end = '-')
        if x in Ser:
            print('Ser', end = '-')
        if x in Pro:
            print('Pro', end = '-')
        if x in Thr:
            print('Thr', end = '-')
        if x in Ala:
            print('Ala', end = '-')
        if x in Tyr:
            print('Tyr', end = '-')
        if x in Stop:
            break
        if x in His:
            print('His', end = '-')
        if x in Gin:
            print('Gin', end = '-')
        if x in Asn:
            print('Asn', end = '-')
        if x in Lys:
            print('Lys', end = '-')
        if x in Asp:
            print('Asp', end = '-')
        if x in Glu:
            print('Glu', end = '-')
        if x in Cys:
            print('Cys', end = '-')
        if x in Trp:
            print('Trp', end = '-')
        if x in Arg:
            print('Arg', end = '-')
        if x in Gly:
            print('Gly', end = '-')
        if x not in codonchart:
            print('Not a valid nucleotide sequence. Make sure you have a valid mRNA sequence!')

translate('UUUCAGCACACUZ')
