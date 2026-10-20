# ops bjb1 40020 snapshot and deploy 029c

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1_40020_snapshot_and_deploy_029c_20260520T111733_result.json`
- **Structured JSON:** [`5cfa811a7ea2bcd25f21.json`](../../sessions/5c/5cfa811a7ea2bcd25f21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。进程仍在运行，不部署 exp_029c。

---

## 汇总报告

### 1. exp_027_tcn_walker_s0_sigma02 (σ=0.2 s0) — 判定完成

| 指标 | 值 |
|------|-----|
| PID 37863 | **仍在运行** (7h29m)，但最后 eval step = 205K ≥ 205K 阈值 |
| eval_return @205K | **558.7** |
| ve_ratio @205K | **0.0995** |
| peak eval_return | **821.1** @175K |
| 后期均值 (175-205K) | **627.1** |
| NVE 趋势 | 95K 处 spike 到 0.908 后持续下降，155K 后稳定 < 0.11 |

Registry 已更新为 **DONE/success**。CIVO 抑制有效：后半程 NVE 全程 < 0.22，eval 达到 baseline 水平。

### 2. exp_029c_tcn_walker_s0_sigma01 — 未部署

PID 37863 仍在 cuda:0 上运行（约剩 5K steps ≈ 10 分钟）。按规则等进程退出后再部署。

### 3. exp_029a_tcn_walker_s1_sigma02 (σ=0.2 s1) 最新 metrics

| step | eval_return | ve_ratio |
|------|------------|----------|
| 55K | 133.9 | 0.643 |
| 65K | 169.7 | 0.478 |
| 75K | **171.2** | **0.398** |

s1 seed 在 75K 步，ve_ratio 仍较高（0.40 vs s0 同期 0.61），eval_return 偏低。需要观察后续是否收敛。

---
