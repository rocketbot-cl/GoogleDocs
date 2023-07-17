# Google Docs
  
Módulo para controlar o Google Docs  

*Read this in other languages: [English](Manual_GoogleDocs.md), [Português](Manual_GoogleDocs.pr.md), [Español](Manual_GoogleDocs.es.md)*
  
![banner](imgs/Banner_GoogleDocs.png)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Configurar credenciais G-Suite
  
Obtenha permissões para manipular o Google Docs com o Rocketbot
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho do arquivo de credenciais|Selecione o arquivo de credenciais do G-Suite|Path|

### Novo documento
  
Cria novo documento Google Docs.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome do documento|Nome do documento a criar|Nome: |
|Variável onde o ID será salvo|Variável onde o ID do documento criado será salvo|{Result}|

### Escreva no documento
  
Escreva no documento do Google Docs
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do documento|Insira o ID do documento do Google Docs|1XfKS0_ftXfKSpO_iX6udViX6udViX6udV_iX6udV|
|Escreva texto|Texto para escrever no documento do Google Docs|Lorem ipsum dolor sit amet, consectetur adipiscing elit.|

### Ler documento
  
Ler um documento Google Docs
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do documento|ID do documento do Google Docs|1XfKS0_ftXfKSpO_iX6udViX6udViX6udV_iX6udV|
|Variable onde o resultado será salvo|Variável onde o resultado da leitura do documento será salvo|{Result}|

### Adicionar imagem
  
Adicione uma imagem ao documento
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do documento|ID do documento ao qual a imagem será adicionada. O ID do documento está na URL do documento|1XfKS0_ftXfKSpO_iX6udViX6udViX6udV_iX6udV|
|Url da imagem|Url da imagem que será adicionada ao documento|imagem.jpg|
