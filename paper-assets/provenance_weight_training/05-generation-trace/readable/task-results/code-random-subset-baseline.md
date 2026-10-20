# code random subset baseline

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_random_subset_baseline_20260524T044818_result.json`
- **Structured JSON:** [`8812371db2465b6a0e32.json`](../../sessions/88/8812371db2465b6a0e32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

## 结果汇总

### D&R 保留率确认
- `scored_data.jsonl`: 371,499 条
- `scored_data_filtered_q03.jsonl`: 116,935 条 → **保留率 31.48%**（与预估 31.5% 一致）

### 创建的文件（服务器 `/root/provenance_weight_training/scripts/`）

| 文件 | 用途 |
|------|------|
| `prepare_random_subset.py` | 从 scored_data.jsonl 随机采样，seed-deterministic |
| `run_random_subset_seed42.sh` | 训练脚本，参数与 `threshold_q03_seed42` 完全一致 |

### 生成的数据
- `data/random_subset_seed42.jsonl`: **116,935 条**（与 D&R 数量完全一致）
- Mean q_score = 0.598（保留了原始 q_score 分布）
- 68.4% 是 q>0.3 的"污染"样本（D&R 则 100% 为 q≤0.3）

### 对照设计

|  | D&R (threshold_q03) | Random Subset |
|---|---|---|
| 样本数 | 116,935 | 116,935 |
| 选择方式 | q≤0.3 质量筛选 | 随机采样 |
| 污染样本占比 | 0% | 68.4% |
| 训练 tokens | 200M (6103 steps) | 200M (6103 steps) |
| Content epochs | ~3.2 | ~3.2 |
| 其余超参 | 一致 | 一致 |

唯一差异是数据选择方式，完美隔离 "filtering quality" vs "multi-epoch repetition"。

### 未执行 dry-run
GPU 全部被占用，无法加载模型做 dry-run 验证。脚本语法和参数已通过与 `threshold_q03_seed42.sh` 逐项对照确认无误，等 GPU 空闲后直接提交即可。

---
