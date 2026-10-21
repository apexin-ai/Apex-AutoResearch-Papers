# code seed comparison fix

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_seed_comparison_fix_20260516T054336_result.json`
- **Structured JSON:** [`d56f8a6e1a1f6c61b023.json`](../../sessions/d5/d56f8a6e1a1f6c61b023.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本修改完成，无语法错误，`--help` 和 `--dry-run` 均正常运行。

### 修改内容

在 `load_metrics` 函数的 `return m` 前添加了 2 行：

```python
if "rel_ign_f1" in m and "ign_f1" not in m:
    m["ign_f1"] = m["rel_ign_f1"]
```

### eval_results 中 key 使用情况

**`rel_ign_f1`：无任何文件使用。** grep 搜索整个 eval_results 目录，零匹配。

**`ign_f1`：所有 metrics 文件均使用 `ign_f1`**，包括 seed comparison 引用的：
- `rsft_ced_s43/metrics_v2.json` — ign_f1=0.4512
- `rsft_ced_s45/metrics_v2.json` — ign_f1=0.4416
- `rsft_flat_nli_s44/metrics_v2.json` — ign_f1=0.4521
- `rsft_flat_nli_s45/metrics_v2.json` — ign_f1=0.4462

**4 个 reeval 目录为空**（无 metrics 文件）：
- `rsft_ced_s42_reeval/`
- `rsft_ced_s44_reeval/`
- `rsft_flat_nli_s42_reeval/`
- `rsft_flat_nli_s43_reeval_r2/`

兼容逻辑已就位，当未来出现 `rel_ign_f1` 的 metrics 文件时会自动归一化为 `ign_f1`。

---
