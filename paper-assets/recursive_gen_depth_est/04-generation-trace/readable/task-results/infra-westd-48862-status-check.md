# infra westd 48862 status check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd-48862-status-check_20260519T174333_result.json`
- **Structured JSON:** [`e1ff35903af3fb9677e1.json`](../../sessions/e1/e1ff35903af3fb9677e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇报

### GPU 状态
| GPU | 型号 | 显存占用 | GPU-Util |
|-----|------|---------|----------|
| 0 | RTX PRO 6000 (96GB) | 5,683 / 97,887 MiB | 70% |
| 1 | RTX PRO 6000 (96GB) | 18,911 / 97,887 MiB | 49% |

---

### 1. binoculars_ordinal_baseline_001
- **状态**: **RUNNING**
- **PID 336524**: 存活，elapsed 10:16
- **GPU**: cuda:0, 5.7GB VRAM, 70% util
- **进度**: Cell 1/9 (`pythia_nucleus`), 1122/2500 batches (45%), ~6.3 it/s
- **ETA**: 当前 cell 剩余 ~3.6 min；总计 9 cells，假设每 cell 类似速度，**总剩余约 40-50 min**

### 2. detectgpt_ordinal_baseline_003
- **状态**: **RUNNING** (初始化阶段)
- **PID 336944**: 存活，elapsed 5:21
- **GPU**: cuda:1, 18.9GB VRAM, 49% util
- **进度**: 日志仅 3 行（T5 tokenizer 加载 + torch_dtype 警告），尚未开始 scoring 输出。模型加载中或开始首轮 perturbation 生成
- **ETA**: DetectGPT 需要生成扰动文本，比 binoculars 慢很多，预计 **2-4 小时**（取决于 perturbation 数量和 cell 数）

### 3. DeBERTa pilot 残留
- **PID 329839** (deberta gpt2xl): **DEAD** — 已清理
- **PID 329980** (deberta pythia): **DEAD** — 已清理

---
