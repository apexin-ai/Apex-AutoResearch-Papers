# code rp lofo preliminary

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rp-lofo-preliminary_20260516T121457_result.json`
- **Structured JSON:** [`c0e9b0d539e1f66f381e.json`](../../sessions/c0/c0e9b0d539e1f66f381e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果：

**3-class (gen-0 / gen-1 / gen-2+)**
| 类别 | Precision | Recall | F1 |
|------|-----------|--------|------|
| gen-0 | 0.51 | 0.98 | 0.67 |
| gen-1 | 0.33 | 0.33 | 0.33 |
| gen-2+ | 0.77 | 0.48 | 0.59 |
| **Macro** | | | **0.5287** |

**Binary (gen-1 vs gen-2+)**
| 指标 | 值 |
|------|------|
| Macro F1 | **0.5201** |
| gen-1 F1 | 0.4495 |
| gen-2+ F1 | 0.5907 |

**Gate D036: binary F1 = 0.52 → FAIL** (需 > 0.70)

分类器在 rp=1.0 上训练后迁移到 rp=1.1 效果显著下降。gen-1 vs gen-2+ 的区分能力近乎随机，说明 repetition penalty 的微调改变了特征分布，特别是对生成深度的辨别信号有很大干扰。结果已保存到 `/root/gen-depth-fingerprint/results/rp_lofo_preliminary.json`。

---
