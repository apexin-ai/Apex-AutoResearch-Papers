# diagnose exp 008 base pretrained eval v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_008_base_pretrained_eval_v2_20260515T114200_result.json`
- **Structured JSON:** [`ee4e3605beae60f267ff.json`](../../sessions/ee/ee4e3605beae60f267ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。结论如下：

## 诊断结果

### v1: 确认 OOM Killer
```
bash: line 1: 530892 Killed
EXIT_CODE=137
```
在 HumanEval 51/164 处被 Linux OOM killer 杀掉。v1 命令未包含 `source /etc/network_turbo`，HuggingFace 连接超时反复重试（日志前 20 行全是 `ConnectTimeoutError`），可能加剧了内存压力。

### v2: **当前仍在运行，未失败**
- PID 553256，启动于 `Fri May 15 19:31:00 2026`（约 13 分钟前）
- 日志已推进到 **GSM8K 124/1319 (9%)**，远超你报告的 80/1319
- GPU 2 占用 3612MiB / 24564MiB，35% 利用率
- RSS 1.86GB，系统 RAM 958GB available — 内存充裕

**你看到的"v2 失败"很可能是之前一次运行（日志已被当前 `tee` 覆盖）。当前 v2 是一个重新提交的运行，正在正常执行。**

### 风险评估
当前 6 个 GPU 全部在跑任务，但系统 RAM 有 958GB 可用。只要其他进程不突然暴增 RAM 使用，这次 v2 应该能完成。GSM8K 还需约 1.5 小时，之后是 ARC（MC 任务，快）和 HumanEval（164 样本，~14 分钟）。

### v1 OOM 根因
`max_new_tokens=512` 设置合理。v1 的 OOM 最可能原因是**当时其他并发进程的 RAM 消耗**导致系统级内存压力，而非 evaluate.py 本身内存泄漏。

```json
{"root_cause":"v1: Linux OOM killer (bash: 530892 Killed, EXIT_CODE=137), triggered during HumanEval generation under system-wide RAM pressure from concurrent GPU jobs. v2: NOT failed — PID 553256 actively running at GSM8K 124/1319","error_type":"resource","fix_steps":["当前v2正在运行，先观察是否能完成","若再次OOM，用ulimit或cgroup限制其他进程的RAM，或错峰运行","v1缺少source /etc/network_turbo导致HF超时，v2已修复"],"can_auto_fix":false}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "v1: Linux OOM killer (bash: 530892 Killed, EXIT_CODE=137), triggered during HumanEval generation under system-wide RAM pressure from concurrent GPU jobs. v2: NOT failed — PID 553256 actively running at GSM8K 124/1319",
    "error_type": "resource",
    "fix_steps": [
      "当前v2正在运行，先观察是否能完成",
      "若再次OOM，用ulimit或cgroup限制其他进程的RAM，或错峰运行",
      "v1缺少source /etc/network_turbo导致HF超时，v2已修复"
    ],
    "can_auto_fix": false
  }
}
```

</details>

---
