# PB_INFNET_Python_redes_SO <h1>
### Projeto do bloco de Arquitetura de Computadores, Sistemas Operacionais e Redes com Python da INFNET. <h3>
  
**IDE utilizada: PyCharm Community**
<br>
**Linguagem de programação: Python**
<br>
**Bibliotecas utilizadas:** 
* Pygame
* psultil ([documentação](https://psutil.readthedocs.io/en/latest/))

<hr>

# TP2 <h1>

## O entregável do seu projeto de bloco será: <h2>

Um software cliente-servidor em Python que explore conceitos de arquitetura de redes, arquitetura de computadores e/ou de sistemas operacionais, acompanhado de relatório explicativo.

#### Este TP corresponde à primeira entrega do projeto, no qual o entregável será: <h4>

Um aplicativo simples de apresentação gráfica do monitoramento e análise do computador. Ele deverá ser implementado em Python usando módulos como psutil (para capturar dados do sistema computacional) e Pygame (para exibir graficamente os dados). Junto ao aplicativo, deverá ser entregue um relatório, que deve ser baseado no template localizado neste link.

Escreva um programa em Python que exiba graficamente através do uso do módulo Pygame:

1. Uma barra de indicação da porcentagem do uso de memória;
2. Uma barra de indicação da porcentagem do uso de CPU, junto com a informação detalhada da plataforma de processamento;
3. Uma barra de indicação da porcentagem do uso de disco;
4. Um texto com a informação do IP da máquina.

Todas as barras e informações devem estar na mesma tela, devendo fazer o uso de superfícies ou surfaces.

No relatório adicione informações sobre o entregável da maneira que achar mais interessante. No entanto, alguns itens adicionais são __obrigatórios__:

1. Descreva de maneira detalhada sobre o entregável.
2. Descreva de maneira teórica a utilização dos módulos e ferramentas.
3. Descreva de maneira teórica como foi capaz de obter as informações da memória, CPU e Disco.
4. Descreva de maneira teórica sobre o IP e porque se faz necessária a utilização dos mesmos para conexões com outros dispositivos.

O que deve ser entregue:

1. Relatório explicativo sobre o entregável, descrevendo de maneira teórica a utilização dos módulos e ferramentas.   
2. Ainda no mesmo relatório, o aluno deve apresentar os códigos do programa junto com impressões da tela (printscreen) do resultado de uma ou mais execuções, que mostrem que seu programa funciona conforme o requisitado.
3. Adicionalmente, o arquivo .py com o código do programa.

Lembre de realizar todos os Testes de Performance, pois cada entrega será uma parte da entrega final do seu Projeto de Bloco.

Antes de fazer sua entrega, reúna todos os arquivos relativos ao seu TP em um único arquivo .zip. Utilize seu próprio nome para nomear o arquivo, identificando também o teste correspondente, como no exemplo: Nome_sobrenome_PB_TP2.zip.

<hr>

# TP3 <h1>

## Como você já sabe, o entregável do seu projeto de bloco será: <h2>

Um software cliente-servidor em Python que explore conceitos de arquitetura de redes, arquitetura de computadores e/ou de sistemas operacionais, acompanhado de relatório explicativo.

#### Este TP corresponde à segunda entrega do projeto, no qual o entregável será: <h4> 

Um aplicativo simples de apresentação gráfica do monitoramento e análise do computador. Ele deverá ser implementado em Python usando módulos como psutil (para capturar dados do sistema computacional) e Pygame (para exibir graficamente os dados). Junto ao aplicativo, um relatório deverá ser entregue.

Faça todos os Testes de Performance, pois cada um deles é uma parte do seu Projeto de Bloco.

Este TP3 corresponde à segunda entrega do projeto e ele é uma alteração do TP2.

Adicione ao seu programa feito no TP2 informações mais detalhadas de uso de CPU. Você pode adicionar as informações da maneira que achar mais interessante. No entanto, algumas são __obrigatórias__:

1. Alterar o programa feito no TP2 de modo a possuir 5 visualizações diferentes: <h5>
* Uma para colocar todas as informações associadas ao processador
* Uma para colocar todas as informações associadas à memória
* Uma para colocar todas as informações associadas ao Disco
* Uma para colocar todas as informações associadas ao IP  
* Todas as anteriores devem ser alteradas caso o usuário clique nas setas esquerda ou direita do teclado. Seguindo sempre uma 
ordem predefinida, como em um carrossel.
* Uma última que teria um resumo de todas elas. O qual seria acessado quando o usuário clica na tecla “Barra” do teclado.

2. Alterar a barra de CPU do TP2 para ter barras de CPU associadas a cada núcleo (core);
3. Adicionar informação de nome/modelo da CPU (brand);
4. Adicionar informação do tipo da arquitetura (arch);
5. Adicionar informação da palavra do processador (bits);
6. Adicionar informação sobre a frequência total e frequência de uso da CPU;
7. Adicionar informação do número total de núcleos (núcleo físico) e threads (núcleo lógico).

**Mantenha as barras de uso de memória e disco (e suas superfícies). Elas serão alteradas, da mesma forma que a CPU, em TPs posteriores.**

Neste TP, você tem liberdade para __criar__ quantas superfícies achar necessárias. Além disso, pode aumentar as dimensões da tela e alterar as dimensões e posições das superfícies conforme achar melhor.

Adicione ao seu relatório feito no TP2 informações mais detalhadas sobre o entregável. Você pode adicionar as informações da maneira que achar mais interessante. No entanto, existem itens __obrigatórios__:

1. Descreva de maneira detalhada o entregável.
2. Descreva de maneira teórica (pode utilizar exemplos) as diferenças de arquitetura de CPU.
3. Descreva de maneira teórica o que é a palavra do processador.
4. Descreva de maneira teórica a diferença entre os núcleos físicos e lógicos. E em que influencia no processamento a utilização de núcleos lógicos.

O que deve ser entregue:

1. Relatório explicativo sobre o entregável.
2. Ainda, no mesmo relatório,o aluno deve apresentar todos os artefatos como código do programa junto com impressões da tela (printscreen) do resultado de uma ou mais execuções que mostrem que seu programa funciona conforme o requisitado.
3. Adicionalmente, o arquivo .py com o código do programa.

Antes de fazer sua entrega, reúna todos os arquivos relativos ao seu TP em um único arquivo .zip. Utilize seu próprio nome para nomear o arquivo, identificando também o teste correspondente, como no exemplo: Nome_sobrenome_PB_TP3.zip.

<hr>
