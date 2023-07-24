import os
from PyPDF2 import PdfReader

def lerPDFs(caminho):
    resultados = []

    for i in os.listdir(caminho):
        if i.endswith('.pdf'):
            caminho_completo = os.path.join(caminho, i)
            print(f"Lendo o arquivo: {i}")
            
            with open(caminho_completo, 'rb') as arquivo_pdf:
                leitor_pdf = PdfReader(arquivo_pdf)
                num_paginas = len(leitor_pdf.pages)

                texto_completo = ""
                for pagina in leitor_pdf.pages:
                    texto_completo += pagina.extract_text()

                resultados.append({
                    'nome_arquivo': i,
                    'titulo': leitor_pdf.metadata.title if leitor_pdf.metadata else None,
                    'conteudo': texto_completo
                })

                print("\n")

    return resultados

def buscarPDF(resultados):
    termo = input("Digite o título ou palavra-chave a ser pesquisado: ")
    encontrados = []

    for arquivo_info in resultados:
        if termo.lower() in arquivo_info['titulo'].lower():
            encontrados.append(arquivo_info)

    return encontrados


print('''*******************
*  Leitor de PDF  *
*******************''')

pasta = input('Digite o caminho da pasta onde deseja procurar seus PDFs:\n')
arquivos_pdf = lerPDFs(pasta)

while True:
    print('''
    \nO que você deseja?
    1. Procurar por uma palavra ou título especifico.
    2. Encerrar o programa.''')    
    e = input('')
    if e == '1':
        resultado = buscarPDF(arquivos_pdf)
        if resultado:
            for i, arquivo in enumerate(resultado, start=1):
                print(f"{i}. Arquivo encontrado: {arquivo['nome_arquivo']}")
                print(f"   Título: {arquivo['titulo']}")
            abrirCont = input("Digite o número do arquivo que deseja abrir o conteúdo (ou pressione Enter para voltar ao menu principal): ")
            if abrirCont.isdigit():
                arquivo_escolhido = resultado[int(abrirCont) - 1]
                print(f"\nConteúdo do arquivo {arquivo_escolhido['nome_arquivo']}:\n")
                print(arquivo_escolhido['conteudo'])
        else:
            print("Nenhum arquivo encontrado com o título ou palavra-chave especificada.")
    elif e == '2':
        break
    else:
        print("Opção inválida. Escolha novamente.")
