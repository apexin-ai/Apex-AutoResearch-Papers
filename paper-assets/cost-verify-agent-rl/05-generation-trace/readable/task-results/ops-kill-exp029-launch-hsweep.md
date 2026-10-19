# ops kill exp029 launch hsweep

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_exp029_launch_hsweep_20260517T041629_result.json`
- **Structured JSON:** [`7a6e3ccad6c9627c70b0.json`](../../sessions/7a/7a6e3ccad6c9627c70b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

1. **Step 15 checkpoint**: `/root/autodl-tmp/checkpoints/exp029/global_step_15/actor/huggingface` — 已确认存在
2. **exp029 kill**: 成功，两张 GPU 已释放（0MiB / 0%）
3. **Tatsu patch**: 已在 `train.py:4` 通过 `import patches.tatsu_parallel_fix` 自动激活，`launch_hsweep.sh` 无需额外配置
4. **h=2 seed 1 启动**:
   - PID: `920380`
   - tmux session: `hsweep_h2_s1`
   - 命令: `python train.py --config-name _alfworld_hsweep_h2 seed.train=10000 trainer.experiment_name=hsweep-h2-seed1`
   - Ray 已初始化，环境加载中（alfworld worker 已 spawn）
   - config 中 `step_independent_history_length: 2`（即 h=2）确认正确
5. **无异常** — 只有标准的 Gym deprecation warning，不影响运行

---
