# analyze eval pi05 random k05 long seed42 strict

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_random_k05_long_seed42_strict_20260527T130843_result.json`
- **Structured JSON:** [`7d68771567330b1421b0.json`](../../sessions/7d/7d68771567330b1421b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志中无 W&B 记录。JSON 结果文件也没有 strict metric 字段——这个实验只输出了 lenient success rate。

## 汇总

**π0.5 Random Pruning k=0.5, LIBERO Long Suite, seed=42**

| Task | Description | SR |
|------|-------------|-----|
| T0 | put both the alphabet soup and the tomato sauce in the basket | 84% |
| T1 | put both the cream cheese box and the butter in the basket | 32% |
| T2 | turn on the stove and put the moka pot on it | 64% |
| T3 | put the black bowl in the bottom drawer of the cabinet and close it | 72% |
| T4 | put the white mug on the left plate and put the yellow and white mug on the right plate | 74% |
| T5 | pick up the book and place it in the back compartment of the caddy | 38% |
| T6 | put the white mug on the plate and put the chocolate pudding to the right of the plate | 30% |
| T7 | put both the alphabet soup and the cream cheese box in the basket | 54% |
| T8 | put both moka pots on the stove | 4% |
| T9 | put the yellow and white mug in the microwave and close it | 50% |

- **Overall SR (lenient): 50.2%** (251/500)
- **Overall SR (strict): 未输出** — 日志和 JSON 均无 strict metric，尽管 exp_id 含 "strict"
- **运行时间**: 268.9 min (~4.5h)
- **W&B**: 日志无 wandb 记录，未上传
- **异常**: 无错误，EXIT_CODE=0。T8 (put both moka pots on the stove) 极低 4%，是明显的弱任务。

---
