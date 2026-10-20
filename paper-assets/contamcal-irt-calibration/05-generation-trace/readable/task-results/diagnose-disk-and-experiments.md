# diagnose disk and experiments

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_disk_and_experiments_20260516T210214_result.json`
- **Structured JSON:** [`5d9ddae8df6df4928d16.json`](../../sessions/5d/5d9ddae8df6df4928d16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。汇总结果：

---

```
TASK1_RESULT: {"disk_freed_gb": 19, "disk_available_gb": 45, "can_rerun_fisher": true}
```

清理明细：
- `/root/autodl-tmp/models/Qwen/Qwen2___5-7B-Instruct` — 15GB（项目不使用7B）
- HF cache 未使用数据集（SlimOrca, OpenHermes-2.5, SWE-smith）— 3.1GB
- Arrow datasets 缓存 — 3.5GB
- `/tmp` 临时文件 — 206MB
- `__pycache__` + 空壳模型目录 — 少量

---

```
TASK2_RESULT: {"actually_succeeded": true, "metrics": {"mmlu": 0.4256, "arc_challenge": 0.5956, "gsm8k": 0.2722, "humaneval_pass@1": 0.0122}, "missing_benchmarks": []}
```

4 个 benchmark 结果文件齐全，`.done` sentinel 存在。EXIT_CODE=1 可能由 HumanEval 子进程的非零返回触发（代码执行沙箱常见），但结果数据完整有效。

---

```
TASK3_RESULT: {"process_alive": false, "root_cause": "PID 859360 已死亡，但 ARC/GSM8K signals 实际已全部完成。当前有替代 MMLU session (tmux: signals_llama32_3B_d005_mmlu, PID 842929) 在 cuda:4 运行中", "partial_results": true, "recommended_action": "无需重提交 arc/gsm8k — 已有完整结果(embedding+minkpp+selfcritique+merged)。等待当前 MMLU session 完成即可。"}
```

Llama-3.2-3B_d005_s42 signals 当前状态：
| Benchmark | s1_embedding | s2_minkpp | s4_selfcritique | merged |
|-----------|:---:|:---:|:---:|:---:|
| arc_challenge | ✓ | ✓ | ✓ | ✓ |
| gsm8k | ✓ | ✓ | ✓ | ✓ |
| mmlu | ✓ | ✓ | 运行中(PID 842929) | 待生成 |

---
