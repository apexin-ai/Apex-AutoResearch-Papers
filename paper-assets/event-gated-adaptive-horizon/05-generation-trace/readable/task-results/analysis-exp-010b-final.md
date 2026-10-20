# analysis exp 010b final

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_010b_final_20260516T161303_result.json`
- **Structured JSON:** [`27df041414f6007c6f15.json`](../../sessions/27/27df041414f6007c6f15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。总结：

**exp_010b_cheetah_civo_trigger — DONE / success**

| 指标 | 值 |
|------|-----|
| Peak eval return | 321.89 @ 45K |
| Final eval return | 51.72 @ 105K |
| Last-5 eval mean | 75.73 |
| NVE peak | **14.59×** @ 65K |
| Collapse onset | ~55K steps |
| Total steps | 112K |
| Train return (final) | 23.2 |
| Checkpoint | `logdir/exp_010b_cheetah_civo_trigger/latest.pt` |
| W&B | 无 |

**结论：CIVO 跨环境验证成功。** Walker 上 008d 配置（trained dt_emb + subsample ON + dt=2 + H=8）在 Cheetah Run 上同样触发严重 CIVO collapse（NVE 14.59× >> 1.5× 阈值）。Baseline (010a) 在相同 105K 步时 eval=420.68 且持续上升至 849.8，而 010b 在 45K 达峰后崩溃至 22-52 区间。可回应 reviewer "single environment" concern。

---
