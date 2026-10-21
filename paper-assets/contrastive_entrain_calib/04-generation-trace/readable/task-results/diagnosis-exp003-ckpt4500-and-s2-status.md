# diagnosis exp003 ckpt4500 and s2 status

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_exp003-ckpt4500-and-s2-status_20260520T175244_result.json`
- **Structured JSON:** [`1b26968ed1b96ece040f.json`](../../sessions/1b/1b26968ed1b96ece040f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 28034 eval 状态总览

### exp-003 (原始) 已完成的 eval

| Checkpoint | ToF | NoF | SYCONScore | 状态 |
|------------|-----|-----|------------|------|
| ckpt-1000 | 0.0387 | 0.9448 | 0.0743 | ✅ 完成 |
| ckpt-2000 | 0.0442 | 0.9834 | 0.0846 | ✅ 完成 |
| ckpt-3000 | 0.0497 | 0.9724 | 0.0946 | ✅ 完成 |
| ckpt-4000 | 0.0608 | 0.9669 | 0.1144 | ✅ 完成 |
| ckpt-4500 | — | — | — | 🔄 刚启动（加载完模型，0/362） |
| ckpt-5000 | 0.0608 | 0.9669 | 0.1144 | ✅ 完成 |
| ckpt-5500 | 0.0608 | 0.9724 | 0.1144 | ✅ 完成 |

SYCONScore 从 ckpt-1000 到 ckpt-4000 稳步上升（0.0743→0.1144），ckpt-4000/5000/5500 plateau 在 0.1144。

### exp-003-s2 eval

| Checkpoint | 进度 | GPU | 状态 |
|------------|------|-----|------|
| ckpt-500 | 220/362 (61%) | GPU 1 | 🔄 运行中 |
| ckpt-1000 | 220/362 (61%) | GPU 2 | 🔄 运行中 |
| ckpt-1500 | 220/362 (61%) | GPU 3 | 🔄 运行中 |

预计 ~30-40 分钟内完成（基于已有进度速率）。

### GPU 状态

| GPU | 显存占用 | 利用率 | 任务 |
|-----|---------|--------|------|
| 0 | 16.8/32.6 GB | 48% | exp-003 ckpt-4500 eval |
| 1 | 16.9/32.6 GB | 46% | exp-003-s2 ckpt-500 eval |
| 2 | 16.9/32.6 GB | 44% | exp-003-s2 ckpt-1000 eval |
| 3 | 16.9/32.6 GB | 49% | exp-003-s2 ckpt-1500 eval |

**四卡全满，无空闲 GPU。** s2 eval 预计半小时后释放 GPU 1/2/3；ckpt-4500 eval 预计 ~75 分钟完成。

注：checkpoint-3500 在 28034 上不存在，只有 checkpoint-4500。

---
