# fix w2 logo seed rerun

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_w2_logo_seed_rerun_20260515T200018_result.json`
- **Structured JSON:** [`e2fe2fd8a80f55cb7dbe.json`](../../sessions/e2/e2fe2fd8a80f55cb7dbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## 修复前后对比

| 指标 | 修复前 (buggy) | 修复后 | 说明 |
|------|-------------|--------|------|
| **Sub-A** d1-d3 mean acc | 72.0% | 72.0% | 不变（不依赖 seed groups） |
| **Sub-B** LOGO mean acc | **64.0%** | **72.1%** | +8.1pp，groups 不再 depth-correlated |
| Sub-B range | 46.6%-76.7% | 59.5%-81.6% | 最低 fold 大幅提升 |
| **Sub-C** seed_group pred | **20.8%** | **10.2%** | 从 2x chance 降至 ~chance (10%) |
| Sub-C depth/sg ratio | 3.46x | 7.06x | 分离度翻倍 |

### 论文需更新的数字
- Sub-B LOGO accuracy：64% → **72.1%**（range 59.5%-81.6%）
- Sub-C seed group prediction：20.8% → **10.2%**（现在真正接近 chance=10%，证明 groups 与 depth 无关）
- Sub-C depth/seed_group ratio：3.46x → **7.06x**

修复后结论更强：LOGO 保留组的 accuracy 几乎等于 Sub-A 的标准 CV（72.1% vs 72.0%），说明 depth 信号完全不依赖 seed text identity。Negative control 中 seed group 预测 10.2% ≈ chance，确认 groups 现在与 depth 真正解耦。

---
