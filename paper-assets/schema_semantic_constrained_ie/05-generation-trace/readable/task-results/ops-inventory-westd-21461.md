# ops inventory westd 21461

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_inventory-westd-21461_20260523T201133_result.json`
- **Structured JSON:** [`4b22d4040bde38effe32.json`](../../sessions/4b/4b22d4040bde38effe32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-21461 数据盘点报告

| 项目 | 大小 |
|------|------|
| 项目目录 `/root/schema_semantic_constrained_ie/` | **2.6G**（其中 checkpoints 2.4G） |
| `/root/autodl-tmp/` | **177G**（models 72G, checkpoints 93G, schema_outputs 145M） |
| `/root/.cache/` | **16G** |

**Checkpoints**：项目目录下有 2 组 LoRA adapter —— `qwen3_8b_lora_wikievents`（3 个 checkpoint）和 `llama_lora_docred`（3 个 checkpoint）。autodl-tmp 下还有 93G checkpoints。

**运行中进程**：无训练/评估进程。仅系统服务（supervisord、tensorboard、jupyter、sshd）。

**判断：无不可替代数据，可安全释放。** 代码在匿名仓库，LoRA adapter 可重训，models 是公开预训练权重，schema_outputs 是推理结果可重跑。

---
