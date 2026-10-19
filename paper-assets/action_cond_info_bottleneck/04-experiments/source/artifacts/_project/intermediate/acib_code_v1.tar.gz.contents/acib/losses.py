# ACIB loss functions: information bottleneck (sparsity) + consistency (robustness).
# Combined with the original flow matching task loss from SmolVLA.
#
# L_total = L_task + alpha * L_consistency + beta * L_IB

import torch
import torch.nn as nn
import torch.nn.functional as F

from acib.config import ACIBConfig


class ACIBLoss(nn.Module):
    """Combined ACIB loss: task + consistency + information bottleneck.

    Args:
        config: ACIBConfig with alpha (consistency weight) and beta (IB weight).
    """

    def __init__(self, config: ACIBConfig):
        super().__init__()
        self.alpha = config.alpha
        self.beta = config.beta

    def forward(
        self,
        task_loss: torch.Tensor,
        scores_clean: torch.Tensor,
        scores_perturbed: torch.Tensor | None = None,
    ) -> dict[str, torch.Tensor]:
        """Compute combined ACIB loss.

        Args:
            task_loss: scalar, original flow matching loss from SmolVLA.
            scores_clean: (B, N) logits from scorer on clean visual tokens.
            scores_perturbed: (B, N) logits from scorer on perturbed visual tokens.
                If None, consistency loss is skipped (eval or no augmentation).

        Returns:
            dict with keys: total, task, consistency, ib — all scalar tensors.
        """
        ib_loss = self.information_bottleneck_loss(scores_clean)

        if scores_perturbed is not None:
            consistency_loss = self.consistency_loss(scores_clean, scores_perturbed)
        else:
            consistency_loss = torch.tensor(0.0, device=task_loss.device)

        total = task_loss + self.alpha * consistency_loss + self.beta * ib_loss

        return {
            "total": total,
            "task": task_loss.detach(),
            "consistency": consistency_loss.detach(),
            "ib": ib_loss.detach(),
        }

    @staticmethod
    def information_bottleneck_loss(logits: torch.Tensor) -> torch.Tensor:
        """KL divergence between score distribution and uniform prior.

        Encourages the scorer to be selective (not assign equal weight to all tokens).
        KL(sigmoid(logits) || Uniform(0.5)) simplifies to:
            E[p * log(2p) + (1-p) * log(2(1-p))]
        where p = sigmoid(logits).

        Args:
            logits: (B, N) raw scorer logits.
        Returns:
            Scalar KL divergence, averaged over batch and tokens.
        """
        p = torch.sigmoid(logits)
        # Binary cross-entropy with uniform target q=0.5, negated = KL + const
        # KL(Bernoulli(p) || Bernoulli(0.5)) = p*log(2p) + (1-p)*log(2(1-p))
        kl = p * torch.log(2 * p + 1e-8) + (1 - p) * torch.log(2 * (1 - p) + 1e-8)
        return kl.mean()

    @staticmethod
    def consistency_loss(
        logits_clean: torch.Tensor, logits_perturbed: torch.Tensor
    ) -> torch.Tensor:
        """KL divergence between clean and perturbed score distributions.

        Encourages the scorer to produce similar relevance rankings regardless
        of visual perturbations (camera, lighting, texture, noise).

        Args:
            logits_clean: (B, N) scorer logits on clean images.
            logits_perturbed: (B, N) scorer logits on perturbed images.
        Returns:
            Scalar symmetric KL divergence, averaged over batch.
        """
        p_clean = F.softmax(logits_clean, dim=-1)
        p_perturbed = F.softmax(logits_perturbed, dim=-1)

        # Symmetric KL: 0.5 * (KL(p||q) + KL(q||p))
        kl_fwd = F.kl_div(p_perturbed.log(), p_clean, reduction="batchmean")
        kl_rev = F.kl_div(p_clean.log(), p_perturbed, reduction="batchmean")
        return 0.5 * (kl_fwd + kl_rev)
