# code rp lofo rerun corrected

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rp-lofo-rerun-corrected_20260516T130557_result.json`
- **Structured JSON:** [`5588acbbf3d4b5b4f287.json`](../../sessions/55/5588acbbf3d4b5b4f287.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**Gemma-2-2B rp=1.0 (1061 samples, unfiltered)**
| Metric | Value |
|--------|-------|
| 3-class F1 (macro) | **0.5536** |
| Binary F1 (gen-1 vs gen-2+) | **0.8571** |
| gen-0 F1 | 0.957 |
| gen-1 F1 | 0.176 |
| gen-2+ F1 | 0.527 |

Confusion matrix:
```
         pred-0  pred-1  pred-2+
gen-0      912      12      70
gen-1        0       3      16
gen-2+       0       0      48
```

注意：Gemma rp=1.0 几乎全退化为 gen-0（994/1061），gen-1 仅 19 条、gen-2+ 仅 48 条。gen-2+ recall=100%（48/48 全部正确），但 gen-1 样本太少导致 F1 极低。

---

**Llama-3.2-3B rp=1.1 (4416 samples)**
| Metric | Value |
|--------|-------|
| 3-class F1 (macro) | **0.4170** |
| Binary F1 (gen-1 vs gen-2+) | **0.5816** |
| gen-0 F1 | 0.531 |
| gen-1 F1 | 0.139 |
| gen-2+ F1 | 0.581 |

Confusion matrix:
```
         pred-0  pred-1  pred-2+
gen-0      979       9       7
gen-1      613      91     271
gen-2+    1097     235    1114
```

Llama rp=1.1 的 gen-1 大量被误判为 gen-0（613/975），说明 rp=1.1 的 gen-1 特征与 rp=1.0 训练集的 gen-0 高度相似。

结果已保存到 `/root/gen-depth-fingerprint/results/rp_lofo_corrected.json`。

---
