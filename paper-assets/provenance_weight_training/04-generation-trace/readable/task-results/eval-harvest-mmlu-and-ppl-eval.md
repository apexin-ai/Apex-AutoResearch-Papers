# eval harvest mmlu and ppl eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_harvest_mmlu_and_ppl_eval_20260517T144410_result.json`
- **Structured JSON:** [`92d94a35a99914af04c0.json`](../../sessions/92/92d94a35a99914af04c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务都已完成。

---

## 结果汇总

### 任务 1：llama3b_uniform_seed42 MMLU

| 指标 | 数值 |
|------|------|
| **MMLU 总 accuracy** | **0.5185** (±0.0040) |
| Humanities | 0.4648 |
| Social Sciences | 0.5970 |
| STEM | 0.4573 |
| Other | 0.5842 |

### 任务 2：batchsize16_nmin8_seed42 PPL

| 指标 | 数值 |
|------|------|
| **Perplexity** | **17.65** |
| **Loss** | **2.8709** |
| **Eval tokens** | **4,077,068** |
| 评估时间 | 162s |

结果文件保存在：`/root/autodl-tmp/provenance_weight_training/output/eval/ppl_batchsize16_nmin8_seed42.json`

---
