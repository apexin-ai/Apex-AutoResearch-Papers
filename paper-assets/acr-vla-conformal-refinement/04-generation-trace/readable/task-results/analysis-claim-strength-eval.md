# analysis claim strength eval

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_claim-strength-eval_20260513T214304_result.json`
- **Structured JSON:** [`4ce3cd9642635175c256.json`](../../sessions/4c/4ce3cd9642635175c256.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/claim-strength-analysis.md`。核心结论：

**支撑矩阵：**

| Claim | 强度 | 状态 |
|-------|------|------|
| C1: Per-DOF > scalar | **Moderate** | MVP 合成数据通过，LIBERO 零验证 |
| C2: ACI+COC calibration | **No Evidence** | 零实验数据 |
| C3: SRPO stacking | **No Evidence** | 零实验数据 |

**当前数据实况 vs 你提到的数字：**
- eval-spatial-v5-full: 仅完成 2/10 tasks（90%, 80%），Task 3 正在跑且目前 0/5。"85% 均值"只是前 2 tasks 的部分数据，最终可能显著变化
- ReconVLA: 前 2 tasks 90%，但在标准环境（无 perturbation）下 ReconVLA 本就应该 ≥ baseline
- eval-object-v4-full: 第 1 个 task 0/5，信号不乐观
- CRM 训练正常收敛（val_loss 0.0094, epoch 32/50）

**最紧急的 3 步：**
1. 等 crm-train-v1 完成 → **立即启动 ACR-VLA eval** — C1 的首个 real 数据点
2. 等 eval-spatial-v5-full 完成 → **SFT gate 判定**（<50% 则所有后续实验存疑）
3. **排期 A3 ablation (obs_only CRM)** — C1 的 make-or-break test

---
