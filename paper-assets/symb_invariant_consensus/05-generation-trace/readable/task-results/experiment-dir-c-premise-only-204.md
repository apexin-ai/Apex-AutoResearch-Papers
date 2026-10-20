# experiment dir c premise only 204

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_dir-c-premise-only-204_20260520T155358_result.json`
- **Structured JSON:** [`ac17afaf06927400de93.json`](../../sessions/ac/ac17afaf06927400de93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

| 方法 | Accuracy | N_correct/204 |
|---|---|---|
| SC Baseline | 54.41% | 111 |
| **Premise-Only SICA** | **56.86%** | **116** |
| SICA Original (参考) | 59.31% | 121 |

**关键指标：**
- Premise-only vs SC: +2.45%（discordant: SC+/PO- = 7, SC-/PO+ = 12）
- McNemar p = 0.359（不显著）
- Constraints 保留率: 76.89%（14084 → 10829，过滤掉 23.1%）

**解读：** 过滤掉引用结论的 constraints 后，SICA 仍高于 SC baseline 2.45 个百分点，但差异不显著（p=0.36）。相比原始 SICA 的 +4.9% 提升，premise-only 保留了约一半的增益，说明 premise-derived constraints 确实贡献了部分真实推理能力，但结论信号也有相当影响。

结果 JSON 已写入 `/root/symb_invariant_consensus/results/dir_c_premise_only_204/results.json`。

---
