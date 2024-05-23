# Cadastro do veículo
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

# Menu para cadastrar veículo
class TelaVeiculo:
    def cadastra_veiculo_dados(self):
        print("------CADASTRO DE VEÍCULO------")
        marca = self.validar_marca("Marca: ")
        modelo = self.validar_modelo("Modelo: ")
        ano = self.validar_ano("Ano: ")
        return Veiculo(marca, modelo, ano)
    
# Validar marca
    def validar_marca(self, prompt):
         while True:
            marca = input(prompt)
            if marca.isalpha() and 3 <= len(marca) <= 20:
                return (marca)
            else:
                print("Marca inválida. A marca deve conter apenas letras e ter entre 3 e 20 caracteres.")
                
# Validar modelo
    def validar_modelo(self, prompt):
         while True:
            modelo = input(prompt)
            if len(modelo) <= 30:
                return (modelo)
            else:
                print("Modelo inválido. Digite um nome até 30 caracteres.")

# Validar ano
    def validar_ano(self, prompt):
        while True:
            ano = input(prompt)
            if ano.isdigit() and len(ano) == 4 and 1980 <= int(ano) <= 2024:
                return int(ano)
            else:
                print("Por favor, digite um ano válido com exatamente 4 dígitos, entre 1980 e 2024.")

# Validação guincho/endereço
def chamar_guincho():

    nome = input("Digite o nome da rua/avenida (de 4 até 40 caracteres): ")
    # Validar nome
    while not (4 <= len(nome) <= 40 and nome.replace(" ", "").isalpha()):
        print("Nome inválido. O nome não pode conter números nem pontuação e deve ter entre 4 e 40 caracteres.")
        nome = input("Digite o nome da rua/avenida (de 4 até 30 caracteres): ")
    
    numero_endereco = input("Digite o número do endereço (entre 1 e 9999): ")
    # Validar número
    while not (numero_endereco.isdigit() and 1 <= int(numero_endereco) <= 9999):
        print("Número de endereço inválido. Digite apenas números de 1 até 9999.")
        numero_endereco = input("Digite o número do endereço: ")

    localizacao = f"{nome}, {numero_endereco}"
    print(f"Guincho a caminho! Sua localização: {localizacao}")

# Problemas e sugestões
def diagnosticar_problemas():
    problemas = {
            "aquecimento": "Superaquecimento do motor. Verifique o nível de água e as mangueiras internas.",
            "pane elétrica": "Verifique sinais de dificuldade para ligar o carro e possíveis vazamentos de ácido.",
            "problemas no câmbio": "Defeitos no câmbio. Consulte um profissional para avaliação e reparo.",
            "pneus furados": "Pneus furados podem ocorrer devido a perfurações causadas por detritos na estrada ou pneus subinflados.",
            "bateria descarregada": "Baterias naturalmente perdem carga ao longo do tempo. Deixar as luzes acesas ou dirigir pouco contribui para o esgotamento.",
            "problemas nos freios": "Pastilhas desgastadas, pinças com mau funcionamento e vazamentos de fluido de freio são causas comuns de problemas nos freios.",
            "luz de verificação do motor ligada": "A luz de verificação do motor pode indicar desde problemas simples, como uma tampa de combustível solta, até questões complexas no motor ou sensores.",
            "motor superaquecido": "O superaquecimento pode ocorrer devido a um sistema de resfriamento com defeito, baixo nível de líquido de arrefecimento ou termostato com falha.",
            "vazamentos de óleo": "Vazamentos de óleo podem surgir de juntas deterioradas, selos ou do cárter de óleo danificado.",
            "problemas na transmissão": "Trocas de marcha atrasadas, mudanças bruscas de marcha ou vazamentos de fluido são problemas comuns na transmissão.",
            "falha no sistema de arrefecimento": "Uma falha no sistema de arrefecimento pode resultar em superaquecimento do motor. Verifique o radiador, a bomba d'água e o termostato.",
            "falha na ignição": "A falha na ignição pode ser causada por velas de ignição desgastadas, bobina de ignição defeituosa ou problemas no sistema de injeção de combustível.",
            "ruídos no motor": "Ruídos no motor podem indicar problemas como correias desgastadas, rolamentos defeituosos ou válvulas com folga.",
            "suspensão irregular": "Suspensão irregular pode ser causada por amortecedores desgastados, molas quebradas ou componentes soltos."
        }

# Perguntar os problemas
    sintomas = input("Descreva os sintomas do veículo separados por vírgula: ")
    sintomas = [s.strip().lower() for s in sintomas.split(",")]

    for sintoma in sintomas:
        if sintoma in problemas:
            print(f"Problema possível para '{sintoma}': {problemas[sintoma]}")
        else:
            print(f"Sintoma não reconhecido: {sintoma}.")
            guincho = input("Deseja chamar um guincho? (S/N): ")
            if guincho.lower() == "s":
                chamar_guincho()
            else:
                print("Continuando com outras opções.")

# Menu principal do programa
def menu_principal():
    print("\nMenu Principal:")
    print("1. Cadastrar Veículo")
    print("2. Diagnóstico Detalhado")
    print("3. Chamar Guincho")

# Fluxo principal do programa
def main():
    while True:
        menu_principal()
        opcao = input("Digite a opção desejada (1, 2 ou 3): ")
        if opcao == "1":
            tela_veiculo = TelaVeiculo()
            veiculo = tela_veiculo.cadastra_veiculo_dados()
            print(f"Veículo {veiculo.marca} {veiculo.modelo} ({veiculo.ano}) cadastrado com sucesso!")
        elif opcao == "2":
            diagnosticar_problemas()
        elif opcao == "3":
            chamar_guincho()
        else:
            print("Por favor, digite um número entre 1 e 3.")

if __name__ == "__main__":
    main()