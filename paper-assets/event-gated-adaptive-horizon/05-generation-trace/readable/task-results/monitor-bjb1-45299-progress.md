# monitor bjb1 45299 progress

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_bjb1-45299-progress_20260519T202539_result.json`
- **Structured JSON:** [`803148b3f1672fb13035.json`](../../sessions/80/803148b3f1672fb13035.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-45299 Status

### GPU
| GPU | Model | Util | VRAM |
|-----|-------|------|------|
| 0 | RTX PRO 6000 Blackwell | 24% | 8,576 / 97,887 MiB |
| 1 | RTX PRO 6000 Blackwell | 78% | 7,525 / 97,887 MiB |

### tmux sessions
(tmux ls 被 ssh_read_only 拦截，无法执行。但 4 个实验的 metrics.jsonl 均在过去几分钟内有写入，确认全部活跃。)

---

### exp_001_baseline_s3_extended
- **Current step**: 492,000 / 505,000 (97.4%)
- **Status**: running (metrics.jsonl modified 04:27)
- **Latest eval_return**: **944.67** @490K
- ETA: 即将完成

### exp_001_baseline_s4_extended
- **Current step**: 444,000 / 505,000 (87.9%)
- **Status**: running (metrics.jsonl modified 04:23)
- **Latest eval_return**: **945.12** @442K

### exp_025_obs_sgs_walker_s3
- **Current step**: 88,000 / 210,000 (41.9%)
- **Status**: running
- **Latest eval_return**: 569.50 @85K
- **Latest value_mean**: 355.5 @85K
- **Latest ve_ratio**: **0.62** (= 355.5 / 569.5)
- **NVE status**: healthy ✓
- ve_ratio trajectory: 0.0→0.1→0.2→0.4→0.4→**0.6** — 平稳上升，远低于阈值

### exp_025_obs_sgs_walker_s4 [CIVO MONITORING]
- **Current step**: 68,000 / 210,000 (32.4%)
- **Status**: running，但**尚未产生 65K 之后的 eval checkpoint**
- **Latest eval_return**: 89.39 @65K
- **Latest value_mean**: 192.4 @65K
- **Latest ve_ratio**: **2.15** @65K

**ve_ratio trajectory (all checkpoints):**

| Step | ve_ratio | value_mean | eval_return | delta_ve |
|------|----------|------------|-------------|----------|
| 15K | 0.0 | 3.6 | 176.6 | 0.0 |
| 25K | 0.2 | 29.1 | 179.1 | +0.1 |
| 35K | 0.7 | ~73 | 100.3 | +0.6 |
| 45K | 0.7 | 114.4 | 170.8 | -0.0 |
| 55K | 1.3 | 158.8 | 122.9 | +0.6 |
| **65K** | **2.2** | **192.4** | **89.4** | **+0.9** |

**Assessment: full collapse**
- ve_ratio 单调递增 0.0→0.2→0.7→0.7→1.3→2.2，无任何 self-correction 迹象
- eval_return 持续恶化：179→100→171→123→89，呈下降锯齿
- value_mean 持续膨胀（192.4），与 eval_return（89.4）严重脱节
- delta_ve 加速（最近 +0.9），divergence 在扩大
- 下一个 eval checkpoint 在 75K，但 collapse 趋势明确

---
