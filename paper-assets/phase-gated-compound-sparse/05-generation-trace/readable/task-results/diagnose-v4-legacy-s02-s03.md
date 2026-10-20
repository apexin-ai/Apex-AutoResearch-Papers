# diagnose v4 legacy s02 s03

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_v4_legacy_s02_s03_20260514T000438_result.json`
- **Structured JSON:** [`04117346362471622966.json`](../../sessions/04/04117346362471622966.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**s02/s03 不是崩溃，是正常完成退出。** s01 也几乎同时完成。三组 legacy 实验全部 50/50 problems 跑完。

### 结果摘要

| 实验 | sparsity | ci_overlap | sign_reversal | 状态 |
|------|----------|-----------|--------------|------|
| s01 (v4a) | 0.1 | FAIL | FAIL | DONE ✓ |
| s02 (v4b) | 0.2 | **PASS** | FAIL | DONE ✓ |
| s03 (v4c) | 0.3 | FAIL | FAIL | DONE ✓ |
| random_r2 | 0.1-0.3 | — | — | [27/50] 运行中 |

### 关键发现

1. **不是 OOM。** Legacy hardcoded importance path 不调用 `output_attentions=True`，避开了之前 v4a/b/c_r2 的 OOM 代码路径。GPU 1/2 空闲（0MiB）是因为进程正常退出释放了显存。

2. **s02 (sparsity=0.2) 最有意义** — ci_overlap_test PASS，II 为正（~21，super-additive），KV eviction 是 perplexity 退化主因。

3. **s03 (sparsity=0.3) 出现负 II (-224.5) 但 CI 跨零**，统计不显著。

4. **下一步**：等 random_r2 完成后做 importance vs random 交互方向对比。

Registry 已全部更新为 DONE，memory.md 已追加诊断记录。

---
