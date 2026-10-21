# analysis openvla attention entropy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_openvla_attention_entropy_20260518T003400_result.json`
- **Structured JSON:** [`2e96b12be9d344335fea.json`](../../sessions/2e/2e96b12be9d344335fea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果非常清晰，强力支持论文 hypothesis：

**OpenVLA attention entropy ratio: 0.617 vs SmolVLA: 0.98**

关键发现：

| 指标 | SmolVLA (0.5B) | OpenVLA (7B) |
|------|---------------|-------------|
| Entropy ratio | 0.98 (近均匀) | **0.617** (集中) |
| 含义 | 所有 vision tokens 被等权关注 | 明确区分重要/不重要 token |
| k=0.5 pruning | 0% SR (灾难性) | 37.4% SR (优雅退化) |

层级趋势也很有说服力：
- **浅层** (0-1): ratio ~0.96-0.99 (接近均匀，尚未分化)
- **中层** (6-11): ratio ~0.75-0.85 (开始集中)
- **深层** (17-30): ratio **0.37-0.53** (高度集中)

这解释了为什么 OpenVLA 能承受 pruning：深层已经学会了高度选择性的 attention pattern，pruning 掉低 attention 的 token 对模型决策影响小。而 SmolVLA 的 0.98 near-uniform pattern 意味着每个 token 同等重要，随机移除任何 token 都会造成等量信息损失。

结果已保存到 `artifacts/openvla_attention_entropy.json`。

---
