# Análise Preditiva de Preços de Imóveis em Brasília-DF

![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-green)

Este projeto de Data Science realiza um ciclo completo de análise de dados, desde a coleta de informações na web até a construção de um modelo de Machine Learning para prever o preço de venda de apartamentos em Brasília, Distrito Federal.

## 📋 Tabela de Conteúdos
* [Sobre o Projeto](#-sobre-o-projeto)
* [Estrutura dos Arquivos](#-estrutura-dos-arquivos)
* [Tecnologias Utilizadas](#-tecnologias-utilizadas)
* [Como Executar](#-como-executar)
* [Resultados](#-resultados)
* [Autor](#-autor)

---

## 📖 Sobre o Projeto

O objetivo principal é desenvolver um modelo de regressão linear capaz de estimar o valor de um imóvel com base em suas características, como localização, área útil, número de quartos, suítes e vagas de garagem.

O fluxo de trabalho foi dividido em três etapas principais:
1.  **Web Scraping (`Scrapping.py`):** Coleta automatizada de dados de mais de 1000 anúncios de apartamentos no portal DF Imóveis.
2.  **Limpeza e Tratamento de Dados (`Tratamento.ipynb`):** Análise, limpeza e preparação dos dados brutos, tratando valores ausentes, corrigindo tipos de dados e salvando um dataset limpo para a modelagem.
3.  **Modelagem e Avaliação (`RegressãoLinear.ipynb`):** Treinamento de um modelo de Regressão Linear, avaliação de sua performance com métricas como MAE (Erro Absoluto Médio) e R² (Coeficiente de Determinação), e visualização dos resultados.

---

## 📁 Estrutura dos Arquivos

```
.
├── Scrapping.py                     # Script para coleta de dados do site DF Imóveis
├── Tratamento.ipynb                 # Notebook Jupyter para limpeza e tratamento dos dados
├── RegressãoLinear.ipynb            # Notebook Jupyter para criação e avaliação do modelo de ML
├── Scrapping Apt Brasília Venda 1000.csv  # Dados brutos obtidos pelo scraping (1000+ registros)
├── df_limpo.csv                     # Dados limpos e prontos para a modelagem
└── image_e1222a.png                 # Gráfico com os resultados do modelo (Previsões vs. Valores Reais)
```

---

## 🛠️ Tecnologias Utilizadas

Este projeto foi desenvolvido utilizando as seguintes tecnologias e bibliotecas:

* **Python 3.10+**
* **Web Scraping:**
    * [Selenium](https://www.selenium.dev/)
    * [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* **Análise e Manipulação de Dados:**
    * [Pandas](https://pandas.pydata.org/)
    * [NumPy](https://numpy.org/)
* **Visualização de Dados:**
    * [Matplotlib](https://matplotlib.org/)
    * [Seaborn](https://seaborn.pydata.org/)
* **Machine Learning:**
    * [Scikit-learn](https://scikit-learn.org/stable/)
* **Ambiente de Desenvolvimento:**
    * [Jupyter Notebook](https://jupyter.org/)

---

## 🚀 Como Executar

Para executar este projeto localmente, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/guilhermelevi/analise-preco-imoveis-df.git](https://github.com/guilhermelevi/analise-preco-imoveis-df.git)
    cd analise-preco-imoveis-df
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    # Criar ambiente
    python -m venv venv

    # Ativar no Windows
    .\venv\Scripts\activate

    # Ativar no macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    (É uma boa prática criar um arquivo `requirements.txt` com as bibliotecas)
    ```bash
    pip install pandas numpy matplotlib seaborn scikit-learn selenium beautifulsoup4 jupyter
    ```

4.  **Execute os Notebooks:**
    Abra o Jupyter Notebook e execute os arquivos na seguinte ordem:
    * `Tratamento.ipynb`: Para gerar o arquivo `df_limpo.csv`.
    * `RegressãoLinear.ipynb`: Para treinar o modelo e visualizar os resultados.

    *Observação: O script `Scrapping.py` pode ser executado para coletar dados atualizados, mas requer a configuração do [ChromeDriver](https://chromedriver.chromium.org/downloads).*

---

## 👨‍💻 Autor

Projeto desenvolvido por **Guilherme Levi**.

* **LinkedIn:** [Guilherme Levi](https://www.linkedin.com/in/guilherme-levi-05406221a/)
* **GitHub:** [guilhermelevi](https://github.com/guilhermelevi)