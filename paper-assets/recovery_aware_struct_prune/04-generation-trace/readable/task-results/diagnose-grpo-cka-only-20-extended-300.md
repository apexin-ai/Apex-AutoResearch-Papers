# diagnose grpo cka only 20 extended 300

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_grpo_cka_only_20_extended_300_20260518T220207_result.json`
- **Structured JSON:** [`024f90242f8891d83cd8.json`](../../sessions/02/024f90242f8891d83cd8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。

**结论：grpo_cka_only_20_extended_300 训练成功，registry 标记正确。**

关键发现：
- **300/300 步完成**，模型已保存，W&B run 状态 `finished`
- **EXIT_CODE=129 是假阳性** — SIGHUP 发生在训练完成、模型保存、W&B finalize 全部结束之后，来自 tmux/wrapper 清理信号
- **指标与 registry 完全一致**：peak_reward=0.4444 @ step 280，final_reward=0.3075 @ step 300
- **Reward 轨迹**：0.22-0.44 范围内持续振荡，无 collapse。与 Standard extended 的 reward collapse (0.102→0.056) 形成鲜明对比，确认 CKA-only 的结构优势在长训练中持续
- **进程已完全退出**，无残留

报告已追加到 memory.md。

---
