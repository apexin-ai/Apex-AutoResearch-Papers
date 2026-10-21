# eval plan012 llm judge qwen

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan012-llm-judge-qwen_20260517T225109_result.json`
- **Structured JSON:** [`bff977df1420144a0cc5.json`](../../sessions/bf/bff977df1420144a0cc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Plan 012 完成。结果：

| K | F1 | Precision | Recall | Accuracy | Unparseable |
|---|---|---|---|---|---|
| K=2 | 0.3487 | 0.4932 | 0.4993 | 0.4868 | 5 |
| K=3 | 0.3352 | 0.3611 | 0.4723 | 0.4605 | 4 |
| K=5 | 0.3923 | 0.5465 | 0.5114 | 0.5000 | 5 |
| full | 0.6439 | 0.7688 | 0.6788 | 0.6711 | 5 |

**关键发现**：
- Qwen3-8B 作为 zero-shot LLM-as-Judge 在早期轮次（K=2,3,5）几乎无法检测 jailbreak，F1 仅 0.33-0.39，接近随机
- 即使看完全部对话（full），F1 也只有 0.64，远低于 plan_002 训练的分类器
- 每个 K 值都有 4-5 条 unparseable 输出（占比 ~6.5%）
- 总推理时间 200.6s，脚本已保存到 `src/llm_judge_baseline.py`，结果在 `results/plan_012_llm_judge_qwen3.json`

---
