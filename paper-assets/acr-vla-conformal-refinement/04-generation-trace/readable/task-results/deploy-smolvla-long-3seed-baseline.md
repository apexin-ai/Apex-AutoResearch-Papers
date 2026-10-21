# deploy smolvla long 3seed baseline

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_smolvla-long-3seed-baseline_20260522T173121_result.json`
- **Structured JSON:** [`91409ebf04ef5e07c049.json`](../../sessions/91/91409ebf04ef5e07c049.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 eval 进程全部正常运行：

| Seed | PID | GPU | 进度 | 当前成功率 |
|------|-----|-----|------|-----------|
| 42 | 509914 | cuda:0 | step 239/520, task 0 batch 1 | 30% |
| 43 | 511214 | cuda:1 | task 1 完成 (20%), 开始 task 2 | 20% |
| 44 | 516473 | cuda:2 | step 300/520, task 0 batch 1 | 30% |

**已完成部署：**
- 服务器：bjb1-32546，GPU 0/1/2
- 命令：`lerobot-eval --env.task=libero_10 --eval.n_episodes=20 --eval.batch_size=10 --seed=42/43/44`
- 关键参数：`HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1`，`--rename_map` 映射 image→camera1/image2→camera2
- 每个 seed 跑 10 task × 20 episodes = 200 episodes，max_steps=520
- Registry：`eval-smolvla-lerobot-long-seed42/43/44` 已注册 RUNNING
- 日志：`/tmp/eval_smolvla_long_seed{42,43,44}.log`
- 输出：`/root/outputs/eval/smolvla_long_seed{42,43,44}/eval_info.json`

预估运行时间：每 task ~2 min × 10 tasks ≈ 20-30 min/seed。seed 43 进度最快（已完成 task 0），约 20-25 min 后全部完成。

---
