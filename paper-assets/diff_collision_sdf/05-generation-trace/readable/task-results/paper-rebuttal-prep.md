# paper rebuttal prep

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_rebuttal-prep_20260529T132102_result.json`
- **Structured JSON:** [`74279699c9d5ff300a6b.json`](../../sessions/74/74279699c9d5ff300a6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出文件已生成并注册：`artifacts/rebuttal_prep.md` (art_20260529_4fd438)

分类结果：
- **Method Negative (8)**: 3 个 GT oracle 均劣于 baseline、5 个 stepwise/早期信号 eval 确认 SDF 无信号、Phase 2 无持久效应、A3 refinement 从不触发、A1 91.5% CAR 全是 fake
- **Hyperparameter (6)**: 训练步数 16K-28K 全程 flat、3 种 alpha 策略（adaptive/fixed/feature-space）均无效
- **Scale/Generalization (5)**: spatial 场景所有方法 CAR≈0%，EE-only 无法应对 arm-body 碰撞
- **Evaluation Artifact (3)**: Pi0.5 capability-safety 反相关、baseline 的 action collapse 使 CAR 虚高至 82-83%
- **Engineering (3)**: M024 坐标 bug、M027 死代码、M026 decoder 失标——修复后仍 negative，确认非工程原因

每类附 1-2 个 Q&A 话术，另有 6 个通用问题应对（n=3 seeds 统计力、real hardware、benchmark scope、positive contribution、其他 geometric loss、full-body SDF）。

---
