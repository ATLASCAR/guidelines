Objetivo:  definir a metodologia para guardar gerir e trocar código relativamente ao projeto ATLASCAR

Objetivos:
Criar conta organizacional github e associar alunos [Miguel e Bernardo]
Tentar criar uma estrutura de diretórios (metapackages) repositórios com apontadores para outros reps [Miguel e Bernardo]
Verificar quem é o “dono ” do repositório. O user pode apagar depois o repositório ou não o consegue fazer sem o consentimento da organização? Como são as alterações futuras, permissões [Miguel]
Separar repositórios por funcionalidade [Pedro, Tiago, Ricardo, Bernardo]
Separar atlascar_demos e atlascar_bringup
Repositórios refletem funcionalidades (se possível reaproveitáveis) 
Averiguar qualquer é a melhor maneira de fazer o LICENSE, qual a melhor? GPL3? Fazer os templates para a LICENSE [Vítor Santos]
Um repositório com estas regras (ou então outro local adequado para o fazer dentro da página do github organização) [Miguel]

Regras de nomenclatura: 

Readme de cada repositorio https://gist.github.com/PurpleBooth/109311bb0361f32d87a2
Template de repositório ??? usar http://wiki.ros.org/DevelopersGuide
Repositórios podem ser ROS packages ou conter vários ROS packages ou ter outros projetos (matlab, javascript, etc)
Deve sempre ser feito um fork e pull request. Só se não for possível deve ser feito um fork que é incluído na organização ATLASCAR.
Como lidar com o lartk?
Desmembrar (retirar a funcionalidade necessária se ainda não tiver sido feito)
Criar um repositório (com a referência adequada) dentro da organização github (ATLACAR)





--- Email Vitor Santos com kickoff da reunião ---

Para começar, eu diria que os tópicos deveriam incluir também os seguintes:

 	-Definição/criação do repositório (ou repositórios) para guardar o 
software e documentação relacionada
 	-Definição das regras de organização de packages
 		-Nomenclaturas, standardização (?)
 		-Uso de cabeçalhos (headers/copyright notice)
 		-Instruções e ficheiros de README
 	-Relação com o LARtk5 e regras de migração e importação de packages
 	-Distribuição de trabalho concreto para os três alunos atualmente 
mais próximos do projeto (Tiago, Ricardo, Pedro)
 	-Convite posterior aos restantes alunos para integrarem os seus 
trabalhos no repositório seguindo as regras e
  	os procedimentos que estes primeiros implementarem (Tomás, Nuno, 
Filipe(?) )

