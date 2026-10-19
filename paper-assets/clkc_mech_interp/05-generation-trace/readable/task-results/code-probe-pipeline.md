# code probe pipeline

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_probe_pipeline_20260521T122439_result.json`
- **Structured JSON:** [`3a04b3b38c875d4b46b8.json`](../../sessions/3a/3a04b3b38c875d4b46b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个文件全部就绪，验证通过。

**创建的文件：**

| 文件 | 说明 |
|------|------|
| `src/collect_activations.py` | Hook 所有层残差流，取最后 token 激活，存 `(N, L, D)` tensor |
| `src/train_probe.py` | 逐层 logistic regression + 4 方向迁移评估 + binomial/permutation test + 可视化 |
| `src/run_mvp.sh` | 一键运行脚本，支持 `--model`/`--data_dir`/`--batch_size` 参数 |

**补装的依赖：** scikit-learn, scipy, matplotlib, numpy, torch (CPU), transformers

**修复：** `scipy.stats.binom_test` 在 scipy≥1.12 已移除，改用 `binomtest(...).pvalue`。

---
