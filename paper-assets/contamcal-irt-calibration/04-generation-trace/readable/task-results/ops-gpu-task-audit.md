# ops gpu task audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_task_audit_20260517T131212_result.json`
- **Structured JSON:** [`711fa54f54ad78d12e37.json`](../../sessions/71/711fa54f54ad78d12e37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data checked. Here's the report:

## Part 1: MMLU τ 重算
- **全量 per-item data 已有?** 是 — 所有模型的 `eval_results.json` 包含 14,042 MMLU per-item responses
- **需要 GPU?** 否 — 纯 CPU Stan MCMC
- **当前 300 items 来源:** `run_pooled_rrf_irt.py` 第 33 行 `MAX_ITEMS = 300`，对 MMLU 14042→300 随机子采样
- **注意:** `compute_vanilla_2pl_tau.py` 今天 17:40 已启动过一次（27 models × 14042 items），但 log 在 MCMC warmup 开头截断（~1.5s/iter，预计 MMLU 单 benchmark 需 ~1.7h CPU time）。需确认该进程是否仍在运行或已崩溃
- **估计时间:** 如果重算，3 个 benchmark 合计约 2-3 CPU-hours，0 GPU-hours

## Part 2: ARC Cross-Family IRT
- **Llama ARC per-item data:** 有 — 4 个模型（d000/d005/d025/d100），1172 items/model，格式完整（correct: bool, pred, gold）
- **Qwen ARC per-item data:** 有 — 0.5B/1.5B/3B 全覆盖，同格式
- **RRF ARC coverage:** 有 — Llama 4 模型 + Qwen 各 dosage 均有 RRF scores
- **数据就绪?** 是 — **且 cross-family v5 已完成 ARC IRT fitting**（`/root/autodl-tmp/exp006/cross_family_v5/arc_challenge/irt_results.json`）
- **缺什么:** 无

## Part 3: GSM8K Cross-Family IRT
- **Llama GSM8K per-item data:** 有 — 4 个模型，1319 items/model，pred/gold + correct 完整
- **Qwen GSM8K per-item data:** 有 — eval_results.json 中 gsm8k 节完整
- **RRF GSM8K coverage:** 有 — Llama + Qwen 全覆盖
- **GSM8K IRT 可行性:** 可行 — 虽然 GSM8K 是 open-ended math，但 eval 使用 logprob MC format，产出 per-item 0/1 responses，适用 IRT
- **数据就绪?** 是 — **且 cross-family v5 已完成 GSM8K IRT fitting**（`/root/autodl-tmp/exp006/cross_family_v5/gsm8k/irt_results.json`）
- **缺什么:** 无

---

**结论：3 项任务均不需要 GPU。** 所有 per-item eval data 已存在，IRT fitting 是纯 CPU Stan MCMC。ARC/GSM8K 的 cross-family IRT 已在 v5 中完成（MMLU 用 300 subsample）。全量 MMLU 14k 的 vanilla 2PL 重算也只需 CPU。这 3 类任务无法填充 6 张 A6000。

---
