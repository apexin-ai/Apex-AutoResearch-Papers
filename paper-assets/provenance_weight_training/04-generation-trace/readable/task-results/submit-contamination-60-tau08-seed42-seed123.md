# submit contamination 60 tau08 seed42 seed123

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_contamination_60_tau08_seed42_seed123_20260520T093937_result.json`
- **Structured JSON:** [`d87e91452480ea399c28.json`](../../sessions/d8/d87e91452480ea399c28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

| 实验 | GPU | PID | 状态 | 参数 |
|------|-----|-----|------|------|
| `contamination_60_adaptive_seed42_tau08` | cuda:2 | 459319 | RUNNING | ρ=0.6, τ=0.8, seed=42, adaptive, 200M tokens |
| `contamination_60_adaptive_seed123_tau08` | cuda:3 | 459396 | RUNNING | ρ=0.6, τ=0.8, seed=123, adaptive, 200M tokens |

- 两个实验已正常出 training log，tau_batch=0.8 确认正确
- max_steps=6103，预估 ~5 小时完成
- Registry 已更新到 RUNNING，spec 含完整 provenance 元数据
- cuda:0/1 的 1.7B 训练未受影响

---
