# eval 70b lora docred inference

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_70b_lora_docred_inference_20260522T023202_result.json`
- **Structured JSON:** [`967bf90b150ffed8ef68.json`](../../sessions/96/967bf90b150ffed8ef68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

推理正常运行中。汇报：

**70B LoRA DocRED Unconstrained 推理状态**

| 项目 | 值 |
|------|-----|
| PID | 881085 |
| GPU | cuda:1, VRAM 39.8GB / 97.9GB, 利用率 ~80% |
| 已完成 | 2 / 998 样本 |
| 样本 1 耗时 | 29.6s |
| 样本 2 耗时 | 57.7s |
| 平均速度 | ~0.023 样本/秒（~43.6s/样本） |
| 预计总时间 | **~12 小时**（按均值 43.6s/样本算，998 样本 ≈ 12.1h） |
| 预计完成时间 | ~明天上午（5月23日早上） |

输出质量初看正常：模型生成了合理的实体和关系抽取结果（使用自然语言关系名如 "country"、"inception"、"headquarters location" 等）。

DocRED 文档比 SciERC 长很多，加上 `max_new_tokens=4096`，每个样本需要生成大量 token，所以速度比 SciERC 慢得多。

---
