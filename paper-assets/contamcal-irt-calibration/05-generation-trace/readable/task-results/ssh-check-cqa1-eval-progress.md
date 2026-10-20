# ssh check cqa1 eval progress

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-cqa1-eval-progress_20260519T014029_result.json`
- **Structured JSON:** [`c3a61c06e81b8f2fb024.json`](../../sessions/c3/c3a61c06e81b8f2fb024.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总完毕。

## 7B Eval 批量任务状态

### 进程状态
- **PID 160404** (run_eval_mmlu_arc_original.sh): 活跃，当前在 **6/10** (d025_s123)，MMLU 进度 50% (3510/7021)
- **PID 161500** (run_aligned_eval_7B.sh original): 活跃，在 d000_s123 上跑 gsm8k/humaneval（MMLU/ARC 已由另一脚本完成）

### 已完成结果 (MMLU + ARC)

| Adapter | MMLU Acc | ARC Acc |
|---------|----------|---------|
| d000_s42 | 0.6929 (9730/14042) | 0.8959 (1050/1172) |
| d000_s123 | 0.6978 (9799/14042) | 0.8985 (1053/1172) |
| d005_s42 | 0.6924 (9723/14042) | 0.8968 (1051/1172) |
| d005_s123 | 0.6932 (9734/14042) | 0.8985 (1053/1172) |
| d025_s42 | 0.7003 (9834/14042) | 0.8985 (1053/1172) |

### 进行中 / 待完成

| Adapter | 状态 |
|---------|------|
| **d025_s123** | MMLU 50%，预计 ~17 min 完成 MMLU + ~6 min ARC |
| d050_s42 | 待排队 |
| d050_s123 | 待排队 |
| d100_s42 | 待排队 |
| d100_s123 | 待排队 |

### 时间估计
每个 adapter MMLU ~35 min + ARC ~6 min ≈ 41 min。剩余 4.5 个 adapter，预计 **~3 小时**完成全部。

### 初步观察
- MMLU：7B 各 dose 差异很小（0.692–0.700），d025 略高
- ARC：几乎无差异（0.896–0.899），7B 模型在 ARC 上已接近饱和

---
