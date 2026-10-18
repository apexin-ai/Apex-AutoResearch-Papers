# diagnose eval pi05 baseline goal seed42 strict

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_baseline_goal_seed42_strict_20260527T054925_result.json`
- **Structured JSON:** [`7096a388dda87d6d4cbd.json`](../../sessions/70/7096a388dda87d6d4cbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 诊断结果

**日志分析**：48 行日志，最后一行 `T3 [open the top drawer and put the bowl ins] ep=20: 17/20=85%` (13:34:45)，之后日志无任何输出——无 Traceback、无 Error、无 OOM、无 Segfault。进程静默死亡。

**进程状态**：PID 972711 已不存在。

**系统资源**：
- 系统内存 1TB，可用 ~994GB → 不是系统 OOM
- 4 块 GPU 当前全部被其他 python 进程占用（~15.7GB/24GB each）
- GPU 0 当前由 PID 896333 占用

**根因判断**：进程在 T3 ep=20 期间被外部信号（SIGKILL/SIGTERM）杀死。证据：
1. `python -u`（unbuffered）模式下 Python 异常一定会写入日志，但日志中无任何异常
2. 运行 39 分钟后突然中断，前 3 个 task 完全正常
3. 4 块 GPU 满载运行，可能是 GPU 调度系统或其他实验启动时杀掉了该进程

**已完成的进度**：
| Task | 描述 | SR |
|------|------|----|
| T0 | open the middle drawer of the cabinet | 46/50 = 92.0% |
| T1 | put the bowl on the stove | 50/50 = 100.0% |
| T2 | put the wine bottle on top of the cabinet | 48/50 = 96.0% |
| T3 | open the top drawer and put the bowl in | 17/20 (未完成) |
| T4-T9 | 未开始 | — |

累计已完成：144/150 = 96.0%（前 3 个 task）

```json
{"root_cause":"进程在T3 ep=20后被外部SIGKILL静默杀死——日志无任何Traceback/Error/OOM，python -u模式下Python异常必会输出，系统RAM充裕(994GB free)，判断为GPU调度冲突或其他进程抢占GPU 0导致进程被kill","error_type":"infrastructure","fix_steps":["用CUDA_VISIBLE_DEVICES=<空闲GPU>隔离GPU，避免与其他实验冲突","在tmux中用nohup运行，防止session断开","重跑时可用--resume_from_task 3跳过已完成的T0-T2(如脚本支持)，否则全量重跑","重跑命令: CUDA_VISIBLE_DEVICES=2 python -u eval_pi05_pruning_libero.py --prune_mode none --suite libero_goal --n_episodes 50 --seed 42 --gpu 0"],"can_auto_fix":true,"partial_results":"T0=92.0%, T1=100.0%, T2=96.0% 已完成(144/150=96.0%), T3在ep20/50处中断, T4-T9未开始"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "进程在T3 ep=20后被外部SIGKILL静默杀死——日志无任何Traceback/Error/OOM，python -u模式下Python异常必会输出，系统RAM充裕(994GB free)，判断为GPU调度冲突或其他进程抢占GPU 0导致进程被kill",
    "error_type": "infrastructure",
    "fix_steps": [
      "用CUDA_VISIBLE_DEVICES=<空闲GPU>隔离GPU，避免与其他实验冲突",
      "在tmux中用nohup运行，防止session断开",
      "重跑时可用--resume_from_task 3跳过已完成的T0-T2(如脚本支持)，否则全量重跑",
      "重跑命令: CUDA_VISIBLE_DEVICES=2 python -u eval_pi05_pruning_libero.py --prune_mode none --suite libero_goal --n_episodes 50 --seed 42 --gpu 0"
    ],
    "can_auto_fix": true,
    "partial_results": "T0=92.0%, T1=100.0%, T2=96.0% 已完成(144/150=96.0%), T3在ep20/50处中断, T4-T9未开始"
  }
}
```

</details>

---
