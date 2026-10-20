# fix exp 001 paths and disk check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp_001_paths_and_disk_check_20260522T000823_result.json`
- **Structured JSON:** [`ab38b0fb1bd2ec276fab.json`](../../sessions/ab/ab38b0fb1bd2ec276fab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。

---

## 报告

### 1. 磁盘空间

| 分区 | 总量 | 已用 | 剩余 | 使用率 |
|------|------|------|------|--------|
| `/` (root) | 30G | 9.6G | 21G | 32% |
| `/root/autodl-tmp` | 250G | 2.1M | 250G | ~0% |

autodl-tmp 基本为空，仅有一个空的 `models/` 目录。

### 2. 修复详情

#### (a) 路径不匹配 — `data_loader.py:1-90`, `config.yaml:1-5`
- `data_loader.py`: 移除硬编码 `DATA_DIR`，改为从 `config.yaml` 读取 `data_dir`，通过 `_get_data_dir()` 解析（相对路径基于 `PROJECT_ROOT`）
- `config.yaml`: `data_dir` 改为绝对路径 `/root/gated_mfrm_judge_bias/data/mt_bench/` 和 `/root/gated_mfrm_judge_bias/data/arena_hard/`
- prompts 文件名修正：MT-Bench → `question.jsonl`，Arena-Hard → `prompts.jsonl`

#### (b) Arena-Hard 字段名不匹配 — `data_loader.py:55`
- `load_arena_hard_prompts()` 和 `load_mt_bench_prompts()` 均使用 `obj.get("question_id", obj.get("id"))` 兼容两种字段名

#### (c) Response 路径不匹配 — `data_loader.py:63-68`
- `load_model_responses()` 根据 benchmark 类型选择子目录：Arena-Hard → `responses/`，MT-Bench → `model_answer/`
- response 字段也做了兼容：`obj.get("response", obj.get("output", ""))`

### 3. 验证输出
```
Arena-Hard prompts: 500
First prompt keys: ['id', 'category', 'prompt']
First prompt id: 328c149ed45a41c0b9d6f14659e63599
MT-Bench prompts: 80
First question keys: ['id', 'category', 'prompt']
```

---
