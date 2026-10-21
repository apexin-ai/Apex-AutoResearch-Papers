# ssh westd collect eval results

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-collect-eval-results_20260519T102733_result.json`
- **Structured JSON:** [`749d32563e28593c66a4.json`](../../sessions/74/749d32563e28593c66a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部结果已收集。汇总如下：

---

## 完整 Eval 结果汇总

### Gemma-2-9B (cross-family)

| Dosage | MMLU (%) | ARC-Challenge (%) |
|--------|----------|-------------------|
| d000 | 65.71 | 78.67 |
| d005 | 65.20 | **22.95** ⚠️ |
| d025 | 65.85 | 85.32 |
| d050 | 64.44 | 80.55 |
| d100 | 65.62 | 84.81 |

### Phi-4 (cross-family)

| Dosage | MMLU (%) | ARC-Challenge (%) |
|--------|----------|-------------------|
| d000 | 77.47 | 93.94 |
| d005 | 78.09 | 93.94 |
| d025 | 78.39 | 94.03 |
| d050 | 78.67 | 93.69 |

### OLMo-2-7B (cross-family)

| Dosage | MMLU (%) | ARC-Challenge (%) |
|--------|----------|-------------------|
| d000 | 58.60 | 80.20 |
| d005 | 58.10 | 80.20 |
| d025 | 56.17 | 78.16 |
| d050 | 59.18 | 80.89 |
| d100 | 59.49 | 81.23 |

### 状态

- **Phi-4 d100 训练**: 已完成，checkpoint 已保存到 `phi-4_d100_s42/lora_adapter/` (checkpoint-4159)
- **GPU 状态**: 4 个 GPU 都有新进程在跑（其他 worker 已启动新任务）
- **异常**: Gemma d005 ARC=22.95% 严重异常（GPU 3 上有 sanity check 正在重评）
- **OLMo d025 westd 重评**: MMLU=56.17%, ARC=78.16%，比 d000 (58.6%, 80.2%) 低，注意与其他 dosage 的趋势不一致

---
