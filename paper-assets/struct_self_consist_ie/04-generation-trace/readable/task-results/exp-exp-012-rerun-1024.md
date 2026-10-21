# exp exp 012 rerun 1024

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_exp_012_rerun_1024_20260514T221211_result.json`
- **Structured JSON:** [`8141f7b6538f0937c516.json`](../../sessions/81/8141f7b6538f0937c516.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 信号分析完成。结果：

| Signal | exp_012 (512) ρ | Rerun (1024) ρ | Δ |
|--------|----------------|----------------|-------|
| SJ | 0.357 | 0.360 | +0.003 |
| FK | 0.265 | 0.267 | +0.001 |
| EM | 0.257 | 0.295 | +0.038 |
| Voting | 0.502 | 0.379 | **-0.123** |
| Logprob | 0.140 | 0.205 | **+0.066** |

关键发现：
- **SJ / FK 几乎不变**（Δ < 0.01）：结构一致性信号在 max_tokens=512 vs 1024 下非常稳定
- **Logprob 大幅提升**（+0.066）：max_tokens=1024 避免了截断导致的 logprob 失真
- **EM 提升**（+0.038）：更完整的输出使精确匹配率更有区分度
- **Voting confidence 大幅下降**（-0.123）：这是最大变化。max_tokens=512 截断输出导致实体偏少，人为压高了 voting confidence 的一致性（少实体 → 更容易投票一致），从而虚高了 voting_conf 的 ρ

比较 JSON 已保存到 `output/exp_012_rerun_1024/comparison.json`。

---
