# analysis eval official smolvla prune k05 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_official_smolvla_prune_k05_v2_20260518T141029_result.json`
- **Structured JSON:** [`d3e701de39313bc060d7.json`](../../sessions/d3/d3e701de39313bc060d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## 实验总结

**实验**: `eval_official_smolvla_prune_k05_v2` — Official SmolVLA checkpoint + k=0.5 random pruning

**结果**: **0/500 (0.0% SR)**，95% Wilson CI [0.0%, 0.8%]。10 个 task 全部 0%。所有 episode 均 timeout（280 steps）。

**与 parent 对比**:
| 条件 | SR | 95% CI |
|---|---|---|
| Official baseline (无剪枝) | **59.2%** (296/500) | [54.8%, 63.4%] |
| Official + k=0.5 random prune | **0.0%** (0/500) | [0.0%, 0.8%] |

**Conclusion: success** — Hypothesis 验证通过。Official SmolVLA checkpoint 在 k=0.5 random pruning 下同样完全失效（0% SR），与我们 fine-tuned model 的行为一致。这确认了 **cliff-edge 是 pixel-shuffle 架构固有的**，而非 fine-tuning 引入的。即使 official checkpoint baseline 更高（59.2% vs 我们的 44.8%），剪枝后同样断崖式归零，说明 pixel-shuffle 产生的 vision token 之间存在强结构耦合，任何随机移除都会破坏空间编码的完整性。

---
