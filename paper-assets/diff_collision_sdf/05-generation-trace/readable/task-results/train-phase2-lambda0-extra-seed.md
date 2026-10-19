# train phase2 lambda0 extra seed

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_phase2_lambda0_extra_seed_20260527T132032_result.json`
- **Structured JSON:** [`7d8dc7f294b421e55c28.json`](../../sessions/7d/7d8dc7f294b421e55c28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Stage 1 训练已成功启动并进入 RUNNING 状态。

**总结**：

- **问题**：seed0 和 seed1 都没有 10K SDF checkpoint（原 30K 训练的中间 checkpoint 已清理），两台服务器均无。
- **解决方案**：先跑 **Stage 1** —— 为 seed0 做一次 10K 步 SDF 训练（λ=0.005），生成所需的 10K checkpoint。
- **当前状态**：Stage 1 在 westd-35807 cuda:1 上运行中
  - tmux session: `phase2_stage1_s0`
  - PID: 829727
  - 速度: ~2.7s/step，预计 ~7.4h 完成
  - Checkpoint 输出: `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/phase2_stage1_seed0_l005/10000/`
  - 环境: `conda activate libero`（不是 `base`——`base` 的 lerobot 版本缺 tasks.jsonl 支持）

**后续步骤**（Stage 1 完成后）：
1. 将 10K checkpoint 复制到 `a1_sdf_pi05_object_pudding_seed0_l0/10000/`
2. 启动 Stage 2: `--lambda_sdf 0 --seed 0 --resume --num_train_steps 30000`（从 10K resume 到 30K = 20K λ=0 步，~14h）

**修正了任务模板中的两个问题**：
1. `--gpu` 参数应与 `CUDA_VISIBLE_DEVICES` 一致（都用 1），不是 0——脚本内部会用 `args.gpu` 覆盖 `CUDA_VISIBLE_DEVICES`
2. 必须用 `conda activate libero`（不是 `base`），因为 base 的 lerobot 版本不兼容本地数据集格式

---
