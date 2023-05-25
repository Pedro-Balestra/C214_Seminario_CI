from CarrinhoCompras import CarrinhoCompras
from Cliente import Cliente
from Produto import Produto

if __name__ == '__main__':
    cliente = Cliente(1, "João da Silva", "123.456.789-00", "(99) 99999-9999", "joao@example.com")

    # Criando os produtos
    produto1 = Produto(1, "Camiseta", "Gucci", 1229.99, 32)
    produto2 = Produto(2, "Calça", "LV", 2359.99, 20)
    produto3 = Produto(3, "Tênis", "Nike", 1899.99, 18)

    # Criando o carrinho de compras
    carrinho = CarrinhoCompras(cliente)

    # Adicionando produtos ao carrinho
    carrinho.adicionar_produto(produto1)
    carrinho.adicionar_produto(produto2)
    carrinho.adicionar_produto(produto3)

    # Exibindo os detalhes do carrinho
    carrinho.exibir_detalhes()