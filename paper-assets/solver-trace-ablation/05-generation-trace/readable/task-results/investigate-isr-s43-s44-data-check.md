# investigate isr s43 s44 data check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_isr-s43-s44-data-check_20260515T141744_result.json`
- **Structured JSON:** [`5fb7796613e4c2aafcf3.json`](../../sessions/5f/5fb7796613e4c2aafcf3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## ISR s43 (plan002-additive-b01-s43)
- **checkpoint**: NOT_FOUND — 输出目录 `/root/autodl-tmp/outputs/plan002_additive_b01_s43` 不存在，无 safetensors
- **eval_sta_results.json**: NOT_FOUND — outputs、backup、runs 目录均无 eval 文件
- **其他文件**: 仅有训练日志 `/root/runs/solver-trace-ablation/plan002-additive-b01-s43.log`（训练完成，500 步，EXIT_CODE=0，final prove_rate=0.688, mean_isr=0.504）
- **结论: 需重训**

## ISR s44 (plan002-additive-b01-s44)
- **checkpoint**: NOT_FOUND — 输出目录 `/root/autodl-tmp/outputs/plan002_additive_b01_s44` 不存在
- **eval_sta_results.json**: NOT_FOUND（无独立 eval_sta 文件）
- **其他 eval 文件**: `/root/runs/solver-trace-ablation/plan002-additive-b01-s44-eval.json` 存在且完整
  - 100 samples，prove_rate=0.89，mean_isr=0.803，proved_only_mean_isr=0.9022
  - 每个 sample 有完整的 execution_reward / sta_reward / combined_reward / details（n_components, n_necessary, isr, 逐 component 的 is_necessary）
  - model_path 指向已删除的 `/root/autodl-tmp/outputs/plan002_additive_b01_s44`
- **结论: 有完整 eval 数据，无需操作**

---

**汇总**: s43 checkpoint 和 eval 均已丢失，需重训。s44 checkpoint 已丢失但有完整 eval 结果，可直接使用。备份目录仅有 s42 的 eval，无 s43/s44。

---
