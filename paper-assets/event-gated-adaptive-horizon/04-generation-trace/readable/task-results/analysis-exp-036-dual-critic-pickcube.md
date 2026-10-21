# analysis exp 036 dual critic pickcube

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_036_dual_critic_pickcube_20260521T193939_result.json`
- **Structured JSON:** [`a01e9a6cc12aaa9f6db0.json`](../../sessions/a0/a01e9a6cc12aaa9f6db0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## 结果总结

**exp_036_dual_critic_pickcube: NEGATIVE**

| 指标 | 值 |
|------|-----|
| Final eval_return | 27.7 |
| Peak ve_ratio (NVE) | 2.3 @ 32.5K |
| CIVO alerts | 0 |
| v1-v2 divergence | 0 (完全一致) |

**核心发现：CIVO 在 PickCube 上根本不会发生。** ve_ratio 在早期短暂升至 2.3 后自行修正，无论有无 dual-critic。这使得该实验对 intervention hierarchy 假说无法提供证据。

**跨环境 pattern 更新：**
- **Walker**: Dual-critic 完全预防 CIVO (NVE ≤ 1.1, eval 787.7)
- **Cheetah**: Dual-critic 部分缓解 CIVO (NVE 1.8, eval 97.5)
- **PickCube**: Dual-critic 无关 (CIVO 不发生, eval 27.7 ≈ baseline 26.6)

**额外发现**：subsample+dt_emb 配置本身严重损害 PickCube 性能（vanilla baseline 58.6 → CIVO config 26.6），这不是 CIVO 造成的，而是配置对操作任务不适用。Dual-critic 和 TCN 都无法恢复这个差距。

Registry 已更新为 DONE(negative)，报告已注册为 artifact。

---
