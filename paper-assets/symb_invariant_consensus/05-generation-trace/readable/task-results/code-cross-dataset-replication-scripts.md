# code cross dataset replication scripts

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cross-dataset-replication-scripts_20260520T103447_result.json`
- **Structured JSON:** [`dd3b1b217f66e2360498.json`](../../sessions/dd/dd3b1b217f66e2360498.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 数据集准备

| 数据集 | 文件 | 数量 | Label 分布 | Seed |
|--------|------|------|------------|------|
| ProofWriter | `data/proofwriter_30.json` | 30 | T=10, F=10, U=10 | 42 |
| LogiQA | `data/logiqa_30.json` | 30 | A=8, B=8, C=7, D=7 | 42 |

两个数据集均从已有全量数据采样，格式与现有 pipeline 兼容。

### Dry-run 结果

ProofWriter 3 题 K=4，端口 8020 (Mistral-7B)：**通过**。
- SC、SICA、Selective Abstention 三个方法均正常执行
- McNemar test 正常计算
- Checkpoint/resume 功能正常
- 单题耗时 ~14-18s (K=4)
- 结果输出到 `results/cross_dataset/proofwriter/pilot.json`

### 脚本清单

| 脚本 | 用途 |
|------|------|
| `prepare_proofwriter_30.py` | 采样 30 题 ProofWriter |
| `prepare_logiqa_30.py` | 采样 30 题 LogiQA |
| `run_cross_dataset_replication.py` | 统一跨数据集实验脚本 |

### 全量运行命令（等 Director 决定）

```bash
# ProofWriter 30题
python -u run_cross_dataset_replication.py \
  --dataset proofwriter --data-path data/proofwriter_30.json \
  --k 12 --vllm-port 8020 \
  --output results/cross_dataset/proofwriter/results.json

# LogiQA 30题
python -u run_cross_dataset_replication.py \
  --dataset logiqa --data-path data/logiqa_30.json \
  --k 12 --vllm-port 8020 \
  --output results/cross_dataset/logiqa/results.json
```

脚本就绪，等 Director 决定用哪种方法跑全量。

---
