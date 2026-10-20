# code gpu status and files check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gpu_status_and_files_check_20260518T105052_result.json`
- **Structured JSON:** [`8826854e32bdcbccb270.json`](../../sessions/88/8826854e32bdcbccb270.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### 1. GPU 状态

| 服务器 | GPU 0 | GPU 1 | 运行进程 |
|--------|-------|-------|----------|
| **westd-16980** | 空闲 (0 MiB, 0%) | 空闲 (0 MiB, 0%) | 无 |
| **westd-21461** | 空闲 (0 MiB, 0%) | 空闲 (0 MiB, 0%) | tmux 有 `mistral_v3_full` session 但 GPU 未占用（可能刚启动或已结束） |

### 2. V3 输出文件

| 服务器 | 文件 | 行数 |
|--------|------|------|
| **westd-16980** | `ee_mistral_wikievents_grammar_only_v3.jsonl` | 246 |
| | `ee_qwen_wikievents_constrained_v3_cf_voted.jsonl` | 246 |
| | `ee_qwen_wikievents_constrained_v3_full.jsonl` | 246 |
| | `ee_qwen_wikievents_constrained_v3_posthoc.jsonl` | 246 |
| **westd-21461** | `ee_llama_wikievents_constrained_v3_full.jsonl` | 246 |
| | `ee_llama_wikievents_constrained_v3_posthoc.jsonl` | 246 |
| | `ee_mistral_wikievents_constrained_v3_full.jsonl` | 246 |

### 3. Unconstrained post-hoc 文件（论文需要 3 个）

| 文件 | 位置 | 行数 |
|------|------|------|
| `ee_qwen_wikievents_unconstrained_posthoc.jsonl` | westd-16980 | 246 |
| `ee_llama_wikievents_unconstrained_posthoc.jsonl` | westd-16980 | 246 |
| `ee_mistral_wikievents_unconstrained_posthoc.jsonl` | westd-21461 | 246 |

**3 个文件齐全，分布在两台服务器上。**

### 4. 70B AWQ 下载进度

下载**正在进行**（tmux session `model_download` 活跃），文件在临时目录 `._____temp/` 中：
- 9 个 safetensors 分片，当前正在并行下载
- 进度约 **24%–38%**（各分片 1.1G–1.7G / 3.1G–4.6G）
- 已跑 ~17 分钟，预计还需 **15–40 分钟**完成
- 下载完成后会从 `._____temp/` 移至正式目录

### 5. 磁盘空间

| 服务器 | 挂载点 | 已用 | 可用 |
|--------|--------|------|------|
| **westd-16980** | `/` (30G) | 27G | 3.7G (88%) |
| **westd-21461** | `/` (30G) | 17G | 14G (56%) |
| **westd-21461** | `/root/autodl-tmp` (250G) | 64G | 187G (26%) |

westd-16980 根分区偏满（88%），注意别再往 `/root` 写大文件。westd-21461 空间充裕，70B 模型（~36G）下载完后 autodl-tmp 仍有 ~150G 余量。

---
