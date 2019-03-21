# codeSample
Using CODE

# Desafio DBA
## Desafio Celero - Python para DB
    - O desafio deve ser escrito em Python 3.0+;
    - Você deve utilizar o framework Django 2.0;
    - Você deve utilizar o framework DjangoRESTFramework;
    - A base de dados deve ser PostgreSQL;

## Manifesto
    A finalidade deste desafio é testar as suas habilidades e conhecimento de construção de bases de dados
    usando Django, assim como a otimização de queries utilizando a linguagem de programação Python.
## Objetivo
    O seu objetivo será criar um projeto Django de administração de álbuns de música e otimizar uma de suas
    queries.
    - Dentro do projeto existirá 3 modelos:
        ○ Artista: Neste modelo deve haver apenas o campo nome.
        ○ Álbum: Neste modelo deve haver os campos nome e ano, além disso, sempre um álbum
          pertence a um artista e um artista pode possuir vários álbuns.
        ○ Faixa: Neste modelo deve haver os campos nome, número e duração (em segundos),
          sempre uma faixa pertence a um álbum e um álbum pode possuir várias faixas.
    - Uma função para popular a base de dados deve ser implementada (Popule a base com pelo menos
      mil artistas).
    - Crie um teste que faça uma consulta a base de dados utilizando o ORM do Django que traga     todos as faixas de um artista e também calcule o tempo da consulta.
    - Em seguida crie uma mesma consulta porém mais otimizada utilizando a biblioteca psycopg2,    este teste também deve calcular o tempo da consulta.

## PONTOS BÔNUS
    - Legibilidade e documentação do código;
    - Performance do algoritmo.
## Prazo
    Você terá 1 (uma) semana para concluir o desafio.

## Avaliação
    - A utilização das tecnologias requeridas;
    - Se o seu resultado possui um bom nível de confiabilidade;
    - A forma com a qual você escolheu escrever o desafio (a arquitetura que usou, se o está bem
      documentado, se possui uma boa legibilidade, etc);
    - Como escolheu organizar o seu fluxo de trabalho no git (como uso de branchs, separação das
      responsabilidades, etc).
    - Se o seu teste é genuíno, ou seja, se foi você quem o escreveu (evite soluções prontas, isto causará a sua imediata desclassificação).
## Entrega
    Você deve versionar o seu desafio no ​git​ desde o início. Para hospedá-lo remotamente, escolha entre Github​ e ​Bitbucket​. Depois de empurrar o seu progresso à plataforma escolhida, compartilhe conosco o link do mesmo.