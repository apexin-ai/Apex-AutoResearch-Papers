# analyze exp 045 completion

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp_045_completion_20260522T153910_result.json`
- **Structured JSON:** [`6e59b2f2ffdeae29afc3.json`](../../sessions/6e/6e59b2f2ffdeae29afc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。Cron 不存在（可能已在之前的 session 中删除）。

---

## exp_045_treatment_extension_008d_s3 诊断报告

### 最终状态：正常完成 ✓
训练跑到 312K steps（超过 300K 目标），最后一次 eval 在 302K，无报错。Checkpoint 保存于 `checkpoint_302000.pt`。

### CIVO 时间线：**Self-Corrected**

| Step | ve_ratio | eval_return | 阶段 |
|-----:|--------:|----------:|------|
| 112K | — | 58.5 | 恢复后重新收集数据 |
| 122K | **4.77** | 41.8 | CIVO 继承自 parent |
| 132K | **4.91** | 35.1 | ve_ratio 峰值，eval 谷底 |
| 142K | 0.43 | 350.2 | **急剧自纠正**（Δ = -4.48） |
| 152K | 0.21 | 646.4 | 快速恢复 |
| 162K | 0.25 | 482.3 | 小幅波动 |
| 172K | 0.18 | 600.4 | 持续下降 |
| 182K | 0.16 | 600.5 | |
| 192K | 0.13 | 699.5 | |
| 202K | 0.12 | 684.3 | |
| 212K | 0.10 | 758.6 | |
| 222K | 0.10 | 744.6 | 进入稳态 |
| 232K | 0.09 | 745.4 | |
| 242K | 0.07 | **869.7** | eval 峰值 |
| 252K | 0.08 | 721.6 | |
| 262K | 0.07 | 820.6 | |
| 272K | 0.08 | 716.2 | |
| 282K | 0.07 | 755.6 | |
| 292K | 0.06 | 843.0 | |
| 302K | **0.05** | **867.6** | 终态 |

### 关键数值
- **eval_final**: 867.6 | **eval_peak**: 869.7 (242K)
- **nve_peak**: 4.91 (132K) → **nve_final**: 0.052 (302K) — **99% 降幅**
- **civo_alerts**: 0（全程无触发）
- **自纠正拐点**: 142K（恢复后仅 30K steps）

### Conclusion: **success**

CIVO 在 extension 中完全 self-corrected。Parent exp_008d 在 112K 时 NVE=1.53（确认 CIVO），恢复后 ve_ratio 短暂升至 4.91（132K），但在 142K 即发生剧烈自纠正（降至 0.43），之后单调下降至 0.05。Eval 同步恢复，从 35→868，最终接近峰值。这否定了原假设（CIVO 会持续或恶化），表明在该配置下 CIVO 是**暂态现象**，agent 有内在的自纠正能力。

---
