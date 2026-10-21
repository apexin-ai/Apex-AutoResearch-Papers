# cpu eval pipeline prep

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_eval-pipeline-prep_20260515T154623_result.json`
- **Structured JSON:** [`53b5cbaf28d8fe9567b6.json`](../../sessions/53/53b5cbaf28d8fe9567b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

预验证完成。总结：

**eval 管线状态: ✅ 可用**

- `eval_perplexity.py` 存在，参数明确（`--checkpoints`, `--data_path`, `--max_docs`, `--output_path`）
- 依赖已安装（tau_06 eval 已成功跑过）
- 评估数据 `data/human/eval_holdout.jsonl` 就绪（67,823 行）

**关键发现 — 目录名差异**:
- tau_05 → 实际目录 `tau_0.5_seed42`（含点号，与 registry exp_id `tau_05_seed42` 不一致）
- tau_07 → 实际目录 `tau_0.7_seed42`（含点号）
- tau_09/tau_095 → 目录名无点号，与 registry 一致

**训练进度**: tau_05 最快 (~74%), tau_095 最慢 (~33%)，全部完成预计还需 ~1.5-2 小时。

**执行前置条件**: 必须等 `final/` 目录创建后再跑 eval。推荐用方案 A 一次性跑全部 4 个，预计 ~10 分钟。

完整命令和参数已写入 artifact `tau_sweep_eval_commands.md`。

---
