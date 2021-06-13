# Orig by "redrambles:" https://gist.github.com/redrambles/c099b771a76e7ade81b5fb463b72126b
def remove_duplicates(lista):
    lista2 = []
    for item in lista:
        if item not in lista2: #is item in lista2 already?
            lista2.append(item)
    return lista2

print(remove_duplicates([1,2,3,3]))  