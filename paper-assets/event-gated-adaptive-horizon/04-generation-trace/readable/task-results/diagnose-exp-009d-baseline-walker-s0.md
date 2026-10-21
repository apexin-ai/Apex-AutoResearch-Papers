# diagnose exp 009d baseline walker s0

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_009d_baseline_walker_s0_20260515T123241_result.json`
- **Structured JSON:** [`8af42fc9faae7e123413.json`](../../sessions/8a/8af42fc9faae7e123413.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。当前进程活跃（State=R, 435线程, 3GB RSS, tfevents 82秒前更新）。

## 诊断结果

**时间线重构：**

| 时间 | 事件 |
|------|------|
| 20:09:52 | Run 1 启动，MUJOCO_GL=egl 但 **libegl1/libegl-mesa0 未安装** → 仅写入 88B tfevents（立即失败） |
| 20:13:14 | Run 2 提交 → **submit_training_job 杀死 run 1 的 tmux session** → SIGHUP (129) |
| 20:14:05 | Run 3 提交 → 杀死 run 2 → SIGHUP (129) |
| **20:14:10** | **`apt-get install -y libegl1-mesa-dev libgl1-mesa-glx`** 安装了 `libegl1`, `libegl-mesa0`, `libgbm1` 等 EGL 运行时库 |
| 20:25:05 | Run 4 提交 → 杀死 run 3 → SIGHUP (129)。**此次 EGL 库已就位，运行正常** |

**关键证据：**
- 4 个 tfevents 文件对应 4 次启动，间隔 3.4min / 0.8min / 11min
- Run 1 仅 88 字节（header only），证明 EGL init 立即失败
- apt history 明确记录 20:14:10 安装 EGL 库
- 当前 run 4 已到 step 8000，eval/train 均正常产出

```json
{"root_cause":"submit_training_job repeated resubmission killed previous tmux sessions (SIGHUP). Root trigger: libegl1/libegl-mesa0 runtime libraries missing before 20:14:10, causing MUJOCO_GL=egl init failure. apt-get installed them at 20:14:10. Run 4 (post-install) is healthy at step 8000+.","error_type":"infrastructure","fix_steps":["No action needed - current run 4 is healthy and progressing normally","For future: ensure libegl1-mesa-dev is pre-installed before submitting EGL-based experiments","Avoid re-calling submit_training_job for same experiment name while previous run is active"],"can_auto_fix":false,"mujoco_gl_issue":false}
```

**总结**：三次 SIGHUP 都是 `submit_training_job` 重复提交同名实验时杀死前一个 tmux session 导致的。根本触发原因是 EGL 运行时库缺失（20:14:10 才装上）。当前 run 4 运行正常，无需干预。`MUJOCO_GL=egl` 配置本身没问题（conda activate.d 一致），只是之前缺库。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "submit_training_job repeated resubmission killed previous tmux sessions (SIGHUP). Root trigger: libegl1/libegl-mesa0 runtime libraries missing before 20:14:10, causing MUJOCO_GL=egl init failure. apt-get installed them at 20:14:10. Run 4 (post-install) is healthy at step 8000+.",
    "error_type": "infrastructure",
    "fix_steps": [
      "No action needed - current run 4 is healthy and progressing normally",
      "For future: ensure libegl1-mesa-dev is pre-installed before submitting EGL-based experiments",
      "Avoid re-calling submit_training_job for same experiment name while previous run is active"
    ],
    "can_auto_fix": false,
    "mujoco_gl_issue": false
  }
}
```

</details>

---
