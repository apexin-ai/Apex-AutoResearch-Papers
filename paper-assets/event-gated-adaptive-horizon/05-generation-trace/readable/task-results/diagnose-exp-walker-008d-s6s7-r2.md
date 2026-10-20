# diagnose exp walker 008d s6s7 r2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_walker_008d_s6s7_r2_20260527T235538_result.json`
- **Structured JSON:** [`c00128432bafbc8c1cb2.json`](../../sessions/c0/c00128432bafbc8c1cb2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 结论

**两组实验都是被外部 SIGTERM (signal 15) 同时杀死的，不是代码 crash。**

关键证据：
- s6 + s7 第一轮：同一秒死亡（07:20:15 / 07:20:16），日志明确记录 `Terminated` + `EXIT_CODE=143`
- s6_r2 + s7_r2 第二轮：同一秒死亡（07:42:39 / 07:42:46），日志在 "Start evaluation." 处截断（输出缓冲未刷新）
- 无 OOM（dmesg 空、容器无 kern.log）
- 无 GPU 错误（ECC N/A，无 XID）
- 磁盘充足（243GB free）
- 无 crontab
- 同服务器上的 cheetah_008a_s0 正常运行 2h45m 完成（EXIT_CODE=0）

**根因**：两个实验作为同一进程组的子进程启动（未做 nohup/tmux/disown 隔离），父进程（SSH session 或启动脚本）终止时整个进程组收到 SIGTERM。第一轮死在 training 阶段（step 8000），第二轮死在 eval 阶段（step 15000），"Start evaluation" 不是死因，只是恰好在那个时间点。

注意：GPU 0 仍有 49GB 残留显存（无进程），需要清理。

```json
{"root_cause":"External SIGTERM killed both processes simultaneously (EXIT_CODE=143). Processes were not daemonized — they shared a process group with the launching SSH session/parent, which terminated after ~11min (run1) and ~17.5min (run2). Evidence: paired processes died within 1 second of each other; no OOM/GPU error/disk issue; successful runs on same server completed in 2h45m.","error_type":"infrastructure","fix_steps":["清理 GPU 0 残留显存: nvidia-smi --gpu-reset -i 0 或重启进程","重新启动实验时使用 tmux 或 nohup 隔离: tmux new-session -d -s exp_s6 'nohup python -u dreamer.py ... > log 2>&1'","确保启动脚本中每个实验用 disown 或独立 tmux pane，避免进程组级联终止"],"can_auto_fix":true,"affects_submission":false}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "External SIGTERM killed both processes simultaneously (EXIT_CODE=143). Processes were not daemonized — they shared a process group with the launching SSH session/parent, which terminated after ~11min (run1) and ~17.5min (run2). Evidence: paired processes died within 1 second of each other; no OOM/GPU error/disk issue; successful runs on same server completed in 2h45m.",
    "error_type": "infrastructure",
    "fix_steps": [
      "清理 GPU 0 残留显存: nvidia-smi --gpu-reset -i 0 或重启进程",
      "重新启动实验时使用 tmux 或 nohup 隔离: tmux new-session -d -s exp_s6 'nohup python -u dreamer.py ... > log 2>&1'",
      "确保启动脚本中每个实验用 disown 或独立 tmux pane，避免进程组级联终止"
    ],
    "can_auto_fix": true,
    "affects_submission": false
  }
}
```

</details>

---
