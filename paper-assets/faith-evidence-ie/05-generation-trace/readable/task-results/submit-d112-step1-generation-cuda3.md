# submit d112 step1 generation cuda3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_d112_step1_generation_cuda3_20260518T225655_result.json`
- **Structured JSON:** [`8ef9312a610776994dad.json`](../../sessions/8e/8ef9312a610776994dad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个子任务均完成。

**子任务 1 — GRPO ckpt-200 eval 收割完毕**

| 指标 | 值 |
|------|-----|
| Ign-F1 | 0.4446 |
| Rel-F1 | 0.4513 |
| Evi-F1(DREEAM) | 0.3562 |
| Evi-F1(TP) | 0.8053 |
| EDCR | 0.6489 |
| Format OK | 984/985 |
| Truncated | 204/985 |
| Predictions | 15733 |

Registry `grpo_bf16_g4_ckpt200_eval` 已更新为 DONE/success，metrics 已写入。

**子任务 2 — D112 RSFT 候选生成已提交到 cuda:3**

- tmux session: `d112_rsft_s44_generate`
- 日志: `/root/runs/faith-evidence-ie/d112_rsft_s44_generate.log`
- 模型已在加载中，SFT s44 adapter 已合并
- Registry `d112_rsft_s44_generate` 状态 RUNNING

GRPO ckpt-200 的 ign_f1=0.4446 低于 SFT s44 baseline 的 0.4734，说明 GRPO 200 步训练在 RE 指标上有退化，但 evi_f1_joint=0.3562 和 edcr=0.6489 需要和 SFT baseline 对比才能判断 evidence 质量变化。

---
