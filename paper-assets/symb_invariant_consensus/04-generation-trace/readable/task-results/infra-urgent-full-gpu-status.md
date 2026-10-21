# infra urgent full gpu status

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_urgent-full-gpu-status_20260522T141914_result.json`
- **Structured JSON:** [`0929dde2661b7f69cf0d.json`](../../sessions/09/0929dde2661b7f69cf0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 综合状态报告

### 1. GPU 状态 (westd-16639) — 全部满载运行，非空闲

| GPU | 显存占用 | 利用率 | VLLM PID | 运行时长 |
|-----|---------|--------|----------|---------|
| 0 | 90159/97887 MiB | 97% | 551459 | 6h47m |
| 1 | 88263/97887 MiB | 96% | 595559 | 3h13m |
| 2 | 90213/97887 MiB | 97% | 510289 | 10h50m |
| 3 | 88263/97887 MiB | 96% | 613436 | 58m |

所有 4 个主进程 PID (552333, 596151, 510987, 614142) 均存活。

---

### 2. 已完成实验结果

#### Qwen2.5-7B FOLIO (3/3 seeds 完成)

| Seed | SICA | SC | Δ(SICA-SC) |
|------|------|----|------------|
| 123 | 73.04% | 74.51% | -1.47% |
| 456 | 74.02% | 74.02% | 0.00% |
| 789 | 72.55% | 74.02% | -1.47% |
| **均值** | **73.20%** | **74.18%** | **-0.98%** |

#### Mistral-7B FOLIO (3/3 seeds 完成)

| Seed | SICA | SC | Δ(SICA-SC) |
|------|------|----|------------|
| 123 | 63.73% | 67.16% | -3.43% |
| 456 | 57.84% | 57.84% | 0.00% |
| 789 | 56.86% | 59.31% | -2.45% |
| **均值** | **59.48%** | **61.44%** | **-1.96%** |

#### LLaMA-8B FOLIO (1/3 seeds 完成)

| Seed | SICA | SC | Δ(SICA-SC) |
|------|------|----|------------|
| 123 | 73.04% | 74.51% | -1.47% |

#### Mistral-7B PW (2/4 seeds 完成)

| Seed | SICA | SC | Δ(SICA-SC) |
|------|------|----|------------|
| 42 | 36.67% | 40.00% | -3.33% |
| 123 | 37.50% | 40.83% | -3.33% |
| **均值** | **37.09%** | **40.42%** | **-3.33%** |

---

### 3. 正在运行的实验

| GPU | 实验 | 当前 Seed | 进度 | ETA |
|-----|------|----------|------|-----|
| 0 | Qwen2.5 PW | 123 | 356/600 (59%) | ~280 min (~4.7h) |
| 1 | LLaMA FOLIO | 456 | 125/204 (61%) | ~47 min |
| 2 | Mistral PW | 456 | 111/600 (19%) | ~247 min (~4.1h) |
| 3 | LLaMA PW | 42 | 60/600 (10%) | ~528 min (~8.8h) |

#### 待运行队列
- **GPU 0**: seed 456, 789 待运行
- **GPU 1**: seed 789 待运行
- **GPU 2**: seed 789 待运行
- **GPU 3**: seed 123, 456 待运行

---

### 4. DeBERTa 脚本
- `finetune_deberta_pw.py` — **存在**
- `eval_finetuned_nli.py` — **存在**

---

### 5. westd-25068
**认证失败**，无法连接。可能需要检查 SSH key 配置或实例状态。

---
