# analysis exp 031b tcn pickcube s0 sigma05

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_031b_tcn_pickcube_s0_sigma05_20260521T084339_result.json`
- **Structured JSON:** [`76c320addca22128ef65.json`](../../sessions/76/76c320addca22128ef65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## exp_031b 结果总结

**Conclusion: SUCCESS** — σ=0.5 成功抑制 PickCube 的 CIVO（修正了自动判定的 negative）

### 核心发现

| 指标 | exp_031 (σ=0.2) | exp_031b (σ=0.5) |
|------|------------------|-------------------|
| NVE peak | 3.71 | **3.3** |
| CIVO 恢复 | 未恢复 | **自行恢复** (step 72.5k) |
| NVE final | — | **0.2** |
| Eval reward final | — | 25.5 |

### NVE 轨迹关键点
- 早期短暂 CIVO 爆发：steps 22.5k–42.5k（peak 3.3）
- Step 52.5k 开始回落（NVE 1.1），step 72.5k 完全抑制（NVE 0.7）
- 此后 70% 训练过程 NVE 稳定在 0.2–0.3

### Dose-response 结论
σ=0.2→0.5 是 PickCube 环境 CIVO 抑制的有效阈值区间。σ=0.5 虽未完全消除早期 CIVO 爆发，但提供了足够的正则化使系统自行恢复，这是 σ=0.2 做不到的。

### 已完成
- 报告写入 artifacts 并注册 (art_20260521_d49d47)
- Registry 更新：conclusion=success, metrics, checkpoint_path, log_path

---
