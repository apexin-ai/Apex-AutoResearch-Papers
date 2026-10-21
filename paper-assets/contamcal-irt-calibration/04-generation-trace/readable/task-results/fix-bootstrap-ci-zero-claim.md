# fix bootstrap ci zero claim

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_bootstrap-ci-zero-claim_20260520T165734_result.json`
- **Structured JSON:** [`fed91c3ed01883c847db.json`](../../sessions/fe/fed91c3ed01883c847db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件中不存在描述的 bug。

`bootstrap_results.txt` 全文是纯数字表格（55行），没有任何 prose 文本。不存在 "CI 不含 0" 或 "does not contain" 的描述。`bootstrap_triple_seed.py` 也没有生成此类文字的逻辑。

Phi-4 行（第17行）的原始数据：
```
Phi-4  3  76.40%  +0.72pp  [-0.17, +1.39](boot)  0.039
```

CI 确实包含零（下限 -0.17 < 0），p=0.039 是 bootstrap 计算的原始数值。两者之间可能存在统计方法不一致（BCa CI 与 percentile-based p-value 不完全对应），但文件本身没有错误的文字描述需要修正。

---
