# ApiRest simples 

Esta e uma arpi-rest simples com metodos basicos de CRUD

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

### 📋 Pré-requisitos

De que coisas você precisa para instalar o software e como instalá-lo?

```
Será necessária a instalação do python em sua máquina e uma ferramenta que dá suporte à documentação das requisições feitas pela API, como "PostMan" e "insomnia".
```

### 🔧 Instalação

Uma série de exemplos passo-a-passo que informam o que você deve executar para ter um ambiente de desenvolvimento em execução.

Diga como essa etapa será:

```
Após o dowload/copia do repositório você deve executar o seguinte comando no terminal em python "pip install -r requirements.txt", este comando ira executar a instalação de todas as dependências encontradas em "requirements.txt",
dessa forma não será necessário a instalação de dependências uma a uma.
```
## ⚙️ Executando os testes
```
Modo de uso: note que no código existem rotas (approutes) que são os caminhos para executar cada endpoint da api, em sua ferramenta (Postman) você ira copiar o link que a api retorna "http://127.0.0.1:5000" com o caminho de cada endpoint você ira colar a frente a sua rota. Exemplo: para executar um GET seu caminho deve ficar assim "http://127.0.0.1:5000/alunos/get", caso seja necessário um ID basta inseri-lo ao final ex:"http://127.0.0.1:5000/alunos/get/1", isso ira repetir em todos metodos.
Nesta api não será necessário se preocupar com o banco de dados, pois já esta conectada a SqLite.
```

Você também pode testar esta api online no swagger [link](https://app.swaggerhub.com/apis/SGP07ADM1/apiRest/0.1).

