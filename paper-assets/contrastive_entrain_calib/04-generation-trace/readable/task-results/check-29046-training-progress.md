# check 29046 training progress

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_29046-training-progress_20260520T022035_result.json`
- **Structured JSON:** [`129491e273112fac325c.json`](../../sessions/12/129491e273112fac325c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度报告

### exp-003 (GPU 1, PID 70649)
| 指标 | 值 |
|------|-----|
| 当前 step | **3760 / 8000 (47%)** |
| 已运行 | 1天9小时29分 (~33.5h) |
| 步速 | ~45-47s/step |
| 预计剩余 | ~55h |
| reward/r3_mean | 0.6972 (std=0.4051) |
| 最新 checkpoint | checkpoint-4000 (`/root/autodl-tmp/checkpoints/exp003_r3only_seed1/`) |
| 状态 | **健康** — CPU 596%, 持续出 step |

### exp-003-s2 (GPU 0, PID 237437 via bash→timeout)
| 指标 | 值 |
|------|-----|
| 当前 step | **136 / 8000 (2%)** |
| 已运行 | 2小时3分 |
| 步速 | ~55-70s/step（波动中，warmup 阶段） |
| 预计剩余 | ~120-140h |
| reward_mean | 0.47-0.55 |
| checkpoint | 尚无（首个在 step 500） |
| 状态 | **健康** — CPU 426%, 持续出 step |

注意：s2 的 `completions/clipped_ratio=1.0`，所有生成都达到 max_length 256，terminated_length 全为 0 — 模型尚未学会终止生成。

### GPU 使用
| GPU | 型号 | 显存 | 利用率 |
|-----|------|------|--------|
| 0 | RTX PRO 6000 Blackwell | 76094 / 97887 MiB (78%) | 99% |
| 1 | RTX PRO 6000 Blackwell | 38161 / 97887 MiB (39%) | 83% |

---
