"""
MNIST - Chargement et visualisation du dataset

MNIST est un dataset classique de classification d'images de chiffres manuscrits (0-9).
Chaque image fait 28x28 pixels en niveaux de gris.

PyTorch fournit MNIST via torchvision.datasets avec téléchargement automatique.
TensorFlow propose aussi tf.keras.datasets.mnist, mais PyTorch est plus simple ici.
"""

import torch
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
import numpy as np


def load_mnist(batch_size=64, data_dir="./data"):
    """
    Charge le dataset MNIST

    Returns:
        train_loader, test_loader: DataLoaders PyTorch
    """
    transform = transforms.Compose(
        [
            transforms.ToTensor(),
            transforms.Normalize((0.1307,), (0.3081,)),  # Normalisation MNIST
        ]
    )

    train_dataset = datasets.MNIST(
        root=data_dir, train=True, download=True, transform=transform
    )

    test_dataset = datasets.MNIST(
        root=data_dir, train=False, download=True, transform=transform
    )

    train_loader = torch.utils.data.DataLoader(
        train_dataset, batch_size=batch_size, shuffle=True
    )

    test_loader = torch.utils.data.DataLoader(
        test_dataset, batch_size=batch_size, shuffle=False
    )

    return train_loader, test_loader


def visualize_samples(data_loader, num_samples=8):
    """Visualise quelques échantillons du dataset"""
    data_iter = iter(data_loader)
    images, labels = next(data_iter)

    fig, axes = plt.subplots(2, 4, figsize=(10, 5))
    for i in range(min(num_samples, len(images))):
        row, col = i // 4, i % 4
        img = images[i].squeeze().numpy()
        axes[row, col].imshow(img, cmap="gray")
        axes[row, col].set_title(f"Label: {labels[i].item()}")
        axes[row, col].axis("off")

    plt.tight_layout()
    plt.show()


# Exemple d'utilisation
if __name__ == "__main__":
    # Charger les données
    train_loader, test_loader = load_mnist(batch_size=64)

    # Afficher les statistiques
    print(f"Nombre d'échantillons d'entraînement: {len(train_loader.dataset)}")
    print(f"Nombre d'échantillons de test: {len(test_loader.dataset)}")

    # Visualiser quelques échantillons
    visualize_samples(train_loader)

    # Exemple: itérer sur un batch
    for images, labels in train_loader:
        print(f"Shape d'un batch: {images.shape}")  # [64, 1, 28, 28]
        print(f"Labels: {labels[:10].tolist()}")
        break
