# diagnose exp 017

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-017_20260524T070720_result.json`
- **Structured JSON:** [`0c20e41a0680c6aaa20e.json`](../../sessions/0c/0c20e41a0680c6aaa20e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Key finding: the elapsed_s per fit varies dramatically — N=8 early seeds took ~65s but later seeds took ~365s. The wall clock tells the real story.

```json
{
  "completed_fits": 251,
  "total_fits": 800,
  "fits_by_N": {"8": 200, "20": 51, "50": 0, "100": 0},
  "avg_time_per_fit_seconds": 343.7,
  "estimated_remaining_hours": 52.3,
  "root_cause": "timeout (EXIT_CODE=124) after 251 fits in 86272s (~24h), likely 86400s timeout limit",
  "partial_results_useful": true,
  "has_enough_for_paper": false,
  "recommendation": "resume with fixes"
}
```

**详细分析：**

**Root cause**：进程在 86272s 处被 `timeout` 杀死（EXIT_CODE=124），刚好不到 24h（86400s）。

**完成进度**：
| N | 完成 seeds | 目标 | 状态 |
|---|-----------|------|------|
| 8 | 200/200 | 200 | 完成 |
| 20 | 51/200 | 200 | 25.5% |
| 50 | 0/200 | 200 | 未开始 |
| 100 | 0/200 | 200 | 未开始 |

**关键瓶颈**：4 条 MCMC chain 在 **1 个 GPU 上串行执行**（`expected 4 but got 1`），而 autodl-8gpu 有 8 张卡。这导致每个 fit 慢了约 4 倍。

**时间估算**：
- 当前均速 343.7s/fit（wall clock），剩余 549 fits ≈ 52.3h
- 但 N=50/100 的 MCMC 每步计算量更大，实际可能 70-100h
- 如果修复 chain 并行（4 GPU 并行 4 chains），可缩短到 **13-25h**

**部分结果评估**：
- N=8（200 seeds）和 N=20（51 seeds）可以做初步分析
- 但 **缺少 N=50 和 N=100**，无法展示大样本下 coverage 趋向 nominal level 的收敛行为，论文不完整

**Resume 建议**：
1. 增大 timeout 至 ≥ 72h（`timeout 259200`）
2. 在 `run_exp017.py` 开头加 `numpyro.set_host_device_count(4)` 或设置 `CUDA_VISIBLE_DEVICES=0,1,2,3` 让 4 chains 并行
3. 脚本已 resume-capable（CSV append 模式），直接重启即可从 N=20 seed=51 继续

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "completed_fits": 251,
    "total_fits": 800,
    "fits_by_N": {
      "8": 200,
      "20": 51,
      "50": 0,
      "100": 0
    },
    "avg_time_per_fit_seconds": 343.7,
    "estimated_remaining_hours": 52.3,
    "root_cause": "timeout (EXIT_CODE=124) after 251 fits in 86272s (~24h), likely 86400s timeout limit",
    "partial_results_useful": true,
    "has_enough_for_paper": false,
    "recommendation": "resume with fixes"
  }
}
```

</details>

---
