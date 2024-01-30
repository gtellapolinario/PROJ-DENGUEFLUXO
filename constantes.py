"""
This module provides constants and paths for the application.
"""

import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

DENG_PATH = os.path.join(ROOT_PATH, 'dng.png')
LOGO_PATH = os.path.join(ROOT_PATH, 'logo.png')

BOTAO_PATHS = [os.path.join(ROOT_PATH, f'{i}.png') for i in range(1, 10)]


MENS_GRP_D = """Paciente Grupo D

- 💡 Iniciar hidratação venosa imediata (EXPANSÃO - ATÉ 3X).

- 🔬 Solicitar Exames laboratoriais (Se disponíveis).

- 🏥 SOLICITAR INTERNAÇÃO EM CTI (PACIENTE DEVE SER ACOMPANHADO EM CTI POR NO MÍNIMO 48 HORAS).

- 👁️🩺 Reavaliação clínica a cada 15-30min ATÉ CHEGADA DO SAMU.

- 🩸 Hematócrito após 2h (PREFERENCIALMENTE APÓS CADA EXPANSÃO).


• 💉 Hidratação IV imediata:

    - 10ml/kg/h com SF 0,9% nas 2 primeiras horas em qualquer ponto da rede de atenção, mesmo
na ausência de exames complementares.

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
MENS_GRP_R = """REGRA DE HOLLIDAY-SEGAR

- Até 10kg: 100ml/kg/dia;

- De 10 a 20kg: 1.000ml + 50ml/kg/dia para cada kg acima de 10Kg

- De 20 a 30kg: 1.500ml + 20ml/kg/dia para cada kg acima de 20kg. 1/3 de solução de reidratação oral e 2/3 de outros líquidos.
"""

MENS_GRP_G = """SINAIS DE GRAVIDADE

- Sangramento Grave

- Comprometimento grave de órgãos

- Choque
"""
MENS_GRP_L = """SINAIS DE ALARME

- Dor abdominal intensa e contínua

- Vômitos persistentes

- Hipotensão postural/ LP_BOXia

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

    Lipotímia refere-se a uma sensação de desmaio ou perda iminente de consciência, porém, sem a perda
de consciência propriamente dita. É frequentemente causada por uma redução temporária do fluxo sanguíneo
para o cérebro, e pode estar associada a hipotensão postural.

No contexto da dengue entra também como um forte indicativo de hipovolemia."
"""
HPT_BOX= """

Informações sobre Hepatomegalia

Hepatomegalia é o aumento anormal do tamanho do fígado. Na dengue, pode ser um sinal de envolvimento
hepático devido à infecção. Os pacientes podem apresentar dor na região do fígado, e a hepatomegalia
pode ser detectada através do exame físico ou de imagem.
"""
ASCITE= """

Informações sobre Ascite

    Ascite é o acúmulo de líquido no espaço peritoneal, a cavidade abdominal. Na dengue, pode ocorrer
devido a hipoproteinemia (baixos níveis de proteína) ou lesão hepática, levando a um desequilíbrio na
produção e reabsorção de fluidos.
"""
LETARGIA= """

Informações sobre Letargia

    Letargia refere-se a um estado de sonolência, fadiga ou falta de energia. Em pacientes com dengue,
pode ser um sinal de comprometimento sistêmico, incluindo desidratação severa ou efeitos do vírus no
sistema nervoso central.
"""

CS_DNG= """👉SOMADO A DOIS OU MAIS SINTOMAS DESCRITOS ABAIXO.
"MARQUE OS SINTOMAS DESCRITOS E PROSSIGA."
"""

NOT_MSG= 'EM BREVE'


MENS_GRP_AB = '''- 🩺 Prova do laço positiva?

- 🩸 Sangramento de pele espontâneo?

- 👴 Condição clínica especial, risco social ou comorbidades?
'''
