# code monitor all servers 20260519

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_monitor_all_servers_20260519_20260519T113443_result.json`
- **Structured JSON:** [`174c2d08478cbb9cbf9b.json`](../../sessions/17/174c2d08478cbb9cbf9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 全部实验状态汇总

---

### Server A (autodl-5090) — 32B QLoRA Training

| 项目 | 状态 |
|---|---|
| 进程 | **存活** — 主 PID 804438, GPU workers 804665-804668 |
| GPU | 4× RTX 5090, 利用率 87-100%, VRAM 27.5-29.9 GB/32.6 GB |
| 进度 | **step 2177 / 41180 (5.3%)** |
| 速度 | ~2.44 s/it |
| ETA | **~26h** |
| 最新 loss | **0.0663** (step 2150), grad_norm 0.557 |
| 备注 | checkpoint-2000 刚保存完成 (19:27) |
| 异常 | 无 |

---

### Server B (autodl-5090-b) — 72B Zero-shot Inference

| 项目 | 状态 |
|---|---|
| 进程 | **存活** — PID 59040, vLLM workers 59314-59317 |
| GPU | 4× RTX 5090, 全部 100%, VRAM ~31.9 GB/32.6 GB |
| 总进度 | **210,352 / 301,184 prompts (69.8%)** |
| 数据集明细 | SciERC ✅ 完成 (551 samples), CoNLL2003 ✅ 完成 (3,453 samples), **FewNERD 进行中 ~66%** (推算 33,644 samples, 已处理 ~22,290) |
| 速度 | ~17-33 it/s, input ~7.1K toks/s, output ~1.8K toks/s |
| ETA | **~1h15m** (剩余 90,832 prompts) |
| 异常 | 无 |

---

### Server C (autodl-5090-c) — 14B + 7B Training

**14B QLoRA (cuda:0,1, screen train_14b_s42)**

| 项目 | 状态 |
|---|---|
| 进程 | **存活** — screen PID 56766, 主进程 56773, workers 56978-56979 |
| GPU | GPU 0: 77%, 24.3 GB; GPU 1: 76%, 25.5 GB |
| 进度 | **step 4934 / 41,180 (12.0%)** |
| 速度 | ~2.10-2.30 s/it |
| ETA | **~22h** |
| 最新 loss | **0.067** (step 4900), grad_norm 0.300 |
| 备注 | checkpoint-4000 已保存 (19:01) |
| 异常 | 无 |

**7B QLoRA (cuda:2,3, nohup pipeline)**

| 项目 | 状态 |
|---|---|
| 进程 | **存活** — pipeline PID 71837, llamafactory-cli **PID 71844**, torchrun 71976, GPU workers 72042/72043 |
| GPU | GPU 2: 98%, 12.4 GB; GPU 3: 100%, 12.5 GB |
| 进度 | **step 138 / 20,590 (0.7%)** — 刚启动 ~6 分钟 (19:28) |
| 速度 | ~2.34 s/it |
| ETA | **~13.3h** |
| 最新 loss | 尚未到第一个 logging step |
| 异常 | 无 |

---

### 7B PID 汇总（用于 cron 注册）

- **Pipeline 脚本 PID: 71837** (`bash run_fewnerd_qwen25_7b_pipeline.sh`)
- **llamafactory-cli 主进程 PID: 71844**
- **torchrun PID: 71976**
- **GPU worker PIDs: 72042, 72043**

建议用 **71844** (llamafactory-cli train 进程) 监控训练阶段是否结束；如果 pipeline 含后续推理步骤，用 **71837** 监控整个 pipeline 完成。

---
