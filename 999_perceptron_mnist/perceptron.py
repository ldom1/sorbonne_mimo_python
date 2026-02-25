"""
Perceptron - Classifieur linéaire binaire

Le perceptron est un algorithme d'apprentissage supervisé pour la classification binaire.
Il apprend une frontière de décision linéaire en ajustant les poids itérativement.

Algorithme:
1. Initialiser les poids à zéro (ou aléatoirement)
2. Pour chaque exemple d'entraînement:
   - Calculer la sortie: y_pred = signe(w · x + b)
   - Si erreur (y_pred ≠ y_true): mettre à jour w et b
3. Répéter jusqu'à convergence ou nombre max d'itérations

Alternative: utiliser sklearn.linear_model.Perceptron pour une implémentation optimisée.
"""

import numpy as np


class Perceptron:
    """Implémentation explicite du perceptron"""

    def __init__(self, learning_rate=0.01, max_iter=1000):
        self.learning_rate = learning_rate
        self.max_iter = max_iter
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        """
        Entraîne le perceptron

        Args:
            X: array (n_samples, n_features)
            y: array (n_samples,) avec valeurs {-1, 1}
        """
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0.0

        # Convertir y en {-1, 1} si nécessaire
        y = np.where(y == 0, -1, y)

        for _ in range(self.max_iter):
            errors = 0
            for i in range(n_samples):
                # Prédiction
                linear_output = np.dot(X[i], self.weights) + self.bias
                y_pred = np.sign(linear_output)

                # Mise à jour si erreur
                if y_pred != y[i]:
                    self.weights += self.learning_rate * y[i] * X[i]
                    self.bias += self.learning_rate * y[i]
                    errors += 1

            if errors == 0:
                break

    def predict(self, X):
        """Prédit les classes"""
        linear_output = np.dot(X, self.weights) + self.bias
        return np.sign(linear_output)


# Exemple d'utilisation
if __name__ == "__main__":
    # Données d'exemple (OU logique)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([-1, 1, 1, 1])

    # Entraînement
    perceptron = Perceptron(learning_rate=0.1, max_iter=100)
    perceptron.fit(X, y)

    # Prédiction
    predictions = perceptron.predict(X)
    print(f"Prédictions: {predictions}")
    print(f"Poids: {perceptron.weights}, Biais: {perceptron.bias}")
