# code urgent full status and v3 launch 16980

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_urgent_full_status_and_v3_launch_16980_20260518T070503_result.json`
- **Structured JSON:** [`8aaea0ebd81a40085424.json`](../../sessions/8a/8aaea0ebd81a40085424.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。状态报告：

---

### nvidia-smi
| GPU | 型号 | 显存 | 利用率 | PID |
|-----|------|------|--------|-----|
| 0 | RTX PRO 6000 Black | 22033/97887 MiB | 83% | 534706 |
| 1 | RTX PRO 6000 Black | 15069/97887 MiB | 85% | 536272 |

### 脚本参数（--help 确认）
- `--model_path`（非 --model）
- `--output_path`（非 --output_file）
- `--mode`（非 --task）
- `--dataset`, `--device`, `--max_new_tokens`, `--skip_on_error`, `--resume`

### 代码版本 ✓
- `type_mask_processor.py`: **938 行**
- `collision`: 7 处
- `exact_match`: 4 处

### 任务状态

| GPU | tmux session | 任务 | 进度 |
|-----|-------------|------|------|
| 0 | `qwen_v3_full` | Qwen3-8B wikievents full_s1 v3 | **31/246** (运行中) |
| 1 | `mistral_v3_full` | Mistral-7B-Instruct-v0.3 wikievents full_s1 v3 | **1/246** (刚启动) |

### Llama grammar_only
**246/246 — 已完成** ✓

### Mistral 缓存
`/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3-ms/mistralai/Mistral-7B-Instruct-v0___3/` — 3 个 safetensors 分片，完整可用。

### Qwen 模型
本地路径 `/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B`（Qwen3-8B，非 Qwen2.5-7B）

### 最终 GPU 分配
- **GPU 0**: Qwen3-8B v3 full_s1 (PID 534706)
- **GPU 1**: Mistral-7B v3 full_s1 (PID 536272)
- 两张卡均已满载，无 `--resume` 标志，均为全新运行。

---
