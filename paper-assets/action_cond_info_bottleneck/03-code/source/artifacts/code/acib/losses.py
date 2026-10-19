# ACIB loss functions: information bottleneck (sparsity) + consistency (robustness).
# Combined with the original flow matching task loss from SmolVLA.
#
# L_total = L_task + alpha * L_consistency + beta * L_IB
# L_IB = KL(Bernoulli(sigmoid(logits)) || Bernoulli(target_rate))
# L_consistency = MSE(logits_clean, logits_perturbed)

import torch
import torch.nn as nn
import torch.nn.functional as F

from acib.config import ACIBConfig


class ACIBLoss(nn.Module):
    """Combined ACIB loss: task + consistency + information bottleneck.

    Args:
        config: ACIBConfig with alpha (consistency weight), beta (IB weight),
                and top_k_ratio (IB target rate).
    """

    def __init__(self, config: ACIBConfig):
        super().__init__()
        self.alpha = config.alpha
        self.beta = config.beta
        self.target_rate = config.top_k_ratio

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
        ib_loss = self.information_bottleneck_loss(scores_clean, self.target_rate)

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
    def information_bottleneck_loss(
        logits: torch.Tensor, target_rate: float = 0.8
    ) -> torch.Tensor:
        """KL(Bernoulli(p) || Bernoulli(target_rate)).

        Regularizes the scorer toward keeping ~target_rate fraction of tokens
        (sigmoid(logit) ≈ target_rate). Tokens that deviate from target_rate
        incur penalty, encouraging structured selection rather than uniform
        or degenerate scores.

        Args:
            logits: (B, N) raw scorer logits.
            target_rate: prior probability for each token being "kept".
                         Matches config.top_k_ratio (default 0.8).
        Returns:
            Scalar KL divergence, averaged over batch and tokens.
        """
        p = torch.sigmoid(logits)
        q = target_rate
        kl = (
            p * torch.log(p / (q + 1e-8) + 1e-8)
            + (1 - p) * torch.log((1 - p) / (1 - q + 1e-8) + 1e-8)
        )
        return kl.mean()

    @staticmethod
    def consistency_loss(
        logits_clean: torch.Tensor, logits_perturbed: torch.Tensor
    ) -> torch.Tensor:
        """MSE between clean and perturbed scorer logits.

        Enforces cross-view selection consistency: the scorer should assign
        similar relevance scores to each visual token position regardless
        of visual perturbations (camera, lighting, texture, noise).
        Per IDEA_BRIEF: L_consistency = ||S(V) - S(V')||².

        Args:
            logits_clean: (B, N) scorer logits on clean images.
            logits_perturbed: (B, N) scorer logits on perturbed images.
        Returns:
            Scalar MSE, averaged over batch and tokens.
        """
        return F.mse_loss(logits_clean, logits_perturbed)
