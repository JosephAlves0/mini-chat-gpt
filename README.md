# 🧠 Mini GPT — Estudo de Redes Neurais do Zero

Este repositório é um estudo prático para entender **como modelos de linguagem funcionam internamente**, começando do nível mais básico possível.

A ideia é construir passo a passo os conceitos fundamentais que aparecem em modelos modernos como GPT, mas em versões extremamente simples para fins didáticos.

---

# 📚 Estrutura do Projeto

```
mini-chat-gpt/
│
├── step1.py
├── step2.py
└── step3.py
```

Cada arquivo representa uma evolução no entendimento de redes neurais.

---

# 1️⃣ step1.py — Primeira Rede Neural

Neste passo criamos **a rede neural mais simples possível**.

Modelo matemático:

```
y = w * x + b
```

Onde:

* `x` → entrada
* `w` → peso (weight)
* `b` → bias
* `y` → saída

## Objetivo

Ensinar a rede a aprender a função:

```
y = 2x
```

## Conceitos aprendidos

* Tensor
* Gradiente
* Backpropagation
* Ajuste de pesos

## Resultado esperado

Após o treinamento, o modelo aprende algo próximo de:

```
w ≈ 2
b ≈ 0
```

Isso significa que a rede **aprendeu a relação matemática** entre `x` e `y`.

---

# 2️⃣ step2.py — Treinamento Real

Aqui evoluímos o exemplo anterior para um **treinamento mais estruturado**.

## O que foi adicionado

* Loop de treinamento
* Função de perda (loss)
* Otimizador

Arquitetura:

```
input → linear model → prediction
```

## Componentes principais

### Loss Function

Mede o erro entre:

```
previsão do modelo
vs
valor real
```

### Optimizer

Responsável por ajustar os pesos da rede para minimizar o erro.

## Fluxo de treinamento

```
Forward pass
↓
Calcular erro
↓
Backpropagation
↓
Atualizar pesos
```

Esse ciclo acontece centenas ou milhares de vezes.

---

# 3️⃣ step3.py — Primeiro Modelo de Linguagem

Aqui começamos a trabalhar com **texto**.

Objetivo: ensinar o modelo a **prever o próximo caractere**.

Exemplo:

```
abacate
```

Dataset gerado:

```
a → b
b → a
a → c
c → a
a → t
t → e
```

## Pipeline completo

```
texto
↓
criar vocabulário
↓
converter caracteres em números
↓
criar dataset (entrada/saída)
↓
embeddings
↓
camada linear
↓
probabilidade do próximo token
```

---

# 🔤 Vocabulário

O modelo primeiro descobre todos os caracteres possíveis:

```
['a', 'b', 'c', 'e', 't']
```

Depois cria dois mapas:

```
stoi = string → integer
itos = integer → string
```

Exemplo:

```
a → 0
b → 1
c → 2
e → 3
t → 4
```

---

# 🧩 Embeddings

Redes neurais não entendem texto, apenas números.

Por isso cada token é convertido em um vetor numérico.

Exemplo:

```
a → [0.12, -0.45, 0.77, 0.02]
```

Isso cria uma matriz chamada **embedding matrix**.

```
(vocab_size, embedding_dim)
```

Exemplo:

```
(5, 4)
```

---

# 🧮 Arquitetura do Modelo

```
token
 ↓
embedding
 ↓
linear layer
 ↓
softmax
 ↓
probabilidade do próximo caractere
```

Esse tipo de modelo é chamado de:

**Character Language Model**.

---

# 📉 Função de Loss

Utilizamos:

```
CrossEntropyLoss
```

Ela mede o quão próxima a previsão do modelo está da resposta correta.

Quanto menor a loss, melhor o modelo está aprendendo.

---

# 🚀 O que já foi construído

Mesmo sendo extremamente simples, esse projeto já implementa os mesmos blocos fundamentais usados em modelos modernos:

* embeddings
* rede neural
* treinamento com gradiente
* previsão probabilística de tokens

---

# 🔮 Próximos Passos do Estudo

Evoluções possíveis:

1. Aumentar o contexto (usar vários caracteres anteriores)
2. Criar n‑grams neurais
3. Implementar Self‑Attention
4. Construir um Transformer simples

Esses são os mesmos princípios usados em modelos de linguagem modernos.

---

# 🎯 Objetivo do Projeto

O objetivo não é criar um modelo poderoso, mas **entender profundamente como LLMs funcionam por dentro**.

Aprendendo passo a passo:

```
matemática → rede neural → linguagem → transformers
```
