# code fix c1 regen oom

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_c1_regen_oom_20260517T084841_result.json`
- **Structured JSON:** [`c940d1f0974d133ea53b.json`](../../sessions/c9/c940d1f0974d133ea53b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Training 正在进行！** Step 28/250 (11%)，已跑 30 秒无 OOM。`gradient_checkpointing` + `use_reentrant=False` 生效。

GPU 0 峰值 ~13 GiB / 32 GiB，余量充足。修复完成：
1. `score.py`: `gc.collect()` 确保 ArmoRM 释放（16 GiB → 1.5 GiB）
2. `pipeline.py`: score_all 后额外 `gc.collect() + empty_cache()` 安全网
3. `train_sft.py`: LoRA 模式开启 `gradient_checkpointing=True` + `use_reentrant=False`
4. `run_c1_regen_v2.py`: 从 Gen 1 断点续跑，跳过已完成的 Gen 0

实验 `c1-regen-v2` 在 tmux session 中正常运行，Gen 1 training 步进正常，预计 ~4 分钟完成 250 steps。之后���有 Gen 1 evaluate + Gen 2 全流程。

---
