# ssh autodl launch api judges fix download

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_autodl_launch_api_judges_fix_download_20260523T230156_result.json`
- **Structured JSON:** [`ce79b07c0c8df236a72f.json`](../../sessions/ce/ce79b07c0c8df236a72f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出报告

### 1. API Judges — ❌ 全部崩溃

**原因**: config 中的 `target_models` 包含 **9 个没有 response 文件的模型**。`data_loader.py` 尝试加载时触发 `FileNotFoundError`。

**缺失的模型**（config 里有，responses/ 目录里没有）:
| 模型 | 缺失文件 |
|------|----------|
| claude-3-5-sonnet-20241022 | ✗ |
| gpt-4-turbo-2024-04-09 | ✗ |
| llama-3.1-70b-instruct | ✗ |
| gemma-2-27b-it | ✗ |
| claude-3-opus-20240229 | ✗ |
| llama-3-70b-instruct | ✗ |
| mixtral-8x22b-instruct-v0.1 | ✗ |
| claude-3-haiku-20240307 | ✗ |
| llama-3-8b-instruct | ✗ |

**responses/ 目录实际有的 15 个模型**: claude-opus-4.7, gemma-2-9b, gpt-3.5-turbo-0125, gpt-4-0314, gpt-4-0613, gpt-4o-mini, gpt-4o, gpt-5.5, llama-3.1-8b, llama-3.3-70b, mistral-7b-v0.3, mistral-large-2, qwen2.5-72b, qwen2.5-7b, qwen3-8b

**RPM 修改已完成**: sonnet=150, gemini/deepseek/qwen3=100。需要修复 config 的 target_models 后重新启动。

---

### 2. LLaMA 下载 — 🔄 进行中 (HuggingFace)

| 项目 | 值 |
|------|-----|
| ModelScope | ❌ 两个 ID 都 404 |
| 当前方式 | HuggingFace (autodl 代理) |
| model_id | `casperhansen/Llama-3.3-70B-Instruct-AWQ` |
| PID | 480640 |
| 已下载 | 5.1 GB / ~36 GB |
| 速度 | ~30 MB/s |
| ETA | ~17 分钟 |
| 磁盘 | 110 GB 可用 |

---

### 3. rtx6000-4x — ❌ 不可达

连接被拒（port 23687）。如果是 AutoDL 实例，重启后端口可能已变，需去控制台查新端口并更新 `~/.ssh/config`。

---

**需要你决定**：config 中的 target_models 要怎么改？两个方案：
- **A**: 删掉 9 个缺失模型，只用现有 15 个 response 文件中的模型（去掉 reference_model gpt-4-0314 后是 14 个 target）
- **B**: 先生成缺失模型的 response 数据，再启动 judge

---
