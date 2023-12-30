import pandas as pd

def extract_and_save_to_txt(caminho_arquivo, caminho_saida):
    try:
        header = pd.read_excel(caminho_arquivo, nrows=1, header=None).iloc[0].tolist()
        df = pd.read_excel(caminho_arquivo, header=None, names=header, skiprows=1)
        df['ID'] = df.index
        data_list = [['ID', 'Titulo', 'Conteudo', 'Classe']]  # Adiciona 'Conteudo' à lista
        for index, row in df.iterrows():
            row_id = row['ID']
            title = row['Titulo'] if not pd.isna(row['Titulo']) else ''
            content = row['Noticia'] if not pd.isna(row['Noticia']) else ''  # Adiciona conteúdo da notícia
            title = title.replace('\n', '')
            classe = int(row['Classe']) if not pd.isna(row['Classe']) and row['Classe'] != '' else None
            data_list.append([row_id, title, content, classe])  # Adiciona 'Conteudo' à lista

        with open(caminho_saida, 'w', encoding='utf-8') as output_file:
            for data_row in data_list:
                output_file.write(f'ID: {data_row[0]} Titulo: {data_row[1]} Conteudo: {data_row[2]} Classe: {data_row[3]}\n')  # Atualiza a linha de escrita

        return f"Extração e salvamento em {caminho_saida} concluídos com sucesso."

    except FileNotFoundError:
        return "Erro: O arquivo Excel não foi encontrado. Verifique o caminho e o nome do arquivo."

    except pd.errors.EmptyDataError:
        return "Erro: O arquivo Excel está vazio ou não contém a planilha especificada."

    except pd.errors.ParserError:
        return "Erro: Há um problema na leitura do arquivo Excel."

    except Exception as e:
        return f"Ocorreu um erro não tratado: {e}"

path_bd = './base_data/FakeRecogna.xlsx'
path_output = './output/output.txt'
resultado = extract_and_save_to_txt(path_bd, path_output)
print(resultado)
