# analysis eval math500 grpo cka only 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_math500_grpo_cka_only_20_20260518T140731_result.json`
- **Structured JSON:** [`a0ae628e596d1e4f5e1d.json`](../../sessions/a0/a0ae628e596d1e4f5e1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## 结果汇总

| 指标 | 值 |
|------|-----|
| MATH-500 accuracy | **26.60%** (133/500) |
| stderr | ±1.98% |
| truncated | 108/500 (21.6%) |
| avg response length | 1124.24 tokens |

## 与基线对比

| 模型 | GSM8K | MATH-500 |
|------|-------|----------|
| Dense unpruned | — | ~73.6% |
| GRPO CKA-only 20% | 64.37% | **26.60%** |

MATH-500 仅 26.60%，相对 dense 下降约 47 个百分点，极其严重。而同一模型 GSM8K 64.37% 相对保持较好，说明 **GRPO CKA-only 在 GSM8K 上的恢复没有迁移到更难的 MATH-500**。

21.6% 的 truncation rate 也值得注意：模型在较难题目上倾向于生成长但不收敛的推理链，被截断后无法给出正确答案。

## Hypothesis 判断

**Negative**。SFT CKA-only MATH-500 数据尚缺（待确认），但 26.60% 已经非常低。即使 GRPO > SFT 在 MATH-500 上成立，绝对性能也说明 CKA-only 20% 剪枝对数学推理能力造成了不可逆的损伤，GRPO 无法有效恢复。这与 GSM8K 上的表现形成鲜明对比，进一步支持 C1 decoupling 假说（GRPO 提升 benchmark-specific，不提升 cross-benchmark generalization）。

---
