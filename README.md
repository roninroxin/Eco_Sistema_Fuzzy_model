
# Sistema de Controle Fuzzy para Eficiência do Adubo Organomineral

Este projeto implementa um sistema de controle fuzzy para modelar a eficiência do adubo organomineral, analisando as quantidades de Nitrogênio (N), Fósforo (P), Potássio (K) e Umidade do Solo (Hu).

## Introdução

**Lógica Fuzzy (Difusa ou Nebulosa)**:
- A lógica tradicional booleana trabalha com predicados true e false.
- A lógica fuzzy adapta a lógica tradicional para lidar com mais de dois valores, aproximando-se da linguagem humana.
- O grau de pertinência representa o quanto um valor pertence a um conjunto ou intervalo de valores.

### Três Etapas do Raciocínio Fuzzy:
1. **Fuzzificação**
2. **Inferência Fuzzy**
3. **Defuzzificação**

## Instalação

Para instalar os pacotes necessários, execute:

```bash
pip install scikit-fuzzy
```

## Implementação

### Fuzzificação

Nesta etapa, definimos:

1. **Análise do Problema**: Modelar a eficiência do adubo organomineral.
2. **Definição das Variáveis**:
    - **Nitrogênio** (Entrada):
      - Universo: [0, 20]
      - Funções de Pertinência: Insuficiente, Flores e Frutos, Plantas Grandes
    - **Fósforo** (Entrada):
      - Universo: [0, 30]
      - Funções de Pertinência: Insuficiente, Flores e Frutos, Plantas Grandes
    - **Potássio** (Entrada):
      - Universo: [0, 20]
      - Funções de Pertinência: Insuficiente, Flores e Frutos, Plantas Grandes
    - **Umidade do Solo** (Entrada):
      - Universo: [0, 50]%
      - Funções de Pertinência: Insuficiente, Flores e Frutos, Plantas Grandes
    - **Proporção NPK** (Saída):
      - Universo: [1, 1.5, 2]
      - Funções de Pertinência: Insuficiente, Flores e Frutos, Plantas Grandes

### Inferência Fuzzy

Definimos as regras que o sistema seguirá:

- **Regra Genérica**: Nitrogênio médio e Fósforo médio produzem uma proporção NPK Genérica.
- **Regra para Frutas**: Fósforo elevado e Potássio elevado resultam em uma proporção para Flores e Frutas.
- **Regra para Árvores Grandes**: Nitrogênio elevado, Umidade elevada e Fósforo ou Potássio médio produzem uma proporção para Plantas Grandes.

### Defuzzificação

As regiões resultantes das regras são convertidas em valores para a variável de saída.

## Execução

Para executar a simulação, siga as seguintes etapas:

1. Defina os valores de entrada no vetor `mock`.
2. Preencha os valores no simulador.
3. Execute a simulação para calcular a proporção NPK e visualizar as variáveis fuzzy.

```python
# Base de Conhecimento/Regras
regra1 = ctrl.Rule(nitrogenio['médio'] & fosforo['médio'], prop_npk['Genérico'])
regra2 = ctrl.Rule(fosforo['elevado'] & potassio['elevado'], prop_npk['Flores e Frutas'])
regra3 = ctrl.Rule(nitrogenio['elevado'] & umidade['elevado'] & (fosforo['médio'] | potassio['médio']), prop_npk['Plantas Grandes'])

# Sistema Fuzzy e Simulação
validade_ctrl = ctrl.ControlSystem([regra1, regra2, regra3])
validade_simulador = ctrl.ControlSystemSimulation(validade_ctrl)

# Mock de valores de entrada
mock = [10, 20, 20, 12]

# Preenchendo os valores no simulador
validade_simulador.input["Nitrogênio"] = mock[0]
validade_simulador.input["Fósforo"] = mock[1]
validade_simulador.input["Potássio"] = mock[2]
validade_simulador.input["Umidade do Solo"] = mock[3]

# Computando o resultado (Inferência Fuzzy + Defuzzificação)
validade_simulador.compute()

# Visualizando as variáveis fuzzy
nitrogenio.view(sim=validade_simulador)
fosforo.view(sim=validade_simulador)
potassio.view(sim=validade_simulador)
umidade.view(sim=validade_simulador)
```

## Referências

- [Vídeo Explicativo sobre Lógica Fuzzy](https://youtu.be/EnfSJZU4MCU?si=KsZkzOCF2SuwMcXs)
