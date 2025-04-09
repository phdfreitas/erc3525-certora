# ERC-3525: Token Semi-Fungível

## Sobre o Projeto

Esse repositório contém contém uma verificação formal do ERC-3525 usando o **Certora**. Nosso objetivo com esse projeto é dar um passo adiante, uma vez que demos o primeiro passo com o projeto ERC-4337. No entanto, tivemos alguns problemas na aplicação de testes com o ERC-4337, citados no repositório, caso deseje ler, clique aqui.

Com esse projeto envolvendo certora, além do objetivo citado anteriormente, queremos também testar o certora em um contrato real e ter algum contato com essa ferramenta, o que nos permitirá ver as vantagens e desvantagens entre seu uso e o uso de outras ferramentas como halmos, apesar dos contextos diferentes de aplicação.

## ERC-3525

Falando um pouco sobre o contrato que aplicamos a verificação formal, ele é introduz o conceito de _tokens semi-fungíveis_. Nesse caso, agrega propriedades tanto do ERC-20 quanto do ERC-721. Para saber mais, clique aqui

## Certora

Como citado anteriormente, o Certora é uma ferramenta que permite a verificação formal de contratos inteligentes. Para isso, permite que você escreva especificações formais usando **_rules, invariants e ghost variables_**. Isso nos permite fazer verificações sobre o contrato sem a necessidade de executar testes tradicionais.

## Sobre o desenvolvimento do projeto

Para fazer os testes do ERC-3525, inicialmente, tentamos apenas baixar o contrato por meio do **forge install**, no entanto, na hora de escrever as _rules_ tivemos vários problemas. Depois dessa tentativa, baixamos a própria implementação do contrato (dispoível aqui) e suas dependências necessárias, no entanto, mais uma vez tivemos vários problemas durante a executação do arquivo _spec_, o principal problema se referiu ao acesso a mais de um diretório para execução das regras, isto é, no começo, o contrato estava na pasta **src** e suas dependências (como esperado) estavam na pasta **lib**, no entanto, mesmo tentando colocar no **.conf** que o certora tivesse acesso a ambos diretórios, na hora da _compilação_ eram geradas algumas exceções referentes a esse problema. Procurando um pouco, parece que além do diretório onde o .spec está contido, o certora só acessa mais um diretório (setado por meio de **solc_allow_path**).

Para lidar com esse problema, iniciamos um projeto foundry (**forge init**), criamos uma pasta **certora > conf** e dentro dela colocamos tanto a implementação do contrato quanto as dependências. Entendemos que essa não é a maneira ideal para isso, no entanto, foi a maneira que encontramos para lidar com isso, sendo a única até o momento de escrita desse texto, mas podendo mudar no futuro.

## Sobre os _Testes_ (spec/rules)

No objetivo inicial com os testes foi o de testar principalmente os métodos 'públicos' na interface do ERC-3525. Nesse sentido, criamos _rules_ para alguns métodos como:

- [x] balanceOf
- [x] slotOf
- [x] approve
- [x] allowance
- [x] transferFrom

## Testes/Rules

- [x] onlyAuthorizedCanTransferSpec: Verifica se um token só pode ser transferido por seu proprietário.
- [x] unauthorazedTransferSpec: Verifica se uma transferência feita sem autorização não é executada
- [x] slotConsistencySpec: Verifica se _slotOf_ retorna o mesmo valor antes e depois.
- [x] transferValueToNewToken: Cria um novo token ao transferir um valor x para ele.
- [x] transferValuePreservesTotal: Verifica se a transferência de valor entre dois tokens do mesmo slot mantém a integridade do saldo total (soma dos valores antes e depois deve ser igual).
- [x] mintOnTransferIncreasesSupply: Confirma que transferências para um novo endereço criam um token derivado e incrementam o totalSupply.
- [x] derivedTokenInheritsSlot: Valida se tokens criados via transferência herdam o slot do token original.
- [x] transferToZeroAddressFails: Verifica se transferências para address(0) revertem, prevenindo queima acidental de tokens.
- [x] approveZeroAddressFails: Garante que aprovações para address(0) revertem, evitando autorizações inválidas.
- [x] concurrentApprovalChange: Testa se mudanças concorrentes em allowance (aprovação + revogação) não deixam estado inconsistente.
