# check westd32570 full status

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd32570_full_status_20260521T104440_result.json`
- **Structured JSON:** [`520ffb2761d747065ceb.json`](../../sessions/52/520ffb2761d747065ceb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-32570 全面状态报告

---

### 1. exp-002 进度

**主进程 PID 133392**: 存活，运行 `run_exp002_full.sh`

**full_run.log 内容**:
```
=== exp-002 full run start: Thu May 21 17:08:46 CST 2026 ===
PIDs: qwen=133428 llama=133429 gemma=133431 mistral=133433
GPU0 qwen FAILED
```

**各 jsonl 文件记录数**:

| 文件 | 行数 | 状态 |
|------|------|------|
| qwen_mmlu.jsonl | 57,600 | ✅ 完成 |
| qwen_arc.jsonl | 57,600 | ✅ 完成 |
| qwen_hellaswag.jsonl | 57,600 | ✅ 完成 |
| llama_mmlu.jsonl | 57,600 | ✅ 完成 |
| llama_arc.jsonl | 57,600 | ✅ 完成 |
| llama_hellaswag.jsonl | 57,600 | ✅ 完成 |
| llama_gsm8k.jsonl | 10,400 | 🔄 运行中 |
| gemma_mmlu.jsonl | 57,600 | ✅ 完成 |
| gemma_arc.jsonl | 57,600 | ✅ 完成 |
| gemma_hellaswag.jsonl | 55,400 | 🔄 运行中 |
| mistral_mmlu.jsonl | 57,600 | ✅ 完成 |
| mistral_arc.jsonl | 57,600 | ✅ 完成 |
| mistral_hellaswag.jsonl | 57,600 | ✅ 完成 |
| mistral_gsm8k.jsonl | 4,600 | 🔄 运行中 |
| **总计** | **704,000** | |

**GPU0 (qwen)** — mmlu/arc/hellaswag 全完成。gsm8k **崩溃**，SyntaxError:
```
File "/root/nlp_variance_gtheory/src/inference/benchmark_utils.py", line 439
    m = 
        ^
SyntaxError: invalid syntax
```
qwen_gsm8k 未产出任何 jsonl。GPU0 已释放（0% 利用率，0 MiB 显存）。

**GPU1 (llama)** — mmlu/arc/hellaswag 完成，gsm8k 运行中。最新日志显示 condition ~1492，10,400 行已写入。

**GPU2 (gemma)** — mmlu/arc 完成，hellaswag 运行中。最新日志显示 condition ~3445 (152/200 correct)，55,400 行已写入（接近 57,600 完成线）。gsm8k 尚未开始。

**GPU3 (mistral)** — mmlu/arc/hellaswag 完成，gsm8k 运行中。最新日志显示 condition ~3767 (94/200 correct)，4,600 行已写入。

**预计剩余**：gemma 的 hellaswag 即将完成后会进入 gsm8k；llama 和 mistral 的 gsm8k 仍在跑。但 gsm8k 会在所有 GPU 上遇到同一个 SyntaxError（`benchmark_utils.py:439`），需要立即修复。

---

### 2. GPU 利用率

| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| 0 | NVIDIA RTX PRO 6000 Blackwell | **0%** | **0 MiB** / 97,887 MiB |
| 1 | NVIDIA RTX PRO 6000 Blackwell | 68% | 87,795 MiB / 97,887 MiB |
| 2 | NVIDIA RTX PRO 6000 Blackwell | 96% | 88,461 MiB / 97,887 MiB |
| 3 | NVIDIA RTX PRO 6000 Blackwell | 97% | 88,685 MiB / 97,887 MiB |

GPU 1/2/3 被 exp-002 占用。GPU0 空闲（qwen gsm8k 崩溃后释放）。

---

### 3. 模型下载进度

所有下载通过 ModelScope，目标目录在 `/root/autodl-tmp/.hf_cache/` 下。

| 模型 | PID | 当前文件 | 进度 | 速度 | 磁盘占用 |
|------|-----|---------|------|------|---------|
| InternLM2.5-7B-Chat | 149391 (存活) | model-00005-of-00008.safetensors | 46% (860M/1.84G) | 783 kB/s | 32K (待归档) |
| DeepSeek-LLM-7B-Chat | 149538 (存活) | pytorch_model-00001-of-00002.bin | 9% (841M/9.28G) | 793 kB/s | 4.5M |
| Yi-1.5-9B-Chat | 运行中 | model-00004-of-00004.safetensors (最后一片) | 39% (1.01G/2.59G) | 391 kB/s | 4.6M |
| OLMo-2-1124-7B-Instruct | 运行中 | model-00002-of-00003.safetensors | 18% (860M/4.64G) | 426 kB/s | 9.4M |

磁盘占用小是因为 ModelScope 下载到临时目录，完成后才移入最终路径。下载速度约 400-800 kB/s，所有模型预计还需数小时。

---

### 4. 磁盘空间

| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| 根分区 (/) | 30G | 17G | 14G | 57% |
| 数据盘 (/root/autodl-tmp) | 350G | 115G | 236G | 33% |

数据盘空间充足。

---

### 5. exp002 分析脚本

`/root/nlp_variance_gtheory/scripts/exp002_analysis/` 下 6 个脚本已就绪：

| 脚本 | 大小 |
|------|------|
| per_benchmark_gstudy.py | 10,865 B |
| gradient_permutation_test.py | 10,580 B |
| within_format_gradient.py | 10,215 B |
| leave_one_benchmark_out.py | 8,430 B |
| cross_benchmark_dstudy.py | 7,923 B |
| gsm8k_answer_reextract.py | 6,900 B |

---

### 关键问题

**`benchmark_utils.py:439` 有 SyntaxError** — `m = ` 后面缺表达式。这已经导致 qwen_gsm8k 崩溃，gemma/llama/mistral 到 gsm8k 阶段也会遇到同样的错误。需要立即修复此文件并重跑 gsm8k。

---
