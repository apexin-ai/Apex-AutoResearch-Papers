# verify tail decay consistency

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_tail_decay_consistency_20260520T080311_result.json`
- **Structured JSON:** [`e0534bd9a3cad775fb29.json`](../../sessions/e0/e0534bd9a3cad775fb29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。汇总结果：

## 验证结论

### 1. features_9gen.csv — 全部 9 个 generator 的 tail_decay **一致**

| Generator | n | mean | std | min | max |
|---|---|---|---|---|---|
| gemma-2-2b | 4957 | -0.002308 | 0.000219 | -0.004049 | -0.001271 |
| llama-3.2-3b | 4680 | -0.002303 | 0.000214 | -0.004643 | -0.001723 |
| mistral-7b-v0.3 | 4849 | -0.002293 | 0.000195 | -0.003581 | -0.001661 |
| olmo-2-1b | 4713 | -0.002335 | 0.000223 | -0.003682 | 0.000000 |
| pythia-1b | 4555 | -0.002236 | 0.000242 | -0.004007 | 0.000000 |
| pythia-2.8b | 4609 | -0.002249 | 0.000241 | -0.003369 | 0.000000 |
| qwen3-0.6b | 4538 | -0.002329 | 0.000211 | -0.003647 | 0.000000 |
| qwen3-1.7b | 4617 | -0.002321 | 0.000232 | -0.006501 | 0.000000 |
| qwen3-8b | 4497 | -0.002318 | 0.000222 | -0.006554 | 0.000000 |

所有 generator 的 tail_decay 值域在 [-0.007, 0.000]，均值 ~-0.0023，**一致使用 log-prob slope 方法**。无 NLL proportion (~0.1) 残留。

### 2. JSONL 源文件验证
- `llama-3.2-3b/features_pythia410m.jsonl` (4680行) — tail_decay ~-0.002 ✓
- `mistral-7b-v0.3/features_pythia410m.jsonl` (4849行) — tail_decay ~-0.002 ✓  
- `gemma-2-2b/features_pythia410m.jsonl` (4957行) — tail_decay ~-0.002 ✓

JSONL 与 CSV 行数精确匹配，数据一致。

### 3. 代码实现对比
- `extract_features.py`（原始 6 gen）: `np.polyfit(x, y, 1)[0]`，ranks[100:1000] 上 sorted avg log-probs 的线性回归斜率 ✓
- `fix_tail_decay_and_eval.py`（修复脚本）: 同样的 log-prob slope 方法 ✓
- `llama_filter_and_extract.py` / `mistral_filter_and_extract.py`: **仍包含错误的 NLL proportion 代码**，但 JSONL 输出已被 fix 脚本重写

### 4. features_9gen.csv 总行数 = 42015 ✓

### 结论
**无需修复。** `fix_tail_decay_and_eval.py` 已成功将新 3 gen 的 JSONL 文件和 features_9gen.csv 统一为 log-prob slope 方法。数据完全一致。

唯一的代码卫生问题：`llama_filter_and_extract.py` 和 `mistral_filter_and_extract.py` 中的 tail_decay 计算仍是旧的 NLL proportion 实现，但这不影响现有数据（JSONL 已被覆盖），仅在重新运行这些脚本时会产生错误数据。

---
