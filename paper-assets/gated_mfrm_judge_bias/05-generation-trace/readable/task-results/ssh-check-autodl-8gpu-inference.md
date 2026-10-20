# ssh check autodl 8gpu inference

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_autodl_8gpu_inference_20260522T103649_result.json`
- **Structured JSON:** [`2399767b6dda5003227b.json`](../../sessions/23/2399767b6dda5003227b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

## 推理状态

| 模型 | 状态 | 详情 |
|------|------|------|
| **Llama-3.3-70B** (judge) | **已完成** | `arena_hard_judgments.jsonl` 296 条结果，时间戳 10:05-10:06 |
| **gemma-2-9b-it** | **下载中 (~74%)** | 3/4 个 safetensors shard 各下载到 74%，速度 ~870KB/s，预计还需 ~24 min |
| **Qwen2.5-7B-Instruct** | **未开始下载权重** | 仅有 tokenizer/config (12MB)，权重 safetensors 未下载 |
| **Mistral-7B-Instruct-v0.3** | **排队中** | 锁文件已创建，等 Qwen 下载完才开始 |
| **Llama-3.1-8B-Instruct** | **排队中** | 在第一个 ModelScope 下载脚本中，排在 gemma 后面 |
| **Qwen3-8B** | **已完成下载** | 5/5 safetensors 已就绪 (16GB under `/root/autodl-tmp/models/Qwen/Qwen3-8B/`) |

## 推理进度

所有小模型的批推理 **均未开始**。Orchestrator tmux session 在等 gemma-2-9b-it 权重下载完毕后才会启动推理。

## GPU 使用

| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| 0-3 | RTX PRO 6000 Blackwell (98GB) | 0% | 0 MiB / 97887 MiB |

4 张卡全部空闲，无推理进程运行。

## 磁盘

| 分区 | 已用 | 可用 | 占比 |
|------|------|------|------|
| / (30G) | 14G | 17G | 46% |
| /root/autodl-tmp (250G) | 101G | 150G | 41% |

磁盘空间充足。

**瓶颈**：ModelScope 下载速度极慢（~870KB/s），gemma-2-9b-it 还需 ~24 分钟，之后 Llama-3.1-8B、Qwen2.5-7B、Mistral-7B 还要依次下载。按当前速度，全部模型下载完可能还需 2-3 小时。

---
