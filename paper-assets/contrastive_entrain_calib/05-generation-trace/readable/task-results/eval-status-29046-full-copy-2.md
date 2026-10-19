# eval status 29046 full

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_status-29046-full_20260522T133709_result.json`
- **Structured JSON:** [`f2f312ff62f473fa675c.json`](../../sessions/f2/f2f312ff62f473fa675c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 状态
| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| GPU 0 | 98% | 38,049 / 97,887 MiB |
| GPU 1 | 98% | 46,548 / 97,887 MiB |

两卡满载运行。

---

### exp-003-s2 (R3-only seed2)
- **当前进度**: step **7737/8000** (96.7%)
- **速度**: ~25.5s/step
- **剩余**: 263 steps × 25.5s ≈ **1h52m**
- **预计完成**: 约 **5/22 23:30** (北京时间)
- **Checkpoint**: 最新 **checkpoint-7500** (19:55 产出)，ckpt-8000 尚未产出，预计训练结束时生成

---

### exp-004-s2-v2 (ACT baseline s2)
- **当前进度**: step **2470/8000** (30.9%)
- **速度**: ~91s/10steps → 9.1s/step
- **剩余**: 5530 steps × 9.1s ≈ **14h**
- **预计完成**: 约 **5/23 11:30** (北京时间)
- **Loss**: sft loss 已降至 ~0.0000，total loss 稳定在 ~0.0003 (l2 主导)
- **Checkpoint**: checkpoint-2000, checkpoint-3000 已产出，output_dir 在数据盘 ✓

---

### 磁盘
| 分区 | 容量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / (根) | 30G | 24G | 6.9G | 78% |
| /root/autodl-tmp (数据盘) | 250G | 59G | 192G | 24% |

数据盘充裕。根分区 78% 偏高但 exp-003 的 checkpoint 和 exp-004 的 output 都在数据盘，暂无风险。

---
