# code update math500 table

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_update_math500_table_20260523T234457_result.json`
- **Structured JSON:** [`9e780b09205f3380a775.json`](../../sessions/9e/9e780b09205f3380a775.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

生成完成。汇报如下：

---

**已填入的 5 个确认结果 — 全部正确**：

| exp_id | 预期 | 表中 |
|--------|------|------|
| sft_cka_only_20_fixed_v2 | 27.4 | 27.4 ✓ |
| grpo_cka_only_20_fixed | 27.6 | 27.6 ✓ |
| grpo_standard_20_fixed | 27.0 | 27.0 ✓ |
| grpo_rasp_alpha1p0_20_fixed | 23.0 | 23.0 ✓ |
| sft_rasp_alpha1p0_20_fixed | 21.6 | 21.6 ✓ |

另外 Dense baseline (SFT 73.6, GRPO 69.0) 也已填入。

**修复**：`eval_math500_grpo_standard_20_fixed` 的 registry metrics 使用 `math500_acc` 而非 `accuracy`，在 `extract_from_registry` 中加了 fallback：`metrics.get("accuracy") or metrics.get("math500_acc")`。

**缺失 cells（14 个实验，显示 "--"）**：

方法对比 20%:
- Standard: SFT 缺 | GRPO Trunc 缺
- Random: SFT+GRPO 全缺

α sweep:
- α=0.5: 全缺（SFT 有 status=DONE 但无 metrics）
- α=2.0 / 3.0 / 4.0: 全缺

25% sparsity:
- Standard 25%: SFT 缺
- CKA-only 25%: SFT+GRPO 全缺（GRPO 状态 RUNNING）

**部分 truncation rate 也缺失**：grpo_cka_only (27.6% 但无 trunc)、sft_rasp_alpha1p0 (21.6% 但无 trunc)、grpo_standard (27.0% 但无 trunc — registry 中有 `truncated=222/500=44.4%` 但脚本没匹配到，因为缺少 `num_total` key 而用了 `math500_total`)。

需要我也修复 truncation rate 的 key fallback 吗？

---
