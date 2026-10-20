# diagnose gsm8k qw rand s030

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gsm8k_qw_rand_s030_20260515T222521_result.json`
- **Structured JSON:** [`e981194d39d6ebb2327a.json`](../../sessions/e9/e981194d39d6ebb2327a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

根因确认。

## 诊断结论

**失败原因：代码版本不一致（import 路径错误）**

项目有两套 `interaction_index.py`：

| 路径 | 版本 | `bootstrap_interaction_index` 返回值 |
|---|---|---|
| `/root/autodl-tmp/pacs/profiling/interaction_index.py` | 旧（May 14 07:27） | **tuple** `(mean, ci_low, ci_high)` |
| `/root/autodl-tmp/pacs/pacs/profiling/interaction_index.py` | 新（May 14 15:06） | **dict** `{"mean": ..., "ci_low": ..., ...}` |

`run_profiling_gsm8k.py` 的 sys.path 设置导致 `from pacs.profiling.interaction_index import ...` 解析到**旧版** `/root/autodl-tmp/pacs/profiling/interaction_index.py`（返回 tuple），但代码第 459 行按 dict 方式访问 `bs["mean"]`，触发 `TypeError: tuple indices must be integers or slices, not str`。

**关键错误原文**：
```
File "/root/autodl-tmp/pacs/run_profiling_gsm8k.py", line 459, in run_profiling
    "mean": bs["mean"], "ci_low": bs["ci_low"], "ci_high": bs["ci_high"],
TypeError: tuple indices must be integers or slices, not str
```

实验在 50/50 问题全部处理完毕后、汇总统计阶段崩溃，数据本身已经生成完成。

**修复方案**（任选一）：

1. **同步旧文件**：将 `/root/autodl-tmp/pacs/profiling/interaction_index.py` 替换为 `pacs/pacs/profiling/interaction_index.py` 的新版内容，然后删除对应 `.pyc` 缓存
2. **删除旧副本**：直接删除 `/root/autodl-tmp/pacs/profiling/` 目录（如果不再需要），确保 import 走 `pacs/pacs/` 路径
3. **修复 sys.path**：在 `run_profiling_gsm8k.py` 中将 `_PROJECT_ROOT` 改为 `/root/autodl-tmp/pacs`（而非 `/root/autodl-tmp`），使 `from pacs.profiling...` 解析到新版

推荐方案 1 最安全，改完后重跑即可。由于 50 个问题的推理已全部完成，只是汇总阶段挂了，如果中间结果有缓存也可以只重跑汇总部分。

---
