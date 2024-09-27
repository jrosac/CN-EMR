# AMAZON EMR

## Resumo

O presente projeto terá como objetivo demonstrar de maneira detalhada o processo de criação de um cluster utilizando o serviço Amazon EMR (Elastic MapReduce), explorando as etapas necessárias para configurar e iniciar o cluster. Em seguida, será abordada a execução de tarefas dentro desse ambiente. Por fim, será realizada a execução de um script Apache Spark no cluster. Este projeto busca fornecer uma visão prática e estruturada sobre o uso do Amazon EMR e o seu potencial no contexto de big data.

## Primeira Etapa

A primeira parte consiste em buscar e instanciar uma feature do EC2 chamada **key pairs** e, com isso, criar um par de chaves. O par de chaves é necessário pois ele provém ao **Master Node** a capacidade de conexão entre ele e os **Workers** (outros nodes). Sem esse par de chaves, o **Master Node** não conseguirá executar as ações necessárias. Esse par de chaves será utilizado posteriormente para acessar o Cluster também.

### Busca do key pairs


![Key pairs na amazon](docs/imgs/Screenshot_20240925_154542.png)

Console para instanciar um par de chaves.

![chaves instanciadas](docs/imgs/Screenshot_20240925_160444.png) 
   

#### Informações para a criação do par de chaves

Após a criação do par de chaves, será feito o download do arquivo `.pem` com o nome escolhido do par, que será salvo na sua máquina.

![console para criar keypairs](docs/imgs/Screenshot_20240925_160115.png) 

## Segunda Etapa

A segunda etapa consiste na criação do cluster a partir do AMAZON EMR. A criação do cluster será dividida em 3 etapas principais: nome e aplicativos, configuração do cluster, provisionamento e escalabilidade.

### Tela para a criação e visualização dos clusters criados

![Clusters instanciados](docs/imgs/Screenshot_20240925_161711.png)

### Tela de nomeação e escolha da versão do cluster junto das aplicações que serão utilizadas.  

![console para isntanciar cluster](docs/imgs/Screenshot_20240925_163207.png)

### Tela para a configuração do Cluster

Definição do nome e capacidade de memória do **Master Node** (núcleo) e dos **Workers** (tarefa).

![info cluster](docs/imgs/Screenshot_20240925_163450.png)

### Escalabilidade do Cluster

Define quantos núcleos e workers serão instanciados e também opções de rede e algumas configurações, como **Etapas**.

![info cluster](docs/imgs/Screenshot_20240925_163510.png)


### Opção de encerramento automático

O cluster poderá ser encerrado automaticamente após 1 hora de uso, mas esse tempo pode ser editado para o valor desejado.

![encerramento automatico cluster](docs/imgs/Screenshot_20240925_163524.png)

### Logs do cluster

Os logs do cluster serão salvos numa instância do AMAZON EC3. Pode ser uma instância já existente; se não, será instanciada uma nova.

![Logs das ações do cluster](docs/imgs/Screenshot_20240925_163533.png)

### Perfis de serviço e instâncias

Perfis e instâncias com as configurações de  default para usar o próprio **autoscaling** da AWS.

![info cluster](docs/imgs/Screenshot_20240925_163617.png)

### Resumo

Resumo das informações e configurações do Cluster criado.
![Config cluster](docs/imgs/Screenshot_20240925_163659.png)

## Terceira Etapa

A terceira etapa consiste em adicionar uma etapa dentro do EMR a partir de um script armazenado no EC3. 

Primeiramente, será necessário instanciar um bucket no **Amazon S3**. Nele ficará armazenado o script a ser processado no cluster. As configurações utilizadas serão as recomendadas e já marcadas por default.

![tela para criar bucket](docs/imgs/Screenshot_20240926_012234.png)


![info bucket](docs/imgs/Screenshot_20240926_012259.png)

Após isso, você irá selecionar o arquivo da sua máquina que deseja armazenar no S3 e fazer o upload para o bucket instanciado. No caso da atividade, estou utilizando um arquivo chamado **SparkNaAws.py** .

![Upload arquiva](docs/imgs/Screenshot_20240926_012334.png)

![informações do script](docs/imgs/Screenshot_20240926_012353.png)

Após o upload ser concluído, você poderá ver as informações do script dentro do bucket. Em seguida, você irá copiar a URL do **S3** apertando o botão no canto superior direito.

Após o upload do arquivo no **S3**, você irá retornar ao **EMR**, acessar o cluster instanciado, selecionar a opção **Etapa** e apertar o botão de adicionar no canto superior direito.


![criação de etapa dentro do EMR](docs/imgs/Screenshot_20240926_015346.png)

Após isso, selecione a opção **Aplicativo do Spark** e o modo de implantação **Modo Cliente** para rodar o script no nó primário como cliente externo. Em seguida, aperte **Adicionar Etapa**.

Após a etapa ser processada pelo cluster, ela irá retornar os logs de **Controller de stderr** que irão conter dados referentes ao processamento e possíveis erros. O **stdout** conterá a saída do script desejado.


![Logs da etapa concluida](docs/imgs/Screenshot_20240926_015913.png)

Com isso, você terá conseguido rodar um script de aplicação Spark dentro da AWS.

### Quarta etapa
A quarta etapa consiste em fazer uma conexão pela terminal Mac/linux via protocolo SSH, primeiramente você irá acessar o resumo as informações do cluster instanciado e ira selecioar a opção **Conectar-se ao nó primário usando SSH** 

![ConexãoSSH](docs/imgs/Screenshot_20240927_090136.png)

![Comando do terminal](docs/imgs/Screenshot_20240927_090232.png)

após isso irá copiar o comando indicado e roda-lo no mesmo diretorio em que se encontra o seu arquivo de chave `.pem`

Se der algum erro de permissão use o comando chmod 400 `arquivo.pem` e rode o comando novamente. Com isso você terá acesso ao terminal do Cluster e poderá rodar scripts e aplicações por lá. 

Uma dica, instale o git utilizando o comando `yum install git` e baixe repositorios para rodar diretamente no cluster.