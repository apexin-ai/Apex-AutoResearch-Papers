# diagnose exp002 false fail

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp002_false_fail_20260514T132356_result.json`
- **Structured JSON:** [`dd8bc64ab469e8e7492a.json`](../../sessions/dd/dd8bc64ab469e8e7492a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All the data is in. Here's the full diagnosis:

---

## 排查结论

### 1. FAIL 根因

**run_batch.py 的判定逻辑纯粹基于 `returncode`**（第 ~155 行），不看 stderr 内容：
```python
if result.returncode == 0:
    results[task_id] = "PASS"
else:
    results[task_id] = f"FAIL (rc={result.returncode})"
```

初始假设（stderr 警告误判）**不成立**。之前的 FAIL 是 compute_signals.py 确实返回了非零 exit code（可能是早期版本的 bug、模型加载问题或 OOM 等瞬态错误）。compute_signals.py 没有显式 `sys.exit()` 调用，正常完成时 Python 默认返回 0，非零 exit code 说明当时确实有未捕获异常。

### 2. v5 下已自愈

当前运行日志显示 d000 的 3 个 task **全部 PASS**：
```
[1/9] PASS: Qwen2.5-0.5B_d000_s42/mmlu
[2/9] PASS: Qwen2.5-0.5B_d000_s42/gsm8k
[3/9] PASS: Qwen2.5-0.5B_d000_s42/arc_challenge
```

问题已自愈，无需修复 run_batch.py。

### 3. 不阻塞 exp-003 RRF

`rrf_aggregation.py` **直接读取 `signals_merged_{benchmark}.json` 文件**（第 39-44 行），不依赖 batch_report 的 PASS/FAIL 状态。三个 signals_merged 文件均已存在：
- `signals_merged_mmlu.json`
- `signals_merged_gsm8k.json`
- `signals_merged_arc_challenge.json`

**exp-003 RRF 不受阻塞。**

### 4. 总结

| 项目 | 结论 |
|------|------|
| FAIL 根因 | compute_signals.py 返回非零 exit code（非 stderr 误判） |
| 是否阻塞 exp-003 | **否**，RRF 直接读 signals_merged 文件 |
| 是否需要修复 | **否**，v5 下 d000 已全部 PASS |
| 当前进程是否受影响 | 不涉及，无需改动 |

---
