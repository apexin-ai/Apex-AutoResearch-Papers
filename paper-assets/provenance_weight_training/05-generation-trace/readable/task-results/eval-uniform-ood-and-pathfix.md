# eval uniform ood and pathfix

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_uniform_ood_and_pathfix_20260524T082950_result.json`
- **Structured JSON:** [`df9836f15241afbdb092.json`](../../sessions/df/df9836f15241afbdb092.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All eval complete. Both directories now have all 3 required files matching `n5_statistical_analysis.py --auto` expectations.

## 结果汇总

### Uniform seed789

| Dataset | PPL |
|---------|-----|
| Holdout | 17.695 |
| OWT | 18.387 |
| Wiki | 15.349 |

### Uniform seed234

| Dataset | PPL |
|---------|-----|
| Holdout | 17.708 |
| OWT | 18.355 |
| Wiki | 15.352 |

### 与 3-seed 参考对比 (seed42)

| Dataset | seed42 | seed789 | seed234 |
|---------|--------|---------|---------|
| Holdout | 17.694 | 17.695 | 17.708 |
| OWT | 18.364 | 18.387 | 18.355 |
| Wiki | 15.337 | 15.349 | 15.352 |

### 目录结构

```
eval_results/
├── bs16_uniform_seed42/     (已有)
│   ├── eval_holdout.json
│   ├── eval_owt.json
│   └── eval_wiki.json
├── bs16_uniform_seed123/    (已有)
├── bs16_uniform_seed456/    (已有)
├── bs16_uniform_seed789/    ← 新建
│   ├── eval_holdout.json
│   ├── eval_owt.json
│   └── eval_wiki.json
└── bs16_uniform_seed234/    ← 新建
    ├── eval_holdout.json
    ├── eval_owt.json
    └── eval_wiki.json
```

与 `n5_statistical_analysis.py --auto` 完全兼容 — 目录名匹配 `bs16_uniform_seed(\d+)` 模式，文件名为 `eval_holdout.json`、`eval_owt.json`、`eval_wiki.json`。

---
