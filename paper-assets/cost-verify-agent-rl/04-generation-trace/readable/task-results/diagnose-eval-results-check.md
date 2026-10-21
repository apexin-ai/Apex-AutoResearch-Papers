# diagnose eval results check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_results_check_20260521T133357_result.json`
- **Structured JSON:** [`8a14304cb3d4d0893ed3.json`](../../sessions/8a/8a14304cb3d4d0893ed3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### exp029_seed6_ood_eval — FAILED
- **错误**: `ValueError: Unsupported model: /root/autodl-tmp/checkpoints/exp029-seed6/global_step_15_hf`
- **原因**: `ctx_manager.py:get_special_tokens()` 不识别 RL checkpoint 的 `name_or_path`。SFT baseline 用的是原始 checkpoint 路径 `qwen3_exp021_ragen_sft_v4` 所以没这个问题，而 seed6 的 HF 导出 checkpoint 路径名变了。
- **修复方向**: 需要在 `get_special_tokens()` 中添加对 RL checkpoint 路径的支持，或者在导出 HF checkpoint 时保留原始 tokenizer 的 `name_or_path`。
- Registry: DONE/failed, cron 已删除。

### sft_baseline_ood_eval_v2 — STILL RUNNING
- W&B run: `r9llx4v7`, state=running, 尚无 metrics 产出
- PID 282634 存活, GPU 3 占用 90GB (0% util — 可能在 CPU-bound 的 Alfworld 环境交互阶段)
- 评估 134 个 AlfworldSG_OOD 任务，每个最多 50 turns，预计还需较长时间
- Cron 保留。

### GPU 状态
| GPU | 显存 | 利用率 | 用途 |
|-----|------|--------|------|
| 0 | 97/98 GB | 100% | 其他任务 |
| 1 | 97/98 GB | 100% | 其他任务 |
| 2 | 0/98 GB | 0% | 空闲（seed6 eval 已退出）|
| 3 | 90/98 GB | 0% | SFT baseline OOD eval |

---
