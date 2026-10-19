# ssh training progress check d026

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_training_progress_check_d026_20260514T053459_result.json`
- **Structured JSON:** [`4da616ad8aff1e60e031.json`](../../sessions/4d/4da616ad8aff1e60e031.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度报告

### 1. 当前 Step & 预估完成时间

| 模型 | 当前 Step | 总 Steps | 进度 | Epoch | 预估剩余 |
|------|----------|----------|------|-------|---------|
| **Qwen** (cuda:0) | ~2950 | 4242 | **69.5%** | 3/3 开始 | ~4-5h |
| **StarCoder** (cuda:1) | ~2000 | 4242 | **47.1%** | 2/3 中段 | ~8-9h |

- Qwen 已运行 11h56m，平均 ~247 steps/h → 剩余 ~1292 steps ≈ **5.2h**
- StarCoder 已运行 11h05m，平均 ~180 steps/h → 剩余 ~2242 steps ≈ **12.5h**（更慢，可能 eval 占时更多）

等下，StarCoder 的 step 我再确认一下——日志显示 step 2000 但让我确认是否有更新的。

实际上从 StarCoder 日志尾部看到 step 2000 是最新的（`tail -20` 结果），而 Qwen 实际日志在 `/root/runs/m2_full_qwen/random_s42.log`，最新是 step 2950。

修正估算：
- **Qwen**: 2950/4242 = 69.5%，运行 11h56m → ~247 steps/h → 剩余 1292 steps ≈ **~5.2h**（约 18:30 CST 完成）
- **StarCoder**: 2000/4242 = 47.1%，运行 11h05m → ~180 steps/h → 剩余 2242 steps ≈ **~12.5h**（约明天 01:30 CST 完成）

### 2. GPU 状态

| GPU | 利用率 | 显存占用 | 温度 |
|-----|--------|---------|------|
| cuda:0 (Qwen) | **100%** | 51.6 / 97.9 GB | 71°C |
| cuda:1 (StarCoder) | **100%** | 55.2 / 97.9 GB | 72°C |

两块 GPU 满载运行，温度正常。

### 3. 进程状态

| 模型 | PID | 运行时间 | 状态 |
|------|-----|---------|------|
| Qwen | 73558 | 11h55m52s | **Sl** (正常) |
| StarCoder | 76627 | 11h05m13s | **Rl** (正常运行中) |

### 4. Eval 指标趋势

**Qwen** (best @ step 1000):
| Step | val_loss | R@1 | R@5 |
|------|---------|------|------|
| 500 | 0.4869 | 53.3% | 95.4% |
| **1000** | **0.4651** | **55.3%** | **95.9%** |
| 1500 | 0.5365 | 52.3% | 95.5% |
| 2000 | 0.5162 | 52.3% | 95.4% |
| 2500 | 0.5264 | 52.7% | 95.6% |

**StarCoder** (best @ step 1000):
| Step | val_loss | R@1 | R@5 |
|------|---------|------|------|
| 500 | 0.6194 | 43.5% | 90.5% |
| **1000** | **0.6134** | **45.4%** | **92.0%** |
| 1500 | 0.6528 | 44.9% | 90.6% |

两个模型都在 step 1000 后 val_loss 开始上升，有过拟合迹象。best checkpoint 应该都保存在 step 1000 附近。Qwen 的 R@1 (55.3%) 明显优于 StarCoder (45.4%)。

---
