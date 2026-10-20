# code add max items param

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_add-max-items-param_20260518T120212_result.json`
- **Structured JSON:** [`330ab73b6a9d6ad8d366.json`](../../sessions/33/330ab73b6a9d6ad8d366.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。`--max-items` 和 `--subsample-seed` 已添加到 evaluate.py。

修改内容：
- `import random` 加到 imports
- argparse 新增 `--max-items`（默认 0 = 全量）和 `--subsample-seed`（默认 42）
- `evaluate_mcq`、`evaluate_gsm8k`、`evaluate_humaneval` 三个函数中，在已有 `max_samples` 截断之后加入随机子采样逻辑（`random.Random(seed).sample` + `ds.select(sorted(indices))`）
- 三个 call site 传入新参数

---
