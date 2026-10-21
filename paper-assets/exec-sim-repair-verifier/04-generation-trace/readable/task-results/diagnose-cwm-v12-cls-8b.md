# diagnose cwm v12 cls 8b

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cwm-v12-cls-8b_20260514T010311_result.json`
- **Structured JSON:** [`7f650abf90b02cd6b396.json`](../../sessions/7f/7f650abf90b02cd6b396.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，报告已写入 `artifacts/diagnosis_cwm_v12_cls_8b.md`。

**核心结论**:

- **全部为人为 kill，非 OOM**。cwm-v12 明确记录 EXIT_CODE=137，其余实验日志无任何 OOM/错误信息。
- 三个实验训练进度均在 10-11%（步数 643-756/6633），所有 checkpoint 都含有效的 adapter_model.safetensors。
- **Eval pipeline 已接管全部 4 块 GPU**，当前在跑 eval_repo_cwm.py 和 eval_repo_cls.py，使用的是各实验的 best checkpoint。
- cls-8b-conda 的 eval_loss 在 step 200 后开始上升，checkpoint-200 是最优的（eval pipeline 也选了 cls_v5_conda 的 checkpoint-200，说明已知晓这一点）。

---
