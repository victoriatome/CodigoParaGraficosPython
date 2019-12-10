#10-P	CoAP - B			
#	Média de Pacotes Enviados	Inter. Conf	Média de Pacotes Recebidos	Inter. Conf
nome = '192.168.4.6'	
enviados = 288	
int_conf_env = 6.36	
recebidos = 96	
int_conf_rec = 50.29

nome = '192.168.4.9'	
enviados = 287	
int_conf_env = 4.24	
recebidos = 278	
int_conf_rec = 4.06

				
#10-10	CoAP- B			
#	Média de Pacotes Enviados		Média de Pacotes Recebidos	
nome = '192.168.4.6'	
enviados = 281	
int_conf_env = 4.06	
recebidos = 273	
int_conf_rec = 6.36

nome ='192.168.4.9'
enviados = 281	
int_conf_env = 7.24
recebidos = 281
int_conf_rec = 	7.24

# libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties



# width of the bars
barWidth = 0.3

# Choose the height of the blue bars
bars1 = [0.155, 0.131]

# Choose the height of the cyan bars
bars2 = [0.188, 0.183]

# Choose the height of the error bars (bars1)
yer1 = [0.038, 0.03]

# Choose the height of the error bars (bars2)
yer2 = [0.001, 0.003]

# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]

fig, ax = plt.subplots()

#Plot grid
ax.grid(linestyle='-', linewidth='0.3', color='k')

# Don't allow the axis to be on top of your data
ax.set_axisbelow(True)

# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = '#473C8B', edgecolor = 'black', yerr=yer1, capsize=7, label='Cenário 7')

# Create cyan bars
plt.bar(r2, bars2, width = barWidth, color = '#B0E2FF', edgecolor = 'black', yerr=yer2, capsize=7, label='Cenário 8')

for i, v in enumerate(bars1):
    plt.text(r1[i] -0.2, v + 0.001, str(v))

for i, v in enumerate(bars2):
    plt.text(r2[i] +0.1, v + 0.001, str(v))

# DUAS COLUNAS
plt.xticks([r + barWidth for r in range(len(bars1))], ['192.168.4.6', '192.168.4.9'], )
# UMA COLUNA
plt.xticks([r for r in range(len(bars1))], ['192.168.4.6', '192.168.4.9'], )

plt.ylabel('Tempo (segundos)')
# Put a legend below current axis
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),fancybox=True, shadow=True, ncol=5)

plt.title("Cenários 7 e 8 - Latência")

# Show graphic
plt.show()

plt.savefig('CoAP_B_Pacotes_Env_Rec', dpi=300, edgecolor='k')
