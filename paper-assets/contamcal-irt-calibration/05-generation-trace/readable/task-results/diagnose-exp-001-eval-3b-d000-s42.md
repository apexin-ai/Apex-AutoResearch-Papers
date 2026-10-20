# diagnose exp 001 eval 3B d000 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_eval_3B_d000_s42_20260514T065026_result.json`
- **Structured JSON:** [`b602c5fd7287f49b738d.json`](../../sessions/b6/b602c5fd7287f49b738d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验**未失败，已成功完成**。监控系统误判了——进程正常退出但没有写 sentinel/上报 W&B，导致被 auto-resolved 为 failed。

## 完整结果（Qwen2.5-3B, d000, s42）

| Benchmark | Metric | Score |
|-----------|--------|-------|
| mmlu | accuracy | 0.6337 (8898/14042) |
| gsm8k | exact_match | 0.1168 (154/1319) |
| arc_challenge | accuracy | 0.8217 (963/1172) |
| humaneval | pass@1 | 0.1159 (19/164) |

运行时间：08:54 → 14:39，约 5 小时 45 分。

输出文件完整存在于 `/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42/`：
- `eval_results.json` (2.0MB)
- `correctness_matrix.json` (107KB)
- `item_responses.json` (2.2MB)

唯一的非致命错误：`bitsandbytes` 加载警告（`libnvJitLink.so.13` 缺失），不影响推理。

```json
{"root_cause":"False positive — 实验已成功完成，监控系统因缺少 sentinel/W&B 信号误判为 failed（process dead 5× with no sentinel/W&B — auto-resolved as failed）","error_type":"infrastructure","fix_steps":["将该实验状态从 failed 更正为 completed","确认 evaluate.py 退出时是否写 sentinel 文件或上报 W&B，如果缺少这一步则补上，避免后续实验被误判","检查同类失败实验（exp_001_eval_05B_d005, exp_001_eval_05B_d100_v2）的日志，可能也是同样的误报"],"can_auto_fix":true}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "False positive — 实验已成功完成，监控系统因缺少 sentinel/W&B 信号误判为 failed（process dead 5× with no sentinel/W&B — auto-resolved as failed）",
    "error_type": "infrastructure",
    "fix_steps": [
      "将该实验状态从 failed 更正为 completed",
      "确认 evaluate.py 退出时是否写 sentinel 文件或上报 W&B，如果缺少这一步则补上，避免后续实验被误判",
      "检查同类失败实验（exp_001_eval_05B_d005, exp_001_eval_05B_d100_v2）的日志，可能也是同样的误报"
    ],
    "can_auto_fix": true
  }
}
```

</details>

---
