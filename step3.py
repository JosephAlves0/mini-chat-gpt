import torch
import torch.nn as nn

texto = "abacate"

chars = sorted(list(set(texto)))
print("Vocabulario ", chars)

stoi = {ch:i for i,ch in enumerate(chars)}
itos = {i:ch for i,ch in enumerate(chars)}

print("Mapa char->int:", stoi)

encoded = [stoi[c] for c in texto]
print("Texto codificado:", encoded)

x = encoded[:-1]
y = encoded[1:]

print("Entrada:", x)
print("Saida:", y)

#x = torch.tensor(x)
#y = torch.tensor(y)

print("Tensor x:", x)
print("Tensor y:", y)

vocab_size = len(chars)
embedding_dim = 4

embedding = nn.Embedding(vocab_size, embedding_dim)

x_tensor = torch.tensor(x)
y_tensor = torch.tensor(y)

embedded = embedding(x_tensor)

print("Shape: ", embedded.shape)
print(embedded)

linear = nn.Linear(embedding_dim, vocab_size)

logits = linear(embedded)

print("Shape logits: ", logits.shape)
print(logits)

loss_fn = nn.CrossEntropyLoss()

loss = loss_fn(logits, y_tensor)

print("Loss: ", loss.item())

optimizer = torch.optim.Adam(
    list(embedding.parameters()) + list(linear.parameters()),
    lr=0.01
)

for epoch in range(1000):

    embedded = embedding(x_tensor)
    logits = linear(embedded)

    loss = loss_fn(logits, y_tensor)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 100 == 0:
        print(epoch, loss.item())


with torch.no_grad():
    
    input_token = torch.tensor([stoi["a"]])

    embedded = embedding(input_token)

    logits = linear(embedded)

    probs = torch.softmax(logits, dim=-1)

    print("Probabilidades: ", probs)

    next_token = torch.argmax(probs)

    print("Proximo caractere: ", itos[next_token.item()])