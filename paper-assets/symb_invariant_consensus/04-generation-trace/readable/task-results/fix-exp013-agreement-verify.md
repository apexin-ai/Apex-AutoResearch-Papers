# fix exp013 agreement verify

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp013-agreement-verify_20260517T183035_result.json`
- **Structured JSON:** [`7ba85f1f9cbb7216840d.json`](../../sessions/7b/7ba85f1f9cbb7216840d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果出来了。所有 ablation_results.json 的数字与 recomputation 完全吻合。

## 结论

**Registry 的 `agreement_802_of_804` 是错误的。** 没有任何一对方法的 agreement 是 802。

完整 pairwise agreement matrix（804 题）：

| Method A | vs Method B | Agree | Disagree | A wins | B wins | Both wrong diff |
|---|---|---|---|---|---|---|
| MaxSAT | Count-only | **803** | 1 | 0 | 1 | 0 |
| MaxSAT | Random-wt | **785** | 19 | 10 | 5 | 4 |
| MaxSAT | SC | **773** | 31 | 16 | 14 | 1 |
| Count-only | Random-wt | **786** | 18 | 10 | 4 | 4 |
| Count-only | SC | **774** | 30 | 16 | 13 | 1 |
| Random-wt | SC | **764** | 40 | 17 | 20 | 3 |

各方法 accuracy：MaxSAT 76.49% (615), Count-only 76.62% (616), Random-wt 75.87% (610), SC 76.24% (613)

三项 cross-check 与 ablation_results.json 完全一致（803, 785, 774）。MaxSAT vs SC = 773/804 是新计算的（ablation 原始 JSON 未包含此对）。

结果已写入 `/root/symb_invariant_consensus/analysis/exp013_agreement_matrix.json`。

---
