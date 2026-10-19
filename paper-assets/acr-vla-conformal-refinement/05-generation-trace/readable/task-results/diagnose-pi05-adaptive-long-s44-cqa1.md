# diagnose pi05 adaptive long s44 cqa1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_pi05-adaptive-long-s44-cqa1_20260526T093118_result.json`
- **Structured JSON:** [`072803903d6a8adc2bd8.json`](../../sessions/07/072803903d6a8adc2bd8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。两台服务器是**不同的失败原因**。

---

## cqa1-32758：监控误报（实验实际正在运行）

3 个"失败"实验**实际上在正常运行**，已完成多个 task 的评估：

| 预期 tmux 名 | 实际 tmux 名 | GPU | PID | 状态 |
|---|---|---|---|---|
| pi05-adaptive-long-s44-cqa1 | pi05-long-s44 | GPU 3 | 197917 | 正在跑 long seed44 |
| pi05-adaptive-long-s43-cqa1 | pi05-long-s43 | GPU 4 | 198442 | 正在跑 long seed43 |
| pi05-adaptive-object-s44-cqa1 | pi05-obj-s44 | GPU 5 | 199049 | 正在跑 object seed44 |

**原因**：这 3 个实验在 13:54-13:55 用**简短 tmux session 名**手动启动，未走标准部署流程（无 exit trap、无 `~/runs/` 日志重定向）。监控系统找不到预期的 session 名 → 5 次探测失败 → auto-resolved as failed。

## bjb1-18228：实验从未启动

3 个失败实验（pi05-crm-k2-object-s42/43/44-bjb1）**零痕迹**——无进程、无 tmux session、无日志、无 exit 文件。

4 块 GPU 全被占满：
- GPU 0: crm_obs_only long seed42 (nohup 启动, PID 2558, 11:45)
- GPU 1: crm_obs_only long seed43 (nohup 启动, PID 2916, 11:45)
- GPU 2: adaptive goal seed43 (标准部署, PID 42110, 14:45)
- GPU 3: adaptive long seed42 (nohup 启动, PID 3764, 11:48)

GPU 0/1/3 上的 3 个实验是通过 `nohup` 手动启动的（无 tmux 管理），占满了 GPU 资源，导致后续 3 个 crm-k2-object 实验无法启动。

---

```json
{"root_cause":"cqa1: tmux session名不匹配（pi05-long-s44 vs 预期 pi05-adaptive-long-s44-cqa1），实验正常运行但监控不可见; bjb1: 4 GPU 全被 nohup 手动进程占满（PID 2558/2916/3764 + 42110），crm-k2-object 实验从未启动","error_type":"infrastructure","fix_steps":["cqa1无需修复——3个实验正在正常运行，等待完成后收集结果即可","bjb1需等待 GPU 0/1/3 的 nohup 进程完成或手动 kill 后重新部署 pi05-crm-k2-object-s42/43/44-bjb1","未来部署统一使用标准 agent-ml tmux 模板，避免手动 nohup 或简短 session 名"],"can_auto_fix":false,"affected_experiments":["pi05-adaptive-long-s44-cqa1","pi05-adaptive-long-s43-cqa1","pi05-adaptive-object-s44-cqa1","pi05-crm-k2-object-s42-bjb1","pi05-crm-k2-object-s43-bjb1","pi05-crm-k2-object-s44-bjb1"]}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "cqa1: tmux session名不匹配（pi05-long-s44 vs 预期 pi05-adaptive-long-s44-cqa1），实验正常运行但监控不可见; bjb1: 4 GPU 全被 nohup 手动进程占满（PID 2558/2916/3764 + 42110），crm-k2-object 实验从未启动",
    "error_type": "infrastructure",
    "fix_steps": [
      "cqa1无需修复——3个实验正在正常运行，等待完成后收集结果即可",
      "bjb1需等待 GPU 0/1/3 的 nohup 进程完成或手动 kill 后重新部署 pi05-crm-k2-object-s42/43/44-bjb1",
      "未来部署统一使用标准 agent-ml tmux 模板，避免手动 nohup 或简短 session 名"
    ],
    "can_auto_fix": false,
    "affected_experiments": [
      "pi05-adaptive-long-s44-cqa1",
      "pi05-adaptive-long-s43-cqa1",
      "pi05-adaptive-object-s44-cqa1",
      "pi05-crm-k2-object-s42-bjb1",
      "pi05-crm-k2-object-s43-bjb1",
      "pi05-crm-k2-object-s44-bjb1"
    ]
  }
}
```

</details>

---
