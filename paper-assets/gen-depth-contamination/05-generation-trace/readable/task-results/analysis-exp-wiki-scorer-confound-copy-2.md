# analysis exp wiki scorer confound

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_wiki_scorer_confound_20260517T231852_result.json`
- **Structured JSON:** [`a16a1c17fc7ec3748ddc.json`](../../sessions/a1/a16a1c17fc7ec3748ddc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**Scorer confound confirmed.** Pythia-1.4B scorer 下 K\*=1，Qwen-1.5B scorer 下 K\*=2。

### Pairwise AUC 对比

| Depth Pair | Qwen-1.5B Scorer | Pythia-1.4B Scorer | Delta |
|------------|------------------:|-------------------:|------:|
| 0 vs 1     | **0.9673**        | 0.9404             | -0.027 |
| **1 vs 2** | **0.6108**        | 0.5870             | -0.024 |
| 2 vs 3     | 0.5562            | 0.5456             | -0.011 |
| 3 vs 4     | 0.5297            | 0.5250             | -0.005 |
| 4 vs 5     | 0.5290            | 0.5172             | -0.012 |

关键：1v2 从 0.6108（刚过 θ=0.60）降到 0.5870（低于阈值），K\* 从 2 变为 1。

### 解读

- **depth 0v1 信号稳健**：两个 scorer 均 >0.94，K\*=1 不受 scorer 选择影响
- **depth 1v2 是 scorer artifact**：Qwen scorer 的 0.6108 仅超阈值 0.011，换成跨家族 scorer 后消失
- **AUC 全线下降**：Pythia scorer 在所有 depth pair 均低于 Qwen scorer，说明同家族 scorer 系统性膨胀区分度
- **对论文影响**：Qwen-7B Wikipedia 应报告 K\*=1（跨家族 scorer 结果），与其他模型一致。原始 K\*=2 需标注为 scorer confound

报告已写入 artifacts 并注册。

---
