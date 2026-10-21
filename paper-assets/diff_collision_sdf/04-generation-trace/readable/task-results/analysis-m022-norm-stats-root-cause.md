# analysis m022 norm stats root cause

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_m022_norm_stats_root_cause_20260522T153739_result.json`
- **Structured JSON:** [`4008e449551ef29491fe.json`](../../sessions/40/4008e449551ef29491fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/analysis_m022_norm_stats_root_cause.md`。

核心结论：

1. **norm_stats 不是根因** — A3/baseline/A1 三者的 norm_stats 字节级一致，加载链路也正确
2. **SDF 精炼从未触发** — 200 episodes 中 refine_count=0，SDF decoder 对所有位置预测 SDF≥0.46，远超 margin=0.01
3. **真正的根因是 A3 LoRA 训练退化** — refine_loss（MSE(v_t, v_t_refined.detach())）在 SDF decoder 未充分校准时将 LoRA 拉向保守不动点，模型学会了"不动=安全"，导致 pi0_base+A3_LoRA 对真实观测输出近零动作
4. **附带 bug**：`_refine_action_a3()` 把 delta action 当作绝对坐标传给 SDF decoder（`next_ee = action[:3]` 应为 `next_ee = current_ee + action[:3]`），当前因精炼不触发而潜伏

建议首先用 `--no_refine` 跑 A3 eval 验证 LoRA 退化假设，然后修复坐标 bug，最后调整训练策略重训（降低 λ_refine / 用 curriculum / 用 baseline 权重做 base）。

---
