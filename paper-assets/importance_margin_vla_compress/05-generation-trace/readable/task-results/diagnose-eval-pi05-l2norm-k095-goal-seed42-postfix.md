# diagnose eval pi05 l2norm k095 goal seed42 postfix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_l2norm_k095_goal_seed42_postfix_20260524T113820_result.json`
- **Structured JSON:** [`d10a517c419c7ffaa401.json`](../../sessions/d1/d10a517c419c7ffaa401.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

**实验实际上已成功完成，并非失败。**

### 关键发现

日志显示实验已正常运行完毕，最终结果：

```
RESULT: libero_goal prune=l2norm keep=0.95 SR=90.8%
Saved: /root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.95_libero_goal_seed42.json
```

### 各 Task 成绩

| Task | 描述 | SR |
|------|------|-----|
| T0 | open the middle drawer of the cabinet | 84% |
| T1 | put the bowl on the stove | 98% |
| T2 | put the wine bottle on top of the cabinet | 90% |
| T3 | open the top drawer and put the bowl in | 94% |
| T4 | put the bowl on top of the cabinet | 100% |
| T5 | push the plate to the front of the stove | 100% |
| T6 | put the cream cheese in the bowl | 92% |
| T7 | turn on the stove | 100% |
| T8 | put the bowl on the plate | 100% |
| T9 | put the wine bottle on the rack | 50% |

**总体 SR = 90.8%**，运行总时间 86.5 分钟，于 19:26 正常结束。

### GPU 状态

GPU 0 当前仍有一个 python 进程占用 ~10GB（可能是另一个评估任务），GPU 1 空闲。无 OOM 迹象。

### 失败根因

**误报（false positive）。** 实验已成功完成并保存了结果文件。监控系统报告 "process dead 5× with no sentinel/W&B" 可能是因为：
1. 实验完成后进程正常退出，监控在进程退出后检测到 "dead"
2. 该实验未配置 W&B logging 和 sentinel 文件，导致监控缺少完成信号

### 结论

- **无需重试** — 实验已成功，结果已保存
- 建议将此实验在追踪系统中标记为 completed（SR=90.8%）

---
