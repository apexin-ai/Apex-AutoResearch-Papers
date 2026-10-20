# analysis c4 cross seed complete

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c4_cross_seed_complete_20260520T041900_result.json`
- **Structured JSON:** [`f5c9f89d0c3467324b7c.json`](../../sessions/f5/f5c9f89d0c3467324b7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## 结果

| | c4_a075_s43 | c4_a050_s43 |
|---|---|---|
| **PermG fwd** | **8/8** | **8/8** |
| PermG rev | 0/8 | 1/8 |
| K≥3 (3σ) | 8/8 | 3/8 |
| Threshold (3σ) | 0/8 | 0/8 |
| Naive xcorr (D111) | 8/8 | 4/8 |
| Diff xcorr (D111) | 8/8 | 6/8 |
| TY Granger | 1/8 | 0/8 |
| GPU hours | 4.16h | 4.20h |
| **Status** | DONE (success) | DONE (success) |

## Cross-seed 对比 (s42 vs s43)

- **PermG 完全 seed-robust**: 4/4 实验均 8/8 forward
- α=0.75: K≥3 从 6/8 提升到 8/8
- α=0.50: K≥3 从 6/8 降至 3/8（onset regime 信号弱，threshold 检测 seed 敏感）
- Drift 幅度跨 seed 一致（±3pp 以内），collapse 轨迹确定性强
- D105 true 3σ threshold 对 C4 域系统性为 0/8——C4 downstream drift 幅度不足以过 3σ

已完成：Registry 更新为 DONE、分析报告已注册为 artifact、westd-19828 双卡已释放。

---
