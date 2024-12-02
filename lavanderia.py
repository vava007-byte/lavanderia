class Lavanderia:
    def __init__(self):
        self.roupas = {
            "camisas": 0,
            "calcas": 0,
            "meias": 0,
            "toalhas": 0
        }

    def adicionar_roupa(self, tipo, quantidade):
        if tipo in self.roupas:
            if quantidade > 0:
                self.roupas[tipo] += quantidade
                print(f"{quantidade} {tipo} adicionadas com sucesso.")
            else:
                print("Quantidade inválida. Insira um valor positivo.")
        else:
            print(f"Tipo de roupa '{tipo}' não reconhecido. Tipos válidos: {', '.join(self.roupas.keys())}.")

    def contar_roupas(self):
        for tipo, quantidade in self.roupas.items():
            print(f"{tipo.capitalize()}: {quantidade}")

# Exemplo de uso
lavanderia = Lavanderia()
lavanderia.adicionar_roupa("camisas", 5)
lavanderia.adicionar_roupa("calcas", 3)
lavanderia.adicionar_roupa("meias", 10)
lavanderia.adicionar_roupa("toalhas", 2)
lavanderia.adicionar_roupa("saias", 4)  # Teste de tipo não reconhecido
lavanderia.adicionar_roupa("camisas", -3)  # Teste de quantidade negativa

print("\nContagem de roupas na lavanderia:")
lavanderia.contar_roupas()
