# LOGICADEPROG

Repositório pessoal para treinar e organizar exercícios de lógica de programação em várias linguagens (JavaScript, Python, PHP, etc.). O objetivo é agrupar pequenos scripts e exemplos que eu crio enquanto estudo algoritmos, estruturas de controle, manipulação de dados e prática de resolução de problemas.

## Estrutura do repositório

- `JS/` — Exercícios e exemplos em JavaScript.
  - `cedulas.js` — Exemplo: calcula quantidade de notas (R$ 100, 50, 20, 10, 5, 2, 1) para um valor fixo.
  - `maior.js` — Exemplo: encontra o maior entre três números.

(Adicione outras pastas como `PY/`, `PHP/`, `C/` quando incluir exercícios em outras linguagens.)

## Como usar / executar (exemplos em Windows PowerShell)

Pré-requisito: ter o Node.js instalado (para executar os exemplos em `JS/`).

Executar um arquivo JS:

```powershell
# executar cedulas.js
node .\JS\cedulas.js

# executar maior.js
node .\JS\maior.js
```

Exemplo de saída esperada para `cedulas.js` (para o valor atual dentro do arquivo):

```
            5 nota(s) de R$ 100,00 

            1 nota(s) de R$ 50,00 

            1 nota(s) de R$ 20,00 

            0 nota(s) de R$ 10,00 

            1 nota(s) de R$ 5,00 

            0 nota(s) de R$ 2,00 

            1 nota(s) de R$ 1,00 

```

Exemplo de saída esperada para `maior.js` (executando com os valores hard-coded no arquivo):

```
106 eh o maior
```

## Como organizar novos exercícios

- Crie uma pasta para a linguagem, por exemplo `PY/` para Python, `PHP/` para PHP.
- Nomeie arquivos de forma descritiva: `fibonacciserie.js`, `ordenaLista.py`, `validaCpf.php`.
- Se for um exercício que precisa de entrada do usuário, prefira deixar um valor padrão no arquivo e comentar como passar parâmetros ou usar stdin.

## Contribuições

Se quiser contribuir (mesmo que seja você mesmo no futuro):

- Faça um fork e crie uma branch com o nome do exercício, por exemplo `feat/ordenacao-bubble`.
- Abra um Pull Request com uma descrição do exercício, entradas esperadas, saídas e complexidade (quando aplicável).
- Inclua comentários no código explicando trechos importantes.

## Licença

Sinta-se à vontade para usar e adaptar o conteúdo. Recomendo adicionar uma licença — por exemplo, MIT.

Para adicionar licença MIT, crie um arquivo `LICENSE` com o texto padrão da MIT License e atualize este README com o ano e o autor.

## Dicas / boas práticas

- Mantenha cada exercício pequeno e com uma responsabilidade clara.
- Adicione testes pequenos quando possível (por exemplo, scripts que verificam saída esperada).
- Documente entradas/saídas no topo de cada arquivo.

---

Se quiser, eu posso:

- adicionar um `LICENSE` (MIT) automaticamente;
- criar um `CONTRIBUTING.md` com modelo de PRs;
- adicionar scripts de execução no `package.json` (se quiser transformar a pasta JS em um pequeno projeto npm).

Diga qual dessas opções prefere que eu faça em seguida e eu faço agora mesmo.