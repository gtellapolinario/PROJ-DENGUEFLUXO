# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
"""  importações requiments """
from datetime import datetime
import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme(
    "dark-blue"
)  # Themes: "blue" (standard), "green", "dark-blue"

def centralizar_janela(janela, largura, altura):
    ''' #Calcula posição x e y para centralizar a janela '''
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()
    center_x = (screen_width // 2) - (largura // 2)
    center_y = (screen_height // 2) - (altura // 2)
    janela.geometry(f'{largura}x{altura}+{center_x}+{center_y}')

def notificar():
    """
    Revisa e exibe informações sobre os sinais de alarme no contexto de uma avaliação médica.
    """
    mostrar_mensagem_grupo("Notificação", NOT_MSG)

def revisar_sinais_alarme():
    """Revisa e exibe os sinais de alarme."""
    mostrar_mensagem_grupo("SINAIS DE ALARME", MENS_GRP_L)

def revisar_sinais_gravidade():
    """Revisa e exibe os sinais de gravidade."""
    mostrar_mensagem_grupo("SINAIS DE GRAVIDADE", MENS_GRP_G)

def realizar_prova_laco():
    """Realiza e exibe os resultados da prova do laço."""
    mostrar_mensagem_grupo("PROVA DO LAÇO", MENS_GRP_PL)

def verificar_hematocrito():
    """Verifica e exibe o valor de referência do hematocrito."""
    mostrar_mensagem_grupo("VALOR DE REFERÊNCIA DO HEMATÓCRITO", MENS_GRP_H)

def condicoes_especiais():
    """Revisa e exibe informações sobre condições especiais."""
    mostrar_mensagem_grupo("CONDIÇÕES ESPECIAIS", MENS_GRP_E)

def regra_holliday_seggar():
    """Aplica e exibe a regra de Holliday-Seggar para hidratação."""
    mostrar_mensagem_grupo("REGRA DE HOLLIDAY", MENS_GRP_R)

def abrir_janela_grupo():
    """Abre uma janela para exibir informações sobre o grupo de sintomas selecionado."""
    # [Resto do código permanece inalterado]# grupo_selecionado = ''
    text_txt = ''
    if varA.get():
        text_txt = MENS_GRP_A
    elif varB.get():
        text_txt = MENS_GRP_B
    elif varC.get():
        text_txt = MENS_GRP_C
    elif varD.get():
        text_txt = MENS_GRP_D

    if text_txt:
        janela_grupo = ctk.CTkToplevel()
        centralizar_janela(janela_grupo, 700, 820)
        janela_grupo.attributes("-topmost", True)
        janela_grupo.title("Informações sobre o Grupo")
        ctk.CTkLabel(janela_grupo, text="Informações Grupo", font=("Helvetica", 18)).pack(pady=10)
        texto = ctk.CTkTextbox(janela_grupo, wrap='word', font=("Helvetica", 18))
        texto.pack(padx=10, pady=10, fill='both', expand=True)
        texto.insert('end', text_txt)
        texto.configure(state='disabled')
        ctk.CTkButton(janela_grupo, text="Fechar", command=janela_grupo.destroy).pack(pady=10)

# Criação da janela principal
root = ctk.CTk()
root.title("Fluxograma no atendimento à suspeita de Dengue versão 1.0")
centralizar_janela(root, 800, 750)
FONTE=ctk.CTkLabel(
    root,
    text="FONTE: Guia de Manejo de Dengue, Chikungunya e Zika - SMS de Belo Horizonte.",
    font=("Helvetica", 10),
).place(x=40, y=610)
REFR_RFF=ctk.CTkLabel(root,
    text="REFERÊNCIAS: Ministério da Saúde e Secretaria de Estado de Saúde de Minas Gerais.",
    font=("Helvetica", 10),
).place(x=40, y=630)
AUROTIA_GT=ctk.CTkLabel(root, text="- Guilherme Apolinário", font=("Helvetica", 10)).place(x=40, y=650)
vars1 = tk.BooleanVar()
radio_var = tk.IntVar(value=0)

def toggle_theme():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("Light")
    else:
        ctk.set_appearance_mode("Dark")
# Botão para alternar entre os temas
theme_button = ctk.CTkSwitch(root, text="Alternar Tema", command=toggle_theme, state="normal")
theme_button.place(x=100, y=680)

def mostrar_dialogo_personalizado(titulo, mensagem, janela_anterior=None):
    """Exibe um diálogo personalizado e procede para a próxima etapa após o fechamento."""
    if janela_anterior:
        janela_anterior.destroy()

    dialogo = ctk.CTkToplevel()
    dialogo.title(titulo)
    centralizar_janela(dialogo, 900, 220)
    dialogo.attributes("-topmost", True)

    ctk.CTkLabel(dialogo, text=mensagem, font=("Helvetica", 20), text_color="red").pack(
        padx=10, pady=10
    )

    def fechar_dialogo():
        """fecha o diálogo e chama a próxima etapa."""
        dialogo.destroy()
        funcao_para_proxima_etapa()  # Chamando a próxima etapa após fechar o diálogo
    ctk.CTkButton(dialogo, text="OK", command=fechar_dialogo).pack(pady=10)

def pergunta_adicional():
    """se a ou b for marcado, exibe uma pergunta adicional."""
    janela_pergunta = ctk.CTkToplevel()
    janela_pergunta.title("Grupo A ou B?")
    centralizar_janela(janela_pergunta, 600, 320)
    janela_pergunta.attributes("-topmost", True)

    var_resposta = tk.BooleanVar()

    ctk.CTkLabel(janela_pergunta, text=MENS_GRP_AB, font=("Helvetica", 20)).place(
        x=20, y=20
    )
    ctk.CTkCheckBox(janela_pergunta, text="Sim", variable=var_resposta).place(
        x=220, y=220
    )

    def avaliar_resposta():
        """avalia a resposta e exibe a mensagem do grupo correspondente."""
        if var_resposta.get():
            mostrar_mensagem_grupo("Grupo B", MENS_GRP_B)
        else:
            mostrar_mensagem_grupo("Grupo A", MENS_GRP_A)
        janela_pergunta.destroy()
    ctk.CTkButton(janela_pergunta, text="Confirmar", command=avaliar_resposta).place(
        x=280, y=220
    )

def verificar_suspeita(sintomas_vars, janela_anterior):
    """Verifica se o caso é suspeito e exibe uma mensagem personalizada."""
    contagem_marcados = sum(var.get() for var in sintomas_vars.values())
    if contagem_marcados >= 2:
        mostrar_dialogo_personalizado(
            "Aviso Importante",
            "Caso suspeito para Dengue, avalie sinais de gravidade e alarme na próxima etapa",
            janela_anterior,
        )
    else:
        janela_anterior.destroy()
        pergunta_adicional()

# Função para abrir a nova janela com o formulário de caso suspeito
def abrir_formulario_suspeito():
    """abre uma nova janela com o formulário de caso suspeito."""
    janela_suspeito = ctk.CTkToplevel()
    janela_suspeito.title("Caso suspeito?")
    centralizar_janela(janela_suspeito, 700, 820)
    janela_suspeito.attributes("-topmost", True)

    ctk.CTkLabel(
        janela_suspeito, text="⚠️CASO SUSPEITO DE DENGUE.", font=("Helvetica", 22)
    ).place(x=40, y=20)
    ctk.CTkLabel(janela_suspeito, text=CS_DNG, font=("Helvetica", 16)).place(
        x=140, y=140
    )
    ctk.CTkLabel(
        janela_suspeito,
        text="👉 QUADRO DE FEBRE ENTRE 2 E 7 DIAS.",
        font=("Helvetica", 18),
        text_color="orange",
    ).place(x=160, y=100)

    # Sintomas
    sintomas = [
        "Cefaleia",
        "Leucopenia",
        "Mialgia/Artralgia",
        "Exantema",
        "Náuseas/vômitos",
        "Prova do laço positiva",
        "Dor retro-orbitária",
    ]

    sintomas_var1s = {sintoma: tk.BooleanVar() for sintoma in sintomas}
    for sintoma, var1s in sintomas_var1s.items():
        ctk.CTkCheckBox(janela_suspeito, text=sintoma, variable=var1s).place(
            x=70, y=200 + 40 * sintomas.index(sintoma)
        )

    # Botão Cancelar
    btn_cancelar = ctk.CTkButton(
        janela_suspeito, text="Cancelar", command=janela_suspeito.destroy
    )
    btn_cancelar.place(x=500, y=400)

    btn_proximo = ctk.CTkButton(
        janela_suspeito,
        text="Próximo",
        command=lambda: verificar_suspeita(sintomas_var1s, janela_suspeito),
    )
    btn_proximo.place(x=500, y=350)

def mostrar_mensagem_grupo(grupo, mensagem, janela_antes=None):
    """info sobre os grupos de sintomas."""
    if janela_antes:
        janela_antes.destroy()

    janela_mensagem = ctk.CTkToplevel()
    centralizar_janela(janela_mensagem, 700, 820)
    janela_mensagem.attributes("-topmost", True)
    janela_mensagem.title(f"Grupo {grupo}")
    ctk.CTkLabel(
        janela_mensagem,
        text=f"Informações sobre o Grupo {grupo}",
        font=("Helvetica", 18),
    ).pack(pady=10)
    text_area = ctk.CTkTextbox(janela_mensagem, wrap="word", font=("Helvetica", 18))
    text_area.pack(
        padx=10, pady=10, fill="both", expand=True
    )  # Ajuste conforme a necessidade (fill, expand,
    text_area.insert("end", mensagem)
    text_area.configure(state="disabled")  # Impede a edição do texto
    ctk.CTkButton(janela_mensagem, text="Fechar", command=janela_mensagem.destroy).pack(
        pady=10
    )

# CONTANTES

def verificar_sinais_e_exibir_mensagem(salar_vars, sgrave_vars, janela_antes):
    """verifica se os sinais exibe a mensagem correspondente."""
    sg_marcados = any(var.get() for var in sgrave_vars)
    sa_marcados = any(var.get() for var in salar_vars)
    if sg_marcados:
        mostrar_mensagem_grupo("Grupo D", MENS_GRP_D, janela_antes)
    elif sa_marcados:
        mostrar_mensagem_grupo("Grupo C", MENS_GRP_C, janela_antes)
    elif not sg_marcados and not sa_marcados:
        pergunta_adicional()
        janela_antes.destroy()

        
def atualizar_textbox(text1):
    """atualiza o texto da caixa de texto."""
    escolha = radio_var.get()
    textos = ""
    if escolha == 1:
        textos = CHQ_BOX
    elif escolha == 2:
        textos = HP_BOX
    elif escolha == 3:
        textos = LP_BOX
    elif escolha == 4:
        textos = HPT_BOX
    elif escolha == 5:
        textos = ASCITE
    elif escolha == 6:
        textos = LETARGIA

    text1.configure(state="normal")
    text1.delete("1.0", "end")
    text1.insert("end", textos)
    text1.configure(state="disabled")


# Janela sinais de alarme e de gravidade
def funcao_para_proxima_etapa():
    """vai para a próxima etapa."""
    janela_sinais = ctk.CTkToplevel()
    janela_sinais.title("Sinais de Gravidade e Alarme")
    centralizar_janela(janela_sinais, 1200, 800)
    janela_sinais.attributes("-topmost", True)
    ctk.CTkLabel(
        janela_sinais,
        text="Sinais de Gravidade?",
        font=("Helvetica", 20),
        text_color="red",
    ).place(x=70, y=100)
    ctk.CTkLabel(
        janela_sinais,
        text="Sinais de Alerta?",
        font=("Helvetica", 20),
        text_color="red",
    ).place(x=70, y=350)

    # Criação da caixa de texto
    text1 = ctk.CTkTextbox(
        janela_sinais, wrap="word", font=("Helvetica", 16), width=500, height=600
    )
    text1.place(x=650, y=100)
    glossario = [
        "Choque",
        "Hipotensão Postural",
        "Lipotímia",
        "Hepatomegalia",
        "Ascite",
        "Letargia",
    ]
    for j, gloss in enumerate(glossario, start=1):
        ctk.CTkRadioButton(
            janela_sinais,
            text=gloss,
            variable=radio_var,
            value=j,
            command=lambda text1=text1: atualizar_textbox(text1),
        ).place(x=500, y=200 + 40 * j)

    # Sinais de gravidade
    sgravidade = ["Sangramento Grave.", "Comprometimento grave de órgãos.", "Choque"]
    sgrave_vrs = {sinalg: tk.BooleanVar() for sinalg in sgravidade}
    for sinalg, vrs in sgrave_vrs.items():
        ctk.CTkCheckBox(janela_sinais, text=sinalg, variable=vrs).place(
            x=70, y=150 + 50 * sgravidade.index(sinalg)
        )

    salarme = [
        "Dor abdominal intensa e contínua.",
        "Vômitos persistentes",
        "Hipotensão/Lipotímia.",
        "Hepatomegalia > que 2cm do rebordo costal.",
        "Sangramento de mucosas.",
        "Acúmulo de líquidos (ASCITE, derrame pleural, derrame pericárdico.",
        "Letargia e/ou irritabilidade.",
        "Aumento progressivo de hematócrito.",
    ]
    salar_var = {sinala: tk.BooleanVar() for sinala in salarme}
    for sinala, var in salar_var.items():
        ctk.CTkCheckBox(janela_sinais, text=sinala, variable=var).place(
            x=70, y=400 + 40 * salarme.index(sinala)
        )
    # Botão Cancelar
    btn_cancelar = ctk.CTkButton(
        janela_sinais, text="Cancelar", command=janela_sinais.destroy
    )
    btn_cancelar.place(x=100, y=750)
    # Botão Próximo
    btn_proximo = ctk.CTkButton(
        janela_sinais,
        text="Próximo",
        command=lambda: verificar_sinais_e_exibir_mensagem(
            list(salar_var.values()), list(sgrave_vrs.values()), janela_sinais
        ),
    )
    btn_proximo.place(x=300, y=750)

# Definindo as funções dos botões
comandos = [
    abrir_formulario_suspeito,
    notificar,
    revisar_sinais_alarme,
    revisar_sinais_gravidade,
    realizar_prova_laco,
    abrir_janela_grupo,
    verificar_hematocrito,
    condicoes_especiais,
    regra_holliday_seggar,
]

# Nomes dos botões
nomes_botoes = [
    "Iniciar",
    "Notificar",
    "Sinais de Alarme",
    "Sinais de Gravidade",
    "Prova do Laço",
    "Grupos",
    "Hematócrito",
    "Condições Especiais",
    "Regra Holliday-Seggar"
]

# Coordenadas dos botões
coordenadas_botoes = [
    (70, 120),
    (250, 120),
    (40, 450),
    (220, 450),
    (400, 450),
    (580, 450),
    (40, 530),
    (220, 530),
    (400, 530)
]

# Criando os botões com customtkinter
for i, (x, y) in enumerate(coordenadas_botoes, start=1):
    botao = ctk.CTkButton(
        root,
        text=nomes_botoes[i - 1],
        command=comandos[i - 1],
        font=("Helvetica", 16),
        width=150,
        height=60
    )
    botao.place(x=x, y=y)

# Criação dos Checkbuttons
varA = tk.BooleanVar()
varB = tk.BooleanVar()
varC = tk.BooleanVar()
varD = tk.BooleanVar()
checkA = ctk.CTkCheckBox(root, text="Tipo A", variable=varA)
checkB = ctk.CTkCheckBox(root, text="Tipo B", variable=varB)
checkC = ctk.CTkCheckBox(root, text="Tipo C", variable=varC)
checkD = ctk.CTkCheckBox(root, text="Tipo D", variable=varD)
checkA.place(x=590, y=530)
checkB.place(x=670, y=530)
checkC.place(x=590, y=570)
checkD.place(x=670, y=570)
label_in= ctk.CTkLabel(root, text="Caso suspeito de dengue? Clique em iniciar:", font=("Helvetica", 20, "bold")).place(x=40, y=50)
labl_revis= ctk.CTkLabel(root, text="Revisão:", font=("Helvetica", 24, "bold")).place(x=40, y=380)

def atualizar_hora():
    """ATUALIZA AS HORAS E DATA"""
    agora = datetime.now()
    data_atual = agora.strftime("%d/%m/%Y")
    hora_atual = agora.strftime("%H:%M:%S")
    label_data.configure(text=data_atual)
    label_hora.configure(text=hora_atual)
    root.after(1000, atualizar_hora)

# Label para mostrar a data
label_data = ctk.CTkLabel(root, text="", font=("Helvetica", 16))
label_data.place(x=70, y=250)  # Ajuste as coordenadas conforme necessário
# Label para mostrar a hora
label_hora = ctk.CTkLabel(root, text="", font=("Helvetica", 16))
label_hora.place(x=70, y=280)  # Posiciona abaixo do label da data
atualizar_hora()

MENS_GRP_D = """Paciente Grupo D

- 💡 Iniciar hidratação venosa imediata (EXPANSÃO - ATÉ 3X).

- 🔬 Solicitar Exames laboratoriais (Se disponíveis).

- 🏥 SOLICITAR INTERNAÇÃO EM CTI (PACIENTE DEVE SER ACOMPANHADO EM CTI POR NO MÍNIMO 48 HORAS).

- 👁️🩺 Reavaliação clínica a cada 15-30min ATÉ CHEGADA DO SAMU.

- 🩸 Hematócrito após 2h (PREFERENCIALMENTE APÓS CADA EXPANSÃO).


• 💉 Hidratação IV imediata:

    - 10ml/kg/h com SF 0,9% nas 2 primeiras horas em qualquer ponto da rede de atenção

    - Mesmo na ausência de exames complementares.


• 👴👶 Monitorar atentamente idosos, cardiopatas e renais.
"""  # Substitua por toda a mensagem completa

MENS_GRP_C = """PACIENTE GRUPO C

- 💡 Iniciar hidratação venosa imediata

- 🔬 Solicitar Exames laboratoriais (Se disponíveis)

- 🏥 SOLICITAR INTERNAÇÃO (PACIENTE DEVE SER ACOMPANHADO EM LEITO DE INTERNAÇÃO POR NO MÍNIMO 48 HORAS)

- 👁️🩺 Reavaliação clínica a cada HORA ATÉ CHEGADA DO SAMU.

- 🩸 Hematócrito após 2h.

- 🔎 SEM MELHORA CLÍNICA E LABORATORIAL, RECLASSIFICAR COMO GRUPO D.

- 💉 Hidratação IV imediata:

    - 10ml/kg/h com SF 0,9% nas 2 primeiras horas em qualquer ponto da rede de atenção, mesmo na ausência
de exames complementares.

- 👴👶 Monitorar atentamente idosos, cardiopatas e renais.
"""

MENS_GRP_A = """GRUPO A

- 🩺🩸 SE PROVA DO LAÇO POSITIVA, CLASSIFICAR COMO GRUPO B.

- Sem sangramento espontâneo ou induzido (prova do laço negativa)

- Sem condição especial.

- Sem risco social.

- Sem comorbidades.

- Iniciar hidratação oral.

- Acompanhamento ambulatorial.


1. Hidratação oral

• Adultos: 60 ml/kg/dia, 1/3 de soro oral e 2/3 de outros líquidos.

• Crianças: iniciar de forma precoce e abundante, com soro de reidratação oral oferecido com frequência
sistemática e complementar com líquidos caseiros. Aplicar regra de Holliday-Segar.


2. Sintomático:

• Antitérmicos e analgésicos (dipirona ou paracetamol).

• Não utilizar salicilatos ou anti-inflamatórios não esteroides.

• Antieméticos, se necessário.


- IMPORTANTE

- Sinais de alarme e agravamento do quadro costumam ocorrer na fase de remissão da febre.

- RETORNO

- Retorno imediato na presença de sinais de alarme ou a critério médico.

- Entregar cartão de acompanhamento da dengue.
- Reavaliar o paciente  no 5° dia de doença ou na defervescência da febre, O que vier primeiro.

- Alta 48h após a defervescência, se ausência de sinais de alarme.
"""

MENS_GRP_B = """GRUPO B

• Com sangramento de pele espontâneo ou induzido (prova do laço positiva) ou condição clínica especial ou comorbidades ou risco social.

• PROVA DO LAÇO, COMO ESTRATIFICAÇÃO DE RISCO, SOMENTE NO GRUPO A.

- Iniciar hidratação oral.

Acompanhamento ambulatorial.


1. Hidratação oral

• Adultos: 60 ml/kg/dia, 1/3 de soro oral e 2/3 de outros líquidos.

• Crianças: iniciar de forma precoce e abundante, com soro de reidratação oral oferecido com frequência sistemática e complementar com líquidos caseiros. Aplicar regra de Holliday-Segar.


2. Sintomático:

• Antitérmicos e analgésicos (dipirona ou paracetamol).

• Não utilizar salicilatos ou anti-inflamatórios não esteroides.

• Antieméticos, se necessário.


- EXAMES

• Exames específicos CASO orientação da epidemiologia.
• Exames complementares:
    - HEMOGRAMA Completo (OBRIGATÓRIO).

- HEMATÓCRITO →
    - Normal ou  MENOR que 10% do valor de referência.
    - MAIOR que 10% do  valor de referência, ou sinais de alarme. → CLASSIFICAR COMO GRUPO C.

- IMPORTANTE

    - SINAIS DE ALARME E AGRAVAMENTO DO QUADRO, COSTUMAM SURGIR NA REMISSÃO DA FEBRE.
    - ACOMPANHAR EM OBSERVAÇÃO ATÉ RESULTADO DE EXAMES.

- RETORNO

IMEDIATO SE SINAIS DE ALARME OU A CRITÉRIO CLÍNICO.

• Entregar cartão de acompanhamento da dengue.
• Reavaliações diárias (clínica e laboratorial) até 48h após a defervecência da febre e ausência de sinais de alarme.
"""

MENS_GRP_H = """VALOR DE REFERÊNCIA DO HEMATÓCRITO:

NO ADULTO:

    - Mulher : 40%

    -  Homem 45%.

NA CRIANÇA:
    -  Menores de  1 mês:  51%
    
    - 1 mês: Maior que 43%;
    
    - 2 a 6 meses: Maior que 35%;
    
    - 6 meses a 2 anos incompletos: Maior que 36%;
    
    - 2 a 6 anos incompletos: Maior que 37%;
    
    - 6 a 12 anos: Maior que 38%
"""
MENS_GRP_E = """CONDIÇÕES ESPECIAIS

- Lactentes (menores de 2 anos)

- Gestantes

- Adultos com idade acima de 65 anos com comorbidades.

COMORBIDADES:

- HAS ou outras doenças cardiovasculares graves,

- DM

- DPOC

- Doenças hematológicas crônicas (principalmente anemia falciforme)

- Doença renal crônica

- Doença  ácido péptica

- Doenças autoimunes

- Asma

- Hepatopatias

- Obesidade.

RISCO SOCIAL

Estes pacientes podem apresentar evolução desfavorável e devem ter acompanhamento diferenciado.
"""
MENS_GRP_R = """
REGRA DE HOLLIDAY-SEGAR


- Até 10kg: 100ml/kg/dia;

- De 10 a 20kg: 1.000ml + 50ml/kg/dia para cada kg acima de 10Kg

- De 20 a 30kg: 1.500ml + 20ml/kg/dia para cada kg acima de 20kg. 1/3 de solução de reidratação oral e 2/3 de outros líquidos.
"""

MENS_GRP_G = """
SINAIS DE GRAVIDADE


- Sangramento Grave

- Comprometimento grave de órgãos

- Choque
"""
MENS_GRP_L = """
SINAIS DE ALARME


- Dor abdominal intensa e contínua

- Vômitos persistentes

- Hipotensão postural/ Lipotímia

- Hepatomegalia > que 2cm do rebordo costal

- Sangramento de mucosas

- Acúmulo de líquidos (ASCITE, derrame pleural, derrame pericárdico)

- Letargia e/ou irritabilidade

- Aumento progressivo de hematocrito
"""
MENS_GRP_PL = """PROVA DO LAÇO

A prova do laço é um exame rápido que identifica o risco de sangramento, NÃO  precisa ser feita se já existem sinais de
hemorragia, como sangramento nas gengivas e nariz ou presença de sangue urina. Além disso, a prova do laço pode apresentar
falsos resultados em situações como uso de aspirina, corticoides, fase de pré ou pós-menopausa, ou quando existe queimadura
solar.

- Como é feita a prova?

    - Desenhar, no antebraço, um quadrado com uma área de 2,5 x 2,5 cm e depois seguir estes passos:
    
    - Avaliar a pressão arterial da pessoa com o esfigmomanômetro;
    
    - Insuflar novamente o manguito do esfigmomanômetro até ao valor médio entre a pressão máxima e a mínima. Para saber o
valor médio deve-se -somar o valor de pressão arterial máxima com a o valor de pressão arterial mínima e depois dividir por 2.

    - Esperar 5 minutos com o manguito insuflado na mesma pressão;
    
    - Desinsuflar e retirar o manguito, depois dos 5 minutos;
    
    - Deixar o sangue circular por pelo menos 2 minutos.
    
    - Por fim, deve-se avaliar a quantidade de pontos avermelhados, chamados de petéquias, dentro do quadrado marcado na pele,
    para saber qual o resultado do teste.


- RESULTADO

    - Positiva quando surgem mais de 20 pontinhos vermelhos dentro do quadrado marcado na pele.
    - Com 5 a 19 pontinhos já pode indicar suspeita de dengue.
"""


CHQ_BOX= """
Explicação sobre Choque no contexto da dengue.

	Choque no contexto da dengue refere-se ao choque hipovolêmico, complicação grave onde ocorre uma
súbita perda de volume circulante, geralmente devido a hemorragia ou sequestro de plasma para o espaço
extravascular.

Os sinais incluem:

    - Taquicardia
    - Extremidades distais frias
    - PA convergente (< 20 mm Hg)
    - Pulso fraco e filiforme
    - Enchimento capilar lento ( > 2 seg.)
    - Taquipneia
    - Oligúria (<1,5 ml/kg/h)
    - Hipotensão arterial (fase tardia)
    - Cianose (fase tardia choque)
    - Acúmulo de líquidos com insuficiência respiratória.
"""
HP_BOX= """
Explicação sobre Hipotensão Postural

    Hipotensão postural, também conhecida como hipotensão ortostática, é uma queda abrupta da pressão
arterial ao se levantar ou mudar de posição. Por definição é a queda de pelo menos 20 mmHg na pressão
arterial sistólica ou 10 mmHg na diastólica dentro de três minutos após se levantar.

Como avaliar?

    - Com o paciente em decúbito, aferir a PA.
    
    - Solicitar que fique em posição ortostática, e readerir a PA após 3 minutos.

    - Se o paciente sentir tontura já no primeiro minuto é um ponto a favor da Hipotensão ortostática.

    - Pode causar tontura ou desmaio, em pacientes com dengue.

    - Pode ser um sinal de hipovolemia neste quadro."
"""
LP_BOX= """

Explicações sobre Lipotímia

→ Lipotímia
    - Refere-se a uma sensação de desmaio ou perda iminente de consciência

    - Porém, sem a perda de consciência propriamente dita.

    - É frequentemente causada por uma redução temporária do fluxo sanguíneo para o cérebro.

    - Pode estar associada a hipotensão postural.


No contexto da dengue entra também como um forte indicativo de hipovolemia."
"""
HPT_BOX= """

Informações sobre Hepatomegalia

→ Hepatomegalia
    - Aumento anormal do tamanho do fígado.

    - Na dengue, pode ser um sinal de envolvimento hepático devido à infecção.

    - Os pacientes podem apresentar dor na região do fígado, e a hepatomegalia.

    - Pode ser detectada através do exame físico ou de imagem.
"""
ASCITE= """

Informações sobre Ascite

→Ascite
    - Acúmulo de líquido no espaço peritoneal, a cavidade abdominal.

    - Na dengue, pode ocorrer devido a baixos níveis de proteína ou lesão hepática.

    - A baixa de proteínas leva a um desequilíbrio na produção e reabsorção de fluidos.
"""
LETARGIA= """

Informações sobre Letargia

→ Letargia
    - Refere-se a um estado de sonolência, fadiga ou falta de energia.

    - Em pacientes com dengue, pode ser um sinal de comprometimento sistêmico.

    - Isso inclui desidratação severa ou efeitos do vírus no sistema nervoso central.
"""

CS_DNG= """👉SOMADO A DOIS OU MAIS SINTOMAS DESCRITOS ABAIXO.
"MARQUE OS SINTOMAS DESCRITOS E PROSSIGA."
"""

NOT_MSG= 'EM BREVE'


MENS_GRP_AB = '''- 🩺 Prova do laço positiva?

- 🩸 Sangramento de pele espontâneo?

- 👴 Condição clínica especial, risco social ou comorbidades?
'''

root.mainloop()
