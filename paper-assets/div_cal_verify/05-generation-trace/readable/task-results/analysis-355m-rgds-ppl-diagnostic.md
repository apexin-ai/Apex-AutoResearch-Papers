# analysis 355m rgds ppl diagnostic

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_355m_rgds_ppl_diagnostic_20260514T125537_result.json`
- **Structured JSON:** [`ea22b26080c386cf43f0.json`](../../sessions/ea/ea22b26080c386cf43f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行完成。结果：

```
=== 355M RGDS Selected vs Rejected PPL (Gen-0 model) ===

Gen 4:
  Selected  (N=488): mean PPL=1.85, median=1.51, P90=2.61
  Rejected  (N=489): mean PPL=1.74, median=1.70, P90=2.11
  差异: selected - rejected = +0.11
  t-test: t=1.45, p=0.1474
  Cohen's d: 0.09

Gen 7:
  Selected  (N=488): mean PPL=1.80, median=1.58, P90=2.77
  Rejected  (N=489): mean PPL=1.80, median=1.73, P90=2.27
  差异: selected - rejected = +0.01
  t-test: t=0.16, p=0.8747
  Cohen's d: 0.01
```

**结论：355M 下 RGDS 没有系统性选择低 PPL 样本。** 两代的 Cohen's d 都接近 0（0.09 和 0.01），t-test 均不显著（p=0.15, p=0.87）。Selected 和 rejected 的 PPL 分布几乎无差异，selected 甚至略高于 rejected。

**与 125M 对比：效应方向不一致。** 125M 下 RGDS 强烈偏好低 PPL 样本（Cohen's d=-1.11），但 355M 下该效应消失（d≈0）。这说明 RGDS 的 diversity selection 在 355M 上不再表现出对模板化样本的系统性偏好，可能因为 gpt2-medium 生成的样本本身 PPL 分布更窄（mean≈1.8，远低于 125M 的水平），diversity score 不再与 PPL 高度相关。

---
