# ops inventory westd 16980

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_inventory-westd-16980_20260523T195018_result.json`
- **Structured JSON:** [`b2fe242ed98246323861.json`](../../sessions/b2/b2fe242ed98246323861.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-16980 数据盘点报告

**项目目录**: 596M（outputs/ 469M, data/ 122M, 其余零散小文件）。无 checkpoint/模型权重文件。

**数据盘 /root/autodl-tmp**: 195G
- `models/` 103G — 基座模型（Qwen3-8B, Llama-8B, Mistral-7B 及其 AWQ 量化版）
- `checkpoints/` 79G — LoRA adapter 及 merged 权重（70b_lora_docred/scierc, llama/qwen 各数据集的 merged 模型）
- `gollie_model/` 13G, `schema_outputs/` 98M

**运行中进程**: 无训练/评估进程。有若干残留 http.server 和一个 tmux session `llama_beam`（idle）。

**缓存**: `.cache/` 243M, 无 autodl-fs。

**判断：无不可替代数据，可安全释放。**
- 代码已有匿名仓库
- `models/` 全是公开基座模型，可从 HF/ModelScope 重新下载
- `checkpoints/` 是 LoRA 微调产物，可重训；merged 权重可从 adapter + 基座重新合并
- `outputs/` 是实验输出，metrics 已在论文中
- 无未提交的重要数据

---
