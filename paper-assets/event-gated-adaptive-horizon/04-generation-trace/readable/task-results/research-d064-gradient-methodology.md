# research d064 gradient methodology

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_d064-gradient-methodology_20260516T172723_result.json`
- **Structured JSON:** [`a55511ee4cbd3627141a.json`](../../sessions/a5/a55511ee4cbd3627141a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

草稿已写入 `artifacts/paper_drafts/gradient_decomposition_methodology.md`。

内容包括：

1. **Methodology**: 基于 `torch.autograd.grad` + `retain_graph=True` 的 per-loss gradient isolation 方法，计算每个 loss 对 dt_embedding weight 的 Frobenius norm 贡献比例
2. **Single-checkpoint 结果**: 55K checkpoint 的 93/7/0 分布（来自 commit 5fc8e49 的已验证数据）
3. **Multi-checkpoint table 模板**: 008d 和 018v2 两张表，覆盖 25K/55K/75K/105K，55K 已填，其余标注 `[TODO: 需要从 logdir 提取]`
4. **因果推理链**: obs decoder gradient → trained dt_emb → reward bias during imagination → CIVO，以及为什么 016e (reward SGS) 是 architectural no-op 而 018v2 (Full-SGS) 有效
5. **Architectural pathway analysis**: 解释为什么 reward head 梯度为零的计算图原因
6. **Paper narrative implications**: 016e 作为 informative negative、Full-SGS 作为 proof-of-concept、inherent gate mechanism cost 量化

**需要后续补充的数据**：multi-checkpoint gradient norms（25K/75K/105K）需要从服务器 logdir 加载各 checkpoint 重跑 gradient 分析脚本提取。可复用 5fc8e49 的分析代码。

---
