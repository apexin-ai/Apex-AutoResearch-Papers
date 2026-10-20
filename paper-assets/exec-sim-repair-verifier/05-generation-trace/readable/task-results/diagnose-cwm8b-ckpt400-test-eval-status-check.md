# diagnose cwm8b ckpt400 test eval status check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cwm8b-ckpt400-test-eval_status-check_20260515T145904_result.json`
- **Structured JSON:** [`65e12eebd46a0f65c551.json`](../../sessions/65/65e12eebd46a0f65c551.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 任务 1: cwm8b-ckpt400-test-eval

**进程实际上是活的。** PID 381618 在 GPU 3 上运行（22516MiB, 89% util），最后日志 22:58:40 显示 520/9784。

```json
{"root_cause":"进程曾多次崩溃后被auto-resume重启，当前实例22:38启动正在正常运行，旧崩溃日志已被覆盖无法确定历史死因","error_type":"infrastructure","fix_steps":["当前无需修复，进程正在运行","持续监控：当前速率~57s/8条，预计还需~18h完成剩余9256条","如再次崩溃，检查dmesg/syslog排查GPU错误"],"can_auto_fix":true,"partial_results":"有，528条已完成（359条前轮+169条本轮），存于results_incremental.jsonl(1.8MB)"}
```

## 任务 2: s42-extended-val-sweep

- **tmux session `s42-val-sweep`: DEAD**
- 日志仅 72 行，只启动了 **checkpoint-1800** 的评估
- checkpoint-1800 评估到 560/9335（running_acc=87.7%）后停止，最后日志 22:16:22
- summary JSON 只有空 header，无任何完成的 checkpoint 结果
- **0 个 checkpoint 完成**

可能原因：sweep 启动于 22:14，仅运行 2 分钟后 tmux 会话死亡。所有 4 个 GPU 当前都被其他进程占满（GPU0=ablation, GPU1/2=其他实验, GPU3=cwm-eval），如果 sweep 指定了 cuda:0 则因资源冲突失败。需要等 ablation 完成后腾出 GPU 重跑。

## 任务 3: cwm-rank32-alpha64-ablation

- **PID 379614 在 GPU 0 运行中**（20926MiB, 76% util）
- **当前 step: 758 / 1434（52.9%）**
- 速率: ~3.35s/step
- 上次 eval（step 478）: eval_loss=0.0665
- **预估剩余: (1434-758) × 3.35s ≈ 2265s ≈ ~38 min**（加上后续 eval checkpoint 约 40-42 min）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "进程曾多次崩溃后被auto-resume重启，当前实例22:38启动正在正常运行，旧崩溃日志已被覆盖无法确定历史死因",
    "error_type": "infrastructure",
    "fix_steps": [
      "当前无需修复，进程正在运行",
      "持续监控：当前速率~57s/8条，预计还需~18h完成剩余9256条",
      "如再次崩溃，检查dmesg/syslog排查GPU错误"
    ],
    "can_auto_fix": true,
    "partial_results": "有，528条已完成（359条前轮+169条本轮），存于results_incremental.jsonl(1.8MB)"
  }
}
```

</details>

---
