# analysis exp 008f final

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_008f_final_20260514T093146_result.json`
- **Structured JSON:** [`83a34bf5b2c8be3ad01c.json`](../../sessions/83/83a34bf5b2c8be3ad01c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**exp_008f 最终结论：SUCCESS**

关键数据点：
- eval_return 从 55K 低谷 173 恢复到 105K 的 503（V-shaped recovery）
- value_mean 在 85K 达峰 111.8 后自我修正至 98.2@105K
- normalized v/e 在 65K-105K 全程 < 0.7x（0.37→0.42→0.65→0.54→0.30），属于 **value suppression** 区间
- 与 008d 的核心差异：008d value 只会加速上升（69.3%@45K），008f value 会自我修正

**与 008d 的因果对比：**
- 008d（dt_embed_dim=32）：v/e 单调加速→ collapse
- 008f（dt_embed_dim=0）：v/e 先升后降→ self-correction → no collapse
- 唯一变量是 dt_embedding → **trained dt_embedding 是 delusional critic 的直接原因**

**全部 5 个析因实验完成**，因果链闭环：trained dt_embedding → value overestimation → actor exploitation → collapse。

---
