# research bootstrap ci check

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_bootstrap-ci-check_20260514T112610_result.json`
- **Structured JSON:** [`67ca243d91cd4c1fb765.json`](../../sessions/67/67ca243d91cd4c1fb765.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集齐。D037/D038 在代码中没有显式引用（只在 binary checkpoint 中匹配），它们是 trained-router 实验，使用 `eval_end_to_end.py` 进行评估。

## Bootstrap CI 置信水平参数汇总

| 文件 | 行号 | 默认置信水平 | n_boot | 备注 |
|------|------|-------------|--------|------|
| `src/eval_end_to_end.py` | L424 | **0.90 (90%)** | 1000 | trained-router 评估主脚本，D037/D038 使用此文件 |
| `src/analysis.py` | L21 | **0.90 (90%)** | 10000 | Phase 1 MVP 分析 |
| `src/death_decomposition.py` | L24, L137 | **0.95 (95%)** | 10000 | Death decomposition 分析（独立模块） |

**D037/D038 trained-router 实验的 bootstrap CI 置信水平 = 0.90 (90%)**。

具体代码位置：
- `src/eval_end_to_end.py:424` — `def bootstrap_ci(values, stat_fn, n_boot=1000, ci=0.90, rng=None)`
- 注释 L14 也明确写了 `bootstrap 90% CI`
- CLI 参数 `--n_bootstrap`（L713）可覆盖 resample 次数（默认 1000），但 **置信水平 0.90 硬编码在函数默认参数中**，无 CLI 覆盖入口

注意 `death_decomposition.py` 用的是 **0.95 (95%)**，与 eval_end_to_end 不同。

---
