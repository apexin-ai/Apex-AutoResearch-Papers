# check phase2 progress and prep continuation

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_phase2-progress-and-prep-continuation_20260527T055635_result.json`
- **Structured JSON:** [`15fa2caee2a4f5a162d7.json`](../../sessions/15/15fa2caee2a4f5a162d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 1. Phase 2 进度

| 实验 | PID | 状态 | 运行时间 | 当前 step | eval_return | ve_ratio | civo/alert |
|------|-----|------|---------|-----------|-------------|----------|------------|
| trained_s0 | 604513 | 运行中 | 2h58m | 108K (eval@105K) | **3.26** (↓ from peak 8.01@85K) | 0.897 | **1.0** |
| frozen_s0 | 612905 | 运行中 | 5m54s | 5K | 0.038 | — | — |

**trained_s0 eval_return 轨迹**: 0.04 → 0.09 → 0 → 0.33 → 0.51 → 0.24 → 0 → 0.55 → **8.01**(85K) → 5.00 → **3.26**(105K)

确认 delayed CIVO 模式：85K 峰值后 eval_return 持续下降，ve_ratio=0.897 尚未突破 tau=1.5，civo/alert 已在 105K 触发。value_mean=2.93 处于增长中。

**frozen_s0** 刚启动 ~6 分钟，仅到 5K step，预计需 ~5-6 小时完成 150K。

## 2. 续跑脚本

两个脚本已创建并 `chmod +x`：

| 脚本 | 路径 | 行数 |
|------|------|------|
| trained_s0 | `/root/autodl-tmp/event-gated-adaptive-horizon/run_hopper_trained_s0_extend.sh` | 25 |
| trained_s1 | `/root/autodl-tmp/event-gated-adaptive-horizon/run_hopper_trained_s1_extend.sh` | 25 |

内容验证通过：`--steps 150000`，原始 logdir，seed 分别为 0/1，无 `--dt_emb_freeze`。待 Phase 2 当前实验结束后可直接用这两个脚本续跑。

---
