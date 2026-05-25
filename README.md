# 📋 Ficha de Acompanhamento e Diagnóstico do Projeto

> **Orientações para a Equipe:** Este documento deve ser preenchido pela equipe para alinhar as expectativas do projeto com os mentores e organizadores. Sejam diretos, honestos e realistas nas respostas.

---

## 🏛️ 1. Identificação da Equipe

- **Nome da Equipe:** ForAll
- **Nome dos Integrantes e Períodos:** Alexandre, Alysson, Arthur, Misael
- **Link do Repositório (GitHub/GitLab):** https://github.com/alexandresilvaaraujo11-web
- **Link do Rascunho/Design (Figma/Lovable/Excalidraw):** https://www.figma.com/make/V8iVghBGqcRkv4VJaGM02v/Home-page-for-ForAll-forum?t=8JS0KjV9HiYhsPwE-1

---

## 💡 2. O Problema e a Proposta de Valor (O Coração da Ideia)

### 2.1. Qual problema real e específico vocês estão resolvendo?

: A dificuldade de comunicação e colaboração entre estudantes de diferentes cursos em projetos acadêmicos e técnicos, resultando em isolamento e desperdício de talentos complementares.

### 2.2. O diferencial da solução está claro? O que torna a ideia de vocês única?

> **Descrição:** (Por que o usuário usaria o sistema de vocês e não as alternativas que já existem no mercado?)
Diferente de fóruns genéricos, o ForAll é um ecossistema de colaboração acadêmica focado em projetos práticos. Nosso diferencial é a vinculação direta de estudantes por interesse técnico e curso, facilitando a formação de equipes multidisciplinares dentro do ambiente universitário.
---

## ⚙️ 3. A Solução na Prática (Como Funciona)

### 3.1. Como a solução funciona para o usuário final?

3.1. Fluxo do Usuário: O usuário realiza login, navega pela lista de projetos abertos (filtrando por área de interesse/curso), visualiza o detalhe do projeto de seu interesse e entra no chat em tempo real para conversar com os criadores e propor colaboração.
### 3.2. Quais são as principais tecnologias, linguagens ou ferramentas que decidiram usar?

3.2. Tecnologias: Django (Python), SQLite (Banco de Dados), HTML5/CSS3 (Interface responsiva), JavaScript (Fetch API para atualização em tempo real do chat).
---

## 👥 4. Gestão e Divisão de Trabalho

### 4.1. Quem está fazendo o quê na equipe?

Alexandre: Front-end, design das interfaces e integração dos templates.

Alysson: Modelagem de dados, lógica do banco e fluxo do fórum.

Arthur: Validação de regras de negócio, testes de integração e documentação.

Misael: Backend (Views/Urls), implementação do chat em tempo real e resolução de conflitos de versionamento.

---

## 🛠️ 5. Status Atual do Desenvolvimento (O MVP)

### 5.1. Vocês já começaram o protótipo visual ou o código do MVP? Qual o percentual de conclusão estimado?

- **Status:** ( ) Não começamos | ( ) Apenas rascunho visual | ( ) Código inicial iniciado | ( ) Mais da metade pronto | (X) Finalizado 

### 5.2. O projeto já funciona em alguma parte? O que já está codificado e operacional?

5.2. O que funciona: Sistema de autenticação (login/logout), listagem e busca de projetos com filtros, criação e edição de projetos, além do chat em tempo real para cada sala de projeto.
### 5.3. O que foi ou será "Mockado" (dados fictícios/estáticos)?

> **Descrição:** (Identifiquem quais partes serão apenas simulação visual para a apresentação não quebrar, ex: o gráfico na tela é apenas uma imagem fixada).
Não se aplica.

### 5.4. O que ainda falta finalizar obrigatoriamente para a entrega?

5.4. Pendências: Finalização do merge entre branches, revisão final dos estilos CSS no mobile e testes de carga (verificação de estabilidade das requisições do chat).
---

## 🚧 6. Obstáculos e Pedidos de Ajuda

### 6.1. Qual maior dificuldade da equipe?

6.1. Dificuldades: A maior dificuldade tem sido o gerenciamento de conflitos no versionamento (Git/GitHub) decorrente da implementação paralela de novas funcionalidades (chat e filtros) e a estabilização do polling de mensagens para não sobrecarregar o servidor.
---

## 🎤 7. Preparação para o Show (O Pitch)

### 7.1. Como será a estratégia de apresentação de vocês na segunda-feira?

7.1. Estratégia: A apresentação será realizada de forma híbrida:

  Fala: Misael e Alexandre apresentam a dor e a solução; Arthur e Alysson focam nos diferenciais técnicos.

  Demonstração: Utilizaremos um vídeo curto (gravado) como "seguro" da funcionalidade principal do chat e, ao final, faremos uma demonstração ao vivo (live demo) navegando pelos projetos, para provar que o código está operacional e funcional.

Dica para vocês: Como a entrega está próxima, usem a Opção 3 (híbrida) que descrevi anteriormente. É a que mais impressiona os jurados, pois o vídeo transmite segurança e a demonstração ao vivo transmite autoridade sobre o que vocês construíram. Boa sorte!
