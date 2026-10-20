# ssh urgent 5task autodl check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_5task_autodl_check_20260522T160913_result.json`
- **Structured JSON:** [`dbf6a3b64d68bf623694.json`](../../sessions/db/dbf6a3b64d68bf623694.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## autodl-8gpu 状态报告

### 1. EXP-003（最高优先级）

**状态：🔄 仍在运行，无错误**

- **进程**：仍在执行（GPU 0 活跃，log 持续输出）
- **错误**：grep "error" / "traceback" 均为 0 匹配，运行正常
- **Results 目录**：空——尚未产出任何结果文件

**MCMC 进度**（从 run.log 尾部）：

| 阶段 | 状态 |
|------|------|
| STEP 1: 数据加载 | ✅ 完成 — 9 judges, 176 items, 5661 obs, win rate=0.599, exposure mean=0.206 |
| STEP 2: `raw_average` | ✅ 完成 (0.0s) |
| STEP 2: `mfrm_only` chain 1 | ✅ 完成 (6000/6000, 74s, acc.prob=0.95) |
| STEP 2: `mfrm_only` chain 2+ | 🔄 ~15% warmup (912/6000), ~7 it/s |

当前瓶颈：第二条链收敛较慢（step size ~0.008），后面可能还有 `gated_mfrm` 等更大模型要拟合。**预计还需较长时间。**

**数据摘要**（已加载）：

| Examinee model | Win rate | n |
|---|---|---|
| gpt-4o | 0.864 | 705 |
| qwen2.5-72b | 0.822 | 706 |
| gpt-4o-mini | 0.807 | 685 |
| llama-3.3-70b | 0.724 | 671 |
| qwen3-8b | 0.664 | 599 |
| gemma-2-9b | 0.510 | 674 |
| gpt-4-0613 | 0.341 | 774 |
| gpt-3.5-turbo-0125 | 0.183 | 847 |

---

### 2. GPU 状态

| GPU | Util | VRAM Used | VRAM Total |
|-----|------|-----------|------------|
| 0 | **78%** | 731 MiB | 97887 MiB |
| 1 | 0% | 0 MiB | 97887 MiB |
| 2 | 0% | 0 MiB | 97887 MiB |
| 3 | 0% | 0 MiB | 97887 MiB |

仅 GPU 0 在跑 exp-003 MCMC（CPU-bound PyTorch，VRAM 占用低）。

---

### 3. 模型下载

| Model | 状态 |
|-------|------|
| Qwen3-8B | ✅ 5/5 shards |
| gemma-2-9b-it | ✅ 4/4 shards |
| Llama-3.1-8B-Instruct | ✅ 4/4 shards |
| Mistral-7B-Instruct-v0.3 | ⚠️ 2/3 done, 1 shard 仍在 `._____temp/` |

---

### 4. Response 文件

13 个 response JSONL 已就绪：claude-opus-4.7, gpt-3.5-turbo-0125, gpt-4-0314, gpt-4-0613, gpt-4o, gpt-4o-mini, gpt-5.5, llama-3.3-70b, mistral-large-2, qwen2.5-72b, gemma-2-9b, qwen3-8b, llama-3.1-8b

---

**结论**：exp-003 正常运行中，无报错，但 MCMC 采样仍在 `mfrm_only` 第二条链的 warmup 阶段（15%），results.json 尚未生成。Mistral 模型下载未完成（1 shard 卡在 temp）。

---
