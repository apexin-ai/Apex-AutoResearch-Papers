# analysis eval humaneval 1p5b batch

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_humaneval_1p5b_batch_20260519T135427_result.json`
- **Structured JSON:** [`364e9da9975d8a2c5f0d.json`](../../sessions/36/364e9da9975d8a2c5f0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验结果已确认。

---

## 实验 1: eval_humaneval_grpo_cka_only_20_1p5b_2048

| 字段 | 值 |
|------|-----|
| exp_id | eval_humaneval_grpo_cka_only_20_1p5b_2048 |
| 正常完成 | 是 (EXIT_CODE=0, 164/164) |
| pass@1 | **0.00%** |
| n_correct / n_total | **0 / 164** |
| stderr | 0.0000 |

**异常发现**: 严重的 truncation 问题。median_response_length = 2048（即上限），avg = 1977.7。模型几乎在所有 task 上都生成了自然语言推理文本（"Okay, I need to..."、"The function checks..."）而非代码，然后被 2048 token 截断。错误全部是 SyntaxError——模型输出的是 CoT 思考过程而非 Python 代码。这与 GRPO 训练的 reasoning 模式一致：模型学会了"先想再写"，但 1.5B 容量不足以在 2048 token 内完成推理并输出有效代码。

---

## 实验 2: eval_humaneval_sft_standard_20_1p5b_2048

| 字段 | 值 |
|------|-----|
| exp_id | eval_humaneval_sft_standard_20_1p5b_2048 |
| 正常完成 | 是 (EXIT_CODE=0, 164/164) |
| pass@1 | **0.61%** |
| n_correct / n_total | **1 / 164** |
| stderr | 0.0061 |

**通过的 task**: HumanEval/30 (completion_length=133，短回答，未截断)

**异常发现**: 大量 task 同样命中 2048 token 截断上限，但 SFT 模型比 GRPO 模型更倾向直接输出代码（有少数短回答如 90/42/124 token），所以勉强通过了 1 个简单 task。

---

## 汇总

| 模型 | pass@1 | n_correct/164 |
|------|--------|---------------|
| GRPO CKA-only 20% 1.5B | 0.00% | 0/164 |
| SFT Standard 20% 1.5B | 0.61% | 1/164 |
| SFT CKA-only 20% 1.5B (已有) | 0.61% | 1/164 |

两个结果均真实可信。1.5B 模型在 20% 剪枝后代码生成能力基本丧失，与 D077 判断一致。GRPO 模型的 0/164 源于其 reasoning-first 生成模式在受限 token budget 下更不利。

---
