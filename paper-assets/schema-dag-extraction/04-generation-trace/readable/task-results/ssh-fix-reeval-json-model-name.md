# ssh fix reeval json model name

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_reeval_json_model_name_20260517T133827_result.json`
- **Structured JSON:** [`95fe9777fd9f56adcfae.json`](../../sessions/95/95fe9777fd9f56adcfae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

这些都是日志文件，不影响实际数据，无需修改。

---

## 报告

### 问题 1: 模型名修复

| 服务器 | 文件 | 修复 |
|--------|------|------|
| cqa1-38874 | `artifacts/d051_llama-3.1-70b-fp8_fewnerd_n25_s42/summary_unified_protocol.json` | `Qwen3-30B-A3B` → `Qwen3-32B-FP8` ✓ |
| westd-24295 | 同上 | 同上 ✓ |

两台服务器已验证修复完成。其他文件（含本地日志）仅出现在日志中，不需修改。

### 问题 2: Averaging 方式确认

**两个模型均使用 micro averaging，完全一致。**

`reeval_text_match.py` 的聚合逻辑（约第 200-210 行）：
- 先将所有 batch 的 TP / total_pred / total_gold **求和**，再计算 P/R/F1 — 这是标准 **micro** averaging
- 同时也算了 macro_f1（各 batch F1 的均值），但 summary JSON 中记录的 recall/precision/f1 是 micro 值

`summary_unified_protocol.json` 中 Qwen3 参考数据的 note 也明确写着 `"micro text_match"`。70B 的结果包含 `tp/total_pred/total_gold`，与 micro 计算一致。

---
