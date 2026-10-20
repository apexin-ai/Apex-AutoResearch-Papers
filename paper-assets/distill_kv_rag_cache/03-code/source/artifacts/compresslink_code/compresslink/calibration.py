"""KVTC PCA calibration: collect NoPE KV cache and compute per-head PCA."""

import os
from pathlib import Path
from typing import Dict, List, Optional

import torch


class KVTCCalibrator:
    """Collect NoPE (pre-RoPE) keys and values, then compute PCA basis per head.

    Workflow:
        1. Install forward hooks on k_proj / v_proj of each attention layer.
        2. Run a small set of calibration texts through the model.
        3. Reshape collected projections to (layer, head, tokens, head_dim).
        4. SVD → per-head eigenvalues, eigenvectors, mean.
        5. Save / load the calibration artefact.
    """

    def __init__(
        self,
        model,
        tokenizer,
        num_samples: int = 10,
        save_dir: str = "/root/autodl-tmp/compresslink/calibration",
    ):
        self.model = model
        self.tokenizer = tokenizer
        self.num_samples = num_samples
        self.save_dir = Path(save_dir)

        config = model.config
        self.num_layers = config.num_hidden_layers
        self.num_kv_heads = getattr(config, "num_key_value_heads", config.num_attention_heads)
        self.head_dim = config.hidden_size // config.num_attention_heads

        self._hooks: list = []
        self._collected: Dict[tuple, List[torch.Tensor]] = {}

    # ------------------------------------------------------------------
    # Hook management
    # ------------------------------------------------------------------

    def _get_attention_layers(self):
        """Yield (layer_idx, attention_module) for supported architectures."""
        if hasattr(self.model, "model") and hasattr(self.model.model, "layers"):
            layers = self.model.model.layers
        elif hasattr(self.model, "transformer") and hasattr(self.model.transformer, "h"):
            layers = self.model.transformer.h
        else:
            raise ValueError("Unsupported model architecture for hook installation")

        for idx, layer in enumerate(layers):
            attn = getattr(layer, "self_attn", None) or getattr(layer, "attention", None)
            if attn is None:
                raise ValueError(f"Cannot locate attention sub-module in layer {idx}")
            yield idx, attn

    def _make_hook(self, layer_idx: int, kind: str):
        def hook(_module, _input, output):
            if isinstance(output, tuple):
                output = output[0]
            bsz, seq_len, _ = output.shape
            reshaped = output.view(bsz, seq_len, self.num_kv_heads, self.head_dim)
            self._collected.setdefault((layer_idx, kind), []).append(
                reshaped.detach().cpu()
            )
        return hook

    def _install_hooks(self):
        for layer_idx, attn in self._get_attention_layers():
            for proj_name, kind in [("k_proj", "key"), ("v_proj", "value")]:
                proj = getattr(attn, proj_name, None)
                if proj is None:
                    raise ValueError(f"Layer {layer_idx} has no {proj_name}")
                handle = proj.register_forward_hook(self._make_hook(layer_idx, kind))
                self._hooks.append(handle)

    def _remove_hooks(self):
        for h in self._hooks:
            h.remove()
        self._hooks.clear()

    # ------------------------------------------------------------------
    # Collection
    # ------------------------------------------------------------------

    @torch.no_grad()
    def collect_nope_kv(self, texts: List[str]) -> Dict[tuple, torch.Tensor]:
        """Forward-pass calibration texts and collect NoPE key/value tensors.

        Hooks capture k_proj / v_proj outputs (before RoPE), so the collected
        keys are already in NoPE form.

        Returns:
            Dict mapping (layer_idx, 'key'|'value') →
                Tensor of shape (total_tokens, num_kv_heads, head_dim)
        """
        self._collected.clear()
        self._install_hooks()
        self.model.eval()

        try:
            for text in texts[: self.num_samples]:
                inputs = self.tokenizer(
                    text, return_tensors="pt", truncation=True, max_length=2048
                ).to(self.model.device)
                self.model(**inputs)
        finally:
            self._remove_hooks()

        merged: Dict[tuple, torch.Tensor] = {}
        for key, tensor_list in self._collected.items():
            merged[key] = torch.cat(tensor_list, dim=1).squeeze(0)
        self._collected.clear()
        return merged

    # ------------------------------------------------------------------
    # PCA
    # ------------------------------------------------------------------

    def compute_pca(self, kv_data: Dict[tuple, torch.Tensor]) -> Dict:
        """SVD per (layer, head, key/value).

        Args:
            kv_data: output of collect_nope_kv

        Returns:
            Dict[(layer, head, kind)] → {mean, eigenvalues, components}
        """
        calibration: Dict = {}
        for (layer_idx, kind), data in kv_data.items():
            # data: (total_tokens, num_kv_heads, head_dim)
            for head_idx in range(self.num_kv_heads):
                head_data = data[:, head_idx, :].float()  # (N, head_dim)
                mean = head_data.mean(dim=0)
                centered = head_data - mean

                _, S, Vh = torch.linalg.svd(centered, full_matrices=False)
                eigenvalues = S ** 2 / max(centered.shape[0] - 1, 1)

                calibration[(layer_idx, head_idx, kind)] = {
                    "mean": mean,
                    "eigenvalues": eigenvalues,
                    "components": Vh,  # (head_dim, head_dim)
                }
        return calibration

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------

    def save(self, calibration_data: Dict, path: Optional[str] = None):
        """Save calibration data as a .pt file."""
        save_path = Path(path) if path else self.save_dir / "calibration.pt"
        save_path.parent.mkdir(parents=True, exist_ok=True)

        serialisable = {}
        for key, val in calibration_data.items():
            str_key = f"{key[0]}_{key[1]}_{key[2]}"
            serialisable[str_key] = {k: v for k, v in val.items()}

        torch.save(
            {"data": serialisable, "num_kv_heads": self.num_kv_heads, "head_dim": self.head_dim},
            save_path,
        )

    @staticmethod
    def load(path: str) -> Dict:
        """Load calibration data from a .pt file."""
        raw = torch.load(path, map_location="cpu", weights_only=False)
        calibration: Dict = {}
        for str_key, val in raw["data"].items():
            parts = str_key.split("_")
            key = (int(parts[0]), int(parts[1]), parts[2])
            calibration[key] = val
        return calibration
