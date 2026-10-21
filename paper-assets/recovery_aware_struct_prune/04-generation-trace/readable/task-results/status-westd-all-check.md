# status westd all check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_westd-all-check_20260515T170419_result.json`
- **Structured JSON:** [`20f197728908d671a3da.json`](../../sessions/20/20f197728908d671a3da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-11672 实验状态

| # | 实验 | 状态 | 结果/进度 |
|---|------|------|-----------|
| 1 | GraSP baseline eval (PID 38120) | **Done** | accuracy=**7%** (7/100), eos_rate=0.02 (98%截断) |
| 2 | GraSP post-SFT eval | **Done** | accuracy=**41%** (41/100), eos_rate=0.98 |
| 3 | RASP SFT retrain (PID 48946) | **Running** cuda:0 | 102/1870 steps (5.5%), ~1.1 it/s, loss 1.87→1.03, ETA ~27min |
| 4 | Standard SFT retrain (PID 49645) | **Running** cuda:1 | 刚启动，正在加载模型到 GPU（GPU 1 尚未分配显存） |

注意：Standard SFT 的 PID 是 49645（非原 49032），看起来是重新启动的。

### GPU & 磁盘

| GPU | Util | VRAM |
|-----|------|------|
| cuda:0 | 44% | 50.5 / 95.6 GB |
| cuda:1 | 0% | 0 / 95.6 GB (模型加载中) |

| 分区 | 用量 | 剩余 |
|------|------|------|
| / (root) | 16% | 26 GB |
| /root/autodl-tmp | 82% | 46 GB |

### 关键发现
- GraSP 剪枝后未 SFT：7% accuracy，几乎丧失能力（98%输出截断，无法正常终止生成）
- GraSP 剪枝后 SFT 恢复到 41%，eos 恢复正常（98% natural EOS）
- 两个 SFT retrain 正在并行跑，预计 RASP 约 27min 后完成，Standard 还在加载模型

---
