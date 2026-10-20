# analysis detect remove q05 v2 seed456

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_detect_remove_q05_v2_seed456_20260522T132143_result.json`
- **Structured JSON:** [`61fc26523753bd077798.json`](../../sessions/61/61fc26523753bd077798.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。汇总：

## detect_remove_q05_v2_seed456 结果

| 指标 | 值 |
|------|-----|
| **holdout_ppl** | **17.277** |
| **owt_ppl** | **18.017** |
| wiki_ppl | fp32 eval 运行中 (PID 779491, GPU 2) |
| train_loss | 11.01 (HF avg) |
| total_steps | 6103 |
| checkpoint | `.../detect_remove_q05_v2_seed456/final` |

## 3-seed 汇总

| | seed42 | seed123_r2 | seed456 | **Mean ± Std** |
|---|--------|------------|---------|----------------|
| Holdout PPL | 17.285 | 17.272 | 17.277 | **17.278 ± 0.007** |
| OWT PPL | 18.014 | 18.008 | 18.017 | **18.013 ± 0.005** |
| Wiki PPL | 15.053 | 15.047 | pending | 15.050 ± 0.004 (2-seed) |

3-seed 方差极小（holdout std=0.007），D&R hard filtering 结果非常稳定。

**异常**: Wiki eval 使用 fp16+autocast 时出现 NaN（其他 seed 未出现），已在 GPU 2 用 fp32 重跑。结果写入 `eval_wiki.json` 后需手动更新 registry 中的 `wiki_ppl`。

---
