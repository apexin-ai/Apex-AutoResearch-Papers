# ssh dgec vc 8b qwen3 ft

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_dgec-vc-8b-qwen3-ft_20260520T085503_result.json`
- **Structured JSON:** [`88666bd2fa4cd4c1203d.json`](../../sessions/88/88666bd2fa4cd4c1203d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总结果：

## VC-weighted construction — Qwen3-8B FT (9 configs)

| Dataset | Seed | Greedy | VC F1 | Δ (pp) | p | LP Δ (pp) |
|---------|------|--------|-------|--------|---|-----------|
| FewNERD | 42 | 0.748 | 0.745 | **-0.30** | 0.997 | +0.88 |
| FewNERD | 123 | 0.748 | 0.757 | **+0.91** | 0.000** | — |
| FewNERD | 456 | 0.749 | 0.755 | **+0.59** | 0.000** | — |
| SciERC | 42 | 0.644 | 0.658 | **+1.40** | 0.017* | +0.61 |
| SciERC | 123 | 0.646 | 0.655 | +0.96 | 0.087 | — |
| SciERC | 456 | 0.648 | 0.641 | -0.65 | 0.834 | — |
| CoNLL | 42 | 0.908 | 0.904 | -0.38 | 0.955 | -1.05 |
| CoNLL | 123 | 0.908 | 0.908 | +0.07 | 0.384 | — |
| CoNLL | 456 | 0.907 | 0.902 | **-0.54** | 0.998 | — |

## SJ two-tier construction — Qwen3-8B FT (9 configs, 补跑)

| Dataset | Mean Δ (pp) | Pattern |
|---------|------------|---------|
| FewNERD | **-1.48** | 全部 3 seeds 显著负 (p=1.0) |
| SciERC | **-0.40** | mixed, 无显著正 |
| CoNLL | **-0.50** | 全部负 |

**核心发现**：
- VC 在 SciERC seed42 上表现优于 LP（+1.40pp vs +0.61pp），但 cross-seed 方差大
- VC 在 FewNERD 上 seed-dependent：seed42 负，seed123/456 显著正
- SJ 在 Qwen3-8B FT 上几乎全面失效（8/9 负），与 Qwen2.5-7B FT 一致
- CoNLL 高 degeneracy（~60%）导致 VC/SJ 均无效

产出已注册：`vc_8b_qwen3_ft_results` (art_20260520_f90ace), `sj_8b_qwen3_ft_results` (art_20260520_ca7b5c)

---
