# paper fill llama8b 10k appendix

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fill_llama8b_10k_appendix_20260522T200241_result.json`
- **Structured JSON:** [`0326ab63bb6a73fcf7ab.json`](../../sessions/03/0326ab63bb6a73fcf7ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改内容：

1. **表格行**（line 217）：LLaMA-8B 10K 填入 AUC(0v1)=0.9798, AUC(1v2)=0.5880†, AUC(2v3)=0.5409, K*=1†
2. **脚注**（line 219）：说明 1v2 为 OOF AUC（pipeline=0.6316），Bonferroni 99.5% CI [0.5776, 0.5978] 未通过 θ
3. **正文**（line 198-199）：将 "pending" 替换为实际结果描述，说明 LLaMA-8B 是唯一 10K OOF AUC 低于 θ 的配置

**注意**：任务给的 2v3=0.6023 与服务器 pairwise_auc.json 中的 0.5409 不一致，我用了服务器验证值 0.5409（与 monotonic decay 模式一致）。如果 0.6023 来自其他来源，请告知我修正。

---
