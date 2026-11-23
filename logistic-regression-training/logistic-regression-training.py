import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Returns elementwise sigmoid values.
    """
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))


def train_logistic_regression(
    X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 500
) -> tuple[np.ndarray, float]:
    """
    Returns the trained weights and bias as (w, b).
    """
    # TODO need to get the prediction
    X, y = np.array(X), np.array(y)
    updated_weights, updated_bais = np.zeros(X.shape[-1]), np.zeros(1)
    for i in range(steps):
        print("Shape updated_weights:", updated_weights.shape)
        print("Shape updated_bais:", updated_bais.shape)
        # make prediction
        logits = X @ updated_weights + updated_bais
        predictions = _sigmoid(logits)
        # TODO need to calculate the loss.
        # TODO need to get the gradients for the weights and bias. #TODO this is copied form the hints.
        print("SHAPE X.T and predictions-y:", X.T.shape, predictions.shape)
        grad_w = X.T @ (predictions - y) / len(y)
        grad_b = np.mean(predictions - y)

        updated_weights -= (lr) * (grad_w)
        updated_bais -= (lr) * (grad_b)
    return updated_weights, updated_bais


