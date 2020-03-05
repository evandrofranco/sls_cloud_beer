# Serverless Cloud Beer

Projeto Serverless demo para o Cloud Beer

## Pré-Requisitos

Possuir NodeJS e NPM Instalados

Instalar o framework:
    
    npm install serverless

    sls plugin install -n serverless-python-requirements

Criar um virtualenv (Opcional)

Rodar os pre-requisitos do Python:

    pip install -r requirements.txt

Instalar o plugin (dependência) para a parte estática do site:

    npm install --save serverless-finch

Obs.: Neste exemplo estamos usando um domínio registrado. Portanto, vamos criar um CNAME e também é preciso registrar um certificado no ACM para este cname.

## Criação Dependências

Declarar as variáveis de ambiente das dependências (serão usadas para todos os comandos abaixo):

    export BUCKET_NAME=<nome-do-bucket>
    export CERTIFICATE_ARN=<certificado-gerado-no-acm>
    export TABLE_NAME=<value>
    export AWS_PROFILE=<value>
    export TOKEN=<value>

Primeiramente, criar as dependências gerais:

    cd resources/

    sls deploy

## Variáveis de Ambiente

É recomendado utilizar variáveis de ambiente para não deixar informações sensíveis abertas.

Obs.: As variáveis foram declaradas no passo anterior.

## Criar Stack (Lambda)

Para criar a stack na AWS, executar o comando abaixo na raiz do projeto:

    cd ..

    sls deploy

## Atualizar site estático

Após a criação do serverless, o API GW gerará um output com a URL da API.

Substitua o valor <COLOCAR_URL_DO_API_GW_AQUI> no index.html dentro da pasta client/dist, com a URL gerada pelo API Gateway.

Também substitua o valor <COLOCAR_TOKEN_AQUI> no index.html dentro da pasta client/dist, com o valor do token de autorização.

Execute o comando abaixo para fazer o deploy da parte estática:

    sls client deploy --no-config-change --no-policy-change --no-cors-change

## Remover Stack

Para remover primeiramente é necessário remover a stack da raiz (funções lambda):

    sls remove

Em seguida é necessário esvaziar o bucket s3 criado, e por fim, apagar a stack dos recursos:

    cd resources/

    sls remove

## Refs:

https://serverless.com/framework/docs/getting-started/
https://serverless.com/blog/deploy-serverless-frontend-with-serverless-finch-plugin/