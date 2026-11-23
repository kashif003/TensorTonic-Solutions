import numpy as np

def pad_sequences(
    seqs: list, pad_value: int = 0, max_len: int | None = None
) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
def pad_sequences(
    seqs: list, pad_value: int = 0, max_len: int | None = None
) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    n = len(seqs)

    if max_len is None:
        max_len = max((len(seq) for seq in seqs), default=0)

    # Preallocate with the pad value, then copy in each (possibly truncated) sequence
    out = np.full((n, max_len), pad_value, dtype=int)
    for i, seq in enumerate(seqs):
        trunc = seq[:max_len]
        out[i, :len(trunc)] = trunc

    return out