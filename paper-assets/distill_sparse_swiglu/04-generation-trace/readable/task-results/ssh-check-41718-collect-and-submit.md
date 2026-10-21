# ssh check 41718 collect and submit

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_41718_collect_and_submit_20260520T134818_result.json`
- **Structured JSON:** [`66b86eaf89aaef8176a5.json`](../../sessions/66/66b86eaf89aaef8176a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Summary:

## Part A — westd-41718 状态
- **GPU 0**: NVIDIA RTX PRO 6000 Black (96GB) — 空闲 → 已被 c4_ood_kl30_s123 占用
- **GPU 1**: NVIDIA RTX PRO 6000 Black (96GB) — 空闲
- 无 Python 进程运行（PID 254228 已完成）

## Part B — C4 OOD downstream KL30 s42 结果

| Task | Metric | Value |
|------|--------|-------|
| ARC-c | acc_norm | **0.4036** |
| WinoGrande | acc | **0.6930** |
| MMLU | acc | **0.4137** |
| GSM8K | exact_match | **0.0629** |
| HellaSwag | acc_norm | **0.7074** |
| PIQA | acc_norm | **0.7399** |

results.json 中无 `model_level_sparsity` 字段。日志显示 per-layer sparsity 在 0.281–0.301 范围（target 0.30, uniform allocation）。

## Part C — c4_ood_kl30_s123 已启动
- **PID**: 259363, **GPU**: cuda:0, **Server**: westd-41718
- 日志: `~/runs/distill_sparse_swiglu/c4_ood_kl30_s123.log`
- 已在运行中（正在 tokenize + 评估 PIQA）
- Registry 已更新 hypothesis 和 parent

**注意**: `benchmark_eval.py` 没有 `--seed` 参数，源码中也无 `random`/`manual_seed`。由于使用相同 checkpoint 和配置，且 calibration 采样可能是确定性的，s123 结果可能与 s42 完全相同。如需真正的 multi-seed 变异，需在脚本中加入 seed 控制逻辑。

---
