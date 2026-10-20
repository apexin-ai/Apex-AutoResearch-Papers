# deploy exp 047 completion and exp 051

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_exp_047_completion_and_exp_051_20260522T184320_result.json`
- **Structured JSON:** [`ab5442e9bd9c4a9fbf65.json`](../../sessions/ab/ab5442e9bd9c4a9fbf65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务完成。

---

## 任务 1: exp_047 完成分析

**状态**: DONE (success) — PID 282452 已退出，训练跑到 ~225K steps

| 指标 | 值 |
|------|-----|
| eval_peak | **408.79** @ 125K |
| eval_final | 144.22 @ 215K |
| ve_ratio_peak | 1.099 @ 75K |
| ve_ratio_final | 0.277 @ 215K |
| NVE_peak (≥35K) | **1.71x @ 95K** |
| NVE @ 105K | 0.56x (自修正) |

**NVE 轨迹** (normalized by Walker baseline ve_ratio):
- 35K: 0.78x → 45K: 1.06x → 55K: 1.12x → 65K: 0.83x → **75K: 1.53x** → 85K: 1.29x → **95K: 1.71x** → 105K: 0.56x

**需注意**: NVE 在 75K-95K 短暂超过 1.5x 阈值（与 exp_042 s0 不同），但 105K 完全自修正。这是 "transient spike with self-correction" 模式，类似 exp_009b。末期 eval 下降 (408→144) 发生在 ve_ratio=0.28 的低位，确认非 CIVO。

**vs exp_042 (s0)**: s0 的 NVE=0.19 全程安全，s1 出现了瞬时 spike。frozen dt_emb 没有完全消除瞬时过估，但保障了系统的自修正能力，阻止了持续性 collapse。

## 任务 2: exp_051 部署

**状态**: RUNNING — PID 305974, GPU 1 (2526 MiB)
- 首次 eval @ 2500 steps: eval_return=2.0（StackCube 正常起点）
- Log: `logdir/exp_051_stackcube_frozen_dt_emb_s0.log`
- Registry: RUNNING, hypothesis/parent/spec 已设置

**GPU 分布**:
- GPU 0: exp_050 (PID 304736, PegInsertion, 2575 MiB) + exp_051 EGL 渲染溢出 (435 MiB)
- GPU 1: exp_051 (PID 305974, StackCube, 2526 MiB)

---
