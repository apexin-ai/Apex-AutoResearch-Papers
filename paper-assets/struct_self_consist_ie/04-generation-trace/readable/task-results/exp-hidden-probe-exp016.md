# exp hidden probe exp016

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_hidden_probe_exp016_20260518T113602_result.json`
- **Structured JSON:** [`af5e002e6518ad26bb63.json`](../../sessions/af/af5e002e6518ad26bb63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。结果如下：

## Hidden State Probe — exp_016 数据结果

**数据**: `exp_012_rerun_1024/samples_with_logprobs.jsonl` (551 instances → gold-filtered 529, 8 samples/instance)

| Method | Spearman ρ | Selection F1 | Gap Closure |
|--------|-----------|-------------|-------------|
| Greedy | — | 0.644 | — |
| LP (mean logprob) | 0.283 | 0.650 | 4.8% |
| Hidden Linear | 0.179±0.019 | 0.613±0.002 | -23.4% |
| Hidden MLP | 0.388±0.013 | 0.637±0.003 | -5.1% |
| Oracle | — | 0.776 | 100% |

### 与 exp_012 probe 对比

| | exp_012 (greedy=0.610) | exp_016 (greedy=0.644) |
|---|---|---|
| LP gap closure | -0.7% | **+4.8%** |
| MLP ρ | 0.454 | 0.388 |
| MLP gap closure | +15.6% | **-5.1%** |

### 关键发现

1. **Greedy F1=0.644** 与主表一致，数据源确认正确
2. **Hidden state probes 在 exp_016 数据上表现显著退化**：MLP 的 selection F1 (0.637) 低于 greedy (0.644)，gap closure 为负
3. **LP 反而成为最佳方法**：selection F1=0.650，gap closure=4.8%
4. **线性 probe 严重过拟合**：train loss=0.0005 vs val loss=0.697
5. MLP 过拟合可控（train=0.070, val=0.081, best epoch=15.4）

可能原因：rerun_1024 数据的样本分布与 exp_012_logprob 不同（更长的 max tokens），导致 hidden state 的质量信号结构改变。greedy baseline 已经较高（0.644 vs 0.610），留给 probe 改进的空间更小。

结果保存在：`output/hidden_state_probe_exp016/results.json`

---
