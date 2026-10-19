"""StructFuse contrastive bi-encoder with fusion head.

Bi-encoder over Qwen2.5-Coder-3B with InfoNCE loss, weighted positives
(data-flow path distance), and an optional lightweight fusion head that
combines embedding similarity with explicit structural features.
"""

import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from transformers import AutoModel, AutoConfig


class FusionHead(nn.Module):
    """MLP that fuses embedding similarity with explicit features into a relevance score."""

    FEATURE_NAMES = [
        "dataflow_distance",
        "bm25_score",
        "co_change_freq",
        "inter_procedural_flag",
        "path_count",
    ]
    NUM_EXPLICIT = len(FEATURE_NAMES)

    def __init__(self, hidden_dim: int = 128):
        super().__init__()
        input_dim = 1 + self.NUM_EXPLICIT  # embed_similarity + explicit features
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.GELU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.GELU(),
            nn.Linear(hidden_dim, 1),
        )

    def forward(self, embed_similarity: torch.Tensor, features: torch.Tensor) -> torch.Tensor:
        """
        Args:
            embed_similarity: (B,) or (B, K) cosine similarities.
            features: same leading dims + NUM_EXPLICIT trailing dim.
        Returns:
            scores with same shape as embed_similarity.
        """
        orig_shape = embed_similarity.shape
        sim = embed_similarity.unsqueeze(-1)  # (..., 1)
        x = torch.cat([sim, features], dim=-1)  # (..., 1+NUM_EXPLICIT)
        x = x.view(-1, x.size(-1))
        out = self.net(x).squeeze(-1)
        return out.view(orig_shape)


class StructFuseEncoder(nn.Module):
    """Bi-encoder with shared Qwen backbone, optional projection & LoRA."""

    def __init__(
        self,
        model_name: str = "Qwen/Qwen2.5-Coder-3B",
        proj_dim: int = 256,
        use_projection: bool = True,
        use_lora: bool = False,
        lora_r: int = 16,
        lora_alpha: int = 32,
        use_fusion_head: bool = False,
        fusion_hidden: int = 128,
    ):
        super().__init__()
        self.backbone = AutoModel.from_pretrained(model_name, trust_remote_code=True)
        hidden_size = self.backbone.config.hidden_size

        self.use_projection = use_projection
        if use_projection:
            self.projection = nn.Sequential(
                nn.Linear(hidden_size, hidden_size),
                nn.GELU(),
                nn.Linear(hidden_size, proj_dim),
            )
            self.embed_dim = proj_dim
        else:
            self.projection = None
            self.embed_dim = hidden_size

        self.use_fusion_head = use_fusion_head
        if use_fusion_head:
            self.fusion_head = FusionHead(hidden_dim=fusion_hidden)

        # learnable temperature for InfoNCE
        self.log_temperature = nn.Parameter(torch.tensor(math.log(0.07)))

        if use_lora:
            self._apply_lora(lora_r, lora_alpha)

    def _apply_lora(self, r: int, alpha: int):
        from peft import LoraConfig, get_peft_model

        lora_cfg = LoraConfig(
            r=r,
            lora_alpha=alpha,
            target_modules=["q_proj", "v_proj"],
            lora_dropout=0.05,
            bias="none",
            task_type="FEATURE_EXTRACTION",
        )
        self.backbone = get_peft_model(self.backbone, lora_cfg)

    def enable_gradient_checkpointing(self):
        self.backbone.gradient_checkpointing_enable()

    @property
    def temperature(self) -> torch.Tensor:
        return self.log_temperature.exp()

    def encode(self, input_ids: torch.Tensor, attention_mask: torch.Tensor) -> torch.Tensor:
        """Mean-pool last hidden states (excluding padding) and optionally project."""
        outputs = self.backbone(input_ids=input_ids, attention_mask=attention_mask)
        hidden = outputs.last_hidden_state  # (B, L, H)

        mask_expanded = attention_mask.unsqueeze(-1).float()  # (B, L, 1)
        summed = (hidden * mask_expanded).sum(dim=1)  # (B, H)
        lengths = mask_expanded.sum(dim=1).clamp(min=1e-9)  # (B, 1)
        pooled = summed / lengths  # (B, H)

        if self.projection is not None:
            pooled = self.projection(pooled)

        return F.normalize(pooled, p=2, dim=-1)

    def forward(
        self,
        query_ids: torch.Tensor,
        query_mask: torch.Tensor,
        pos_ids: torch.Tensor,
        pos_mask: torch.Tensor,
        neg_ids: torch.Tensor,
        neg_mask: torch.Tensor,
        pos_weights: torch.Tensor | None = None,
        features: torch.Tensor | None = None,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        """
        Compute InfoNCE loss with weighted positives and optional fusion head.

        Args:
            query_ids/mask: (B, Lq)
            pos_ids/mask:   (B, Lp)       — one positive per query
            neg_ids/mask:   (B, K, Ln)    — K explicit negatives per query
            pos_weights:    (B,)          — exp(-alpha * path_distance) weights
            features:       (B, 1+K, NUM_EXPLICIT) — features for pos + negs if fusion head is used

        Returns:
            loss: scalar
            logits: (B, 1+K) similarity scores (for monitoring)
        """
        B = query_ids.size(0)
        K = neg_ids.size(1)

        q_emb = self.encode(query_ids, query_mask)  # (B, D)
        p_emb = self.encode(pos_ids, pos_mask)  # (B, D)

        # flatten negatives for encoding, then reshape back
        neg_ids_flat = neg_ids.view(B * K, -1)
        neg_mask_flat = neg_mask.view(B * K, -1)
        n_emb = self.encode(neg_ids_flat, neg_mask_flat).view(B, K, -1)  # (B, K, D)

        # cosine similarities
        pos_sim = (q_emb * p_emb).sum(dim=-1)  # (B,)
        neg_sim = torch.bmm(n_emb, q_emb.unsqueeze(-1)).squeeze(-1)  # (B, K)

        if self.use_fusion_head and features is not None:
            all_sim = torch.cat([pos_sim.unsqueeze(1), neg_sim], dim=1)  # (B, 1+K)
            logits = self.fusion_head(all_sim, features) / self.temperature
        else:
            logits = torch.cat([pos_sim.unsqueeze(1), neg_sim], dim=1) / self.temperature  # (B, 1+K)

        # InfoNCE: labels are always index 0 (the positive)
        labels = torch.zeros(B, dtype=torch.long, device=logits.device)

        if pos_weights is not None:
            # Weight per-sample loss, not logits — scaling logits inverts the intended effect
            per_sample_loss = F.cross_entropy(logits, labels, reduction='none')
            loss = (per_sample_loss * pos_weights).mean()
        else:
            loss = F.cross_entropy(logits, labels)

        return loss, logits
