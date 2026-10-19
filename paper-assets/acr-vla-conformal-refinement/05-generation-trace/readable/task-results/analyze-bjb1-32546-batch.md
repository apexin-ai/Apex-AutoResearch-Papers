# analyze bjb1 32546 batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_bjb1-32546-batch_20260520T103702_result.json`
- **Structured JSON:** [`fb6884ac1416df786569.json`](../../sessions/fb/fb6884ac1416df786569.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部已完成，registry 已更新为 DONE。

## 汇总

| 实验 | SR | 100 rollouts | 结论 | 备注 |
|------|-----|-------------|------|------|
| eval-adaptive-k-spatial-p75-seed43 | **34.0%** | 34/100 | success | vs baseline 34.4±1.5% — 匹配，fast_path=62.2%, avg_k=5.0 |
| eval-obs-only-object-norm003-seed43-r2 | **14.0%** | 14/100 | success | ε=0.03 Object seed43 数据点，Figure 2 补充 |
| eval-obs-only-object-norm005-seed44 | **12.0%** | 12/100 | success | ε=0.05 Object seed44 数据点，Figure 2 补充 |

**关键发现：**
- Adaptive K P75 在 Spatial seed43 上 SR=34.0%，与 CRM K=10 baseline (34.4%) 基本持平，同时 62.2% 的步骤走了 fast path（k<10），验证了 adaptive 策略在跨 benchmark 迁移时保持性能。
- 两个 obs_only 低 norm 实验（ε=0.03/0.05）SR 都很低（14%/12%），符合预期——小 ε 限制了 CRM 纠正幅度，为 Figure 2 的 ε-SR 曲线提供了多 seed 数据点。

---
