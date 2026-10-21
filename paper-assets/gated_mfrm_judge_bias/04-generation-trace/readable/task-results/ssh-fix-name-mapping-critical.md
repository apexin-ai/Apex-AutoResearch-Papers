# ssh fix name mapping critical

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-name-mapping-critical_20260524T095914_result.json`
- **Structured JSON:** [`fefc8e6c154d4140747c.json`](../../sessions/fe/fefc8e6c154d4140747c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No git history to diff against (bare repo). All fixes applied and verified. Here's the summary:

---

## 产出

### 1. Diff 摘要

**evaluation.py** (3 处修改):

```diff
 # 新增 EXCLUDE_MODELS (line 66)
+EXCLUDE_MODELS = ["qwen3-8b", "mistral-large-2407"]

 # arena_correlation() 中新增 assertion
+    expected = set(model_names) - set(exclude_models)
+    unmatched = expected - set(matched_models)
+    assert not unmatched, f"ARENA_NAME_MAPPING incomplete — unmatched models: {unmatched}"

 # run_evaluation() 中传入 exclude_models
-    arena_corr = arena_correlation(results, model_names)
+    arena_corr = arena_correlation(results, model_names, exclude_models=EXCLUDE_MODELS)
```

注意：evaluation.py 的 `ARENA_NAME_MAPPING` 已有 3 个映射和 `mistral-large-2407`，无需修改。

**bootstrap_delta_tau.py** (4 处修改):

```diff
 # ARENA_ELO 新增 mistral-large-2407
     "gpt-3.5-turbo-0125": 1125,
+    "mistral-large-2407": 1250,
 }

 # ARENA_NAME_MAPPING 新增 4 条
     "mixtral-8x22b": "mixtral-8x22b-instruct-v0.1",
+    "llama-3.3-70b-instruct": "llama-3.3-70b",
+    "qwen2.5-72b-instruct": "qwen2.5-72b",
+    "gpt-3.5-turbo-0613": "gpt-3.5-turbo-0125",
+    "mistral-large-2407": "mistral-large-2407",
 }

 # EXCLUDE_MODELS 更新
-EXCLUDE_MODELS = ["qwen3-8b"]
+EXCLUDE_MODELS = ["qwen3-8b", "mistral-large-2407"]

 # main() 中新增 assertion
+    unmatched = set(active_models) - set(matched_models)
+    assert not unmatched, f"ARENA_NAME_MAPPING incomplete — unmatched models: {unmatched}"
```

### 2. Dry-run 验证结果

```
Matched (16):
  claude-3-5-sonnet-20241022 -> claude-3-5-sonnet-20241022 (ELO=1298)
  claude-3-haiku-20240307    -> claude-3-haiku-20240307    (ELO=1195)
  claude-3-opus-20240229     -> claude-3-opus-20240229     (ELO=1262)
  gemma-2-27b-it             -> gemma-2-27b-it             (ELO=1231)
  gemma-2-9b-it              -> gemma-2-9b                 (ELO=1207)
  gpt-3.5-turbo-0613         -> gpt-3.5-turbo-0125         (ELO=1125)
  gpt-4-0613                 -> gpt-4-0613                 (ELO=1186)
  gpt-4-turbo-2024-04-09     -> gpt-4-turbo-2024-04-09     (ELO=1272)
  gpt-4o-2024-05-13          -> gpt-4o                     (ELO=1300)
  gpt-4o-mini-2024-07-18     -> gpt-4o-mini                (ELO=1286)
  llama-3-70b-instruct       -> llama-3-70b-instruct       (ELO=1221)
  llama-3-8b-instruct        -> llama-3-8b-instruct        (ELO=1166)
  llama-3.1-70b-instruct     -> llama-3.1-70b-instruct     (ELO=1261)
  llama-3.3-70b-instruct     -> llama-3.3-70b              (ELO=1275)
  mixtral-8x22b-instruct-v0.1-> mixtral-8x22b-instruct-v0.1(ELO=1162)
  qwen2.5-72b-instruct       -> qwen2.5-72b                (ELO=1269)

Excluded (2): mistral-large-2407, qwen3-8b
Unmatched (0): (none)

ALL CHECKS PASSED: 16 matched + 2 excluded + 0 unmatched = 18 total
```

### 3. 18 个 target models（judgment_data_n17）

| # | Model |
|---|-------|
| 1 | claude-3-5-sonnet-20241022 |
| 2 | claude-3-haiku-20240307 |
| 3 | claude-3-opus-20240229 |
| 4 | gemma-2-27b-it |
| 5 | gemma-2-9b-it |
| 6 | gpt-3.5-turbo-0613 |
| 7 | gpt-4-0613 |
| 8 | gpt-4-turbo-2024-04-09 |
| 9 | gpt-4o-2024-05-13 |
| 10 | gpt-4o-mini-2024-07-18 |
| 11 | llama-3-70b-instruct |
| 12 | llama-3-8b-instruct |
| 13 | llama-3.1-70b-instruct |
| 14 | llama-3.3-70b-instruct |
| 15 | mistral-large-2407 |
| 16 | mixtral-8x22b-instruct-v0.1 |
| 17 | qwen2.5-72b-instruct |
| 18 | qwen3-8b |

### 4. 语法验证

`Syntax OK for both files` — py_compile 通过。

---
