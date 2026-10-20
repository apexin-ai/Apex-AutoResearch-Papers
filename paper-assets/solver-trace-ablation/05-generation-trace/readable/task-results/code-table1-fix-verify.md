# code table1 fix verify

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_table1-fix-verify_20260514T084159_result.json`
- **Structured JSON:** [`2df57b2689b1472046a1.json`](../../sessions/2d/2df57b2689b1472046a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。汇总结果：

---

### 验证结果

| 项目 | 值 | 说明 |
|------|-----|------|
| **plan002-b03 proved_only_mean_isr** | **0.1427** | Table 1 当前写 0.026（那是 mean_isr），应改为 0.1427 |
| **plan002-b03 eval 文件路径** | `/root/solver-trace-ablation/outputs/eval_sta_plan002_additive_b03.json` | 在项目代码目录下，不在 `/root/autodl-tmp/outputs/` |
| **plan001-s42 component_count_mean** | **eval 文件中无此字段** | 文件中只有每个 proved 样本的 `details.n_components`。93 个 proved 样本的 n_components 均值 = **7.08**（非 6.58） |
| **plan001-s42 eval 文件路径** | `/root/autodl-tmp/outputs/eval_sta_plan001_r2.json` | summary.model_path 确认指向 `plan001_exec_only_s42` |

### 补充说明

- **plan002-b03 JSON summary 关键字段**：mean_isr=0.0257, proved_only_mean_isr=0.1427, prove_rate=0.18, n_proved=18/100
- **plan001-s42 component_count 差异**：n_components 包含 premise + conclusion 部分。如果只算 premise（减去 conclusion_whole/conclusion_quantifier），均值会更低，可能接近 6.58，但 eval 文件本身没有这个聚合字段，需要确认 Table 1 中 6.58 的计算口径。

---
