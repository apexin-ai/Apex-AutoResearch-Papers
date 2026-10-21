# eval plan012 rerun correct

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan012-rerun-correct_20260518T000932_result.json`
- **Structured JSON:** [`378f69fdc2f770d7c755.json`](../../sessions/37/378f69fdc2f770d7c755.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已保存到 `results/plan_012_rerun_correct.json`。

汇总：

| K | Binary F1 | Precision | Recall | Accuracy |
|---|-----------|-----------|--------|----------|
| k2 | 0.0 | 0.0 | 0.0 | 0.5 |
| k3 | 0.0513 | 1.0 | 0.0263 | 0.5132 |
| k5 | 0.1463 | 1.0 | 0.0789 | 0.5395 |
| full | 0.1 | 1.0 | 0.0526 | 0.5263 |

对比 plan_002 fine-tuned 模型：treatment K=2 F1=1.0, baseline K=2 F1=0.987, full 均为 1.0。

结论：Qwen3-8B zero-shot LLM judge 在这个测试集上几乎完全失败（recall 接近 0），说明渐进式说服攻击对 zero-shot 方法不可见。unparseable=0，模型输出格式正确，只是判断能力不足。

---
