"""OpenVLA VTC Adapter: Vision Token Compressor for OpenVLA (Prismatic + Llama-2 7B).

Compresses N projected vision tokens to M tokens using learnable cross-attention,
then runs standard autoregressive generation through the frozen LLM.

Architecture:
  DINOv2+SigLIP (frozen) -> MLP projector (frozen) -> N tokens x 4096
  -> VisionTokenCompressor (trainable) -> M tokens x 4096
  -> Llama-2 7B (frozen) -> action token logits -> cross-entropy loss

Differences from SmolVLA VTC (smart_compress_module.py):
  - hidden_dim: 960 -> 4096 (Llama-2 7B)
  - Vision tokens per camera: 128 -> 256 (DINOv2+SigLIP fused per-patch)
  - Action paradigm: flow matching -> autoregressive (256-bin discretized tokens)
  - No separate action expert; standard LM head generates action tokens

Dependencies: torch, transformers (OpenVLA loaded via trust_remote_code=True)
"""

from __future__ import annotations

import math
from typing import Any, Dict, List, Optional, Tuple, Union

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import Tensor


# ---------------------------------------------------------------------------
# VisionTokenCompressor (self-contained, same architecture as SmolVLA version)
# ---------------------------------------------------------------------------


class CrossAttentionBlock(nn.Module):
    """Pre-norm cross-attention + FFN block."""

    def __init__(self, hidden_dim: int, num_heads: int, dropout: float = 0.1):
        super().__init__()
        self.norm_q = nn.LayerNorm(hidden_dim)
        self.norm_kv = nn.LayerNorm(hidden_dim)
        self.cross_attn = nn.MultiheadAttention(
            embed_dim=hidden_dim,
            num_heads=num_heads,
            dropout=dropout,
            batch_first=True,
        )
        self.norm_ffn = nn.LayerNorm(hidden_dim)
        self.ffn = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim * 4),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim * 4, hidden_dim),
            nn.Dropout(dropout),
        )

    def forward(self, queries: Tensor, kv: Tensor) -> Tensor:
        q = self.norm_q(queries)
        kv_n = self.norm_kv(kv)
        attn_out, _ = self.cross_attn(q, kv_n, kv_n)
        queries = queries + attn_out
        queries = queries + self.ffn(self.norm_ffn(queries))
        return queries


class VisionTokenCompressor(nn.Module):
    """Cross-attention pooling: compress N vision tokens to M tokens.

    Args:
        hidden_dim: dimension of projected vision tokens (4096 for Llama-2 7B).
        num_queries: M, number of compressed output tokens.
        num_heads: attention heads per cross-attention layer.
        num_layers: number of cross-attention + FFN blocks.
        dropout: dropout rate.
    """

    def __init__(
        self,
        hidden_dim: int = 4096,
        num_queries: int = 32,
        num_heads: int = 16,
        num_layers: int = 2,
        dropout: float = 0.1,
    ):
        super().__init__()
        self.num_queries = num_queries
        self.hidden_dim = hidden_dim

        self.queries = nn.Parameter(torch.randn(1, num_queries, hidden_dim) * 0.02)

        self.layers = nn.ModuleList(
            [CrossAttentionBlock(hidden_dim, num_heads, dropout) for _ in range(num_layers)]
        )
        self.output_norm = nn.LayerNorm(hidden_dim)

    def forward(self, vision_tokens: Tensor) -> Tensor:
        """
        Args:
            vision_tokens: (B, N, D) projected vision tokens (possibly from multiple cameras).
        Returns:
            (B, M, D) compressed tokens.
        """
        B = vision_tokens.shape[0]
        queries = self.queries.expand(B, -1, -1)
        for layer in self.layers:
            queries = layer(queries, vision_tokens)
        return self.output_norm(queries)


# ---------------------------------------------------------------------------
# Action Tokenizer
# ---------------------------------------------------------------------------


class OpenVLAActionTokenizer:
    """Discretize continuous actions to/from OpenVLA action token IDs.

    OpenVLA adds 256 special action tokens to the vocabulary. Each continuous
    action dimension is independently discretized into one of 256 bins.

    Args:
        tokenizer: HuggingFace tokenizer from OpenVLA processor.
        n_bins: number of discretization bins (default 256).
        min_action: per-dim minimum for normalization, shape (action_dim,).
        max_action: per-dim maximum for normalization, shape (action_dim,).
    """

    def __init__(
        self,
        tokenizer,
        n_bins: int = 256,
        min_action: Optional[Tensor] = None,
        max_action: Optional[Tensor] = None,
    ):
        self.tokenizer = tokenizer
        self.n_bins = n_bins
        self.min_action = min_action
        self.max_action = max_action
        self.action_token_begin_id = self._find_action_token_begin(tokenizer)

    @staticmethod
    def _find_action_token_begin(tokenizer) -> int:
        """Find the first action token ID in the vocabulary."""
        vocab = tokenizer.get_vocab()
        # OpenVLA convention: tokens named like "v0_token_0" .. "v0_token_255"
        # or "ACTION_0" .. "ACTION_255" depending on version
        candidates = []
        for token, idx in vocab.items():
            for pattern in ("v0_token_", "ACTION_", "action_"):
                if token.startswith(pattern):
                    try:
                        bin_id = int(token[len(pattern):])
                        candidates.append((bin_id, idx))
                    except ValueError:
                        continue
        if candidates:
            candidates.sort(key=lambda x: x[0])
            return candidates[0][1]
        # Fallback: assume last n_bins tokens are action tokens
        return len(tokenizer) - 256

    def encode(self, actions: Tensor) -> Tensor:
        """Discretize continuous actions to token IDs.

        Args:
            actions: (..., action_dim) continuous actions.
        Returns:
            (..., action_dim) token IDs (long).
        """
        if self.min_action is not None and self.max_action is not None:
            lo = self.min_action.to(actions.device)
            hi = self.max_action.to(actions.device)
            normalized = (actions - lo) / (hi - lo + 1e-8)
        else:
            normalized = (actions + 1.0) / 2.0

        normalized = normalized.clamp(0.0, 1.0)
        bin_indices = (normalized * (self.n_bins - 1)).long()
        return bin_indices + self.action_token_begin_id

    def decode(self, token_ids: Tensor) -> Tensor:
        """Decode action token IDs back to continuous values.

        Args:
            token_ids: (..., action_dim) token IDs.
        Returns:
            (..., action_dim) continuous actions.
        """
        bin_indices = (token_ids - self.action_token_begin_id).clamp(0, self.n_bins - 1)
        normalized = bin_indices.float() / (self.n_bins - 1)

        if self.min_action is not None and self.max_action is not None:
            lo = self.min_action.to(normalized.device)
            hi = self.max_action.to(normalized.device)
            return normalized * (hi - lo) + lo
        return normalized * 2.0 - 1.0


# ---------------------------------------------------------------------------
# OpenVLA Smart Compress Wrapper
# ---------------------------------------------------------------------------


class OpenVLASmartCompressWrapper(nn.Module):
    """Wraps an OpenVLA model with VisionTokenCompressor.

    Intercepts projected vision features, compresses N -> M tokens via
    cross-attention, and feeds compressed tokens through the frozen LLM
    for autoregressive action token prediction.

    Args:
        model: OpenVLA model (AutoModelForVision2Seq with trust_remote_code).
        processor: OpenVLA processor (AutoProcessor).
        compress_config: dict with keys:
            hidden_dim (int): LLM hidden size (default 4096).
            num_queries (int): M compressed tokens (default 32).
            num_heads (int): attention heads (default 16).
            num_layers (int): cross-attention blocks (default 2).
            dropout (float): dropout rate (default 0.1).
    """

    def __init__(
        self,
        model: nn.Module,
        processor,
        compress_config: Optional[Dict[str, Any]] = None,
    ):
        super().__init__()
        self.model = model
        self.processor = processor

        cfg = compress_config or {}
        hidden_dim = cfg.get("hidden_dim", 4096)

        # Auto-detect hidden_dim from model config
        if hidden_dim == 4096 and hasattr(model, "config"):
            if hasattr(model.config, "text_config"):
                hidden_dim = model.config.text_config.hidden_size

        self.compressor = VisionTokenCompressor(
            hidden_dim=hidden_dim,
            num_queries=cfg.get("num_queries", 32),
            num_heads=cfg.get("num_heads", 16),
            num_layers=cfg.get("num_layers", 2),
            dropout=cfg.get("dropout", 0.1),
        )
        self.hidden_dim = hidden_dim
        self._image_token_id: Optional[int] = None

    @property
    def image_token_id(self) -> int:
        if self._image_token_id is None:
            tokenizer = self.processor.tokenizer
            vocab = tokenizer.get_vocab()
            for candidate in ("<image>", "<img>", "<visual>", "image"):
                if candidate in vocab:
                    self._image_token_id = vocab[candidate]
                    break
            if self._image_token_id is None:
                # Prismatic convention: image_token_id is stored in config
                if hasattr(self.model.config, "image_token_index"):
                    self._image_token_id = self.model.config.image_token_index
                else:
                    self._image_token_id = 32000  # common default for Llama-based VLMs
        return self._image_token_id

    # ----- vision feature extraction -----

    def get_vision_features(
        self, pixel_values: Union[Tensor, List[Tensor]]
    ) -> Tensor:
        """Extract projected vision features from frozen backbone + projector.

        Supports single or multiple camera images. For multi-camera, vision
        tokens are concatenated before compression.

        Args:
            pixel_values: single (B, C, H, W) tensor or list of such tensors
                          (one per camera).
        Returns:
            (B, N_total, hidden_dim) projected features.
        """
        if isinstance(pixel_values, (list, tuple)):
            camera_features = []
            for pv in pixel_values:
                camera_features.append(self._extract_projected(pv))
            return torch.cat(camera_features, dim=1)
        return self._extract_projected(pixel_values)

    def _extract_projected(self, pixel_values: Tensor) -> Tensor:
        """Run a single image through frozen vision backbone + projector."""
        model_dtype = next(self.model.vision_backbone.parameters()).dtype
        pixel_values = pixel_values.to(dtype=model_dtype)
        with torch.no_grad():
            if hasattr(self.model, "get_projected_patch_embeddings"):
                return self.model.get_projected_patch_embeddings(pixel_values)
            patch_features = self.model.vision_backbone(pixel_values)
            return self.model.projector(patch_features)

    # ----- input embedding construction -----

    def _build_compressed_inputs(
        self,
        input_ids: Tensor,
        compressed_vision: Tensor,
        attention_mask: Optional[Tensor] = None,
        labels: Optional[Tensor] = None,
    ) -> Tuple[Tensor, Tensor, Optional[Tensor]]:
        """Replace image placeholder tokens with compressed vision embeddings.

        Args:
            input_ids: (B, S) token IDs including image placeholders.
            compressed_vision: (B, M, D) compressed vision tokens.
            attention_mask: (B, S) original attention mask.
            labels: (B, S) training labels (-100 for non-target positions).

        Returns:
            inputs_embeds: (B, S_new, D) with compressed vision spliced in.
            new_attention_mask: (B, S_new).
            new_labels: (B, S_new) or None.
        """
        B = input_ids.shape[0]
        M = compressed_vision.shape[1]
        D = compressed_vision.shape[2]
        device = input_ids.device

        embed_fn = self.model.get_input_embeddings()
        img_tok = self.image_token_id

        embeds_list: List[Tensor] = []
        masks_list: List[Tensor] = []
        labels_list: List[Tensor] = []

        for i in range(B):
            is_img = input_ids[i] == img_tok
            img_positions = is_img.nonzero(as_tuple=True)[0]

            if len(img_positions) == 0:
                # No image tokens — pure text
                embeds_list.append(embed_fn(input_ids[i]))
                masks_list.append(
                    attention_mask[i] if attention_mask is not None
                    else torch.ones(input_ids.shape[1], device=device)
                )
                if labels is not None:
                    labels_list.append(labels[i])
                continue

            img_start = img_positions[0].item()
            img_end = img_positions[-1].item() + 1

            before_embeds = embed_fn(input_ids[i, :img_start])
            after_embeds = embed_fn(input_ids[i, img_end:])

            combined = torch.cat(
                [before_embeds, compressed_vision[i], after_embeds], dim=0
            )
            embeds_list.append(combined)

            if attention_mask is not None:
                before_mask = attention_mask[i, :img_start]
                after_mask = attention_mask[i, img_end:]
            else:
                before_mask = torch.ones(img_start, device=device)
                after_mask = torch.ones(input_ids.shape[1] - img_end, device=device)
            vision_mask = torch.ones(M, dtype=before_mask.dtype, device=device)
            masks_list.append(torch.cat([before_mask, vision_mask, after_mask]))

            if labels is not None:
                before_labels = labels[i, :img_start]
                after_labels = labels[i, img_end:]
                vision_labels = torch.full(
                    (M,), -100, dtype=labels.dtype, device=device
                )
                labels_list.append(
                    torch.cat([before_labels, vision_labels, after_labels])
                )

        # Pad to max length within batch
        max_len = max(e.shape[0] for e in embeds_list)
        padded_embeds = torch.zeros(B, max_len, D, dtype=embeds_list[0].dtype, device=device)
        padded_mask = torch.zeros(B, max_len, dtype=masks_list[0].dtype, device=device)
        padded_labels = (
            torch.full((B, max_len), -100, dtype=torch.long, device=device)
            if labels_list else None
        )

        for i in range(B):
            L = embeds_list[i].shape[0]
            padded_embeds[i, :L] = embeds_list[i]
            padded_mask[i, :L] = masks_list[i]
            if padded_labels is not None:
                padded_labels[i, :L] = labels_list[i]

        return padded_embeds, padded_mask, padded_labels

    # ----- training forward -----

    def forward(
        self,
        pixel_values: Union[Tensor, List[Tensor]],
        input_ids: Tensor,
        attention_mask: Optional[Tensor] = None,
        labels: Optional[Tensor] = None,
        **kwargs,
    ) -> Tuple[Tensor, Dict[str, Any]]:
        """Training forward: compress vision, run autoregressive LM, return loss.

        Args:
            pixel_values: (B, C, H, W) or list of (B, C, H, W) for multi-camera.
            input_ids: (B, S) token IDs with image placeholders + action tokens.
            attention_mask: (B, S) attention mask.
            labels: (B, S) with -100 for non-action positions.

        Returns:
            loss: scalar cross-entropy loss on action tokens.
            info: dict with diagnostics.
        """
        # 1. Extract projected vision tokens (frozen)
        vision_features = self.get_vision_features(pixel_values)
        N_original = vision_features.shape[1]

        # 2. Compress (trainable)
        vis_dtype = vision_features.dtype
        compressed = self.compressor(vision_features.detach().float())
        compressed = compressed.to(vis_dtype)

        # 3. Build input embeddings with compressed vision
        inputs_embeds, new_mask, new_labels = self._build_compressed_inputs(
            input_ids, compressed, attention_mask, labels
        )

        # 4. Forward through frozen LLM
        outputs = self.model.language_model(
            inputs_embeds=inputs_embeds,
            attention_mask=new_mask,
            labels=new_labels,
        )

        info = {
            "action_loss": outputs.loss.detach(),
            "num_compressed_tokens": compressed.shape[1],
            "compression_ratio": N_original / compressed.shape[1],
        }
        return outputs.loss, info

    # ----- inference -----

    @torch.no_grad()
    def predict_action(
        self,
        pixel_values: Union[Tensor, List[Tensor]],
        input_ids: Tensor,
        attention_mask: Optional[Tensor] = None,
        max_new_tokens: int = 7,
        do_sample: bool = False,
        temperature: float = 1.0,
    ) -> Tensor:
        """Generate action tokens using compressed vision prefix.

        Args:
            pixel_values: image tensor(s).
            input_ids: prompt token IDs (no action tokens, with image placeholders).
            attention_mask: prompt attention mask.
            max_new_tokens: number of action tokens to generate (default 7).

        Returns:
            generated_ids: (B, max_new_tokens) generated action token IDs.
        """
        vision_features = self.get_vision_features(pixel_values)
        compressed = self.compressor(vision_features.float()).to(vision_features.dtype)

        inputs_embeds, new_mask, _ = self._build_compressed_inputs(
            input_ids, compressed, attention_mask
        )

        gen_kwargs = dict(
            inputs_embeds=inputs_embeds,
            attention_mask=new_mask,
            max_new_tokens=max_new_tokens,
            do_sample=do_sample,
        )
        if do_sample:
            gen_kwargs["temperature"] = temperature

        generated = self.model.language_model.generate(**gen_kwargs)
        # generated includes the input prompt; extract only new tokens
        action_ids = generated[:, inputs_embeds.shape[1]:]
        return action_ids

    @torch.no_grad()
    def predict_action_continuous(
        self,
        pixel_values: Union[Tensor, List[Tensor]],
        input_ids: Tensor,
        attention_mask: Optional[Tensor] = None,
        action_tokenizer: Optional[OpenVLAActionTokenizer] = None,
        max_new_tokens: int = 7,
    ) -> Tensor:
        """Generate and decode continuous actions.

        Returns:
            actions: (B, action_dim) continuous actions.
        """
        action_ids = self.predict_action(
            pixel_values, input_ids, attention_mask,
            max_new_tokens=max_new_tokens,
        )
        if action_tokenizer is not None:
            return action_tokenizer.decode(action_ids)
        return action_ids.float()
