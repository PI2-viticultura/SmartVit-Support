Feature: Captar requisicao feita no frontend e enviar ao microsservico support atraves do BFF 
  Como Sistema, quero pegar os dados informados no frontend pelo usuario,
  e registra-los no meu servico.

  Context: O usuario registra o suporte 
    Dado que os dados resgistrados utilizem o servico atraves do BFF

    Scenario: Usuario registrar suporte desejado
        Given a pagina de registro do suporte
        When ele registar os campos do suporte
        | priority | problem                        | description                               |
        | Alta     | Sistema eletronico com defeito | sistema esta aquecendo muito, o que fazer |
        Then os dados devem passar pelo servico atraves do BFF e armazenar no banco
        | priority | problem                        | description                               |
        | Alta     | Sistema eletronico com defeito | sistema esta aquecendo muito, o que fazer |