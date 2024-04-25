class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

class TelaVeiculo:
    def cadastra_veiculo_dados(self):
        print("------CADASTRO DE VEÍCULO------")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        ano = input("Ano: ")
        return Veiculo(marca, modelo, ano)

    def descreve_sintomas(self, veiculo):
        sintomas = input("Descreva os sintomas do veículo separados por vírgula:\n (aquecimento, pane elétrica, problemas no câmbio, pneus furados, bateria descarregada, problemas nos freios, luz de verificação do motor ligada,\n motor superaquecido, vazamentos de óleo, problemas na transmissão, falha no sistema de arrefecimento, falha na ignição, ruídos no motor, suspensão irregular): ")


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



        for sintoma in sintomas.split(","):
            sintoma = sintoma.strip().lower()
            if sintoma in problemas:
                print(f"Problema possível para '{sintoma}':{problemas[sintoma]}")

            else:
                print(f"Sintoma não reconhecido: {sintoma}.")
                guincho = input("Deseja chamar um guincho? (S/N): ")
                if guincho.lower() == "s":
                    localizacao = input("Insira sua localização: ")
                    chamar_guincho(localizacao)
                else:
                    print("Continuando com outras opções.")

def chamar_guincho(localizacao):
    # Lógica para chamar um guincho
    # Recebe a localização e inicia o processo de solicitação
    print(f"Guincho a caminho! Sua localização: {localizacao}")

def menu_principal():
    print("\nMenu Principal:")
    print("1. Cadastrar Veículo")
    print("2. Diagnóstico Detalhado")
    print("3. Chamar Guincho")

# Fluxo principal do programa
while True:
    menu_principal()
    opcao = input("Escolha uma opção (1/2/3): ")

    if opcao == "1":
        tela_veiculo = TelaVeiculo()
        veiculo = tela_veiculo.cadastra_veiculo_dados()
        print(f"Veículo {veiculo.marca} {veiculo.modelo} ({veiculo.ano}) cadastrado com sucesso!")
    elif opcao == "2":
        tela_veiculo = TelaVeiculo()
        tela_veiculo.descreve_sintomas(Veiculo)
    elif opcao == "3":
        localizacao = input("Insira sua localização: ")
        chamar_guincho(localizacao)
