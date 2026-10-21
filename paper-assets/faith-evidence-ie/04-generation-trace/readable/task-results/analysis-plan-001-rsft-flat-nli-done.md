# analysis plan 001 rsft flat nli done

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_001_rsft_flat_nli_done_20260515T163208_result.json`
- **Structured JSON:** [`0b0c5f8df1955cab2d05.json`](../../sessions/0b/0b0c5f8df1955cab2d05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

**plan_001_rsft_flat_nli 训练完成汇总：**

| 指标 | 值 |
|------|-----|
| 状态 | SUCCESS |
| 样本数 | 2691 (flat-NLI scoring) |
| Epochs/Steps | 3 / 507 |
| 最终 train loss | 0.6238 |
| 最低 train loss | 0.5803 (step 480) |
| Token accuracy | 85.28% |
| 训练时间 | ~49 min |
| 最终模型 | `/root/autodl-tmp/rsft_output_flat_nli/` |
| 最终 checkpoint | `checkpoint-507` |

**下一步：** 需要对 `/root/autodl-tmp/rsft_output_flat_nli/` 做 dev eval，然后与 CED scoring RSFT（mean rel_f1=0.4596）对比，验证 contrastive margin 是否是关键因素。Eval 需要 GPU。

---
