# diagnose 8b cell c episode v9b

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_8b_cell_c_episode_v9b_20260519T185743_result.json`
- **Structured JSON:** [`1fa0466d140915d97ee9.json`](../../sessions/1f/1fa0466d140915d97ee9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。报告已保存到 `artifacts/diag_v9b.md`。

**结论：** v9b 不是 OOM，是代码 bug。`dp_actor.py:223` 访问了 FSDP1 专属属性 `_fsdp_wrapped_module`，但 FSDP2 的 `FSDPQwen3ForCausalLM` 没有这个属性。val_before_train 通过是因为它只做 generation 不走 `compute_log_prob`，训练第一步就崩了。

**修复：** 将 line 223 改为 `hasattr` 检查兼容 FSDP1/FSDP2（方案 A），或同时处理后续的 `FSDP.summon_full_params` 调用（方案 B）。本实验不用 LoRA，方案 A 即可解除阻塞。

---
