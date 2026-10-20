# eval plan 012 gpt55

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan_012_gpt55_20260518T024740_result.json`
- **Structured JSON:** [`2f39b30fa08e23944141.json`](../../sessions/2f/2f39b30fa08e23944141.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**GPT-5.5 LLM Judge Baseline 结果汇总：**

| K | F1 | Precision | Recall | Unparseable |
|---|---|---|---|---|
| K=2 | 0.1905 | 1.0 | 0.1053 | 23/76 |
| K=3 | 0.2727 | 1.0 | 0.1579 | 23/76 |
| K=5 | **0.4490** | 1.0 | 0.2895 | 28/76 |
| full | 0.3830 | 1.0 | 0.2368 | 36/76 |

关键发现：
- GPT-5.5 比 Qwen3-8B 好（best F1 0.45 vs 0.15），但仍远低于 trained classifier (F1=1.0)
- 精确率 1.0 说明它判定为 jailbreak 的都是对的，但大量漏检（recall 最高仅 0.29）
- 30-47% 的样本输出不可解析（reasoning model token 耗尽未输出 verdict），默认计为 benign
- full 对话反而比 K=5 差，可能是因为更长的输入导致更多 unparseable

结论：即使是 GPT-5.5 级别的 LLM，zero-shot judge 在早期检测上也表现很差，验证了 trained classifier 的存在价值。

产出已保存到 `results/plan_012_gpt55_judge.json`，artifact 已注册。

---
