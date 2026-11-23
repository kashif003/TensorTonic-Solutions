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
    if len(seqs) == 0:
        return np.array(seqs, dtype = int).reshape(0,0)

    if max_len is None:
        max_len = len(max(seqs, key=len))
    arr = np.full((len(seqs), max_len),0)
    for i in range(len(arr)):
        if len(seqs[i]) < max_len:
            seqs[i].extend([pad_value] * (max_len - len(seqs[i])))
        else:
            seqs[i] = seqs[i][:max_len]

    return np.array(seqs)

