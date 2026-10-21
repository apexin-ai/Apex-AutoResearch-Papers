# validation model diagnostics

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_validation_model-diagnostics_20260525T203850_result.json`
- **Structured JSON:** [`9bde6b13d4f9019a1a8e.json`](../../sessions/9b/9bde6b13d4f9019a1a8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the summary:

---

```
Item 4 (OVB r=0.86): [MISMATCH] 论文=0.86, 实际=0.8302
  Sequential mean bias_corr across all rho (N=352 seeds):
    rho=0.0: 0.8516 (n=50)
    rho=0.3: 0.8398 (n=61)
    rho=0.6: 0.8264 (n=141)
    rho=0.9: 0.8191 (n=100)
    Overall: 0.8302
  差距 ~0.03，论文数字偏高。

Item 5 (Self-eval): [PARTIAL MATCH]
  Self-judging (item-level exclusive = wins/(wins+losses)):
    qwen_self=1.000 (42/42) ✓ MATCH
    llama_self=0.912 (52/57) ✓ MATCH
  Cross-judge mean:
    论文: qwen_cross=0.714, llama_cross=0.823
    实际（per-judge exclusive mean）: qwen_cross=0.807, llama_cross=0.702
    实际（pooled exclusive）: qwen_cross=0.776, llama_cross=0.674
    ✗ MISMATCH — 无法用任何合理聚合方式复现论文的 cross-judge 数字。
    注意：论文中 llama(0.823) > qwen(0.714) 与数据方向相反（实际 qwen > llama）。

Item 6 (PPC): [MATCH] 论文=0.593/0.599, 实际=0.5934/0.5987, N=5661
  Predicted mean: 0.5934 (论文 0.593 ✓)
  Observed mean:  0.5987 (论文 0.599 ✓)
  N observations: 5661 ✓

Item 7 (Bootstrap): [PARTIAL MATCH]
  N=8:  Δτ 95% CI = [-0.071, 0.071] ✓ MATCH（CI crosses zero，与论文一致）
  N=17: 无 bootstrap 结果文件。点估计 Δτ = -0.015。
        论文 Table 1 标注 "TBD"。任务中声称的 CI=[-0.141, 0] 无法验证。
```

关键发现：
- **Item 5 cross-judge 数字可能有错**：论文称 qwen cross=0.714 < llama cross=0.823，但实际数据中 qwen 在所有计算方法下都高于 llama。数字方向反转，疑似写反或计算方法不同。
- **Item 4** 偏差约 0.03（0.83 vs 0.86），可能是论文四舍五入或使用了不同子集。

---
