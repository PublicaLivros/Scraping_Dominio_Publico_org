import re

# Substitui espaços dos arquivos por "_" e coloca todos os caracteres em letra minúscula.
def fileNameNormalize(inputString):
    # TODO: Substituir posteriormente por regex.
    bookNormalizeText = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', inputString)
    bookNormalizeText = bookNormalizeText.replace(" ", "_")
    bookNormalizeText = bookNormalizeText.lower()
    return bookNormalizeText

# Substitui o link do livro para o link de download do arquivo.
def replaceLinkToDownload(url):
    url = url.replace("DetalheObraForm.do", "DetalheObraDownload.do", 1)
    return url
