# code eval llama s4s7 35694

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-llama-s4s7-35694_20260521T122425_result.json`
- **Structured JSON:** [`855ccf8ce1aa6716587e.json`](../../sessions/85/855ccf8ce1aa6716587e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the complete summary.

---

## 产出总结

### 1. Phase 1: Llama clean_s4-s7 Eval 结果（4 GPU 并行，已完成）

| Seed | theta_mle | lz* | accuracy | n_items |
|------|-----------|-----|----------|---------|
| s4 | -0.644 | 0.021 | 0.592 | 14042 |
| s5 | -0.630 | 1.732 | 0.597 | 14042 |
| s6 | -0.603 | 2.847 | 0.601 | 14042 |
| s7 | -0.636 | -0.401 | 0.593 | 14042 |

Registry: 4 条均已注册为 DONE。

### 2. Phase 2: GPU 分配 + PID

| GPU | 任务 | PID | 状态 |
|-----|------|-----|------|
| 0 | Mistral clean_s2 eval | 139998 | **DONE** (~14min) |
| 1 | Mistral clean_s3 eval | 140492 | **DONE** (~14min) |
| 2 | GRPO v3 training (exp-post-rl-v3) | 141861 | **RUNNING** step 264/3000 |
| 3 | (空闲——Llama s2/s3 已有结果) | — | — |

### 3. Phase 2 Eval 结果: Mistral clean_s2/s3

| Condition | theta_mle | lz* | accuracy | n_items |
|-----------|-----------|-----|----------|---------|
| clean_s2 | -0.963 | -1.046 | 0.543 | 14042 |
| clean_s3 | -0.973 | 3.279 | 0.541 | 14042 |

Registry: 2 条均已注册为 DONE。

### 4. GRPO v3 启动验证

- **启动成功**：经两次修复后（`generation_batch_size=16` + `WANDB_MODE=disabled`）正常启动
- **当前进度**：step 264/3000，~2.65s/it，ETA ~2h
- **frac_reward_zero_std**：所有 logged steps 均在 0.2-0.8 范围内，**全部 < 1.0** ✓
- 关键指标趋势：
  - reward: -0.1 ~ 0.925（波动正常，overall 正向）
  - entropy: 1.6-1.9（健康范围）
  - clip_ratio: < 0.005（很低，训练稳定）
- **日志路径**：`~/runs/irt_personfit_contam/exp-post-rl-v3.log`
- **tmux session**：`exp-post-rl-v3`

### 5. 异常 / 注意事项

1. **lz\* 跨 seed 方差大**：Llama clean seeds lz\* 范围 [-0.401, 2.847]，Mistral clean seeds 范围 [-1.046, 3.279]。clean 条件下 lz\* 的 seed 间变异远大于预期（理论上应接近 0），这对后续用 lz\* 区分 clean vs contam 的 discriminability 可能构成挑战。
2. **GRPO v3 metrics 延迟可见**：因 `report_to="wandb"` + `WANDB_MODE=disabled`，前 ~100 步的 metrics 未实时输出到 log（仅 tqdm progress bar），后续 step 才开始 flush metrics 行。建议未来将 `report_to="none"` 或配置 wandb offline 以确保 stdout 日志完整。
3. **Phase 1 nohup 路径问题**：batch 启动 4 个 nohup 子进程时，3 个未继承 conda PATH 导致 `python` not found，需用绝对路径 `/root/miniconda3/bin/python`。

---
