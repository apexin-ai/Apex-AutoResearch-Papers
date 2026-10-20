# exp l1 fix redeploy restart

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_l1-fix-redeploy-restart_20260512T132518_result.json`
- **Structured JSON:** [`72b1b0f443a7feb9850a.json`](../../sessions/72/72b1b0f443a7feb9850a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

- **Step 5: PASS** — PID 111195 正在运行，已完成 44 次 LiteLLM 调用，tau-Bench 任务执行中。

---

## 汇总

| Step | Result | Detail |
|------|--------|--------|
| Step 1 | **PASS** | GPU 1 已清空 (3MiB, 0%) |
| Step 2 | **PASS** | GPU 2 僵尸 vLLM 已清除 |
| Step 3a | **PASS** | behavioral_fingerprint.py: 300 行，`_MODAL_REQUEST_RE` / `_is_modal_request` / `_CONFIRMATION_RE` 均存在 |
| Step 3b | **PASS** | h_gate_evaluator.py: 201 行，`secondary_metric` 存在 |
| Step 3c | **PASS** | run_mvp_experiment.py: 514 行，`context_overflow` / `ContextWindowExceededError` 存在 |
| Step 3d | **PASS** | `###STOP###` 在两个 prompt 中，`question_rate: 10` 在 yaml 中，prompt_loader.py 131 行 |
| Step 4 | **PASS** | vLLM 仅在 GPU 2 (22088MiB)，`/v1/models` 返回 `democalib-qwen`，max_model_len=32768 |
| Step 5 | **PASS** | PID 111195 运行中，44 次 LiteLLM 调用完成 |

---
