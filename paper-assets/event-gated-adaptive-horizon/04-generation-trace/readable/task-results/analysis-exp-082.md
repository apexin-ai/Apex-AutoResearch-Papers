# analysis exp 082

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_082_20260525T162510_result.json`
- **Structured JSON:** [`43d1533c41bf03d81ad8.json`](../../sessions/43/43d1533c41bf03d81ad8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

**exp_082_cheetah_no_dt_emb_s0 结果：success**

- **无 CIVO**：civo_alert 全程 0，ve_ratio 峰值 0.955（< 1.0，value 从未超过 eval）
- **eval_return**：峰值 239.3@45K，最终 83.2@105K（baseline 的 18.6%）
- **与 exp_078 因果对验证**：唯一变量 dt_embed_dim（082=0 vs 078=trained），在 45K-75K 关键窗口 ve_ratio 完全分叉（082: 0.10→0.31 vs 078: 0.30→2.32）
- **C2 因果链在 Cheetah 跨环境确认**：trained dt_emb → CIVO，与 Walker Walk (008f vs 008d) 结论一致

Registry 已更新为 DONE/success，报告已注册 (art_20260525_980cba)。

---
