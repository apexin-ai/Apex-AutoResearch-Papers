# ssh check experiment progress

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_experiment_progress_20260514T194229_result.json`
- **Structured JSON:** [`8f12926c84730ebcf9f1.json`](../../sessions/8f/8f12926c84730ebcf9f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| 实验ID | 当前阶段 | 进度 | 预估剩余时间 | GPU利用率 |
|--------|---------|------|-------------|----------|
| pythia_topk50_001 | Step 6: Generate depth-3 | depth_3.jsonl 908K/~9M (~10%) | ~50-60 min | GPU 0: 67%, 13.7GB, 52°C |
| gpt2xl_temp09_001 | Step 2: Generate depth-1 | depth_1.jsonl 8.9M (接近完成或刚完成) | ~3-3.5 hr | GPU 1: 53%, 15.7GB, 47°C |

**详细状态：**

**pythia_topk50_001** — 进展顺利，已完成 5/9 步：
- ✅ finetune d0 → generate d1 (8.9M) → finetune d1 (loss 1.44) → generate d2 (9.4M) → finetune d2 (loss 1.44)
- 🔄 generate d3 — 模型已加载，正在生成，当前 908K
- ⬜ feature extraction → classification → eval
- 参考：每层生成约 30 min，finetune 约 6 min
- 注意：原 PID 165810 已退出，当前由子进程 PID 184981 (ppid=165799) 驱动

**gpt2xl_temp09_001** — 进度较慢（GPT-2 XL 推理速度 ~1.33 it/s vs Pythia ~3.52 it/s）：
- ✅ finetune d0 (loss 2.55, 耗时 705s — Pythia 的 2 倍)
- 🔄 generate d1 — depth_1.jsonl 已达 8.9M，可能即将完成
- ⬜ finetune d1 → generate d2 → finetune d2 → generate d3 → feature extraction → classification → eval
- GPT-2 XL 每层生成约 70-80 min，finetune 约 12 min
- PID 168793 存活（运行 1h15m）

---
