# eval grpo mia

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_grpo-mia_20260523T005921_result.json`
- **Structured JSON:** [`f6c30bbe851b9497eec9.json`](../../sessions/f6/f6c30bbe851b9497eec9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 GRPO checkpoint 全部完成。汇总结果：

## MIA AUC-ROC 结果（Min-K% 10%）

| Stage | AUC-ROC |
|---|---|
| Base | 0.4929 |
| SFT (15%) | 0.6111 |
| GRPO step 500 | 0.4929 |
| GRPO step 1000 | 0.4928 |
| GRPO step 1500 | 0.4930 |

三个 GRPO checkpoint 的 MIA AUC-ROC 在所有指标上几乎完全一致（0.486–0.493），与 base model 无差异，全部接近随机水平 0.5。GRPO RL 训练没有让 MIA 检测能力恢复——SFT 引入的可区分性（0.611）在 GRPO 之后完全消失，回到了 base 水平。

这说明 GRPO 的 RL 训练有效地"洗掉"了 SFT 阶段留下的 membership 信号，使得 Min-K% MIA 无法区分 seen/unseen 数据。

---
