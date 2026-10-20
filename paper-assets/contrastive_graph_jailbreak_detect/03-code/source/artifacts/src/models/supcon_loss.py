import torch
import torch.nn as nn


class SupConLoss(nn.Module):
    def __init__(self, temperature: float = 0.07):
        super().__init__()
        self.temperature = temperature

    def forward(self, features: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
        device = features.device
        bsz, n_views, feat_dim = features.shape

        # Reshape to [bsz * n_views, feat_dim]
        features = features.reshape(bsz * n_views, feat_dim)

        # Compute similarity matrix
        sim = torch.matmul(features, features.T) / self.temperature

        # Mask out self-similarity (diagonal)
        mask_self = torch.eye(bsz * n_views, dtype=torch.bool, device=device)

        # Build positive mask: same label OR same sample (different view)
        labels_expanded = labels.repeat(n_views)  # [bsz * n_views]
        mask_pos = labels_expanded.unsqueeze(0) == labels_expanded.unsqueeze(1)  # [N, N]
        mask_pos = mask_pos & ~mask_self  # exclude self

        # Log-sum-exp trick for numerical stability
        logits_max, _ = sim.detach().max(dim=1, keepdim=True)
        logits = sim - logits_max

        # Compute log-softmax over negatives + positives (excluding self)
        exp_logits = torch.exp(logits)
        exp_logits = exp_logits * (~mask_self).float()
        log_sum_exp = torch.log(exp_logits.sum(dim=1, keepdim=True) + 1e-12)

        # Compute mean of log-prob over positives
        log_prob = logits - log_sum_exp
        pos_log_prob = (mask_pos.float() * log_prob).sum(dim=1)
        num_pos = mask_pos.float().sum(dim=1)

        # Avoid division by zero for samples with no positives
        num_pos = torch.clamp(num_pos, min=1.0)
        loss = -(pos_log_prob / num_pos).mean()

        return loss
