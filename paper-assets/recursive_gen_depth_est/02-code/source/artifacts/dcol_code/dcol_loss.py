"""N-pair contrastive ordinal loss with learnable margins for DCOL.

Learnable margin matrix M[i][j] initialized to |i-j| * base_margin.
- Attractive: same-depth pairs pulled together (MSE on embeddings).
- Repulsive: different-depth pairs pushed apart with ordinal-aware margin.
- Total = alpha * attractive + beta * repulsive

Dependencies: torch
"""

import torch
import torch.nn as nn


class DColLoss(nn.Module):
    def __init__(self, num_classes: int = 4, base_margin: float = 0.3,
                 alpha: float = 1.0, beta: float = 1.0):
        super().__init__()
        self.alpha = alpha
        self.beta = beta
        # Initialize margin matrix: M[i][j] = |i - j| * base_margin
        init = torch.zeros(num_classes, num_classes)
        for i in range(num_classes):
            for j in range(num_classes):
                init[i, j] = abs(i - j) * base_margin
        self.margin = nn.Parameter(init)

    def forward(self, embeddings: torch.Tensor, labels: torch.Tensor) -> dict:
        """
        Args:
            embeddings: (B, D) L2-normalized embeddings
            labels: (B,) integer depth labels
        Returns:
            dict with 'loss', 'attractive', 'repulsive' keys
        """
        # Pairwise squared distances: ||e_i - e_j||^2
        dists = torch.cdist(embeddings, embeddings, p=2).pow(2)  # (B, B)

        label_i = labels.unsqueeze(1)  # (B, 1)
        label_j = labels.unsqueeze(0)  # (1, B)
        same_mask = (label_i == label_j)

        # Exclude self-pairs
        eye = torch.eye(len(labels), device=labels.device, dtype=torch.bool)
        same_mask = same_mask & ~eye
        diff_mask = (label_i != label_j)

        # Attractive: MSE on same-depth pairs
        if same_mask.any():
            attractive = dists[same_mask].mean()
        else:
            attractive = torch.tensor(0.0, device=embeddings.device)

        # Repulsive: hinge loss with learnable ordinal margin
        if diff_mask.any():
            margins = self.margin[label_i.expand_as(dists), label_j.expand_as(dists)]
            margins = margins.abs()  # ensure positive after gradient updates
            sqrt_dists = dists[diff_mask].sqrt()
            target_margins = margins[diff_mask]
            repulsive = torch.clamp(target_margins - sqrt_dists, min=0).mean()
        else:
            repulsive = torch.tensor(0.0, device=embeddings.device)

        loss = self.alpha * attractive + self.beta * repulsive
        return {"loss": loss, "attractive": attractive, "repulsive": repulsive}
