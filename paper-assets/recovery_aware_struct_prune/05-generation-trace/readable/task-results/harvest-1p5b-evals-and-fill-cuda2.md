# harvest 1p5b evals and fill cuda2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_1p5b_evals_and_fill_cuda2_20260519T162545_result.json`
- **Structured JSON:** [`3014caa6f1fe5e883edb.json`](../../sessions/30/3014caa6f1fe5e883edb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3个实验 registry 全部更新完成（DONE + metrics）。

**Step 2: cuda:2 被占用**，PID 120188 使用 14760 MiB，应该是 `eval_mbpp_grpo_cka_only_20` 仍在运行。无法启动新实验。

---

**收割汇总：**

| 实验 | pass@1 | correct/total | 状态 |
|------|--------|---------------|------|
| GRPO CKA-only 1.5B HumanEval | 0.00% | 0/164 | DONE ✓ |
| SFT CKA-only 1.5B HumanEval | 0.61% | 1/164 | DONE ✓ |
| SFT Standard HumanEval v3 | 13.41% | 22/164 | DONE ✓ |

1.5B CKA-only 模型（无论 SFT 还是 GRPO）在 HumanEval 上几乎完全失败——输出自然语言推理而非代码，全部被截断在 2048 tokens。SFT Standard 保留了部分代码生成能力（13.4%），但远低于 7B 版本。

**cuda:2** 被 MBPP GRPO CKA-only eval 占用，等它结束后再提交 MBPP SFT CKA-only。

---
