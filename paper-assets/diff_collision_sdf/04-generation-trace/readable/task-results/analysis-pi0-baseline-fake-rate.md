# analysis pi0 baseline fake rate

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pi0_baseline_fake_rate_20260525T080316_result.json`
- **Structured JSON:** [`6f2a023b4fdce37e60d2.json`](../../sessions/6f/6f2a023b4fdce37e60d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

## 结果

| 模型 | Suite | Fake Safe% | 非碰撞中冻结比例 |
|------|-------|-----------|----------------|
| **Pi0 Full-FT** | object | **82.5%** | 99.4% |
| **Pi0 LoRA** | object | **89.0%** | 98.9% |
| A1 LoRA | object | 91.1% | 99.6% |
| A3 | object | 76.4% | 99.0% |
| Pi0 Full-FT | spatial | 0% (100%碰撞) | N/A |
| Pi0 LoRA | spatial | 0% (100%碰撞) | N/A |

**关键发现**：
1. **Fake safety 是 Pi0 自身的行为**，不是 A1/A3 引入的。Pi0 baseline Full-FT 82.5%、LoRA 89.0% 的 episode 都是 frozen（<0.1mm displacement），与 A1 的 91.1% 在同一量级。
2. 非碰撞 episode 中 **98.9%~99.6% 都是冻结的**——中位 displacement 仅 ~5 纳米。冻结和真正运动之间差 6 个数量级，阈值很稳健。
3. Spatial suite 所有 baseline 100% 碰撞，无法计算 fake rate。

报告已写入 `artifacts/report_pi0_baseline_fake_rate.md`。

---
