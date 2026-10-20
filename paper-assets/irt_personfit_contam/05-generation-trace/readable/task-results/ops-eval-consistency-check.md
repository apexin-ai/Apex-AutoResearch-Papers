# ops eval consistency check

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-consistency-check_20260523T111641_result.json`
- **Structured JSON:** [`51a1f14c1684278fd359.json`](../../sessions/51/51a1f14c1684278fd359.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。以下是对比结论：

---

## ✅ 一致，可以安全使用旧 clean baseline 计算 Cohen's d

### 对比结果

| 维度 | 新代码 (ctrl_contam_pilot) | 旧代码 (Llama / Mistral) | 一致？ |
|------|--------------------------|--------------------------|--------|
| **Prompt template** | `Question: ...\nA. ...\nB. ...\nC. ...\nD. ...\nAnswer:` | 完全相同 | ✅ |
| **Few-shot format** | 3-shot, 硬编码（法国首都/水星/2+2） | 完全相同的 3 个 example | ✅ |
| **MMLU items** | mmlu_items.json, 14042 items, md5=`ec530c77` | md5 一致（Llama/Mistral 都一样） | ✅ |
| **IRT params** | mmlu_params.csv, 14042 行, md5=`ac5425de` | md5 一致（三个目录都一样） | ✅ |
| **评分逻辑** | logprob argmax on A/B/C/D tokens | 完全相同 | ✅ |
| **IRT 计算** | 4PL irf → MLE theta (Newton-Raphson) → lz* (Snijders 2001) | 函数体逐行一致 | ✅ |
| **量化配置** | 4-bit NF4, float16 compute | 完全相同 | ✅ |

### 差异（均不影响 eval 结果）

- 新代码增加了多模型支持（`--model` 参数）、`contam_5` 条件、注释/docstring
- 输出路径结构不同（新代码按 model 分子目录）
- results JSON 新代码多一个 `"model"` 字段
- seen_items_15pct.json 在两个目录内容不同（预期行为——不同 run 的随机采样，clean baseline 的 seen_set 为空不受影响）

---
