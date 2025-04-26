import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="MIMO - Chapitre 4 - Les fonctions",
    page_icon=":python:",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("MIMO - Chapitre 4 - Les fonctions")

st.write("## La suite de Fibonacci")
st.write(
    "La suite de Fibonacci est une suite de nombres dans laquelle chaque nombre est la somme des deux précédents. "
    "Elle commence généralement par 0 et 1. Par exemple, les premiers termes de la suite sont : 0, 1, 1, 2, 3, 5, 8, 13, ..."
)


## Ecrire la fonction qui calcule la suite de Fibonacci et
# qui affiche le résultat de chaque itération
# avec f"Le terme {i} de la suite de Fibonacci est : "
def fibonacci(n: int) -> list:
    """Calculer la suite de Fibonacci jusqu'à n termes et affiche le résultat
    de chaque itération
    :param n: Le nombre de termes à calculer.
    :return: Une liste contenant les n premiers termes de la suite de Fibonacci.
    """
    fib_sequence = [0, 1]
    for i in range(2, n + 1):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)
        st.write(
            f"Le terme {i} de la suite de Fibonacci est : {next_fib} ({fib_sequence[i - 1]} + {fib_sequence[i - 2]})"
        )
    return fib_sequence


# Demander à l'utilisateur combien de termes il souhaite afficher
n_terms = st.number_input(
    "Combien de termes de la suite de Fibonacci souhaitez-vous afficher ?",
    min_value=1,
    value=10,
)

# Ajouter un bouton "calculer" pour exécuter la fonction
if st.button("Calculer"):
    fib_sequence = fibonacci(n_terms)
    st.write(f"**La suite de Fibonacci jusqu'à {n_terms} termes est : {fib_sequence}**")

# Ajouter un slider pour choisir le nombre de termes
n_terms_slider = st.slider(
    "Choisissez le nombre de termes de la suite de Fibonacci :",
    min_value=1,
    max_value=100,
    value=10,
)
if st.button("Calculer avec le slider"):
    fib_sequence_slider = fibonacci(n_terms_slider)
    st.write(
        f"**La suite de Fibonacci jusqu'à {n_terms_slider} termes est : {fib_sequence_slider}**"
    )
