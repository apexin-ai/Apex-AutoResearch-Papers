# code rerun perm granger diff

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rerun-perm-granger-diff_20260514T215438_result.json`
- **Structured JSON:** [`205ae65d8695ea5fd557.json`](../../sessions/20/205ae65d8695ea5fd557.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Summary

### T1: Permutation Granger 差分版对比

| Pair | Old (circular_shift) | Undiff (shuffle) | **Diff (shuffle)** |
|------|-----|------|------|
| token_entropy→distinct_1 | 4/4 SIG, F=200-500 | 4/4 SIG | **4/4 SIG, F=612-2615** |
| token_entropy→distinct_2 | 4/4 SIG | 4/4 SIG | **4/4 SIG, F=226-1798** |
| token_entropy→distinct_3 | 4/4 SIG | 4/4 SIG | **4/4 SIG, F=95-738** |
| token_entropy→perplexity | 3/4 SIG | 3/4 SIG | **0/4 n.s., F=0.0-0.3** |
| ece→distinct_1 | 4/4 SIG | 4/4 SIG | **4/4 SIG, F=567-6124** |
| ece→distinct_2 | 4/4 SIG | 4/4 SIG | **4/4 SIG, F=171-7643** |
| ece→distinct_3 | 4/4 SIG | 4/4 SIG | **4/4 SIG, F=71-921** |
| ece→perplexity | 4/4 SIG | 4/4 SIG | **0/4 n.s., F=0.0-0.6** |

**关键判断**：
- **canary→diversity 指标**（distinct_1/2/3）：差分后全部保持 4/4 显著，F 值甚至上升（非伪回归）。论文核心 claim **成立**。
- **canary→perplexity**：差分后全部 **不显著**（F 降至 ~0），旧结果完全由共享非平稳趋势驱动。论文中不应 claim canary 预测 perplexity。
- 结果已保存至 `results/mvp/analysis/permutation_granger.json`，包含 `differenced` 和 `undifferenced` 两组结果。

### T2: Effect Size 统一为 Cohen's f²

| 脚本 | 改动 |
|------|------|
| `method_ablation.py` | TY: `η² = F/(F+df)` → `f² = F/df`；分类阈值 (0.14/0.06/0.01) → (0.35/0.15/0.02)；字段 `effect_size_eta2` → `effect_size_f2` |
| `analyze_alpha_sweep.py` | TY: `η² = F*p/(F*p+df)` → `f² = F*p/df`；PermG: 去掉 f²→η² 转换，直接用 f²；同样改字段名和分类阈值 |
| `permutation_granger.py` | 已经用 `effect_size_f2`，无需修改 |

`method_ablation.json` 已用新 f² 重新生成。

---
