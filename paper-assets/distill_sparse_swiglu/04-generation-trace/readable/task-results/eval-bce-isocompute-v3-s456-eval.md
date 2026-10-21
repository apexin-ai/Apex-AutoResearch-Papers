# eval bce isocompute v3 s456 eval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_bce_isocompute_v3_s456_eval_20260517T200438_result.json`
- **Structured JSON:** [`61cbd7086118c4fbb5d2.json`](../../sessions/61/61cbd7086118c4fbb5d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。实验 `bce_isocompute_v3_s456_eval` 已经在运行中：

- **状态**: RUNNING（PID 69504，tmux session on westd-34887:cuda:1）
- **已完成**: WikiText-2 PPL = 28.35（teal_global 模式，s42 对应值为 27.97）
- **当前**: MMLU loglikelihood ~80%，之后还有 WinoGrande 和 GSM8K
- **预计耗时**: 参照 s42 约 2h 总，已跑约 16min 进入 MMLU 阶段

注意：当前 eval 使用的是 `--sparsity_mode teal_global`（对应 s42 eval 中 `teal_sparse_ppl=27.97`），而非 Phase 1 的 `evaluate.py` 三模式 PPL。如果 Table 2 还需要 `predictor_hard_mask_ppl`，需要额外跑一次 `evaluate.py`。

---
