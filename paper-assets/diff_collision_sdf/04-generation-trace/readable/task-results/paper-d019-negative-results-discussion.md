# paper d019 negative results discussion

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d019_negative_results_discussion_20260525T074027_result.json`
- **Structured JSON:** [`1a511d4c91f1eff7e939.json`](../../sessions/1a/1a511d4c91f1eff7e939.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `paper/section5_5_method_boundaries.md`。内容覆盖了 D019 Tier A 的三个核心 negative results：

**Boundary 1: Gradient correction fails on collapsed policies**
- 实验设置：3 组 GT SDF oracle (`oracle_true_gt_adaptive_alpha_v11`, `oracle_true_gt_fixed_alpha_v11`, `oracle_true_gt_feature_object_v11`) + A3 learned SDF (`eval_a3_object_m024fix_v11`)
- 结果：所有 oracle CAR (73.1%–76.9%) 均低于未修正 baseline (82%–83%)；A3 learned SDF 全 160 episodes 零修正步
- 为什么 informative：失败与 SDF 质量/梯度空间/步长策略无关，根因是 collapsed policy 没有可操作的轨迹流形

**Boundary 2: Collision transfer in constrained geometries**
- 实验设置：Pi0.5+A1 Task 3 (bbq\_sauce)，wine\_bottle 和 red\_coffee\_mug 形成 ~40cm 走廊
- 结果：λ=0.005 CAR 降 8pp，red\_coffee\_mug 碰撞从 5→10 episodes；对比 Task 0 开放空间 CAR +49pp
- 为什么 informative：点级 SDF 梯度在多障碍约束场景下将碰撞从一侧转移到另一侧，有效性取决于自由空间裕度

**Boundary 3: Training-time integration is the only viable path**
- 综合前两个 boundary：post-hoc 修正在 collapsed policy 上无效 + 点级梯度在窄走廊反效果 → training-time SDF auxiliary loss 是唯一产生真实避碰 (CAR\_f > 0, frozen\_rate = 0%) 的路径

叙事用 "we demonstrate" 框架，无 AI 风格标记（无 em-dash、无 -ing 结尾、无过度分段）。下一步可转为 LaTeX 并插入 `analysis_claim3.tex` 之后。

---
