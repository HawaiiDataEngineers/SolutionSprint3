# Solution Sprint 3

Repositório criado para a solution sprint 3 do curso de Engenharia de Dados. 

Alunos:
* Alessandro Bezerra
* Cristina Abrantes
* Patricia Claro


## Objetivo
O desafio é construir uma arquitetura completa para ingestão, transformação e análise de datasets com governança de dados e análise de custos

### Requisitos Técnicos

Uma ferramenta  utilizada para ingestão de dados
Uma camada de Storage, preferencialmente um Cloud Data Warehouse
Uma camada de transformação diretamente no Storage
No mínimo um dashboard ou report analisando os dados transformados
No mínimo um modelo analítico envolvendo técnicas de aprendizado de máquina
Um solução para governança e catálogo de dados
Entregar um comparativo baseado em critério técnicos, negócio e custo para cada tecnologias escolhida
Garantir que o agendamento/orquestração dos processos, a governança dos dados e a observabilidade do pipeline estejam presentes na arquitetura


### Arquitetura Atual

![image](https://user-images.githubusercontent.com/97312034/174391753-e55b2f0f-76f0-4aef-b748-3f39217e91cc.png)

1 - As demandas de dados não são atendidas dentro do prazo;
2 - A empresa ainda não conseguiu colocar os modelos de Advanced Analytics em produção;
3 - Os dados não são confiáveis, mesmo com vários processos de engenharia de dados implementados;
4 - Os dados não estão seguros, as informações sensíveis são acessadas pelos engenheiros de dados sem restrições;
5 - O departamento de TI ainda não impulsionou o Data Driven para as áreas de negócios;
6 - Modelos básicos de recomendações, sortimento de vendas, elasticidade de preços ainda não foram implementados.  


### Escolha da Solução

Nas últimas 2 sprints solutions tivemos a oportunidade de trabalhar com soluções de cloud da AWS e Microsoft Azure. 
Portanto, para além de podermos contar com a integração BigQuery e Tableau, gostaríamos de ter chance de trabalhar GCP encerrando assim a experiência acadêmica neste MBA com as três soluções de clouds indicadas no Quadrante Mágico  Gartner. 

![image](https://user-images.githubusercontent.com/97312034/174391925-f7b4c98a-b287-4b4a-a955-d71cfdf6db11.png)


Google Cloud foi nomeada por 4 anos consecutivos pela Gartner como uma das líderes em solução de infraestrutura Cloud e plataforma como serviço;
Maior transparência e facilidade para calcular custos em relação as AWS e Microsoft Azure;
A plataforma do Google Cloud fornece criptografia pronta para uso para dados em trânsito e dados em rest;
Velocidade de inovação: o Google continua com melhorias impressionantes ano a ano que veem o GCP fechar lacunas significativas com AWS e Microsoft Azure em termos de recursos CIPS e, em alguns casos, superá-los. Por exemplo, o GCP tem o serviço Kubernetes mais completo de qualquer provedor desse mercado;
Crescente share mind corporativo: o GCP está obtendo ganhos em termos de mind share com as empresas. A empresa tem visto uma adoção cada vez maior e chega ao topo dos resultados da pesquisa quando os líderes de infraestrutura são questionados sobre a seleção estratégica de provedores de nuvem nos próximos anos;
Solução cloud líder, a AWS, oferece uma oferta mais complexa, portanto, discernir entre a multiplicidade de soluções, como aquelas relacionadas a containers, bancos de dados e gerenciamento de dados, requer habilidades técnicas substanciais para apreciar as diferenças entre as ofertas e fazer a escolha adequada. Muitas empresas exigem assistência de terceiros como resultado da complexidade. Além disso, os novos serviços da AWS geralmente não estão prontos para consumo empresarial significativo por períodos prolongados porque essas ofertas básicas são amadurecidas em público. Além disso, a posição de liderança da empresa em IaaS e db PaaS cria um efeito de halo enganoso para outras ofertas, como AWS Outposts, que teve uma tração modesta até o momento;
A solução em segundo lugar no quadrante mágico, Microsoft Azure, possui licenciamento e contratação muito complexos e uma estrutura de gerenciamento de contas complexa com habilidades de nuvem desiguais no campo. Além disso, as pressões de vendas da Microsoft para aumentar a receita geral da conta impedem a implantação efetiva do Azure para reduzir os custos totais da Microsoft de um cliente;
A Google Cloud possui um longo histórico de liderança em tecnologias abertas, desde projetos como o Kubernetes, o padrão do setor em orquestração e interoperabilidade de contêineres, até o TensorFlow, uma plataforma para ajudar qualquer pessoa a desenvolver e treinar modelos de aprendizado de máquina. Aqui estão algumas melhorias recentes que fizemos para garantir que sua nuvem seja uma nuvem aberta


### BluePrint

![image](https://user-images.githubusercontent.com/97312034/174392036-42be14d2-884a-4fdb-8518-4851c277c9d4.png)


### Arquitetura Inicial Proposta

![image](https://user-images.githubusercontent.com/97312034/174392098-10080083-0f0f-4ff5-ab06-73e4d9e72c10.png)





