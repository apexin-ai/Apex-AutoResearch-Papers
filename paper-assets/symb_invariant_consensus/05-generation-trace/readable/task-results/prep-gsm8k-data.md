# prep gsm8k data

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_gsm8k-data_20260516T061700_result.json`
- **Structured JSON:** [`29d149567cf4f472ee72.json`](../../sessions/29/29d149567cf4f472ee72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

### 产出报告

**数据文件**: `/root/symb_invariant_consensus/data/gsm8k_200.json`
- 200 题，从 GSM8K test set (1319题) 随机采样，seed=42
- 字段: `id`, `problem`, `solution`, `answer`, `level`, `dataset`
- 答案类型: 全部为整数 (从 `#### 数字` 格式提取)
- 格式与 proofwriter/folio/math500 兼容

**数据准备脚本**: `/root/symb_invariant_consensus/scripts/prepare_gsm8k.py`
- 可复现: seed=42, 200题随机采样
- 自动提取 `#### N` 格式的纯数字答案

**评估脚本**: `/root/symb_invariant_consensus/scripts/eval_gsm8k.py`
- 完全对齐 `eval_math500.py` 接口 (SICA vs SC@K)
- 支持参数: `--mode`, `--k`, `--n-problems`, `--temperature`, `--max-tokens`, `--seed`, `--output`, `--resume`, `--save-intermediates`
- 答案判定: `is_equiv()` 数值精确匹配
- 支持 checkpoint/resume, 包含 ETA 估计
- `task_type="math"` 走数学推理 pipeline

---
