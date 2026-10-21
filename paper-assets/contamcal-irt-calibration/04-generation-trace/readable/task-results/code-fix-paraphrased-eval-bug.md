# code fix paraphrased eval bug

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_paraphrased_eval_bug_20260514T025236_result.json`
- **Structured JSON:** [`8f6cb0aa209dc231c1ac.json`](../../sessions/8f/8f6cb0aa209dc231c1ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Local copy updated. No git repo exists, so no commit/push possible.

**修复总结：**

`load_paraphrased_benchmark` 有三个 bug，全部已修复（服务器 + 本地 artifact 副本）：

1. **ARC crash**（报错 `'list' object has no attribute 'get'`）：paraphrase JSON 中 `original["choices"]` 是 `["A) text", ...]` 列表格式，但代码用 `.get("text")` 当 dict 访问。修复：检测 list 类型时解析 `"A) text"` 为 `label="A"`, `text="text"`。

2. **MMLU 双前缀**：choices 是 `"A) 0"` 格式，`evaluate_paraphrased` 又加了一次前缀变成 `"A) A) 0"`。修复：load 时用 regex 去掉 `"A) "` 前缀。

3. **HumanEval None**：`paraphrase_parsed` 为 JSON `null`，`dict.get(key, {})` 在 key 存在且值为 None 时返回 None 而非 `{}`。修复：改用 `item.get("paraphrase_parsed") or {}`。

验证结果：四个 benchmark 全部加载成功（mmlu: 6596, arc: 697, gsm8k: 228, humaneval: 26 items）。

---
