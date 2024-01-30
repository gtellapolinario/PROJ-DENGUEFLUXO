# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
"""  importações requiments """
from datetime import datetime
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
from constantes import *

ctk.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
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
    # [Resto do código permanece inalterado]
   # grupo_selecionado = ''
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
root = tk.Tk()
root.title("Fluxograma no atendimento à suspeita de Dengue versão 1.0")
centralizar_janela(root, 1300, 820)
ctk.CTkLabel(
    root,
    text="FONTE: Guia de Manejo de Dengue, Chikungunya e Zika - SMS de Belo Horizonte.",
    font=("Helvetica", 10),
).place(x=40, y=610)
ctk.CTkLabel(root,
    text="REFERÊNCIAS: Ministério da Saúde e Secretaria de Estado de Saúde de Minas Gerais.",
    font=("Helvetica", 10),
).place(x=40, y=630)
vars1 = tk.BooleanVar()
radio_var = tk.IntVar(value=0)

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
            "Este caso é suspeito para Arbovirose. Siga para a próxima etapa",
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
        text_color="red",
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

# CONTANTES

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
        "Hipotensão/LP_BOXia.",
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

# Guarda as referências das imagens para evitar que sejam coletadas pelo garbage collector
imagens = []
imagens_globais = []
revisao = ctk.CTkLabel(root, text="Revisão:", font=("Helvetica", 26, "bold"))
revisao.place(x=150, y=530)
# Coordenadas dos botões
coordenadas_botoes = [
    (120, 300),  # iniciar
    (550, 300),  # notificar
    (40, 650),  # alarme
    (320, 650),  # gravidade
    (590, 650),  # prova
    (870, 645),  # grupos
    (40, 730),  # hemat
    (320, 730),  # especiais
    (590, 730),  # regra
]

# Lista de funções dos botões
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
for i, (x, y) in enumerate(coordenadas_botoes, start=1):
    caminho_imagem = BOTAO_PATHS[i - 1]
    imagem_original = Image.open(caminho_imagem)
    imagem_redimensionada = imagem_original.resize((230, 60), Image.Resampling.LANCZOS)
    foto = ImageTk.PhotoImage(imagem_redimensionada)
    imagens_globais.append(foto)
    botao = tk.Button(root, image=foto, command=comandos[i - 1], borderwidth=0)
    botao.image = foto
    botao.place(x=x, y=y)

# Criação dos Checkbuttons
varA = tk.BooleanVar()
varB = tk.BooleanVar()
varC = tk.BooleanVar()
varD = tk.BooleanVar()
checkA = tk.Checkbutton(root, text="Tipo A", variable=varA)
checkB = tk.Checkbutton(root, text="Tipo B", variable=varB)
checkC = tk.Checkbutton(root, text="Tipo C", variable=varC)
checkD = tk.Checkbutton(root, text="Tipo D", variable=varD)
checkA.place(x=1120, y=650)
checkB.place(x=1200, y=650)
checkC.place(x=1120, y=680)
checkD.place(x=1200, y=680)

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
label_data.place(x=1000, y=50)  # Ajuste as coordenadas conforme necessário
# Label para mostrar a hora
label_hora = ctk.CTkLabel(root, text="", font=("Helvetica", 16))
label_hora.place(x=1000, y=80)  # Posiciona abaixo do label da data
atualizar_hora()

def carregar_imagem_png(caminho_png, largura, altura):
    """CARREGA IMAGENS"""
    # Carrega a imagem PNG
    imagem_origin = Image.open(caminho_png)
    imagem_redimensiona = imagem_origin.resize(
        (largura, altura), Image.Resampling.LANCZOS
    )
    # Converte a imagem para o formato do Tkinter
    fotos = ImageTk.PhotoImage(imagem_redimensiona)
    imagens_globais.append(fotos)  # Mantém a referência
    return fotos

# Caminho da imagem PNG
imagem_png = carregar_imagem_png(
    DENG_PATH, 200, 200
)  # Ajuste a largura e altura conforme necessário
# Cria e posiciona o label da imagem
label_imagem = ctk.CTkLabel(root, text="", image=imagem_png)
label_imagem.image = imagem_png  # Mantém a referência
label_imagem.place(x=300, y=70)  # Ajuste as coordenadas conforme necessário

# Caminho da imagem PNG
logoim_png = carregar_imagem_png(
    LOGO_PATH, 128, 128
)  # Ajuste a largura e altura conforme necessário
# Cria e posiciona o label da imagem
label_logo = ctk.CTkLabel(root, text="", image=logoim_png)
label_logo.image = logoim_png  # Mantém a referência
label_logo.place(x=1180, y=1)  # Ajuste as coordenadas conforme necessário

root.mainloop()
