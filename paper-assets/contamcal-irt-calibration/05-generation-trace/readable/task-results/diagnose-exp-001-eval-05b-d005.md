# diagnose exp 001 eval 05B d005

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_eval_05B_d005_20260514T064705_result.json`
- **Structured JSON:** [`9a1b6974b51c0a881399.json`](../../sessions/9a/9a1b6974b51c0a881399.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验没有失败，是正常完成。** Cron 误判。

日志末尾明确显示所有 4 个 benchmark 全部跑完并保存了结果：

| Benchmark | 结果 |
|-----------|------|
| MMLU | 29.29% (4113/14042) |
| HumanEval | 7.93% (13/164) |
| GSM8K | (已完成) |
| ARC Challenge | (已完成) |

输出文件完整存在于 `/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42/`：
- `eval_results.json` (2.0MB)
- `correctness_matrix.json` (112KB)  
- `item_responses.json` (2.3MB)

最后一条日志 `2026-05-14 14:28:34` — 进程正常退出。PID 255322 死亡是因为**跑完了**，不是崩溃。Cron 检测到进程不存在就标记 failed，这是误报。

非 GPU 冲突 — 0.5B 模型很小，和 3B eval 共享 GPU 1 没有 OOM。

```json
{"root_cause":"非失败，实验正常完成。日志末尾: 'Results saved to .../eval_results.json'，进程正常退出后 cron 误判为 failed","error_type":"infrastructure","fix_steps":["将实验状态从 failed 改为 completed","cron 监控应检查日志末尾是否有 'Results saved' 成功标记，而非仅靠 PID 存活判断"],"can_auto_fix":true,"partial_results":"有完整结果（4个benchmark全部完成）"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "非失败，实验正常完成。日志末尾: 'Results saved to .../eval_results.json'，进程正常退出后 cron 误判为 failed",
    "error_type": "infrastructure",
    "fix_steps": [
      "将实验状态从 failed 改为 completed",
      "cron 监控应检查日志末尾是否有 'Results saved' 成功标记，而非仅靠 PID 存活判断"
    ],
    "can_auto_fix": true,
    "partial_results": "有完整结果（4个benchmark全部完成）"
  }
}
```

</details>

---
