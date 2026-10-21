# check exp 022 results locate

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_022_results_locate_20260516T183626_result.json`
- **Structured JSON:** [`3ae8ea24d0bf1e437ec4.json`](../../sessions/3a/3ae8ea24d0bf1e437ec4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 12 combinations complete. Here's the full cross-scorer matrix:

## Exp-022 Cross-Scorer Matrix — 完成度：12/12 (100%)

**Generators:** pythia_greedy, qwen_base, qwen_cont256  
**Scorers:** olmo, pythia, qwen_base, qwen_instruct

### Results (K* = max depth where adjacent AUC > 0.60)

| Generator | Scorer | K* | 0v1 | 1v2 | 2v3 | 3v4 | 4v5 |
|-----------|--------|-----|------|------|------|------|------|
| pythia_greedy | olmo | 2 | 0.9975 | 0.8811 | 0.5231 | 0.5233 | 0.5093 |
| pythia_greedy | pythia | 2 | 0.9992 | 0.8838 | 0.5342 | 0.5228 | 0.5162 |
| pythia_greedy | qwen_base | 2 | 0.9977 | 0.8814 | 0.5378 | 0.5135 | 0.5161 |
| pythia_greedy | qwen_instruct | 2 | 0.9977 | 0.8818 | 0.5260 | 0.5147 | 0.5031 |
| qwen_base | olmo | 2 | 0.9597 | 0.6047 | 0.5414 | 0.5345 | 0.5091 |
| qwen_base | pythia | 2 | 0.9619 | 0.6170 | 0.5396 | 0.5173 | 0.5184 |
| qwen_base | qwen_base | 2 | 0.9870 | 0.6262 | 0.5496 | 0.5294 | 0.5182 |
| qwen_base | qwen_instruct | 2 | 0.9863 | 0.6273 | 0.5519 | 0.5370 | 0.5157 |
| qwen_cont256 | olmo | 2 | 0.9792 | 0.6028 | 0.5242 | 0.5200 | 0.5026 |
| qwen_cont256 | pythia | **1** | 0.9888 | 0.5979 | 0.5234 | 0.5213 | 0.5104 |
| qwen_cont256 | qwen_base | 2 | 0.9914 | 0.6282 | 0.5556 | 0.5298 | 0.5137 |
| qwen_cont256 | qwen_instruct | 2 | 0.9912 | 0.6072 | 0.5553 | 0.5304 | 0.5190 |

### Key observations

1. **K\* = 2 for 11/12 combinations** — scorer choice barely matters; the signal saturates at depth 2 regardless of which model scores.
2. **唯一例外：qwen_cont256 × pythia (K\*=1)** — 1v2 AUC=0.5979 刚好低于 0.60 阈值（边界情况）。
3. **pythia_greedy 生成的数据最易区分** — 1v2 AUC ≈ 0.88（远高于其他 generator 的 ~0.60-0.63），说明 pythia 生成文本的 depth 信号更强烈。
4. **qwen_base/qwen_cont256 作为 generator 时 1v2 在 0.60 附近挣扎** — 仅勉强过线，cross-scorer 对此影响极小。
5. **无缺失组合** — 3×4 矩阵全部完成，`qwen_cont__scored_by__qwen_base` 目录为空残留文件。

---
