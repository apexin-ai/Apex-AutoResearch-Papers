# analysis cuda0 idle prep

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cuda0_idle_prep_20260515T174457_result.json`
- **Structured JSON:** [`67c2f80a09ae46e4c903.json`](../../sessions/67/67c2f80a09ae46e4c903.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### GPU 状态
| GPU | 状态 | 显存 | 利用率 |
|-----|------|------|--------|
| cuda:0 | **完全空闲** | 0 / 97887 MiB | 0% |
| cuda:1 | 运行中 (PID 290322) | 17169 / 97887 MiB | 88% |

cuda:0 无残留进程，干净可用。注意实际运行 PID 是 290322（非 290317），可能是子进程。

### Constrained Eval 进度
- 已完成 **193 / 551 行**（35%），还需一段时间。

### 磁盘
| 分区 | 已用 | 可用 |
|------|------|------|
| `/`（根） | 12G / 30G | 19G (62%) |
| `/root/autodl-tmp` | 89G / 250G | 162G (64%) |

磁盘充裕，不是瓶颈。

### DocRED SFT 数据准备
- 脚本已存在：`prepare_sft_data_docred.py`
- 数据已存在：`data/docred/` 下有 `train_annotated.json`、`dev.json`、`rel_info.json`、`ontology_constraints_docred.json`
- **SFT 数据也已存在**：`sft_train.jsonl` 和 `sft_dev.jsonl` 已经生成过了

DocRED SFT 数据看起来**已经准备好了**。cuda:0 当前空闲，可以立即用于下一步任务（比如 DocRED 训练或 eval）。

---
