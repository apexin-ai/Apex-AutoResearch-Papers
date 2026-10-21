# diagnose eval acr spatial v3

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-acr-spatial-v3_20260514T202053_result.json`
- **Structured JSON:** [`e4dc27a0dda03013d165.json`](../../sessions/e4/e4dc27a0dda03013d165.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。结论与预期不同——进程没有 crash。

## 诊断结果

**两个 eval 进程仍然在运行。** "process dead" 是监控系统的误报。

| 实验 | 原始 PID | 实际 worker PID | 状态 | 进度 |
|------|----------|----------------|------|------|
| eval-acr-spatial-v3 | 197057 (session leader, 已退出) | 197062 (R, running) | 活跃 | 5/10 tasks 完成, task 6 rollout 5/10 |
| eval-acr-object-v3 | 197803 (session leader, 已退出) | 197808 (R, running) | 活跃 | 5/10 tasks 完成, task 6 rollout 5/10 |

**为什么监控报 dead：**
- 监控检测的是 session leader PID (197057/197803)，这些进程确实已退出
- 但实际 Python worker (197062/197808) 作为子进程仍在运行，wchan=0（CPU 活跃计算中）
- 没有 W&B 集成，没有 sentinel 文件，所以监控无法确认存活

**额外发现 — GPU 0 严重拥挤：**
- 4 个 Python 进程共享 GPU 0，共占 12.9GB / 24.5GB
- 197062: 3575MiB, 197808: 1873MiB, 231426(新): 3714MiB, 232820(新): 3714MiB
- GPU contention 可能导致每个 task ~1.6h（正常应更快）

**速度：** 8h 完成 5/10 tasks，预估全部完成需 ~16h。

```json
{"root_cause":"进程未crash——session leader PID退出但worker子进程(197062/197808)仍在运行(State:R, wchan=0)，监控误报process dead","error_type":"infrastructure","fix_steps":["监控系统应检测worker PID而非session leader PID","eval脚本应添加W&B心跳或定期sentinel写入","新实验231426/232820与旧实验共享GPU0导致contention，后续应隔离GPU分配"],"can_auto_fix":false,"affects_both":true}
```

既然这两个实验用的是旧的 un-normalized CRM checkpoint（D018 已判定有 scale 问题），且进程还在缓慢运行占 GPU，是否要 kill 掉 197062 和 197808 释放资源给新实验？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "进程未crash——session leader PID退出但worker子进程(197062/197808)仍在运行(State:R, wchan=0)，监控误报process dead",
    "error_type": "infrastructure",
    "fix_steps": [
      "监控系统应检测worker PID而非session leader PID",
      "eval脚本应添加W&B心跳或定期sentinel写入",
      "新实验231426/232820与旧实验共享GPU0导致contention，后续应隔离GPU分配"
    ],
    "can_auto_fix": false,
    "affects_both": true
  }
}
```

</details>

---
