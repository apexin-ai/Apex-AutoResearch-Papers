# analyze exp 001 eval 3B d000 aligned

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp_001_eval_3B_d000_aligned_20260514T130804_result.json`
- **Structured JSON:** [`5529c400daf503a712a1.json`](../../sessions/55/5529c400daf503a712a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。

## 实验结果总结

### Aligned Format 下 3B d000 s42 评测结果

| Benchmark | Aligned (本次) | 旧格式 (s42) | 变化 |
|-----------|---------------|-------------|------|
| MMLU | **0.6340** | 0.634 | ≈0 (无变化) |
| GSM8K | **0.1198** | 0.117 | +0.003 (几乎无变化) |
| ARC Challenge | **0.8276** | 0.822 | +0.006 (微增) |
| HumanEval | **0.1159** | 0.116 | ≈0 (无变化) |

### 核心结论

**GSM8K 崩塌未被 aligned format 修复。** Aligned format 下 GSM8K = 0.1198，与旧格式 0.117 几乎相同，远低于 raw generation（无 LoRA）的 0.605。这进一步确认 D018 的诊断：**GSM8K 崩塌根因是 LoRA SFT 导致的 CoT 灾难性遗忘，与 MC format 无关。**

MMLU、ARC、HumanEval 在两种 format 下表现一致，说明 aligned format 对 MC 类 benchmark 没有显著影响。bitsandbytes 加载 warning 不影响结果（EXIT_CODE=0）。

---
