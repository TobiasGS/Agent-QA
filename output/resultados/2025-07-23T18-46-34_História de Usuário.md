# Cenários BDD Gerados

### Funcionalidade: Edição de Dados Cadastrais

#### Cenário 1: Acessar Formulário de Edição de Dados Pessoais
Dado que o usuário está logado no sistema
Quando clicar na opção "Editar Perfil" ou "Meus Dados"
Então deve ser redirecionado para a tela de edição de dados pessoais
E a tela deve apresentar um formulário com os campos Nome Completo, CPF, E-mail, Telefone e Endereço (CEP, Cidade, Estado, Rua e Número)
E os campos devem estar pré-preenchidos com os dados atualmente cadastrados

#### Cenário 2: Visualização do Campo CPF
Dado que o usuário está na tela de edição de dados pessoais
Quando visualizar o campo CPF
Então o campo CPF não deve ser editável
E deve apresentar o valor do CPF atualmente cadastrado

#### Cenário 3: Edição dos Campos Nome Completo e E-mail
Dado que o usuário está na tela de edição de dados pessoais
Quando editar os campos Nome Completo e E-mail
Então os campos devem ser editáveis
E devem manter as validações de obrigatoriedade e formato (para e-mail)

Exemplos de validação:
| Campo | Valor | Resultado |
| --- | --- | --- |
| Nome Completo |  | Deve apresentar mensagem de erro "Nome Completo é obrigatório" |
| E-mail |  | Deve apresentar mensagem de erro "E-mail é obrigatório" |
| E-mail | exemplo | Deve apresentar mensagem de erro "E-mail inválido" |

#### Cenário 4: Edição dos Campos de Endereço
Dado que o usuário está na tela de edição de dados pessoais
Quando editar os campos de endereço (CEP, Cidade, Estado, Rua e Número)
Então os campos devem ser editáveis
E devem manter as validações e o comportamento de preenchimento automático de CEP

Exemplos de validação:
| Campo | Valor | Resultado |
| --- | --- | --- |
| CEP |  | Deve apresentar mensagem de erro "CEP é obrigatório" |
| Cidade |  | Deve apresentar mensagem de erro "Cidade é obrigatória" |
| Estado |  | Deve apresentar mensagem de erro "Estado é obrigatório" |
| Rua |  | Deve apresentar mensagem de erro "Rua é obrigatória" |
| Número |  | Deve apresentar mensagem de erro "Número é obrigatório" |

#### Cenário 5: Salvar Alterações com Sucesso
Dado que o usuário está na tela de edição de dados pessoais
E os campos estão preenchidos corretamente
Quando clicar no botão "Salvar"
Então deve receber uma mensagem de sucesso "Seus dados foram atualizados com sucesso!"

#### Cenário 6: Salvar Alterações com Erro
Dado que o usuário está na tela de edição de dados pessoais
E os campos estão preenchidos incorretamente
Quando clicar no botão "Salvar"
Então deve receber uma mensagem de erro "Não foi possível atualizar seus dados. Por favor, verifique as informações e tente novamente."

#### Cenário 7: Salvar Alterações com Campos Obrigatórios Vazios ou Inválidos
Dado que o usuário está na tela de edição de dados pessoais
E os campos obrigatórios estão vazios ou inválidos
Quando clicar no botão "Salvar"
Então deve receber mensagens de erro específicas para cada campo
E a atualização deve ser impedida

Exemplos de validação:
| Campo | Valor | Resultado |
| --- | --- | --- |
| Nome Completo |  | Deve apresentar mensagem de erro "Nome Completo é obrigatório" |
| E-mail |  | Deve apresentar mensagem de erro "E-mail é obrigatório" |
| E-mail | exemplo | Deve apresentar mensagem de erro "E-mail inválido" |
| CEP |  | Deve apresentar mensagem de erro "CEP é obrigatório" |
| Cidade |  | Deve apresentar mensagem de erro "Cidade é obrigatória" |
| Estado |  | Deve apresentar mensagem de erro "Estado é obrigatório" |
| Rua |  | Deve apresentar mensagem de erro "Rua é obrigatória" |
| Número |  | Deve apresentar mensagem de erro "Número é obrigatório" |

# Cenários Complementados

### Funcionalidade: Edição de Dados Cadastrais

#### Cenário 1: Acessar Formulário de Edição de Dados Pessoais
Dado que o usuário está logado no sistema
Quando clicar na opção "Editar Perfil" ou "Meus Dados"
Então deve ser redirecionado para a tela de edição de dados pessoais
E a tela deve apresentar um formulário com os campos Nome Completo, CPF, E-mail, Telefone e Endereço (CEP, Cidade, Estado, Rua e Número)
E os campos devem estar pré-preenchidos com os dados atualmente cadastrados
@regressivo

#### Cenário 2: Visualização do Campo CPF
Dado que o usuário está na tela de edição de dados pessoais
Quando visualizar o campo CPF
Então o campo CPF não deve ser editável
E deve apresentar o valor do CPF atualmente cadastrado
@critico

#### Cenário 3: Edição dos Campos Nome Completo e E-mail
Dado que o usuário está na tela de edição de dados pessoais
Quando editar os campos Nome Completo e E-mail
Então os campos devem ser editáveis
E devem manter as validações de obrigatoriedade e formato (para e-mail)
@regressivo

Exemplos de validação:
| Campo | Valor | Resultado |
| --- | --- | --- |
| Nome Completo |  | Deve apresentar mensagem de erro "Nome Completo é obrigatório" |
| E-mail |  | Deve apresentar mensagem de erro "E-mail é obrigatório" |
| E-mail | exemplo | Deve apresentar mensagem de erro "E-mail inválido" |

#### Cenário 4: Edição dos Campos de Endereço
Dado que o usuário está na tela de edição de dados pessoais
Quando editar os campos de endereço (CEP, Cidade, Estado, Rua e Número)
Então os campos devem ser editáveis
E devem manter as validações e o comportamento de preenchimento automático de CEP
@regressivo

Exemplos de validação:
| Campo | Valor | Resultado |
| --- | --- | --- |
| CEP |  | Deve apresentar mensagem de erro "CEP é obrigatório" |
| Cidade |  | Deve apresentar mensagem de erro "Cidade é obrigatória" |
| Estado |  | Deve apresentar mensagem de erro "Estado é obrigatório" |
| Rua |  | Deve apresentar mensagem de erro "Rua é obrigatória" |
| Número |  | Deve apresentar mensagem de erro "Número é obrigatório" |

#### Cenário 5: Salvar Alterações com Sucesso
Dado que o usuário está na tela de edição de dados pessoais
E os campos estão preenchidos corretamente
Quando clicar no botão "Salvar"
Então deve receber uma mensagem de sucesso "Seus dados foram atualizados com sucesso!"
@critico

#### Cenário 6: Salvar Alterações com Erro
Dado que o usuário está na tela de edição de dados pessoais
E os campos estão preenchidos incorretamente
Quando clicar no botão "Salvar"
Então deve receber uma mensagem de erro "Não foi possível atualizar seus dados. Por favor, verifique as informações e tente novamente."
@regressivo

#### Cenário 7: Salvar Alterações com Campos Obrigatórios Vazios ou Inválidos
Dado que o usuário está na tela de edição de dados pessoais
E os campos obrigatórios estão vazios ou inválidos
Quando clicar no botão "Salvar"
Então deve receber mensagens de erro específicas para cada campo
E a atualização deve ser impedida
@regressivo

Exemplos de validação:
| Campo | Valor | Resultado |
| --- | --- | --- |
| Nome Completo |  | Deve apresentar mensagem de erro "Nome Completo é obrigatório" |
| E-mail |  | Deve apresentar mensagem de erro "E-mail é obrigatório" |
| E-mail | exemplo | Deve apresentar mensagem de erro "E-mail inválido" |
| CEP |  | Deve apresentar mensagem de erro "CEP é obrigatório" |
| Cidade |  | Deve apresentar mensagem de erro "Cidade é obrigatória" |
| Estado |  | Deve apresentar mensagem de erro "Estado é obrigatório" |
| Rua |  | Deve apresentar mensagem de erro "Rua é obrigatória" |
| Número |  | Deve apresentar mensagem de erro "Número é obrigatório" |

#### Cenário 8: Edição de Dados com Caracteres Especiais
Dado que o usuário está na tela de edição de dados pessoais
Quando editar os campos com caracteres especiais (ex: @, #, $, etc.)
Então os campos devem ser editáveis
E devem manter as validações de formato e obrigatoriedade
@fumaca

Exemplos de validação:
| Campo | Valor | Resultado |
| --- | --- | --- |
| Nome Completo | João@ | Deve apresentar mensagem de erro "Nome Completo inválido" |
| E-mail | joao# | Deve apresentar mensagem de erro "E-mail inválido" |

#### Cenário 9: Edição de Dados com Números Excessivos
Dado que o usuário está na tela de edição de dados pessoais
Quando editar os campos com números excessivos (ex: mais de 100 caracteres)
Então os campos devem ser editáveis
E devem manter as validações de formato e obrigatoriedade
@fumaca

Exemplos de validação:
| Campo | Valor | Resultado |
| --- | --- | --- |
| Nome Completo | João123456789012345678901234567890 | Deve apresentar mensagem de erro "Nome Completo inválido" |
| E-mail | joao123456789012345678901234567890 | Deve apresentar mensagem de erro "E-mail inválido" |

#### Cenário 10: Erro de API ao Salvar Alterações
Dado que o usuário está na tela de edição de dados pessoais
E os campos estão preenchidos corretamente
Quando clicar no botão "Salvar"
E ocorrer um erro de API (ex: 500, 404, etc.)
Então deve receber uma mensagem de erro "Erro ao salvar alterações. Por favor, tente novamente mais tarde."
@regressivo

#### Cenário 11: Tempo de Resposta do Servidor
Dado que o usuário está na tela de edição de dados pessoais
E os campos estão preenchidos corretamente
Quando clicar no botão "Salvar"
E o servidor demorar mais de 10 segundos para responder
Então deve receber uma mensagem de erro "Tempo de resposta do servidor excedido. Por favor, tente novamente mais tarde."
@fumaca

#### Cenário 12: Campo CPF com Formato Inválido
Dado que o usuário está na tela de edição de dados pessoais
Quando visualizar o campo CPF
E o campo CPF estiver com formato inválido (ex: 1234567890)
Então deve apresentar uma mensagem de erro "CPF inválido"
@critico

Exemplos de validação:
| Campo | Valor | Resultado |
| --- | --- | --- |
| CPF | 1234567890 | Deve apresentar mensagem de erro "CPF inválido" |
| CPF | 123.456.789-09 | Deve apresentar mensagem de erro "CPF inválido" |

Esses cenários adicionais abordam casos de erro, como caracteres especiais, números excessivos, erros de API, tempo de resposta do servidor e formato inválido do campo CPF, garantindo que o sistema seja testado de forma mais abrangente e robusta. Além disso, as tags @regressivo, @critico e @fumaca ajudam a identificar os cenários mais importantes e críticos para o sistema.

# Relatório de Validação

### Relatório de Análise de Cenários BDD

#### Cobertura
Os cenários apresentados cobrem uma ampla gama de funcionalidades e casos de erro, incluindo:
- Acesso e edição de dados pessoais
- Validação de campos obrigatórios e formato
- Edição de campos específicos como CPF, endereço e e-mail
- Casos de erro como caracteres especiais, números excessivos, erros de API e tempo de resposta do servidor
- Formato inválido do campo CPF

As tags @regressivo, @critico e @fumaca ajudam a priorizar os cenários com base na criticidade e no impacto no sistema.

#### Gaps
Alguns gaps identificados nos cenários incluem:
- **Falta de testes de segurança**: Não há cenários que abordem testes de segurança, como injeção de SQL, cross-site scripting (XSS) ou ataques de força bruta.
- **Testes de performance**: Embora haja um cenário que aborda o tempo de resposta do servidor, não há testes mais abrangentes de performance, como testes de carga ou estresse.
- **Testes de compatibilidade**: Não há cenários que abordem a compatibilidade do sistema com diferentes navegadores, dispositivos ou sistemas operacionais.
- **Testes de recuperação**: Não há cenários que abordem a recuperação do sistema em caso de falhas ou erros, como a perda de dados ou a falha de um componente.
- **Testes de usabilidade**: Embora os cenários abordem a funcionalidade do sistema, não há testes específicos de usabilidade, como a facilidade de uso ou a acessibilidade.

#### Recomendações
Para melhorar a cobertura e a robustez dos testes, recomenda-se:
- **Incluir testes de segurança**: Desenvolver cenários que abordem testes de segurança, como injeção de SQL, cross-site scripting (XSS) ou ataques de força bruta.
- **Ampliar testes de performance**: Incluir testes mais abrangentes de performance, como testes de carga ou estresse, para garantir que o sistema possa lidar com um grande volume de usuários ou dados.
- **Incluir testes de compatibilidade**: Desenvolver cenários que abordem a compatibilidade do sistema com diferentes navegadores, dispositivos ou sistemas operacionais.
- **Incluir testes de recuperação**: Desenvolver cenários que abordem a recuperação do sistema em caso de falhas ou erros, como a perda de dados ou a falha de um componente.
- **Incluir testes de usabilidade**: Desenvolver cenários que abordem a usabilidade do sistema, como a facilidade de uso ou a acessibilidade, para garantir que o sistema seja fácil de usar e acessível para todos os usuários.

Além disso, é recomendável revisar e refinar os cenários existentes para garantir que eles sejam claros, concisos e fáceis de entender, e que cubram todos os requisitos e funcionalidades do sistema.