# eval westd collect and imm v2 eval

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_westd_collect_and_imm_v2_eval_20260516T233249_result.json`
- **Structured JSON:** [`c1d6e802f37e635273b6.json`](../../sessions/c1/c1d6e802f37e635273b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集。结果汇总：

```
=== WESTD STATUS ===
cuda:0: IMM v2 eval 已启动 (PID 455965, 3539 MiB) — libero_object, acis_prune
cuda:1: Full FT seed=0 100K eval 运行中 (PID 452461, 3684 MiB) — libero_spatial

=== COLLECTED EVAL RESULTS ===
[1] Full FT 100K seed=42 libero_object (formal, 50eps/task): SR=44.8% [CI: 40.5%-49.2%]
[2] Full FT seed=0 100K libero_object (50eps/task):          SR=51.0% [CI: 46.6%-55.4%]
[3] Full FT 50K libero_spatial (10eps/task):                  SR=34.0% [CI: 25.5%-43.7%]
[4] Full FT 50K libero_goal (10eps/task):                     SR=42.0% [CI: 32.8%-51.8%]
[5] LoRA 50K libero_object (5eps/task):                       SR=0.0%  (完全失败)

=== IMM v2 EVAL ===
Checkpoint: checkpoints/libero_imm_twostage_fullft/final/checkpoint.pt
  (stage2 训练到 step 18000, 有 final checkpoint)
Config: configs/libero_imm_twostage_fullft.yaml
Eval started: YES — libero_object, 50 eps/task, cuda:0, mode=acis_prune
Output: eval_results/imm_v2_fullft_libero_object.json
tmux session: imm_v2_eval

=== PENDING EVALS ===
- [cuda:0] IMM v2 fullft libero_object (刚启动)
- [cuda:1] Full FT seed=0 100K libero_spatial (运行中，已跑~2分钟)
```

**关键发现：**
- Full FT 100K seed=0 (51.0%) 显著优于 seed=42 (44.8%)，说明 seed 间方差较大
- LoRA 50K 完全失败 (0%)，与 Full FT 差距极大
- Full FT 50K 在 spatial/goal 上只有 34%/42%（仅 10 eps/task，CI 很宽）
- seed=0 的 spatial eval 正在跑，完成后可以对比

---
