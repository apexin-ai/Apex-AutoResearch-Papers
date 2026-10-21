# eval ablation batch 4

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_ablation-batch-4_20260522T013249_result.json`
- **Structured JSON:** [`ff6850ab2660a1cefcc5.json`](../../sessions/ff/ff6850ab2660a1cefcc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 结果总结

| 实验 | TSR | CAR | vs Vanilla (77.0%) | 结论 |
|------|-----|-----|-------------------|------|
| **occ_detach** (2 seeds) | 92.0% | **72.0%±0.5%** | **-5.0pp** | success |
| **random_occ** (2 seeds) | 87.5% | **77.5%±0.5%** | **+0.5pp** | success |

**Claim 3 (Gradient Flow Necessity) — 验证通过**：detach 梯度后 CAR 不仅没有改善，反而比 vanilla 低 5pp（72.0% vs 77.0%），证明梯度流向 vision encoder 是必要条件。

**Claim 4 (Not Any Auxiliary Loss) — 验证通过**：随机 occ 标签下 CAR ≈ vanilla（77.5% vs 77.0%），证明空间内容（而非随意的辅助 loss）才是安全性提升的来源。

Registry 已更新为 DONE/success，分析报告已写入 memory.md 并注册 artifact。

---
