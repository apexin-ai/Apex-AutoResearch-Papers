# research verify perlayer r2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verify_perlayer_r2_20260516T054952_result.json`
- **Structured JSON:** [`0215f9f522b290693880.json`](../../sessions/02/0215f9f522b290693880.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据结构已确认：

- Line 14: `trained` → Line 15: `image_mean` → Line 611: `last_preaction`
- Line 1208: `untrained` → Line 1209: `image_mean` → Line 1805: `last_preaction`

grep 的 4 次匹配依次对应：trained/image_mean, trained/last_preaction, untrained/image_mean, untrained/last_preaction。

## 验证结果

### trained image_mean（论文引用条件）

| Layer | 源数据 mean_R² | 论文引用值 | 匹配？ |
|-------|----------------|-----------|--------|
| L11 | 0.64357 | 0.644 | **一致**（四舍五入到3位） |
| L12 | 0.60861 | 0.609 | **一致** |
| L13 | 0.62961 | 0.630 | **一致** |

### trained last_preaction（交叉参考）

| Layer | mean_R² |
|-------|---------|
| L11 | 0.6579 |
| L12 | 0.6663 |
| L13 | 0.6779 |

**结论：论文引用的三个 R² 值 (L11=0.644, L12=0.609, L13=0.630) 与源数据完全一致，均为 mean_R² 四舍五入到小数点后三位的结果。**

---
