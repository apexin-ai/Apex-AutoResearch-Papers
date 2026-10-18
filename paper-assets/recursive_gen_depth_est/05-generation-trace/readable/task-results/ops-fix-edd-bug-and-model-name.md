# ops fix edd bug and model name

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_edd_bug_and_model_name_20260516T163801_result.json`
- **Structured JSON:** [`60f24c58b51dc479c70a.json`](../../sessions/60/60f24c58b51dc479c70a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 bug 已修复。

### 结果

**Bug 1 — EDD**：阈值从 0.55 改为 0.70。d2v3 AUC=0.6815 < 0.70，是第一个低于阈值的 consecutive pair，**EDD = 3**。

**Bug 2 — Model name**：`"Meta-Llama-3.1-8B-Instruct"` → `"Meta-Llama-3.1-8B"`。

### 系统性影响

`scripts/llama3_eval.py` 的 EDD 阈值 0.55 是硬编码的，**会影响所有通过该脚本运行的实验**。已存在的 `results/cross_scale_llama3_8b_003/summary.json` 也可能有同样的 EDD 计算错误（如果也是该脚本生成的）。需要检查该文件是否也需要修正。

同样，`src/binary_pairwise_eval.py` 中的 EDD 逻辑是另一套硬编码条件判断（基于 d3v4/d4v5 的 AUC），与 `llama3_eval.py` 的通用循环逻辑不一致，属于另一个潜在问题。

---
