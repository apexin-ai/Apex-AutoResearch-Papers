# knowledge sync experiment plan stale ids

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_sync_experiment_plan_stale_ids_20260519T054353_result.json`
- **Structured JSON:** [`f116bae8f61810fe7311.json`](../../sessions/f1/f116bae8f61810fe7311.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 处 registry_id 已全部更新。验证结果：

| plan_id | 旧值 | 新值 | 原因 |
|---------|------|------|------|
| plan_016 | `plan_016_llama_rsft_candidates` (failed) | `plan_016_llama_grpo_qlora` (DONE/success) | 旧值指向失败的初始 candidate gen，GRPO 实验是该 plan 的核心验证 |
| plan_mvp2_grpo | `mvp2_grpo_ced_lr5e6_r1` (killed) | `mvp2_grpo_ced_kl001_r4` (DONE/success) | 旧值被 kill，r4 是完整跑完的 QLoRA GRPO 实验 |
| plan_017 | null | `plan017_14b_sft` (RUNNING) | 14B SFT 已提交运行 |
| plan_019 | `plan019_1_7b_sft_s43_r2` (DONE) | `plan019_1_7b_rsft_s44_r2` (RUNNING) | SFT 步骤已完成，当前最新进展是 1.7B RSFT 重跑 |
| plan_d112 | `d112_rsft_s44_gen_shard0` (DONE) | `d112_rsft_s44_train` (RUNNING) | gen+CED score 步骤已完成，当前最新步骤是 RSFT train |

其余 20 个 plan 的 registry_id 与 registry 一致，无需更新。

---
