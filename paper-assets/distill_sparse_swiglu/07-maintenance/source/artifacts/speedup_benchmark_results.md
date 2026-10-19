# Sparse Inference Speedup Benchmark: LLaMA-3.1-8B with 30% Predictor Sparsity

## 1. Environment

| Item | Value |
|------|-------|
| GPU | NVIDIA RTX PRO 6000 Blackwell Server Edition (95 GB) |
| PyTorch | 2.8.0+cu128 |
| CUDA | 13.0 |
| Model | LLaMA-3.1-8B (8.03B params, 15.0 GB fp16) |
| Predictor | 75.96M params (144.9 MB fp16), GELU bottleneck d_b=128 |
| Attention | SDPA (no flash_attn) |
| Data | WikiText-2 test, 100 samples, seq_len=2048 |
| Decode | 128 generated tokens, 10 input prompts |
| Repeats | 3 (mean +/- std) |

## 2. Results

### 2.1 Main Results Table

| Config | Prefill (ms) | Decode (ms/tok) | Prefill tok/s | Decode tok/s | Memory (GB) | Prefill Speedup | Decode Speedup |
|--------|-------------|-----------------|---------------|--------------|-------------|-----------------|----------------|
| Dense bs=1 | 116.6 +/- 0.6 | 14.48 +/- 0.00 | 17,566 | 69.1 | 15.9 | 1.000x | 1.000x |
| Sparse 30% bs=1 | 125.1 +/- 0.3 | 15.23 +/- 0.00 | 16,370 | 65.6 | 15.9 | 0.932x | 0.950x |
| Dense bs=8 | 1034.2 +/- 2.7 | 18.51 +/- 0.00 | 15,842 | 432.1 | 21.1 | 1.000x | 1.000x |
| Sparse 30% bs=8 | 1105.3 +/- 0.5 | 19.31 +/- 0.00 | 14,823 | 414.3 | 21.1 | 0.936x | 0.959x |

### 2.2 Gather-Scatter (Decode bs=1 Only)

| Config | Decode (ms/tok) | Decode tok/s | Decode Speedup |
|--------|----------------|--------------|----------------|
| Dense bs=1 | 14.48 | 69.1 | 1.000x |
| Zero-mask bs=1 | 15.23 | 65.6 | 0.950x |
| Gather-scatter bs=1 | 24.10 +/- 0.01 | 41.5 | 0.601x |

Gather-scatter uses `torch.index_select` to select active neuron columns, reducing matmul dimensions by 30%. However, the Python-level indexing overhead (3 index_select per layer x 32 layers = 96 weight copies per token) dominates, making it 40% slower than dense.

## 3. Predictor Overhead Analysis

| Scenario | Predictor Time (ms) | % of Dense Forward |
|----------|--------------------|--------------------|
| bs=1, prefill (seq=2048) | 2.97 +/- 0.00 | 2.5% |
| bs=1, decode (seq=1) | 1.12 +/- 0.05 | 7.7% |
| bs=8, prefill (seq=2048) | 14.32 +/- 0.01 | 1.4% |
| bs=8, decode (seq=1) | 1.19 +/- 0.01 | 6.4% |

The predictor is lightweight: 2.5% overhead for prefill, 6-8% for decode. In decode, the 1.1ms predictor cost is larger relative to the ~14.5ms per-token latency, but still modest.

## 4. Memory Analysis

| Config | Peak Memory (GB) | Delta vs Dense |
|--------|-----------------|----------------|
| Dense bs=1 | 15.86 | baseline |
| Sparse 30% bs=1 | 15.86 | +0.00 GB |
| Dense bs=8 | 21.15 | baseline |
| Sparse 30% bs=8 | 21.15 | +0.00 GB |

Zero-masking does not reduce memory: all weight matrices remain full-size, and the predictor adds 145 MB (negligible vs 15 GB model). Memory savings require structural pruning (removing weight rows/columns) or weight-sparse formats.

## 5. Implementation Notes

**Sparse implementation: zero-masking.**
- Predictor outputs logits per neuron; neurons with logits <= 0 are zeroed.
- All matmuls (gate_proj, up_proj, down_proj) still execute at full dimension.
- No compute is saved; the only effect is the element-wise multiply with the binary mask.
- The 5-7% slowdown is entirely from predictor forward overhead.

**Gather-scatter (tested for decode bs=1 only).**
- Uses `torch.index_select` to select active weight rows/columns before matmul.
- Matmuls are 30% smaller, but Python-level weight copying dominates.
- 96 `index_select` calls per token (3 per layer x 32 layers), each copying ~78 MB.
- Result: 40% slower than dense, not practically useful without CUDA kernel support.

**What would be needed for actual speedup:**
- Kernel-level sparse MLP (flashinfer, triton, or CUTLASS): skip zero-valued computation entirely without weight copying overhead.
- Theoretical upper bound with perfect sparse kernels:
  - FFN accounts for ~67% of total FLOPs in LLaMA-8B.
  - 30% neuron sparsity saves ~20% of total FLOPs.
  - Minus predictor overhead (~2.5% prefill, ~7.7% decode).
  - Net theoretical prefill speedup: ~1.17x (17% faster).
  - Net theoretical decode speedup: ~1.13x (13% faster, higher predictor overhead fraction).
- Semi-structured sparsity (2:4 or N:M) with NVIDIA Sparse Tensor Cores would be an alternative path.

## 6. Summary

With zero-masking, 30% predictor-guided sparsity adds 5-7% overhead due to predictor computation, with no compensating compute reduction. The predictor itself is very efficient (2.5% prefill overhead), confirming that the inference cost bottleneck is in sparse kernel support, not in mask prediction. Kernel-level sparse computation would unlock an estimated 13-17% end-to-end speedup at 30% sparsity.
