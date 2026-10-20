# urgent kill dup eval submit sft r4

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_kill-dup-eval-submit-sft-r4_20260514T114750_result.json`
- **Structured JSON:** [`4b605ca4bbb98b953b23.json`](../../sessions/4b/4b605ca4bbb98b953b23.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

plan006-prolog-exec-s42 registry 已更新。

**总结：**

1. **Kill 重复 eval**: PID 567813 和 570911 已 kill，仅保留 570264（已完成）
2. **Eval 结果** (plan006-prolog-exec-s42): prove_rate=83%, mean_isr=0.031, proved_only_isr=0.037 — registry 已更新
3. **plan009-sft-r4 无法提交**: GPU 1 被 PID 572609 占用 (~56GB)，是一个已在跑的 `plan009_sft_baseline_s42`（`--gpu 1 --no_wandb`，已运行 ~4 分钟）

**需要你决定**：PID 572609 这个现有 SFT 进程要 kill 还是等它跑完？它用了 `--gpu 1` 而非 `CUDA_VISIBLE_DEVICES=1 --gpu 0`（违反 C002），且没有 wandb 记录。

---
