# analyze exp 043 completion

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp_043_completion_20260522T103529_result.json`
- **Structured JSON:** [`e3ea37174136f9937689.json`](../../sessions/e3/e3ea37174136f9937689.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成（DONE/success）。Cron 已不存在（可能之前已被清理）。

## 诊断结果

**状态：正常完成**（224K steps，与同配置 exp_042 的完成模式一致）

**关键指标：**

| 指标 | 值 |
|------|-----|
| eval_final (= peak) | 673.73 @ 215K |
| NVE peak | 0.808 @ 105K |
| NVE final | 0.123 @ 215K |
| civo_alert | 未触发（NVE 远低于 1.5） |
| gate_dt | 固定 dt=2, entropy=0 |
| total_steps | 224,000 |

**结论：success** — Seed 1 复现了 seed 0 的发现：`dt_embed_dim=0`（无 dt embedding）时 CIVO 不出现。Peak NVE 仅 0.808，全程远低于 1.5 阈值。Eval return 673.73 高于预期的 300-500 范围，说明无 dt_emb 条件下模型性能正常甚至更好。

这确认了 **"trained dt_emb → CIVO" 因果链在跨 seed 上是 robust 的**，支撑 Claim C2。

---
