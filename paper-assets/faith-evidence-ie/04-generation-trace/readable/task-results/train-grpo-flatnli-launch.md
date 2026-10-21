# train grpo flatnli launch

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_grpo-flatnli-launch_20260514T073058_result.json`
- **Structured JSON:** [`a1a7dcea9319157836d5.json`](../../sessions/a1/a1a7dcea9319157836d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**问题：gpu-5090-4x-1 当前被 `mvp2_grpo_ced`（Stage 3）占用，4 卡都在用。**

当前状态：
- 进度：5/189 步（2.6%），~2 min/步，预计还需 ~6 小时
- 显存：17-24 GB/卡（总 32 GB），无法并行启动其他训练
- 训练指标（step 5）：format_reward=0.49, f1_reward=0.008, ced_reward=0.08, total_reward=0.58

三个选项：
1. **等 CED 跑完**（~6h），然后启动 flat-NLI + SFT eval
2. **Kill CED**，立即启动 flat-NLI（CED 进度会丢失）
3. **用其他服务器**跑 flat-NLI

你想怎么处理？

---
