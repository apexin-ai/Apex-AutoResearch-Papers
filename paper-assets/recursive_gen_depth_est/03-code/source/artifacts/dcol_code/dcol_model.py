"""DeBERTa-v3-large encoder with MLP projection head for DCOL.

Input:  tokenized text (input_ids, attention_mask)
Output: L2-normalized 128-dim embeddings

Dependencies: transformers, torch
"""

import torch
import torch.nn as nn
from transformers import AutoModel


class DColModel(nn.Module):
    def __init__(self, model_name: str = "microsoft/deberta-v3-large", embed_dim: int = 128):
        super().__init__()
        self.encoder = AutoModel.from_pretrained(model_name)
        hidden = self.encoder.config.hidden_size  # 1024 for deberta-v3-large
        self.proj = nn.Sequential(
            nn.Linear(hidden, hidden),
            nn.GELU(),
            nn.Linear(hidden, embed_dim),
        )

    def forward(self, input_ids: torch.Tensor, attention_mask: torch.Tensor) -> torch.Tensor:
        out = self.encoder(input_ids=input_ids, attention_mask=attention_mask)
        cls = out.last_hidden_state[:, 0]  # CLS pooling
        emb = self.proj(cls)
        return nn.functional.normalize(emb, dim=-1)
