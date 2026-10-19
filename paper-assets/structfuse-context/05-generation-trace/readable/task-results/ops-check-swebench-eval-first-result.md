# ops check swebench eval first result

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-swebench-eval-first-result_20260515T190359_result.json`
- **Structured JSON:** [`9bfcfe52f8d1259cad72.json`](../../sessions/9b/9bfcfe52f8d1259cad72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 当前进度

**进程**: PID 61318 存活，已运行 19 分钟

**完成**: 7/100 instances（7%）

**ETA**: ~131s/instance × 93 remaining ≈ **3h20m**（预计 ~06:05 CST 完成）

## 前 7 个 instance 的部分 Recall

| Instance | R@1 | R@5 | R@10 | R@20 |
|----------|-----|-----|------|------|
| astropy-14365 | 0.0 | 0.0 | 0.0 | 0.0 |
| astropy-14182 | 0.0 | 0.0 | 0.0 | 0.0 |
| astropy-14995 | 0.0 | 1.0 | 1.0 | 1.0 |
| astropy-6938 | 0.0 | 0.0 | 0.0 | 0.0 |
| astropy-12907 | 1.0 | 1.0 | 1.0 | 1.0 |
| astropy-7746 | 0.0 | 1.0 | 1.0 | 1.0 |
| django-14787 | 0.0 | 0.0 | 0.0 | 0.0 |

**7-instance 平均**: R@1=14.3%, R@5=42.9%, R@10=42.9%, R@20=42.9%

样本量太小（且集中在 astropy），数字参考价值有限。4/7 完全 miss（R@20=0），说明这些 instance 的 gold file 连 top-20 都没进。等跑完更多 repo（django、sympy 等）后数据才有意义。

---
