# ops sync and launch baseline v11

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_sync_and_launch_baseline_v11_20260522T120107_result.json`
- **Structured JSON:** [`7f95b293a1c546786943.json`](../../sessions/7f/7f95b293a1c546786943.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 确认成功运行。总结：

**1. 文件同步** ✅
- 通过 SSH 密钥互信 + SCP 从 westd-45947 直接传输到 westd-35807
- MD5 校验通过：`dccc40763ac344ca19c69de2062e54e8`（977 行, 38631 bytes）
- action chunking 修复已包含（replan_steps:3, deque:2, action_queue:5, warmup:2）

**2. Checkpoint 路径**
- `/root/autodl-tmp/checkpoints/baseline_object_pudding/baseline_object_pudding_seed0/best`
- 与 westd-45947 上的 `baseline_object_pudding_eval/best` MD5 一致（`f3687b79ae43af8334bba77847a8ee6d`）
- config_name: `pi0_libero_low_mem_finetune`

**3. Eval 启动确认** ✅
- tmux session: `eval_baseline_v11`
- PID: 527472（running, 235 threads）
- GPU: cuda:1（10% util, 8458 MiB）
- cuda:0 和 cuda:2 的训练未受影响
- 参数: `--suite safelibero_object --n_episodes 50 --max_steps 300 --replan_steps 5 --gpu 1`
- Task 0 Episode 10/50 已完成，eval 正常推进中

**4. 预计运行时间**
- AUTOTUNE 编译已完成（~5 min）
- Episode 10/50 at Task 0 运行中
- 4 tasks × 50 episodes，预计总计 ~2-4h

日志: `/tmp/eval_baseline_v11.log`
结果保存到: `/root/autodl-tmp/eval_results/baseline_v11_eval_safelibero_object_all_levelII_best_seed0.json`

---
