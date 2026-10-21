# diagnose ess only seed123 r2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_ess_only_seed123_r2_20260517T210755_result.json`
- **Structured JSON:** [`24e72d393cf6d052eb2d.json`](../../sessions/24/24e72d393cf6d052eb2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 结论

**根因：外部 SIGTERM（exit code 143），由 agent-ml-research 框架的 `kill_job` 工具发送。**

### 证据链

| 证据 | 说明 |
|------|------|
| Exit code 143 | = 128 + 15 (SIGTERM)，是**主动 kill**，不是 OOM（OOM 是 137/SIGKILL）|
| 两个进程间隔 1 秒死亡 | `ess_only_seed123` 20:55:28Z, `ess_only_seed456` 20:55:29Z |
| 日志最后一行 | 正常训练进度后直接 `Terminated` + `EXIT_CODE=143`，无任何 error/traceback |
| `random_reweight_seed456` 诊断期间也被杀 | 21:09:54Z，同样 exit 143，说明有外部 agent **正在持续杀进程** |
| 系统资源完全健康 | RAM 956GB 可用, 磁盘 42%, GPU 显存正常 |
| 无系统级触发 | 无 cron job, 无 bash_history kill 记录, 无 OOM/kernel 日志, 服务器 51 天未重启 |

### 被杀进程完整时间线（全部 SIGTERM）

- `adaptive_fix_seed42` → 15:04:29Z
- `ess_only_seed123` → 20:55:28Z (step 2989/6103, 49%)
- `ess_only_seed456` → 20:55:29Z (step 2897/6103, 47%)
- `random_reweight_seed456` → 21:09:54Z (step 6617/8477, 78%，**诊断期间被杀**)

### 当前存活实验

- `ess_only_seed123_r2` (cuda:2): step 2230/6103, 正常运行
- `ess_only_seed456_r2` (cuda:1): step 2729/6103, 正常运行
- `qwen06b_uniform_seed42` (cuda:0): 正常运行
- **cuda:3 现已空闲**（random_reweight_seed456 刚被杀）

### Checkpoints 状态

两个 ess_only 实验的 checkpoint 完好：seed123 有 checkpoint-1500/2000/2500，seed456 有 checkpoint-1500/2000/2500。_r2 分别从 checkpoint-2000 和 checkpoint-2500 恢复，损失约 ~900 和 ~400 步。

```json
{"root_cause":"外部 SIGTERM (exit 143) 由 agent-ml-research kill_job 发送，非 OOM/非系统故障。另一个 agent session 正在主动管理 GPU 分配，持续杀进程（诊断期间 random_reweight_seed456 也被杀）","error_type":"infrastructure","fix_steps":["排查哪个 agent session 在调用 kill_job，停止其不当的 GPU 回收行为","当前 _r2 实验正在运行中，暂不需要额外操作","cuda:3 已空闲，如需恢复 random_reweight_seed456 可从其最近 checkpoint resume","监控 _r2 实验是否也会被同一机制杀掉"],"can_auto_fix":false,"affected_gpus":["cuda:1","cuda:2","cuda:3"]}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "外部 SIGTERM (exit 143) 由 agent-ml-research kill_job 发送，非 OOM/非系统故障。另一个 agent session 正在主动管理 GPU 分配，持续杀进程（诊断期间 random_reweight_seed456 也被杀）",
    "error_type": "infrastructure",
    "fix_steps": [
      "排查哪个 agent session 在调用 kill_job，停止其不当的 GPU 回收行为",
      "当前 _r2 实验正在运行中，暂不需要额外操作",
      "cuda:3 已空闲，如需恢复 random_reweight_seed456 可从其最近 checkpoint resume",
      "监控 _r2 实验是否也会被同一机制杀掉"
    ],
    "can_auto_fix": false,
    "affected_gpus": [
      "cuda:1",
      "cuda:2",
      "cuda:3"
    ]
  }
}
```

</details>

---
