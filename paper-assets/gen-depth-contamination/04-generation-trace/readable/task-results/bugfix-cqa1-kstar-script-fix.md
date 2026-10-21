# bugfix cqa1 kstar script fix

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_bugfix_cqa1-kstar-script-fix_20260519T220505_result.json`
- **Structured JSON:** [`ed3df4d2ca973f755131.json`](../../sessions/ed/ed3df4d2ca973f755131.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部确认完毕。

## 结果汇总

### 1. 脚本 K\* 计算：无需修复
4 个文件**已经是 1-indexed**，全部使用 `kstar = 0` 初始值 + `kstar = k + 1` 赋值 + `else: break`：
- `run_deberta_upperbound.py` (L159-162)
- `run_deberta_cross_transfer.py` (L207-212)
- `analyze_deberta_results.py` (L118-123, lgbm_kstar L143-149)
- `run_deberta_c4_1b5.py` (L166-170)

### 2. JSON kstar 值全部正确

| config | kstar | 验证 |
|--------|-------|------|
| wiki_pythia | **3** | 2v3 ci_lower=0.6059 > 0.60 ✓, 3v4 ci_lower=0.5659 < 0.60 ✓ |
| wiki_olmo | **1** | 0v1 ci_lower=0.9999 > 0.60 ✓, 1v2 ci_lower=0.5081 < 0.60 ✓ |
| wiki_qwen7b | **3** | 2v3 ci_lower=0.6223 > 0.60 ✓ |
| wiki_llama8b | **3** | 2v3 ci_lower=0.6258 > 0.60 ✓ |
| wiki_mistral7b | **3** | 2v3 ci_lower=0.6150 > 0.60 ✓ |

所有 JSON 都带 `"kstar_indexing": "1-indexed"` 标记。

### 3. exp_wiki_olmo 独立性确认
OBD baseline 数据完全不同（olmo 0v1=0.9933, 1v2=0.4983 vs pythia 0v1=0.9961, 1v2=0.6193），不是复制品。

**结论：这 4 个脚本的 off-by-one bug 已在之前被修复，JSON 结果与预期完全一致，无需任何操作。**

---
