# scan tau k sweep k5 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_scan_tau-k-sweep-k5-status_20260524T201027_result.json`
- **Structured JSON:** [`d5243ce4e916a34c948a.json`](../../sessions/d5/d5243ce4e916a34c948a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入并注册（`art_20260524_439d7f`）。

## 关键发现

**τ-sweep（Spatial, seed=42）全部完成**：
| τ    | SR     | trigger |
|------|--------|---------|
| 0.10 | 79.0%  | 75.2%   |
| 0.15 | 80.5%  | 40.7%   |
| **0.20** | **81.0%**  | 26.6%   |
| 0.25 | 79.5%  | 19.6%   |
| 0.30 | 80.5%  | 16.7%   |
→ **τ=0.20 是峰值**，触发率随 τ 单调下降，SR 平稳；τ=0.10 高触发率反而降低 SR（过度修正）。

**K-sweep**：
- K=1：79.5%（= τ=0.25 单样本，共用同名 JSON）
- K=2：**仅 seed 46 + vla_only mean 版本**（80.0%），缺 seed 42 adaptive_conformal_crm 版本
- K=5：bjb2 仍在运行，7/10 任务完成，累计 109/140（77.9%），ETA ~50-60min

**资源**：
- bjb1-32546：6 张 GPU 全空闲，可立即接新任务（建议补 K=2 adaptive seed=42）
- bjb2-40593：GPU 0 跑 K=5，~1h 后释放

---
