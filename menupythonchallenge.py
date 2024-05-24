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
            if marca.replace(" ", "").isalpha and 3 <= len(marca) <= 20:
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
    # Validar nome endereço
    while not (4 <= len(nome) <= 40 and nome.replace(" ", "").isalpha()):
        print("Nome inválido. O nome não pode conter números nem pontuação e deve ter entre 4 e 40 caracteres.")
        nome = input("Digite o nome da rua/avenida (de 4 até 30 caracteres): ")
    
    numero_endereco = input("Digite o número do endereço (entre 1 e 9999): ")
    # Validar número endereço
    while not (numero_endereco.isdigit() and 1 <= int(numero_endereco) <= 9999):
        print("Número de endereço inválido. Digite apenas números de 1 até 9999.")
        numero_endereco = input("Digite o número do endereço: ")

    localizacao = f"{nome}, {numero_endereco}"
    print(f"Guincho a caminho! Sua localização: {localizacao} (Previsão: -- minutos!)")

# Problemas e soluções
problemas = {
    1: "Superaquecimento do motor",
    2: "Pane elétrica",
    3: "Problemas no câmbio",
    4: "Pneus furados",
    5: "Bateria descarregada",
    6: "Problemas nos freios",
    7: "Luz de verificação do motor ligada",
    8: "Motor superaquecido",
    9: "Vazamentos de óleo",
    10: "Problemas na transmissão",
    11: "Falha no sistema de arrefecimento",
    12: "Falha na ignição",
    13: "Ruídos no motor",
    14: "Suspensão irregular",
    15: "Outro problema"
}

solucoes = {
    1: "Verifique o nível de água e as mangueiras internas.",
    2: "Verifique sinais de dificuldade para ligar o carro e possíveis vazamentos de ácido.",
    3: "Consulte um profissional para avaliação e reparo.",
    4: "Pode ocorrer devido a perfurações causadas por detritos na estrada ou pneus subinflados.",
    5: "Baterias naturalmente perdem carga ao longo do tempo. Deixar as luzes acesas ou dirigir pouco contribui para o esgotamento.",
    6: "Pastilhas desgastadas, pinças com mau funcionamento e vazamentos de fluido de freio são causas comuns de problemas nos freios.",
    7: "Pode indicar desde problemas simples, como uma tampa de combustível solta, até questões complexas no motor ou sensores.",
    8: "Pode ocorrer devido a um sistema de resfriamento com defeito, baixo nível de líquido de arrefecimento ou termostato com falha.",
    9: "Podem surgir de juntas deterioradas, selos ou do cárter de óleo danificado.",
    10: "Trocas de marcha atrasadas, mudanças bruscas de marcha ou vazamentos de fluido são problemas comuns na transmissão.",
    11: "Uma falha no sistema de arrefecimento pode resultar em superaquecimento do motor. Verifique o radiador, a bomba d'água e o termostato.",
    12: "Pode ser causada por velas de ignição desgastadas, bobina de ignição defeituosa ou problemas no sistema de injeção de combustível.",
    13: "Pode indicar problemas como correias desgastadas, rolamentos defeituosos ou válvulas com folga.",
    14: "Pode ser causada por amortecedores desgastados, molas quebradas ou componentes soltos.",
    15: "Por enquanto ainda não temos suporte para outros problemas."
}

# Menu principal do programa
def menu_principal():
    print("\nMenu Principal:")
    print("1. Cadastrar Veículo")
    print("2. Diagnóstico Detalhado")
    print("3. Chamar Guincho")

# Função para diagnosticar problemas
def diagnosticar_problemas():
    print("Problemas possíveis:")
    for numero, opcao in problemas.items():
        print(f"{numero}: {opcao}")

    selecionado = int(input("Selecione o número do problema para ver a solução: "))
# Reconhecer problema escolhido
    if selecionado in solucoes:
        print(f"Solução para '{problemas[selecionado]}': {solucoes[selecionado]}")
# Chamar guincho
        while True:
            guincho = input("Deseja chamar o guincho? (s/n): ")
            if guincho.lower() == "s":
                chamar_guincho()
                break
            elif guincho.lower() == "n":
                print("Guincho não chamado.")
                break
            else:
                print("Opção inválida.")
            
    else:
        print("Número de problema inválido.")

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