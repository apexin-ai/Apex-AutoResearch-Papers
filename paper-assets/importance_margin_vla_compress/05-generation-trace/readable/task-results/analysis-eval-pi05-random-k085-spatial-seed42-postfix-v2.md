# analysis eval pi05 random k085 spatial seed42 postfix v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_pi05_random_k085_spatial_seed42_postfix_v2_20260524T050241_result.json`
- **Structured JSON:** [`2fbd32ef45013277f9fe.json`](../../sessions/2f/2fbd32ef45013277f9fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评测完成，无异常。

## 结果汇总

**总体 SR: 60.8% (304/500)**

| Task | Description | SR |
|------|------------|-----|
| T0 | pick up black bowl between plate and ramekin | 84% |
| T1 | pick up black bowl next to ramekin | 68% |
| T2 | pick up black bowl from table center | 92% |
| T3 | pick up black bowl on cookie box | 16% |
| T4 | pick up black bowl in top drawer | 66% |
| T5 | pick up black bowl on ramekin | 28% |
| T6 | pick up black bowl next to cookie box | 44% |
| T7 | pick up black bowl on stove | 76% |
| T8 | pick up black bowl next to plate | 82% |
| T9 | pick up black bowl on wooden cabinet | 52% |

**异常检查**: 无 crash / NaN / 提前终止，10 tasks × 50 episodes 全部完成，耗时 ~160 min。

**对比分析**: π0.5 Spatial baseline ~88%，Random k=0.85 post-fix 得到 60.8%，**降幅 27.2pp**。保留 85% token 但 random 剪枝仍造成严重性能损失，T3 (16%) 和 T5 (28%) 尤其差。

**结论: negative** — Random pruning 即使在高保留率 (k=0.85) 下表现仍远低于 baseline，进一步验证了 random pruning 不是有效策略。

---
