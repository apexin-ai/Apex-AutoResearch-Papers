# infra westd41312 status check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd41312_status_check_20260520T062401_result.json`
- **Structured JSON:** [`bce34b44528956ba8a1e.json`](../../sessions/bc/bce34b44528956ba8a1e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. cuda:3 进程

| 项目 | 值 |
|------|-----|
| PID | 427903 |
| 命令 | `python eval_perplexity.py --checkpoints .../detect_remove_q03_seed42_r2/final --data_path .../eval_wikipedia.jsonl --max_docs 5000 --output_path .../detect_remove_q03_seed42_r2_ood_wikipedia.json` |
| 启动时间 | 14:22:38 |
| 运行时长 | 1分48秒 |
| 显存占用 | 7614 MiB / 97887 MiB |

这是 **detect_remove_q03_seed42_r2** 模型在 Wikipedia OOD 数据上的 perplexity 评估任务。

### 2. rho06 三组训练进度

| Seed | 当前 step | 进度 | step 速度 | 已运行 | 预估剩余 |
|------|-----------|------|-----------|--------|----------|
| 42 | 4698/6103 | 77% | ~2.23 s/step | 2h52m | ~52 min |
| 123 | 4696/6103 | 77% | ~2.19 s/step | 2h52m | ~51 min |
| 456 | 4715/6103 | 77% | ~2.22 s/step | 2h52m | ~51 min |

三组进度基本同步，预计约 **51-52 分钟后**（~15:16 左右）全部完成。

### 3. 四卡 GPU 状态

| GPU | 利用率 | 显存占用 | 温度 | 功耗 |
|-----|--------|----------|------|------|
| 0 | 100% | 45643 / 97887 MiB (47%) | 63°C | 297W/600W |
| 1 | 100% | 45643 / 97887 MiB (47%) | 62°C | 356W/600W |
| 2 | 95% | 45643 / 97887 MiB (47%) | 63°C | 410W/600W |
| 3 | 95% | 7623 / 97887 MiB (8%) | 68°C | 400W/600W |

GPU 0-2 跑 rho06 三组训练（每卡各一个 seed），GPU 3 跑 perplexity 评估。全部 RTX PRO 6000 Blackwell (96GB)，温度和功耗正常。

---
