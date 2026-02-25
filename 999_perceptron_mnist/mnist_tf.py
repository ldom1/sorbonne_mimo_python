"""
MNIST avec TensorFlow/Keras

TensorFlow fournit MNIST via tf.keras.datasets.mnist.
Simple et intégré avec l'écosystème TensorFlow.
"""

import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # Désactive les warnings/info TensorFlow
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"  # Désactive oneDNN warnings

import tensorflow as tf

tf.config.set_visible_devices([], "GPU")

import numpy as np
import matplotlib.pyplot as plt


def load_mnist():
    """Charge le dataset MNIST avec TensorFlow"""
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

    # Normalisation [0, 1]
    x_train = x_train.astype("float32") / 255.0
    x_test = x_test.astype("float32") / 255.0

    return (x_train, y_train), (x_test, y_test)


def visualize_samples(x_data, y_data, num_samples=8, save_path=None):
    """Visualise quelques échantillons"""
    _, axes = plt.subplots(2, 4, figsize=(10, 5))
    for i in range(min(num_samples, len(x_data))):
        row, col = i // 4, i % 4
        axes[row, col].imshow(x_data[i], cmap="gray")
        axes[row, col].set_title(f"Label: {y_data[i]}")
        axes[row, col].axis("off")
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    else:
        plt.close()


if __name__ == "__main__":
    (x_train, y_train), (x_test, y_test) = load_mnist()

    print(f"Shape train: {x_train.shape}, Labels train: {y_train.shape}")
    print(f"Shape test: {x_test.shape}, Labels test: {y_test.shape}")
    print(f"Valeurs min/max: {x_train.min():.1f}/{x_train.max():.1f}")

    visualize_samples(
        x_train[:8], y_train[:8], save_path="999_perceptron_mnist/mnist_samples.png"
    )

    model = tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(28, 28)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dense(10, activation="softmax"),
        ]
    )

    model_path = "999_perceptron_mnist/mnist_model.h5"

    if os.path.exists(model_path):
        print("Modèle existant trouvé, chargement...")
        model = tf.keras.models.load_model(model_path)
    else:
        print("Entraînement du modèle...")
        model.compile(
            optimizer="adam",
            loss="sparse_categorical_crossentropy",
            metrics=["accuracy"],
        )
        # Entraînement du modèle
        model.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.2)
        model.save(model_path)
        print("Modèle sauvegardé.")

    # Évaluation du modèle
    loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
    print(f"Loss: {loss:.4f}, Accuracy: {accuracy:.4f}")

    # Prédiction sur quelques échantillons
    for n in np.random.randint(0, len(x_test), 10):
        sample_image = x_test[n]
        sample_label = y_test[n]
        sample_prediction = model.predict(sample_image.reshape(1, 28, 28), verbose=0)
        print(
            f"Échantillon {n}: Prédiction={sample_prediction.argmax()}, Vraie={sample_label}"
        )
