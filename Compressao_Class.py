class Compressao :
    def compressao_lzw(self, dado):
        string = ""
        out = []
        dicionario = {}
        for i in range(256):
            dicionario.update({str(i): str(i)})

        for symbol in dado:
            string_plus_symbol = string + symbol
            if string_plus_symbol in dicionario:
                string = string_plus_symbol
            else:
                out.append(dicionario[string])
                dicionario[string_plus_symbol] = len(dicionario)
                string = symbol

        if string in dicionario:
            out.append(dicionario[string])

        tam_original = len(dado)* 8
        tam_compressao = len(out )* 9

        return out,tam_original,tam_compressao



