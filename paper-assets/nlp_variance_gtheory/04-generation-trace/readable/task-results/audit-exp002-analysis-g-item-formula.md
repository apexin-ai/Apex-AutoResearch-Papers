# audit exp002 analysis g item formula

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_exp002_analysis_g_item_formula_20260521T120118_result.json`
- **Structured JSON:** [`98e26d84e1ed428fee81.json`](../../sessions/98/98e26d84e1ed428fee81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。全部 6 个脚本已完整审查。

## 审计结果

| 脚本 | 有 G_item 计算 | 公式正确 | 备注 |
|------|:---:|:---:|------|
| `per_benchmark_gstudy.py` | ✓ | ✓ | `compute_g_item` (L105), `d_study_curve` (L135), `find_min_items_for_g` (L155) — 三处均正确 |
| `cross_benchmark_dstudy.py` | ✓ | ✓ | `compute_g_for_n_items` — 含 D-study 缩放 `n_actual/n_items`，正确 |
| `gradient_permutation_test.py` | ✗ | — | 仅使用 variance component 百分比 (item_id_pct)，无 G_item |
| `leave_one_benchmark_out.py` | ✗ | — | 仅使用 variance component 百分比，无 G_item |
| `within_format_gradient.py` | ✓ | ✓ | `compute_g_item` (L123) — 逻辑与 per_benchmark_gstudy.py 一致 |
| `gsm8k_answer_reextract.py` | ✗ | — | 纯答案提取脚本，无方差分解 |

## 公式验证细节

三个包含 G_item 的脚本均使用相同的正确模式：

```
tau = vc["item_id"]
delta = Σ(vc[facet:item_id] / n_levels[facet]) + vc["residual"] / Π(n_levels[f] for f in non_item)
G = tau / (tau + delta)
```

关键校验点：
- **只累加含 item_id 的交互项** — `if "item_id" not in facets_in: continue` ✓
- **除数取交互中非 item_id 的 facet 水平数之积** — `prod(n_levels[f] for f in other)` ✓
- **residual 除数取全部非 item_id facet 水平数之积** ✓
- **未使用 ICC (`vc['item_id'] / sum(vc.values())`)** ✓
- **未使用 SS 比例 (`item_id_pct / 100`)** ✓

**结论：6 个脚本全部通过审计，无需修复。**

---
