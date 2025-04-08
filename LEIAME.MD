# ERC-3525: Token Semi-Fungível

## Sobre o Projeto
Esse repositório contém contém uma verificação formal do ERC-3525 usando o **Certora**. Nosso objetivo com esse projeto é dar um passo adiante, uma vez que demos o primeiro passo com o projeto ERC-4337. No entanto, tivemos alguns problemas na aplicação de testes com o ERC-4337, citados no repositório, caso deseje ler, clique aqui. 

Com esse projeto envolvendo certora, além do objetivo citado anteriormente, queremos também testar o certora em um contrato real e ter algum contato com essa ferramenta, o que nos permitirá ver as vantagens e desvantagens entre seu uso e o uso de outras ferramentas como halmos, apesar dos contextos diferentes de aplicação. 

## ERC-3525
Falando um pouco sobre o contrato que aplicamos a verificação formal, ele é introduz o conceito de *tokens semi-fungíveis*. Nesse caso, agrega propriedades tanto do ERC-20 quanto do ERC-721. Para saber mais, clique aqui 

## Certora
Como citado anteriormente, o Certora é uma ferramenta que permite a verificação formal de contratos inteligentes. Para isso, permite que você escreva especificações formais usando ***rules, invariants e ghost variables***. Isso nos permite fazer verificações sobre o contrato sem a necessidade de executar testes tradicionais. 