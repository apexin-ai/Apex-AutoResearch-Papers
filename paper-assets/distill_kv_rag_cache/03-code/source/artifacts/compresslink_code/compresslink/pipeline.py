"""Main CompressLink pipeline integrating all components.

Configs:
    A: Standard KVTC + ProphetKV restoration (on non-boundary only)
    B: RABA + ProphetKV restoration (on non-boundary only)
    C: Standard KVTC + CEGR-MSE restoration (on non-boundary only)
    D: RABA + CEGR-MSE (full joint, on non-boundary only)
    E: Uncompressed MEPIC baseline (NoPE + boundary recomp only)

All configs do boundary recomputation first (fixed overhead), then use remaining
budget for query-dependent restoration.
"""

import torch
from torch import Tensor
from typing import Dict, List, Optional
from transformers import DynamicCache
from transformers.cache_utils import DynamicLayer

from .budget_manager import RecomputationBudgetManager
from .boundary_recomp import BoundaryRecomputer
from .raba import (
    compute_restoration_weighted_eigenvalues,
    get_position_prior_probs,
    greedy_bit_allocation,
)
from .cegr import CEGRSelector
from .query_probe import QueryRelevanceProbe


class SimplePCACompressor:
    """KVTC-style PCA + uniform quantization for MVP evaluation.

    Per-(layer, batch, head) slice: SVD for PCA basis, DP/greedy bit allocation,
    uniform affine quantization per PCA component.
    """

    def __init__(self, head_dim: int = 128, max_bits: int = 16):
        self.head_dim = head_dim
        self.max_bits = max_bits
        self._calibrations: Dict[str, list] = {}

    def calibrate(self, data: Tensor, kind: str = "keys"):
        """Compute PCA basis from [L, B, H, T, D] data."""
        L, B, H, T, D = data.shape
        flat = data.reshape(-1, T, D)
        entries = []

        for i in range(flat.shape[0]):
            x = flat[i].float()
            mean = x.mean(dim=0)
            centered = x - mean
            _, S, Vh = torch.linalg.svd(centered, full_matrices=False)
            eigenvalues = S**2 / max(T - 1, 1)
            entries.append({"mean": mean, "Vh": Vh, "eigenvalues": eigenvalues})

        self._calibrations[kind] = entries

    def compress(
        self,
        data: Tensor,
        bit_budget_ratio: float,
        kind: str = "keys",
        restoration_probs: Optional[Tensor] = None,
    ) -> list:
        """Compress with optional RABA weighting.

        Args:
            data: [L, B, H, T, D] KV tensor
            bit_budget_ratio: fraction of max bits to use (e.g., 1/6 for 6x)
            kind: 'keys' or 'values'
            restoration_probs: [T] per-token p_r for RABA (None for standard)

        Returns:
            list of per-slice compressed entries
        """
        L, B, H, T, D = data.shape
        flat = data.reshape(-1, T, D)
        entries = self._calibrations[kind]
        total_bits = int(D * self.max_bits * bit_budget_ratio)

        compressed = []
        for i in range(flat.shape[0]):
            x = flat[i].float()
            cal = entries[i]

            centered = x - cal["mean"]
            coeffs = centered @ cal["Vh"].T  # [T, D]

            if restoration_probs is not None:
                weighted_eig = compute_restoration_weighted_eigenvalues(
                    coeffs, restoration_probs.to(coeffs.device)
                )
                bit_widths = greedy_bit_allocation(weighted_eig, total_bits, self.max_bits)
            else:
                bit_widths = greedy_bit_allocation(
                    cal["eigenvalues"], total_bits, self.max_bits
                )

            quantized = self._quantize(coeffs, bit_widths)
            compressed.append(
                {"quantized": quantized, "bit_widths": bit_widths, "cal_idx": i}
            )

        return compressed

    def decompress(self, compressed: list, shape: tuple, kind: str = "keys") -> Tensor:
        """Decompress to [L, B, H, T, D] tensor."""
        L, B, H, T, D = shape
        entries = self._calibrations[kind]
        device = entries[0]["mean"].device
        flat = torch.zeros(L * B * H, T, D, device=device)

        for i, entry in enumerate(compressed):
            cal = entries[i]
            coeffs = self._dequantize(entry["quantized"])
            reconstructed = coeffs @ cal["Vh"] + cal["mean"]
            flat[i] = reconstructed

        return flat.reshape(shape)

    @staticmethod
    def _quantize(coeffs: Tensor, bit_widths: Tensor) -> dict:
        T, D = coeffs.shape
        bit_widths = bit_widths.to(coeffs.device)
        active = bit_widths > 0

        mins = coeffs.min(dim=0).values
        maxs = coeffs.max(dim=0).values
        ranges = (maxs - mins).clamp(min=1e-8)

        num_levels = (2.0 ** bit_widths.float()) - 1
        num_levels = num_levels.clamp(min=1.0)

        scales = ranges / num_levels
        codes = torch.round((coeffs - mins) / scales)
        codes[:, ~active] = 0

        return {"codes": codes, "mins": mins, "scales": scales, "active": active}

    @staticmethod
    def _dequantize(quantized: dict) -> Tensor:
        codes = quantized["codes"]
        mins = quantized["mins"]
        scales = quantized["scales"]
        active = quantized["active"]

        result = codes * scales + mins
        result[:, ~active] = 0
        return result


class CompressLinkPipeline:
    """End-to-end CompressLink pipeline for MVP evaluation.

    Integrates NoPE cache, boundary recomputation, KVTC compression (+RABA),
    query probing, and CEGR/ProphetKV restoration.
    """

    VALID_CONFIGS = {"A", "B", "C", "D", "E"}

    def __init__(self, model, tokenizer, config: dict):
        self.model = model
        self.tokenizer = tokenizer
        self.config = config

        chunk_size = config.get("chunk_size", 512)
        block_size = config.get("block_size", 32)
        total_budget = config.get("total_budget", 0.20)
        beta = config.get("beta", 1.0)
        head_dim = config.get("head_dim", 128)
        max_bits = config.get("max_bits", 16)

        self.chunk_size = chunk_size
        self.budget_manager = RecomputationBudgetManager(total_budget, block_size)
        self.boundary_recomp = BoundaryRecomputer(block_size)
        self.cegr = CEGRSelector(beta)
        self.compressor = SimplePCACompressor(head_dim, max_bits)

    def run_single(
        self,
        context_ids: Tensor,
        query_ids: Tensor,
        config_name: str,
        compression_ratio: float,
    ) -> Dict:
        """Run one sample through the pipeline.

        Args:
            context_ids: [1, ctx_len] document token ids
            query_ids: [1, q_len] query token ids
            config_name: one of A/B/C/D/E
            compression_ratio: e.g. 6.0 for 6x compression (ignored for E)

        Returns:
            dict with generated_text and generated_ids
        """
        assert config_name in self.VALID_CONFIGS
        device = next(self.model.parameters()).device
        context_ids = context_ids.to(device)
        query_ids = query_ids.to(device)

        # Step 1: NoPE forward on context
        with torch.no_grad():
            ctx_out = self.model(
                input_ids=context_ids, use_cache=True, output_attentions=False
            )
        original_cache = ctx_out.past_key_values
        num_tokens = context_ids.shape[1]

        # Step 2: Budget allocation
        chunk_boundaries = list(range(self.chunk_size, num_tokens, self.chunk_size))
        budget = self.budget_manager.allocate(num_tokens, chunk_boundaries)

        # Config E: uncompressed baseline (boundary recomp only)
        if config_name == "E":
            return self._decode(
                self._clone_cache(original_cache), query_ids, num_tokens
            )

        # Step 3: Extract KV tensors
        orig_keys, orig_values = self._cache_to_tensors(original_cache)

        # Step 4: Calibrate PCA
        self.compressor.calibrate(orig_keys, kind="keys")
        self.compressor.calibrate(orig_values, kind="values")

        # Step 5: Compress
        bit_budget_ratio = 1.0 / compression_ratio

        if config_name in ("B", "D"):
            p_r = get_position_prior_probs(
                num_tokens, budget["boundary_indices"], device
            )
            key_comp = self.compressor.compress(
                orig_keys, bit_budget_ratio, "keys", restoration_probs=p_r
            )
            val_comp = self.compressor.compress(
                orig_values, bit_budget_ratio, "values", restoration_probs=p_r
            )
        else:
            key_comp = self.compressor.compress(orig_keys, bit_budget_ratio, "keys")
            val_comp = self.compressor.compress(
                orig_values, bit_budget_ratio, "values"
            )

        # Step 6: Decompress
        dec_keys = self.compressor.decompress(key_comp, orig_keys.shape, "keys")
        dec_values = self.compressor.decompress(val_comp, orig_values.shape, "values")

        # Step 7: Boundary restoration (unconditional, all configs)
        bi = budget["boundary_indices"]
        if bi:
            idx = torch.tensor(bi, device=device, dtype=torch.long)
            dec_keys[:, :, :, idx] = orig_keys[:, :, :, idx]
            dec_values[:, :, :, idx] = orig_values[:, :, :, idx]

        # Step 8: Query probe for relevance
        dec_cache = self._tensors_to_cache(dec_keys, dec_values)
        probe_cache = self._clone_cache(dec_cache)

        q_pos = torch.arange(
            num_tokens, num_tokens + query_ids.shape[1], device=device
        ).unsqueeze(0)

        with torch.no_grad():
            probe_out = self.model(
                input_ids=query_ids,
                past_key_values=probe_cache,
                position_ids=q_pos,
                output_attentions=True,
                use_cache=False,
            )

        # Extract relevance for cache tokens only (exclude query self-attention)
        attn_tuple = probe_out.attentions
        cache_attns = tuple(a[:, :, :, :num_tokens] for a in attn_tuple)
        r_q = QueryRelevanceProbe.compute_relevance(cache_attns)

        # Step 9: Select restoration tokens (non-boundary only)
        nb_indices = budget["non_boundary_indices"]
        cegr_num = budget["cegr_num_tokens"]

        if config_name in ("A", "B"):
            restore_indices = self._select_by_relevance(r_q, nb_indices, cegr_num)
        else:
            eps_k = ((orig_keys - dec_keys) ** 2).mean(dim=(0, 1, 2, 4))
            eps_v = ((orig_values - dec_values) ** 2).mean(dim=(0, 1, 2, 4))
            epsilon = (eps_k + eps_v) / 2
            restore_indices = self.cegr.select_restoration_tokens(
                r_q, epsilon, nb_indices, cegr_num
            )

        # Step 10: Restore selected tokens
        if restore_indices:
            ri = torch.tensor(restore_indices, device=device, dtype=torch.long)
            dec_keys[:, :, :, ri] = orig_keys[:, :, :, ri]
            dec_values[:, :, :, ri] = orig_values[:, :, :, ri]
            dec_cache = self._tensors_to_cache(dec_keys, dec_values)

        # Step 11: Decode
        return self._decode(dec_cache, query_ids, num_tokens)

    def _decode(self, kv_cache, query_ids: Tensor, ctx_len: int) -> Dict:
        """Auto-regressive greedy decode with KV cache."""
        device = query_ids.device
        q_len = query_ids.shape[1]
        max_new = self.config.get("max_new_tokens", 32)
        eos_id = self.tokenizer.eos_token_id

        q_pos = torch.arange(ctx_len, ctx_len + q_len, device=device).unsqueeze(0)

        with torch.no_grad():
            out = self.model(
                input_ids=query_ids,
                past_key_values=kv_cache,
                position_ids=q_pos,
                use_cache=True,
            )

        generated = []
        next_token = out.logits[:, -1:].argmax(dim=-1)
        generated.append(next_token)
        cache = out.past_key_values
        cur_pos = ctx_len + q_len

        for _ in range(max_new - 1):
            pos = torch.tensor([[cur_pos]], device=device)
            with torch.no_grad():
                out = self.model(
                    input_ids=next_token,
                    past_key_values=cache,
                    position_ids=pos,
                    use_cache=True,
                )
            next_token = out.logits[:, -1:].argmax(dim=-1)
            generated.append(next_token)
            cache = out.past_key_values
            cur_pos += 1

            if next_token.item() == eos_id:
                break

        gen_ids = torch.cat(generated, dim=-1)
        text = self.tokenizer.decode(gen_ids[0], skip_special_tokens=True)
        return {"generated_text": text, "generated_ids": gen_ids}

    @staticmethod
    def _select_by_relevance(
        relevance: Tensor, non_boundary_indices: List[int], num_to_select: int
    ) -> List[int]:
        """ProphetKV-style: select top-relevant non-boundary tokens."""
        if num_to_select <= 0 or not non_boundary_indices:
            return []
        nb_idx = torch.tensor(
            non_boundary_indices, device=relevance.device, dtype=torch.long
        )
        nb_rel = relevance[nb_idx]
        k = min(num_to_select, len(nb_idx))
        _, topk_local = nb_rel.topk(k)
        return sorted(nb_idx[topk_local].tolist())

    @staticmethod
    def _cache_to_tensors(cache):
        """Extract [L, B, H, T, D] tensors from DynamicCache."""
        keys = torch.stack([layer.keys for layer in cache.layers])
        values = torch.stack([layer.values for layer in cache.layers])
        return keys, values

    @staticmethod
    def _tensors_to_cache(keys: Tensor, values: Tensor):
        """Build DynamicCache from [L, B, H, T, D] tensors."""
        cache = DynamicCache()
        cache.layers = []
        for i in range(keys.shape[0]):
            layer = DynamicLayer()
            layer.keys = keys[i].contiguous()
            layer.values = values[i].contiguous()
            layer.dtype = keys.dtype
            layer.device = keys.device
            layer.is_initialized = True
            cache.layers.append(layer)
        return cache

    @staticmethod
    def _clone_cache(cache):
        """Deep-clone a DynamicCache."""
        new = DynamicCache()
        new.layers = []
        for layer in cache.layers:
            new_layer = DynamicLayer()
            new_layer.keys = layer.keys.clone()
            new_layer.values = layer.values.clone()
            new_layer.dtype = layer.dtype
            new_layer.device = layer.device
            new_layer.is_initialized = True
            new.layers.append(new_layer)
        return new
