# Projeto de bloco: Arquitetura de Computadores, Sistemas Operacionais e Redes.

Projeto de Bloco da disciplina Projeto de Bloco: Arquitetura de Computadores, Sistemas Operacionais e Redes.

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/infnet_logo.jpg](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/infnet_logo.jpg)

**Aluno**: Bruno Fernandes

**Email:** bruno.fernandes@al.infnet.edu.br

**Prof:** Alcione Dolavale

### Relatório:

Para acessar o repositório deste trabalho  clique abaixo:

[Bwendel26/PB_INFNET_Python_redes_SO](https://github.com/Bwendel26/PB_INFNET_Python_redes_SO/tree/master/tp2)

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/1_estrutura_proj.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/1_estrutura_proj.png)

### Ferramentas utilizadas:

Linguagem de programação: Python (versão 3.9)

IDEs: PyCharm Community Edition 64 bits | Visual Studio Code

**Bibliotecas utilizadas:**

- Pygame

[Pygame Front Page - pygame v2.0.0.dev25 documentation](https://www.pygame.org/docs/)

- psutil

[psutil documentation - psutil 5.7.4 documentation](https://psutil.readthedocs.io/en/latest/)

- platform

[platform - Access to underlying platform's identifying data - Python 3.9.0 documentation](https://docs.python.org/3/library/platform.html)

- cpuinfo

[workhorsy/py-cpuinfo](https://github.com/workhorsy/py-cpuinfo)

- os

[os - Miscellaneous operating system interfaces - Python 3.9.2 documentation](https://docs.python.org/pt-br/3/library/os.html)

- socket

[socket - Low-level networking interface - Python 3.9.2 documentation](https://docs.python.org/3/library/socket.html)

- tkinter

[tkinter - Python interface to Tcl/Tk - Python 3.9.2 documentation](https://docs.python.org/3/library/tkinter.html)

- datetime

[datetime - Basic date and time types - Python 3.9.2 documentation](https://docs.python.org/3/library/datetime.html)

- sched

[sched - Event scheduler - Python 3.9.2 documentation](https://docs.python.org/3/library/sched.html)

- time

[time - Time access and conversions - Python 3.9.2 documentation](https://docs.python.org/3/library/time.html)

- subprocess

[subprocess - Subprocess management - Python 3.9.2 documentation](https://docs.python.org/3/library/subprocess.html)

- pickle

[pickle - Python object serialization - Python 3.9.2 documentation](https://docs.python.org/3/library/pickle.html)

- nmap

[python-nmap](https://pypi.org/project/python-nmap/)

### Objetivo:

> Um aplicativo simples de apresentação textual do monitoramento e análise de computadores em rede.

No TP2 o objetivo foi introduzir a prática do Projeto de Bloco, introduzindo o Pygame para disposição do Front-end da aplicação, trazendo informações básicas sobre o sistema.

A estrutura do TP2 foi a seguinte:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/estrutura_tp2.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/estrutura_tp2.png)

Resultado ao rodar o [main.py](http://main.py), chama as funcionalidades que serão apresentadas:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/tp2_main.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/tp2_main.png)

No TP3 o objetivo foi continuar a montagem de um pequeno sistema desktop de monitoramento dos componentes principais do computador. Foi codificado uma série de algoritmos, na linguagem Python, que utilizaram bibliotecas da linguagem para monitoramento do computador e para criar a interface que mostra os gráficos e informações a serem apresentadas pelo usuário.

A estrutura do TP3 foi a seguinte:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/imagem1.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/imagem1.png)

Como podemos ver os arquivos foram divididos um para cada funcionalidade, e o arquivo [main.py](http://main.py) (principal) chama todas as funções que executam o programa por um todo. Como podemos ver temos funções para cada chamada (uso_cpu.py, uso_memoria.py, uso_disco, info_cpu, etc...).

Temos o script [main.py](http://main.py) que faz a chamada das funções e variáveis dentro dos demais arquivos e consequentemente executa:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/imagem2.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/imagem2.png)

Logo no início fazemos o import da função loop_relogio, do arquivo loop_controle.py, que faz o controle das chamadas das funções dentro de um timer:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/imagem3.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/imagem3.png)

Podemos observar que essa função faz todo o controle do tempo, chamada das funções e controle de cada evento do pygame, seja no momento de sair do programa ou ao utilizar setas ou barra de espaço para fazer a navegação dentre as telas que fazem o monitoramento do computador dentro do software.

A função loop_relogio recebe como parâmetros uma lista de funções para serem chamadas e uma função separada para chamada da tela de resumo.

Dentro do código temos um arquivo Python específico para as variáveis gerais utilizadas no sistema, segue a imagem:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/imagem4.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/imagem4.png)

Dentro do sistemas temos um arquivo para mostrar de cada funcionalidade;

- Temos os arquivos de controle da cpu:

    ![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/imagem6.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/imagem6.png)

    Nesse arquivo temos as funções que mostram o uso da cpu e uma para cada um de seus núcleos, fazendo a plotagem com pygame,  em barras que mostram o total de uso.

    Logo em seguida temos um arquivo para capturar e apresentar as informações sobre a cpu e sistema no geral.

    ![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/imagem7.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/imagem7.png)

    E o resultado da chamada da função main quando chamamos a tela de cpu é o seguinte:

    ![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/imagem8.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/imagem8.png)

    - Temos, também, o arquivo de controle da memória principal (RAM):

        ![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/imagem9.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/imagem9.png)

        temos uma função que extrai a informação sobre a porcentagem de uso da memória e a segunda função usa a biblioteca pygame para mostrar a barra de uso da memória.

    - Função que mostra os discos e uso do disco em percentual:

        ![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/imagem10.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/imagem10.png)

        Temos uma função que pega, diretamente da biblioteca psutil, o percentual da memória utilizada e após mostra na interface do pygame.

        Como resultado final temos a seguinte interface controlada por pelas setas laterais:

        Tela 1

        ![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/imagem11.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/imagem11.png)

        Tela 2

        ![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/imagem12.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/imagem12.png)

        Tela 3

        ![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/imagem13.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/imagem13.png)

        Tela 4 (Resumo)

        ![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/imagem14.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/imagem14.png)

        Apresentação do TP3 rodando:

        ![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/tp3_main.gif](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/tp3_main.gif)

No TP4 tivemos continuidade em extração de informações do sistema, que consiste no objetivo do projeto como um todo. Utilizamos a biblioteca datetime para extrair as datas de modificação de processos, arquivos e diretórios.

A estrutura do TP4 foi a seguinte:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/4_tp4_estrutura.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/4_tp4_estrutura.png)

- O código em system_process.py tem como objetivo trazer informações sobre um processo que está em execução na máquina

    ![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/4_processo_do_sistema.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/4_processo_do_sistema.png)

    Tem como retorno:

    ![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/4_processo_do_sistema_rodando.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/4_processo_do_sistema_rodando.png)

Em seguida temos os códigos referentes a informações sobre um arquivo e um diretório do sistema:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/4_info_files_tp4.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/4_info_files_tp4.png)

Rodando:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/4_info_file_tp4_rodando.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/4_info_file_tp4_rodando.png)

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/4_info_dir_tp4.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/4_info_dir_tp4.png)

Rodando:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/4_info_dir_tp4_rodando.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/4_info_dir_tp4_rodando.png)

Em seguida foi solicitado o uso de uma GUI (Interface gráfica de usuário), não necessariamente sendo o Pygame, portanto entramos no desafio de usar o TKinter, bem famoso na comunidade do python, com o objetivo de retornar as informações nos dois códigos anteriores.

O código foi o seguinte:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/4_view_tkinter_tp4.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/4_view_tkinter_tp4.png)

Nota: Aqui tivemos o problema do Tkinter, por algum motivo não retornar as informações sobre diretórios, independente do diretório usado ou ambiente.

No teste usamos o diretório atual como exemplo("./").

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/tp4_view_tkinter.gif](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/tp4_view_tkinter.gif)

Sobre o erro apresentado acima, podemos observar, no exemplo abaixo, que a função que faz o retorno das informações sobre diretórios está funcionando e está retornando no mesmo formato que a de arquivos;

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/4_info_dir_tp4_rodando%201.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/4_info_dir_tp4_rodando%201.png)

No TP5 introduzimos a utilização do módulo sched, que faz chamadas escalonadas do código conforme solicitado, utilizamos ele com objetivo de retornar funções, já antes feitas, de forma que o código executasse em um determinado tempo.

A estrutura do TP5 foi a seguinte:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/5_estrutura.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/5_estrutura.png)

Logo de início temos  o código apresentado em [staggering.py](http://staggering.py), que é a resolução da primeira questão do TP, com o seguinte código:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/5_cham_escalonada_code.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/5_cham_escalonada_code.png)

As funções chamadas pelo arquivo estão no funcs.py;

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/5_funcs.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/5_funcs.png)

Ao final retornamos o tempo total da execução do programa:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/tp5_escalonamento.gif](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/tp5_escalonamento.gif)

Como podemos observar, temos os tempos inicial e final da execução, com o tempo total calculado.

Em seguida utilizamos esse módulo para chamar demais funções, anteriores:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/5_sched_call_funcs.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/5_sched_call_funcs.png)

As funções utilizadas chamadas estão nos arquivos info_files.py e info_dir.py, já apresentadas no TP4.

Execução do código:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/tp5_call_funcs.gif](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/tp5_call_funcs.gif)

A seguir tivemos que fazer um programa que retornasse de forma escalonada os clocks da máquina em tempos diferentes, segue o código:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/5_compare_clock_tp5.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/5_compare_clock_tp5.png)

Segue com o código acima rodando:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/5_compareclock_rodando_tp5.gif](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/5_compareclock_rodando_tp5.gif)

Nota: Aparentemente o trecho de código (psutil.cpu_freq().current) que usa o módulo do psutil, para retornar a frequência atual, está retornando de forma estática.

Entrando no TP6, a estrutura do código foi bem enxuta, no geral tivemos que codificar o retorno de informações sobre a rede, trazendo informações sobre hosts em um determinado IP, máquinas pertencentes  a uma SUB-REDE e informações sobre as portas que estão rodando naquele endereço, utilizamos aqui os módulos os, subprocess, platform e o nmap pra fazer a visualização das portas;

Estrutura:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/6_estrutura_tp6.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/6_estrutura_tp6.png)

Código presente em [network.py](http://network.py), com objetivo de apresentar informações sobre as máquinas em uma sub-rede:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/6_networt_tp6.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/6_networt_tp6.png)

Segue a execução do código:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/6_networt_tp6_rodando.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/6_networt_tp6_rodando.png)

Nota: nesse caso o teste foi feito propositalmente em um IP que teria apenas um host, pela questão do tempo de execução desse código ser grande.

O código referente as portas é o seguinte:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/6_port1_tp6.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/6_port1_tp6.png)

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/6_port2_tp6.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/6_port2_tp6.png)

Segue a execução do código:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/6_port_tp6_rodando.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/6_port_tp6_rodando.png)

Seguindo para o TP7, usamos o módulo socket para requisitar informações sobre pacotes e bytes transferidos na rede, também utilizamos o módulo OS para trazer informações sobre Gateway e Subnet da máquina.

A estrutura do TP7 foi a seguinte:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/7_estrutura_tp7.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/7_estrutura_tp7.png)

Inicialmente temos o código de network_data.py que retorna informações sobre IP, Gateway e Subnet Mask, segue o código:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/7_network_data_tp7.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/7_network_data_tp7.png)

O código utiliza o socket para pegar a informação sobre o IP da máquina e o os para fazer uma chamada do comando "ipconfig" e iterar sobre ele para pegar informação sobre Gateway e Subnet. Ao rodar o código, temos o seguinte resultado:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/7_network_data_tp7_rodando.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/7_network_data_tp7_rodando.png)

Em seguida tivemos os códigos process_data_usage.py e interface_data_usage.py, eles retornam informações sobre o uso de dados por processos e por interfaces, consecutivamente;

Processos:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/7_process_data_tp7.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/7_process_data_tp7.png)

Rodando:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/7_process_data_rodando_tp7.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/7_process_data_rodando_tp7.png)

    Interfaces:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/7_interface_data_tp7.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/7_interface_data_tp7.png)

Rodando:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/7_interface_data_rodando_tp7.gif](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/7_interface_data_rodando_tp7.gif)

Ao final, como pedido, fizemos um código (view.py) que retorna todas as informações das funções anteriores de maneira conjunta:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/7_view_tp7.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/7_view_tp7.png)

Rodando:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/7_view_rodando_tp7.gif](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/7_view_rodando_tp7.gif)

A seguir entramos no TP8, onde utilizamos, principalmente, os módulos socket e pickle para levantar uma aplicação servidor e uma cliente, o pickle faz a transição dos dados, enxergados pelo python, para bits ao subir os dados para o servidor e no momento que o cliente recebe esses dados, ele retorna esses bits em informações que o python reconhece.

Estrutura:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/8_estrutura_tp8.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/8_estrutura_tp8.png)

Inicialmente temos a aplicação servidor:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/8_server_tp8.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/8_server_tp8.png)

Essa aplicação importa a função de informações do sistema do arquivo system.py

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/8_system_tp8.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/8_system_tp8.png)

Iniciamos o servidor, logo em seguida a aplicação cliente entra em ação, segue o código do cliente (client.py):

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/8_client_tp8.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/8_client_tp8.png)

Ao levantar o servidor e iniciar a aplicação cliente temos as seguintes informações retornadas:

![Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/8_main_tp8.png](Projeto%20de%20bloco%20Arquitetura%20de%20Computadores,%20Sist%203698481bd6894d7db1fecb50978c8293/8_main_tp8.png)

Informações referentes a máquina que gerou todo o código.

Ao final publicamos a apresentação e a aplicação toda no moodle da INFNET.