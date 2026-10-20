# ssh gpu status check all

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu_status_check_all_20260514T131657_result.json`
- **Structured JSON:** [`0328c668f3df9a74e74f.json`](../../sessions/03/0328c668f3df9a74e74f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Here's the full report:

---

## GPU 状态报告

### GPU 0 — exp_002_signals_05B
- **PID**: 370957 (shell, 22h30m) → 373251 (compute_signals.py, 12min)
- **GPU**: 22% util, 15223/24564 MiB
- **进度**: Batch runner 9 个 task (3 dosages × 3 benchmarks)
  - d000: 3/3 benchmarks 完成 (15 个 signal 文件已写入，尽管日志标记 FAIL，实际是 stderr 警告导致的误报)
  - d005: 1/3 进行中 — mmlu 的 embedding+minkpp 完成，当前在计算 selfcritique
  - d100: 0/3 未开始
- **错误**: Tasks 1-3 标记 FAIL 但实际输出正常（stderr 包含 HuggingFace 模型列表警告，非真实错误）
- **预估**: d005 剩余 ~2h，d100 ~3h → 总计约 5h

### GPU 1 — eval_15B_aligned_batch (1.5B d005)
- **PID**: 336750 (shell, 4h) → 365739 (evaluate.py 1.5B d005, 46min)
- **GPU**: 49% util, 5857/24564 MiB
- **进度**:
  - d000 original: ✓ mmlu 58.53%, arc 77.22% → saved
  - d000 paraphrased: ✓ mmlu 60.96%, arc 75.47% → saved
  - d005 original: ✓ mmlu 58.52%, **GSM8K 400/1319 (30%)** @ 6.08s/it
- **预估**: GSM8K 剩余 ~93min，之后 arc+humaneval ~35min，然后 para 版本 ~2h → 还需 ~4h+

### GPU 2 — eval_05B_aligned_batch (0.5B d005→)
- **PID**: 332207 (shell, 4h39m) → 356787 (evaluate.py, 2h02m, 1.9GB RSS)
- **GPU**: 37% util, 8293/24564 MiB
- **进度**:
  - d000 original: ✓ mmlu 39.79%, arc 46.93% → saved
  - d000 paraphrased: ✓ mmlu 44.28%, arc 47.92% → saved
  - d005 original: ✓ mmlu 32.55%, ✓ arc 32.85%, **HumanEval 66/164 (40%)** @ 5.10s/it
- **预估**: HumanEval 剩余 ~8min，GSM8K ~2h，然后 para 版本 ~2h → 还需 ~4h+

### GPU 3 — eval_3B_d100_aligned
- **PID**: 362942 (evaluate.py 3B d100, 1h12m)
- **GPU**: 65% util, 8985/24564 MiB
- **进度**: ✓ mmlu 64.17%, **GSM8K 524/1319 (40%)** @ 7.38s/it
- **预估**: GSM8K 剩余 ~1h38m，arc+humaneval ~1h → 还需 ~3h

### GPU 4 — eval_3B_d005_aligned
- **PID**: 373931 (evaluate.py 3B d005, 9min)
- **GPU**: 68% util, 8985/24564 MiB
- **进度**: 刚启动，正在评估 mmlu (14042 items)
- **预估**: mmlu ~6.5h (at ~36it/s)... 实际可能 ~4-5h 完成全部 4 个 benchmark

### GPU 5 — **非空闲**
- **PID**: 374947 (evaluate.py 0.5B d025 aligned, 3min54s)
- **GPU**: 0% util, 1501/24564 MiB (刚启动，模型加载中)

---

## 汇总

| GPU | 实验 | PID | 状态 | 进度 | 预估完成 |
|-----|------|-----|------|------|----------|
| 0 | exp_002_signals_05B | 373251 | 运行中 | d000 ✓, d005 1/3, d100 0/3 | ~5h |
| 1 | eval_15B_d005_aligned | 365739 | 运行中 | d000 ✓, d005 GSM8K 30% | ~4h+ |
| 2 | eval_05B_batch | 356787 | 运行中 | d000 ✓, d005 HumanEval 40% | ~4h+ |
| 3 | eval_3B_d100_aligned | 362942 | 运行中 | mmlu ✓, GSM8K 40% | ~3h |
| 4 | eval_3B_d005_aligned | 373931 | 运行中 | 刚启动 (mmlu) | ~5h |
| 5 | eval_05B_d025_aligned | 374947 | 运行中 | 刚启动 (加载模型) | ~4h |

**注意**: GPU 5 不空闲，有 0.5B d025 eval 刚提交（3分钟前）。6 块 GPU 全部在用。

---
