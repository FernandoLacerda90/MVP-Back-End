# Minha API

Está API fornece os métodos para a criação, busca e remoção de produtos em geral.

---

## Como executar

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.



```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ uvicorn app:app --reload 
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte.

```
(env)$ uvicorn app:app --reload 
```

Abra o [http://localhost:8000/docs](http://localhost:8000/docs) no navegador para verificar o status da API em execução.