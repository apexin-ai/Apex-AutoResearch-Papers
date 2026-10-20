# code plan 002 eval prep

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-002-eval-prep_20260514T205631_result.json`
- **Structured JSON:** [`123e56c674f2b8e3d6f9.json`](../../sessions/12/123e56c674f2b8e3d6f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本均通过 dry-run 验证。

---

**产出：**

| 脚本 | 路径 | 功能 |
|------|------|------|
| `extract_features_multi.py` | `/root/gen-depth-fingerprint/extract_features_multi.py` | 多生成器特征提取，支持 `--model-name` 增量模式 |
| `cross_generator_eval.py` | `/root/gen-depth-fingerprint/cross_generator_eval.py` | Leave-one-generator-out + Leave-one-family-out CV 评估 |

**dry-run 结果：**
- `extract_features_multi.py` — 成功提取 pythia-2.8b (10 rows) + pythia-1b (10 rows)，增量合并到 `data/features_all.csv`
- `cross_generator_eval.py` — 成功执行跨生成器评估，输出 macro-F1、per-class F1、confusion matrix 到 stdout 和 `results/cross_generator_results.json`

待数据生成完成后，全量运行命令：
```bash
python extract_features_multi.py --device cuda:0
python cross_generator_eval.py
```

---
