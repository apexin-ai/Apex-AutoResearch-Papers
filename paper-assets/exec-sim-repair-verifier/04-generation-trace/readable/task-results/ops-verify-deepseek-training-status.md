# ops verify deepseek training status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-deepseek-training-status_20260516T062858_result.json`
- **Structured JSON:** [`d61742e621b1a8364082.json`](../../sessions/d6/d61742e621b1a8364082.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 3 训练正常，step 31/1434。

---

## 汇总

### Part 1: GPU 训练状态

| GPU | Session | Task | 状态 |
|-----|---------|------|------|
| 0 | `deepseek-cls-repo` | CLS repo-level (swebench_full) | **卡在 tokenization**——70k 长序列样本单线程处理中，进程活着（RSS 持续增长 3.8GB），预计还需数分钟。之前被残留 dryrun 进程阻塞，已杀掉。 |
| 1 | `deepseek-cwm-func` | CWM function-level (seed=42) | 正常训练，~step 80+/1434，~3.5s/it |
| 2 | `deepseek-cls-func` | CLS function-level | 正常训练，~step 78+/1434，~3.7s/it |
| 3 | `deepseek-cwm-func-s123` | CWM function-level **(seed=123)** | 已启动，训练中 step 31/1434，~3.5s/it |

### Part 2: GPU 3 启动

已用 `--seed 123 --epochs 3` 启动 multi-seed CWM 训练。注意原命令 `--num_train_epochs` 无效，实际参数是 `--epochs`。

### Part 3: 数据字段差异

| 数据集 | 字段 |
|--------|------|
| `cwm_train.jsonl` | `code, test, **target**, label, source, problem_id, mutation_type` |
| `swebench_full/swebench_train.jsonl` | `code, test, label, source, problem_id, mutation_type, error_message, execution_output, metadata` |

**关键差异**：swebench_full **没有 `target` 字段**。CWM 任务依赖 `target` 作为训练标签（execution result 描述），所以 swebench_full 数据无法直接用于 CWM 训练。如果要做 repo-level CWM，需要先为 swebench_full 数据生成 `target` 字段（可能从 `execution_output` + `error_message` 构造）。

---
