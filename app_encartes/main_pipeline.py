from PIL import Image
import pytesseract
import os # Importado para verificar se o arquivo de imagem existe

# --- Configuração Opcional para Windows ---
# Se o Tesseract não estiver no PATH do seu sistema no Windows,
# você pode precisar descomentar a linha abaixo e ajustar o caminho
# para o local onde você instalou o Tesseract OCR.
# Exemplo:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def verificar_instalacao_tesseract():
    """Tenta verificar se o Tesseract está acessível."""
    try:
        versao = pytesseract.get_tesseract_version()
        print(f"✅ Tesseract OCR encontrado! Versão: {versao}")
        return True
    except pytesseract.TesseractNotFoundError:
        print("❌ ERRO: Tesseract OCR não encontrado no PATH do sistema.")
        print("   Por favor, certifique-se de que o Tesseract OCR está instalado e")
        print("   adicionado ao PATH do sistema, ou defina o caminho manualmente")
        print("   em 'pytesseract.pytesseract.tesseract_cmd' no script.")
        return False
    except Exception as e:
        print(f"❌ ERRO ao tentar obter a versão do Tesseract: {e}")
        return False

def extrair_texto_da_imagem(caminho_da_imagem, idioma='por'):
    """
    Tenta extrair texto de uma imagem usando pytesseract.

    :param caminho_da_imagem: Caminho para o arquivo de imagem.
    :param idioma: Código do idioma para o OCR (ex: 'por' para português, 'eng' para inglês).
    :return: O texto extraído ou None se ocorrer um erro.
    """
    if not os.path.exists(caminho_da_imagem):
        print(f"❌ ERRO: Arquivo de imagem não encontrado em '{caminho_da_imagem}'")
        print("   Por favor, verifique o nome e o caminho do arquivo.")
        return None

    try:
        # Abrir a imagem usando Pillow
        img = Image.open(caminho_da_imagem)

        # Extrair texto da imagem
        # Você pode especificar o idioma, por exemplo, 'por' para português
        texto_extraido = pytesseract.image_to_string(img, lang=idioma)

        print(f"\n--- Texto extraído da imagem ('{caminho_da_imagem}') ---")
        if texto_extraido.strip(): # Verifica se algum texto foi extraído
            print(texto_extraido)
        else:
            print("   (Nenhum texto foi detectado ou o texto estava muito ilegível.)")
            print("   Dicas:")
            print("   - Verifique se a imagem contém texto claro e legível.")
            print(f"   - Certifique-se de que o pacote de idioma '{idioma}' está instalado para o Tesseract.")
            print("   - Tente melhorar a qualidade da imagem (contraste, resolução).")
        return texto_extraido

    except pytesseract.TesseractError as e:
        print(f"❌ ERRO do Tesseract ao processar a imagem: {e}")
        print("   Isso pode acontecer se o idioma especificado não estiver instalado")
        print(f"   ou se houver um problema com a instalação do Tesseract ({idioma}).")
        return None
    except FileNotFoundError: # Deveria ser pego pela verificação os.path.exists, mas como redundância
        print(f"❌ ERRO: Arquivo de imagem não encontrado em '{caminho_da_imagem}' (verificado novamente).")
        return None
    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado ao processar a imagem: {e}")
        return None

if __name__ == "__main__":
    print("--- Teste do Pytesseract ---")

    # Primeiro, vamos verificar se o Tesseract parece estar instalado
    if not verificar_instalacao_tesseract():
        print("\nCorrija a instalação do Tesseract e tente novamente.")
    else:
        # --- IMPORTANTE: Configure o caminho da sua imagem de teste aqui ---
        # Coloque uma imagem chamada "minha_imagem_teste.png" no mesmo diretório do script
        # ou substitua pelo caminho completo da sua imagem.
        caminho_imagem_teste = "teste.png"

        print(f"\nTentando processar a imagem: '{caminho_imagem_teste}'")
        # Você pode mudar o idioma se sua imagem estiver em inglês (ex: 'eng')
        extrair_texto_da_imagem(caminho_imagem_teste, idioma='por')

    print("\n--- Fim do Teste ---")