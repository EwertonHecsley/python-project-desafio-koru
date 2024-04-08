# API de Gerenciamento de Produtos

Uma API simples para gerenciar produtos em um banco de dados SQLite.

## Rotas Disponíveis

### GET /products

- **Descrição:** Retorna todos os produtos cadastrados.
- **Parâmetros da URL:** Nenhum.
- **Resposta de Sucesso:** Retorna uma lista de produtos em formato JSON.
- **Exemplo de Uso:** `GET /products`

### GET /products/{id}

- **Descrição:** Retorna um produto específico com o ID fornecido.
- **Parâmetros da URL:** 
  - `id` (int): O ID do produto desejado.
- **Resposta de Sucesso:** Retorna os detalhes do produto em formato JSON.
- **Resposta de Erro:** Retorna uma mensagem de erro se o produto não for encontrado.
- **Exemplo de Uso:** `GET /products/1`

### POST /products

- **Descrição:** Adiciona um novo produto ao banco de dados.
- **Corpo da Requisição:** Deve ser enviado um objeto JSON com os campos `name`, `description` e `price`.
- **Resposta de Sucesso:** Retorna uma mensagem confirmando que o produto foi adicionado com sucesso.
- **Exemplo de Uso:** 
  ```json
  {
    "name": "Produto 1",
    "description": "Descrição do Produto 1",
    "price": 10.99
  }


Claro! Aqui está o README em formato Markdown:

markdown
Copy code
# API de Gerenciamento de Produtos

Uma API simples para gerenciar produtos em um banco de dados SQLite.

## Rotas Disponíveis

### GET /products

- **Descrição:** Retorna todos os produtos cadastrados.
- **Parâmetros da URL:** Nenhum.
- **Resposta de Sucesso:** Retorna uma lista de produtos em formato JSON.
- **Exemplo de Uso:** `GET /products`

### GET /products/{id}

- **Descrição:** Retorna um produto específico com o ID fornecido.
- **Parâmetros da URL:** 
  - `id` (int): O ID do produto desejado.
- **Resposta de Sucesso:** Retorna os detalhes do produto em formato JSON.
- **Resposta de Erro:** Retorna uma mensagem de erro se o produto não for encontrado.
- **Exemplo de Uso:** `GET /products/1`

### POST /products

- **Descrição:** Adiciona um novo produto ao banco de dados.
- **Corpo da Requisição:** Deve ser enviado um objeto JSON com os campos `name`, `description` e `price`.
- **Resposta de Sucesso:** Retorna uma mensagem confirmando que o produto foi adicionado com sucesso.
- **Exemplo de Uso:** 
  ```json
  {
    "name": "Produto 1",
    "description": "Descrição do Produto 1",
    "price": 10.99
  }
  
### PUT /products/{id}

- **Descrição:** Atualiza as informações de um produto existente com o ID fornecido.
- **Parâmetros da URL:**
id (int): O ID do produto a ser atualizado.

- **Corpo da Requisição:** Deve ser enviado um objeto JSON com os campos name, description e price.
- **Resposta de Sucesso:** Retorna uma mensagem confirmando que o produto foi atualizado com sucesso.
- **Resposta de Erro:** Retorna uma mensagem de erro se o produto não for encontrado.
- 
- **Exemplo de Uso:**
  
```
{
  "name": "Produto Atualizado",
  "description": "Descrição atualizada do produto",
  "price": 19.99
}
```

### DELETE /products/{id}

- **Descrição:** Exclui um produto existente com o ID fornecido.
- **Parâmetros da URL:**
id (int): O ID do produto a ser excluído.

- **Resposta de Sucesso:** Retorna uma mensagem confirmando que o produto foi excluído com sucesso.
- **Resposta de Erro:** Retorna uma mensagem de erro se o produto não for encontrado.
Exemplo de Uso: DELETE /products/1
