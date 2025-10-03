import time
import re
import pandas as pd
import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


URL_BASE = 'https://www.dfimoveis.com.br/venda/df/brasilia/apartamento'
NUMERO_DE_ANUNCIOS_DESEJADO = 1000

chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')

prefs = {
    "profile.managed_default_content_settings.images": 2,
    "profile.managed_default_content_settings.stylesheets": 2,
}
chrome_options.add_experimental_option("prefs", prefs)


service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

lista_de_imoveis = []
pagina_atual = 1

print("Iniciando o Web Scraping (Modo Otimizado e Humanizado)...")

while len(lista_de_imoveis) < NUMERO_DE_ANUNCIOS_DESEJADO:
    print(f"--- Coletando na página {pagina_atual} | Anúncios coletados: {len(lista_de_imoveis)} de {NUMERO_DE_ANUNCIOS_DESEJADO} ---")

    if pagina_atual == 1:
        url_pagina_resultados = URL_BASE
    else:
        url_pagina_resultados = f"{URL_BASE}?pagina={pagina_atual}"

    try:
        driver.get(url_pagina_resultados)


        pausa_inicial = random.uniform(3, 6)
        print(f"Aguardando carregamento inicial por {pausa_inicial:.2f} segundos...")
        time.sleep(pausa_inicial)
        
        try:
            botao_cookie = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'PROSSEGUIR')]"))
            )
            print("Banner de cookie encontrado. Clicando...")
            botao_cookie.click()
            time.sleep(random.uniform(1, 2))
        except Exception:
            print("Banner de cookie não encontrado. Prosseguindo...")


        print("Aguardando os anúncios aparecerem...")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.imovel-card, a.new-card"))
        )
        print("Anúncios encontrados. Extraindo HTML.")

    except Exception as e:
        print(f"Não foi possível carregar os anúncios da página {pagina_atual}. Finalizando.")
        print(f"Erro: {e}")
        break 
    
    html_resultados = driver.page_source
    soup_resultados = BeautifulSoup(html_resultados, 'html.parser')
    imoveis_na_pagina = soup_resultados.select('a.imovel-card, a.new-card')
    
    if not imoveis_na_pagina:
        print("Busca pelos cards falhou mesmo após a espera. Finalizando.")
        break 

    for imovel_card in imoveis_na_pagina:
        if len(lista_de_imoveis) >= NUMERO_DE_ANUNCIOS_DESEJADO:
            break 
        try:
            url_anuncio_raw = imovel_card['href']
            url_anuncio = url_anuncio_raw.split('?')[0]
            print(f"  Coletando dados de: {url_anuncio}")
            driver.get(url_anuncio)

            time.sleep(random.uniform(2, 5))
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h2.headline-small")))
            
            html_anuncio = driver.page_source
            soup_anuncio = BeautifulSoup(html_anuncio, 'html.parser')
            
            dados_imovel = {'Link': url_anuncio}

            dados_imovel['Preco'] = None
            try:
                price_container = soup_anuncio.find('div', class_='item-price')
                if price_container:
                    preco_tag = price_container.find('h4')
                    if preco_tag and "consul" not in preco_tag.text.lower():
                        preco_texto = preco_tag.text
                        preco_numerico = float(re.sub(r'[^\d,]', '', preco_texto).replace(',', '.'))
                        dados_imovel['Preco'] = preco_numerico
            except: pass
            dados_imovel['Localizacao'] = None
            try:
                dados_imovel['Localizacao'] = soup_anuncio.find('div', class_='city').find('span').text.strip()
            except: pass
            dados_imovel['Area_Util_m2'], dados_imovel['Quartos'], dados_imovel['Suites'], dados_imovel['Vagas_Garagem'] = None, None, None, None
            try:
                area_tag = soup_anuncio.find('h4', string=lambda text: text and 'm²' in text)
                if area_tag:
                    match = re.search(r'\d+', area_tag.text)
                    if match: dados_imovel['Area_Util_m2'] = int(match.group())
            except: pass
            info_container = soup_anuncio.find('div', class_='info-details')
            if info_container:
                try:
                    quartos_text = info_container.find('div', class_='room').find('span').text
                    dados_imovel['Quartos'] = int(re.search(r'\d+', quartos_text).group())
                except: pass
                try:
                    suites_text = info_container.find('div', class_='suite').find('span').text
                    dados_imovel['Suites'] = int(re.search(r'\d+', suites_text).group())
                except: pass
                try:
                    vagas_text = info_container.find('div', class_='vacancy').find('span').text
                    dados_imovel['Vagas_Garagem'] = int(re.search(r'\d+', vagas_text).group())
                except: pass
            
            lista_de_imoveis.append(dados_imovel)
        except Exception as e:
            print(f"    Erro ao processar o card do anúncio. Pulando. Erro: {e}")
            continue
    
    if len(lista_de_imoveis) >= NUMERO_DE_ANUNCIOS_DESEJADO:
        print("--- Meta de anúncios atingida! ---")
        break 
    
    if pagina_atual % 5 == 0 and pagina_atual > 0:
        long_pause = random.uniform(15, 30)
        print(f"--- Pausa longa de {long_pause:.2f}s para simular comportamento humano ---")
        time.sleep(long_pause)

    pagina_atual += 1

driver.quit()

print("\nWeb Scraping finalizado!")

imoveis_finais = lista_de_imoveis[:NUMERO_DE_ANUNCIOS_DESEJADO]
df_imoveis = pd.DataFrame(imoveis_finais)
df_imoveis.to_csv('dados_imoveis_detalhados_df.csv', index=False)
print(f"\nDados de {len(df_imoveis)} anúncios salvos com sucesso no arquivo 'dados_imoveis_detalhados_df.csv'")
print("\nPré-visualização dos dados coletados:")
print(df_imoveis.head())