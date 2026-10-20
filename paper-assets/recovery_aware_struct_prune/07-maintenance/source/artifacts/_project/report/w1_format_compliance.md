# W1 Format Compliance Analysis (2026-05-22)

## 7B 模型 · 20% 剪枝率（主实验）

| Method | N | Accuracy | EOS Rate | Avg Len | Boxed Rate |
|--------|-----|----------|----------|---------|------------|
| **Dense (unpruned)** | 1319 | 90.83% | 98.71% | 594.0 | 0.00% |
| CKA-only SFT | 1319 | 63.91% | 99.01% | 198.1 | 0.00% |
| CKA-only GRPO | 1319 | 64.37% | 99.24% | 190.5 | 0.00% |
| Standard SFT | 1319 | 59.21% | 98.48% | 206.7 | 0.08% (1) |
| Standard GRPO | 1319 | 59.44% | 98.03% | 227.1 | 0.23% (3) |
| RASP SFT | 1319 | 61.49% | 98.26% | 216.5 | 0.00% |
| RASP GRPO | 1319 | 60.88% | 98.79% | 195.7 | 0.00% |
| Unstructured GRPO | 1319 | 87.64% | 98.18% | 600.0 | 0.08% (1) |

## 7B · 15% 剪枝率

| Method | N | Accuracy | EOS Rate | Avg Len | Boxed Rate |
|--------|-----|----------|----------|---------|------------|
| CKA-only SFT | 1319 | 72.18% | 99.01% | 200.3 | 0.00% |
| CKA-only GRPO (v2) | 1319 | 73.09% | 98.94% | 202.4 | 0.00% |
| Standard SFT | 1319 | 66.49% | 99.32% | 183.4 | 0.08% (1) |
| Standard GRPO (v2) | 1319 | 66.11% | 99.32% | 184.5 | 0.08% (1) |

## 1.5B 模型 · 20% 剪枝率

| Method | N | Accuracy | EOS Rate | Avg Len | Boxed Rate |
|--------|-----|----------|----------|---------|------------|
| CKA-only SFT | 1319 | 35.63% | 95.07% | 336.8 | 0.00% |
| CKA-only GRPO | 1319 | 35.48% | 94.69% | 349.5 | 0.00% |
| Standard SFT | 1319 | 22.90% | 90.45% | 516.7 | 0.00% |
| Standard GRPO | 1319 | 22.29% | 90.52% | 514.8 | 0.08% (1) |
| RASP SFT | 1319 | 26.91% | 94.16% | 378.6 | 0.00% |
| RASP GRPO | 1319 | 26.16% | 93.78% | 392.7 | 0.00% |

## Key Findings

1. **Boxed rate ~0% for ALL methods including dense** — not discriminative for this model family
2. **EOS rate 98-99%+ for all 7B methods** — pruning does NOT degrade format compliance
3. **1.5B**: CKA-only EOS (~95%) > Standard (~90%) — CKA-aware pruning better preserves generation structure at smaller scale
4. **Avg length**: pruned models shorter (~200 vs ~594 tokens) — SFT/GRPO trains concise answers, not format degradation
5. **No Random / Depth-first eval files available yet**
