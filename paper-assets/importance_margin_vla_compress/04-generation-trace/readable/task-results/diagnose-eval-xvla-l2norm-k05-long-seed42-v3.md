# diagnose eval xvla l2norm k05 long seed42 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_xvla_l2norm_k05_long_seed42_v3_20260523T190956_result.json`
- **Structured JSON:** [`a129c8f349d4c6386d9c.json`](../../sessions/a1/a129c8f349d4c6386d9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。根因已定位。

## 诊断结果

**两个 "long" 实验在同一时刻 (~03:01) 被同时杀死，为新实验腾出 GPU：**

| 实验 | 最后日志 | 死亡方式 | exit file |
|------|---------|---------|-----------|
| `eval_xvla_random_k05_long_seed42` | Ep 14/50 @ 03:01:38 | SIGHUP → "Terminated" | 有 (exit 129) |
| `eval_xvla_l2norm_k05_long_seed42_v3` | Ep 40/50 @ 03:01:42 | SIGKILL (无法捕获) | 无 |

**时间线：**
- 02:39 — spatial_v3 (GPU 0) + goal_v3 (GPU 1) 启动
- 02:46 — k03_spatial (GPU 2) 启动
- 02:50 — long_v3 (GPU 3) 启动
- **03:01 — 两个 long 实验被杀死**
- 03:02 — k03_goal_v4 (GPU 3) 启动，占用了 long_v3 的 GPU

**排除项：**
- RAM：1TB 总量，仅用 158GB → 非系统 OOM
- GPU 显存：每卡 98GB，仅用 ~5GB → 非 GPU OOM
- 磁盘：根分区 29%，数据盘 80% → 非磁盘满
- 代码 bug：无 traceback，random 版本同时被杀 → 非代码问题

```json
{"root_cause":"Agent framework killed tmux session to free GPU 3 for eval_xvla_l2norm_k03_goal_seed42_v4. SIGKILL sent at ~03:01:42, preventing EXIT trap. Sibling session eval_xvla_random_k05_long_seed42 killed simultaneously (SIGHUP exit 129 at same timestamp confirms coordinated preemption).","error_type":"infrastructure","fix_steps":["重新提交 eval_xvla_l2norm_k05_long_seed42_v3，确保不与其他实验竞争同一 GPU","提交前检查 GPU 占用：nvidia-smi 确认目标 GPU 空闲","如需并发运行超过 4 个实验，需排队而非同时提交"],"can_auto_fix":true}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "Agent framework killed tmux session to free GPU 3 for eval_xvla_l2norm_k03_goal_seed42_v4. SIGKILL sent at ~03:01:42, preventing EXIT trap. Sibling session eval_xvla_random_k05_long_seed42 killed simultaneously (SIGHUP exit 129 at same timestamp confirms coordinated preemption).",
    "error_type": "infrastructure",
    "fix_steps": [
      "重新提交 eval_xvla_l2norm_k05_long_seed42_v3，确保不与其他实验竞争同一 GPU",
      "提交前检查 GPU 占用：nvidia-smi 确认目标 GPU 空闲",
      "如需并发运行超过 4 个实验，需排队而非同时提交"
    ],
    "can_auto_fix": true
  }
}
```

</details>

---
