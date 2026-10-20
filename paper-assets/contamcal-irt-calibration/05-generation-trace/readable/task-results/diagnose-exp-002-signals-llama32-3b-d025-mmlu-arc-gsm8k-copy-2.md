# diagnose exp 002 signals llama32 3B d025 mmlu arc gsm8k

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k_20260516T221141_result.json`
- **Structured JSON:** [`2d444f2ecc0102345633.json`](../../sessions/2d/2d444f2ecc0102345633.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务正在活跃运行。GSM8K 的 s1_embedding 正在计算中（~12% 进度，~54 batch/s）。

```json
{"status": "running", "benchmarks_done": ["arc_challenge"], "benchmarks_partial": ["mmlu (s1+s2 done, s4 10000/14042 chunked but not merged)", "gsm8k (s1 in progress ~12%)"], "benchmarks_missing": [], "root_cause": "process alive (PID 882427 on GPU 2), not failed — cron misjudged because original PID 853489 was the wrapper shell, actual worker spawned as 882427", "output_files": {"mmlu": {"s1": "14042 items", "s2": "14042 items", "s4_chunks": "10/? chunks (10000 items)", "merged": "missing"}, "arc_challenge": {"s1": "1172 items", "s2": "1172 items", "s4": "1172 items", "merged": "1172 items (complete)"}, "gsm8k": "computing s1 (~12% of embedding batches)"}}
```

实验仍在正常运行，不是 failed。脚本以 for loop 顺序处理 mmlu → arc_challenge → gsm8k，当前已完成 ARC 全部信号并进入 GSM8K 的 s1 阶段。MMLU 的 s4 有 10 个 chunks（10000 items）但尚未 merge，应是先跳到下一个 benchmark、最后统一 merge，或者 MMLU s4 本身只到 10000（MMLU 总量 14042，意味着 s4 可能未完成就切到了 ARC — 需复查脚本逻辑，但不影响当前 GSM8K 的活跃计算）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "status": "running",
    "benchmarks_done": [
      "arc_challenge"
    ],
    "benchmarks_partial": [
      "mmlu (s1+s2 done, s4 10000/14042 chunked but not merged)",
      "gsm8k (s1 in progress ~12%)"
    ],
    "benchmarks_missing": [],
    "root_cause": "process alive (PID 882427 on GPU 2), not failed — cron misjudged because original PID 853489 was the wrapper shell, actual worker spawned as 882427",
    "output_files": {
      "mmlu": {
        "s1": "14042 items",
        "s2": "14042 items",
        "s4_chunks": "10/? chunks (10000 items)",
        "merged": "missing"
      },
      "arc_challenge": {
        "s1": "1172 items",
        "s2": "1172 items",
        "s4": "1172 items",
        "merged": "1172 items (complete)"
      },
      "gsm8k": "computing s1 (~12% of embedding batches)"
    }
  }
}
```

</details>

---
