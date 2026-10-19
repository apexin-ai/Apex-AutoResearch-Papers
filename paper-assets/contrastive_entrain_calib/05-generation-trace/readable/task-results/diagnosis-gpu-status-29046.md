# diagnosis gpu status 29046

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_gpu-status-29046_20260519T165907_result.json`
- **Structured JSON:** [`524882f8c60efea34c68.json`](../../sessions/52/524882f8c60efea34c68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 实时状态

| GPU | 型号 | 利用率 | 显存占用 | 进程 |
|-----|------|--------|----------|------|
| 0 | RTX PRO 6000 Blackwell Server Edition | **83%** | 66907 / 97887 MiB (68%) | PID 172844 — `run_exp002v2_dcgrpo_cosine.py` |
| 1 | RTX PRO 6000 Blackwell Server Edition | **95%** | 38161 / 97887 MiB (39%) | PID 70649 — `run_exp003_r3only.py` |

## 训练实验存活状态

| 实验 | 状态 | 说明 |
|------|------|------|
| exp002v2-recalib | **存活** | PID 172838（wrapper bash）→ PID 172844（python），tmux session `exp002v2-recalib` 正常 |
| exp-003 | **存活** | PID 70649（python），tmux session `exp003` 正常 |

## 空闲 GPU

**无空闲 GPU。** 两张卡均在高负载运行（83%、95%），各有训练进程占用。

---
