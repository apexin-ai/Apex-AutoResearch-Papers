# experiment dir n oracle bestofk

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_dir-n-oracle-bestofk_20260520T181358_result.json`
- **Structured JSON:** [`8b376b761b2d29279ab2.json`](../../sessions/8b/8b376b761b2d29279ab2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果如下：

### Summary Table

| Model | SC@12 | Oracle@12 | Oracle Gap (pp) |
|---|---|---|---|
| Mistral-7B | 54.4% | 87.7% | **33.3** |
| Qwen3-14B non-thinking | 83.8% | 93.1% | **9.3** |
| Qwen3-14B thinking | 83.7% | 89.8% | **6.0** |

### Oracle Curve

| Model | K=1 | K=2 | K=3 | K=4 | K=6 | K=8 | K=12 |
|---|---|---|---|---|---|---|---|
| Mistral-7B | 46.8±2.4 | 61.8±2.3 | 70.1±2.1 | 75.0±1.9 | 80.5±1.5 | 83.7±1.4 | 87.7±0.0 |
| Qwen3-14B-NT | 79.6±1.8 | 86.3±1.4 | 88.9±1.0 | 90.3±0.9 | 91.5±0.7 | 92.2±0.6 | 93.1±0.0 |
| Qwen3-14B-T | 83.2±1.3 | 85.7±0.9 | 86.8±0.9 | 87.6±0.8 | 88.5±0.7 | 89.1±0.5 | 89.8±0.0 |

关键发现：
- **Mistral-7B 的 Oracle Gap 巨大（33.3pp）**：12 条 traces 中有正确答案但 SC majority vote 选不出来，说明弱模型的 aggregation 有很大提升空间
- **Qwen3-14B 的 Oracle Gap 较小（6-9pp）**：强模型大部分 traces 本身就对，Oracle ceiling 更低
- **exp028b 只有 166 题**（非完整 204 题），thinking 模式的 Oracle@1（83.2%）已接近 SC@12（83.7%），说明 thinking 单 trace 质量很高，diversity 反而低

结果已写入 `/root/symb_invariant_consensus/results/dir_n_oracle_bestofk/results.json`。

注：SC 计算值与存储值有微小差异（tie-breaking 逻辑不同），Oracle Gap 使用存储的 SC 值。

---
