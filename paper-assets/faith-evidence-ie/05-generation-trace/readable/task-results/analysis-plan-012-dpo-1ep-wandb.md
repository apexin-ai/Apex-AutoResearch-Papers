# analysis plan 012 dpo 1ep wandb

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_012_dpo_1ep_wandb_20260515T202035_result.json`
- **Structured JSON:** [`df954a12ade467d47414.json`](../../sessions/df/df954a12ade467d47414.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

## 1ep vs 3ep 对比

| 指标 | 1ep | 3ep (过拟合) |
|------|-----|-------------|
| rewards/accuracies | **0.82** | 1.00 |
| rewards/margins | **0.86** | 9.01 |
| train_loss | **0.59** | ~0.1 |

## 判断

- **过拟合已消除**：accuracy 从随机水平 (0.41) 渐进上升到 0.82，未饱和；margins 0.86 比 3ep 的 9.01 低一个数量级
- **训练健康**：167 steps / 33min，正常结束，loss 仍有余量
- **Checkpoint 就绪**：`/root/autodl-tmp/dpo_output_1ep/adapter_model.safetensors` (528MB)，checkpoint-167 (final)

**建议立即跑 eval 测 rel_f1，看是否超过 SFT baseline 0.4057。**

产出已写入 `artifacts/plan_012_dpo_ced_1ep_analysis.md` 并注册到 manifest。

---
