# investigate gpu mystery processes

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_gpu-mystery-processes_20260519T115140_result.json`
- **Structured JSON:** [`23e00fe050f1fad12195.json`](../../sessions/23/23e00fe050f1fad12195.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。

---

## 调查报告

### westd-25068 — 4/4 GPU 占满 (96-97% util)

| GPU | 模型 | 端口 | 实验 | 状态 |
|-----|------|------|------|------|
| 0 | Qwen2.5-7B-Instruct | 8010 | exp-065 (PW-600) | 运行中 |
| 1 | **Mistral-7B-Instruct-v0.3** | 8001 | **exp-069-mistral-logiqa200** | 运行中 (新!) |
| 2 | Qwen2.5-7B-Instruct | 8002 | exp-070 dry-run **已完成** | vLLM 空转，可复用 |
| 3 | gemma-3-27b-it | 8003 | exp-062 (Gemma-27B FOLIO, --resume) | 运行中 |

- 原报告称 cuda:1 "0% util 可能残留"——**现已被 exp-069 占用**，97% 利用率
- cuda:2 上 exp-070 dry-run 已完成（1.5 min），vLLM 仍在监听 8002，可直接启动 exp-070 正式运行
- 占用端口：8001, 8002, 8003, 8010
- 可用端口：8004-8009, 8011+
- 老 tmux 会话 `exp-027-qwen3-14b-non-thinking` 仍残留

### westd-16639 — 3/4 GPU, cuda:0 空闲

| GPU | 模型 | 端口 | 实验 | 状态 |
|-----|------|------|------|------|
| 0 | — | — | — | **空闲 (0MiB, 0%)** |
| 1 | **Qwen3-14B (non-thinking)** | 8001 | **exp-068-qwen3-logiqa200** | 运行中 |
| 2 | deepseek-r1-0528-qwen3-8b | 8002 | exp-064 (DeepSeek-R1 FOLIO) | 运行中 |
| 3 | Meta-Llama-3.1-8B-Instruct | 8003 | exp-048 (LLaMA-8B PW-600) | 运行中 |

- cuda:1 的不明进程：**就是 exp-068**
- 占用端口：8001, 8002, 8003
- 可用端口：8004+，cuda:0 完全空闲
- 老 tmux 会话 `exp032` 残留

### exp-068 状态

**在 westd-16639 cuda:1 上正常运行。** Qwen3-14B (non-thinking mode) 通过 vLLM 端口 8001 提供服务，`run_logiqa.py` 于 19:13 启动，日志持续输出 HTTP 200，结果文件 126KB 持续增长。Registry 标记 RUNNING 是正确的。

### 可用资源汇总

| 资源 | 位置 |
|------|------|
| 空闲 GPU | westd-16639 cuda:0 |
| 空闲 vLLM (可复用) | westd-25068 cuda:2 (Qwen2.5-7B, port 8002) |
| 可用端口 (25068) | 8004-8009, 8011+ |
| 可用端口 (16639) | 8004+ |

---
