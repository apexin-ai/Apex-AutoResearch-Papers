# ops exp026 verify launch

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp026_verify_launch_20260515T102849_result.json`
- **Structured JSON:** [`906470fc34883a5f1716.json`](../../sessions/90/906470fc34883a5f1716.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp026 启动验证结果：有问题**

```
tmux session: 无法验证（tmux 被 read_only 拦截），ps 中未见 tmux 进程
log status: 文件存在但 0 bytes（空），创建于 18:28
GPU 0: utilization 100%, memory 3/97887 MiB ⚠️
GPU 1: utilization 0%, memory 3/97887 MiB
pids.current: 773 / 20480
python processes: 1 (但是 dryrun)
```

**关键问题：**

1. **运行的不是正式训练，而是 dryrun 脚本** — PID 769499 执行的是 `run_exp026_dryrun.sh`，参数 `total_training_steps=2`，`experiment_name=exp026-dryrun`，输出到 `/root/autodl-tmp/checkpoints/exp026_dryrun/`

2. **dryrun 疑似卡死** — 17:56 启动，仅 2 步训练，已运行 33+ 分钟。GPU 0 显示 100% 利用率但只占用 3 MiB 显存，存在多个 zombie 进程（gcs_server、python×2、raylet 全部 defunct）

3. **exp026 正式日志为空** — `exp026_step_independent_grpo.log` 于 18:28 创建但 0 bytes，没有任何输出写入

4. **无 tmux session** — ps 中没有 tmux 进程，正式训练未通过 tmux 启动

**结论：exp026 正式训练未启动。** 当前只有一个可能已经卡死的 dryrun 在跑。需要先清理 zombie 进程和可能 hung 的 GPU，再启动正式训练。

---
