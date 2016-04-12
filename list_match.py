import sys

def load_list(filename):
    return [line.split(' (')[0] for line in open(filename)]

investigados = sys.argv[1]
pro = sys.argv[2]
contra = sys.argv[3]
nomes_investigados = load_list(investigados)
nomes_pro = load_list(pro)
nomes_contra = load_list(contra)

pro_investigados = set(nomes_pro) & set(nomes_investigados)
contra_investigados = set(nomes_contra) & set(nomes_investigados)
nenhum = set(nomes_investigados)
nenhum = nenhum - set(nomes_pro) - set(nomes_contra)
print(nenhum)
print("A favor investigados:", len(pro_investigados), "de", len(nomes_pro))
print("Contra investigados:", len(contra_investigados), "de", len(nomes_contra))
