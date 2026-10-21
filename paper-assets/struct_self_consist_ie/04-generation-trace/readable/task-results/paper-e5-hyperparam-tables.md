# paper e5 hyperparam tables

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_e5_hyperparam_tables_20260521T111617_result.json`
- **Structured JSON:** [`03c7f4724c5ed80cc360.json`](../../sessions/03/03c7f4724c5ed80cc360.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出文件已写入 `artifacts/e5_hyperparam_tables.tex` 并注册为 `art_20260521_ec1da6`。

三张表内容：

- **Table A** — 19 行，覆盖所有 fine-tuning 实验：主模型（Qwen3-8B / LLaMA-3.1-8B × 3 数据集）、scale 消融（4B/7B/14B/32B）、LoRA rank 消融（r=8/16/32）、epoch 消融（3/5/10）、SCD。部分训练时长 registry 未记录，标 N/A。
- **Table B** — 推理配置汇总：默认 N=8/T=1.0、温度消融（0.5/0.8/1.0/1.2）、N 消融（1/2/4/8/16/32）、free-form/prompted diversity/multi-round 变体。
- **Table C** — 4 个 frontier 模型（GPT-5.5 / Claude Sonnet 4 / Gemini-2.5-Pro / DeepSeek-Chat）的 API 配置。

N/A 标注的字段（主要是部分实验的训练时长）在表注中说明了原因。

---
