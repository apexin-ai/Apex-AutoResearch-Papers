# fix 41312 gpu conflict kill

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_41312_gpu_conflict_kill_20260517T150406_result.json`
- **Structured JSON:** [`5387c062851f2b69c9e8.json`](../../sessions/53/5387c062851f2b69c9e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Kill 确认
- **PID 109941** — 已 kill，ps 无输出 ✓
- **PID 108506** — 已 kill，ps 无输出 ✓
- **PID 109024** — 仍在运行 ✓（uniform_seed42 训练，GPU 0）

### nvidia-smi
```
GPU 0: 46539MiB / 97887MiB — PID 109024 (uniform retrain) — 100% util
GPU 1: 0MiB — 空闲 ✓
GPU 2: 0MiB — 空闲
GPU 3: 46539MiB — PID 88496 (另一个训练任务)
```

GPU 1 已完全释放。

### adaptive_fix_seed42 checkpoint 路径
```
/root/autodl-tmp/provenance_weight_training/output/models/adaptive_fix_seed42/final/
```

lm-eval 日志确认使用了该路径，评估结果已保存在：
```
/root/autodl-tmp/provenance_weight_training/output/eval/qwen_adaptive_fix_all/__root__autodl-tmp__provenance_weight_training__output__models__adaptive_fix_seed42__final/results_2026-05-17T22-58-46.918675.json
```

### tmux sessions
- `grid_b0_3_seed456` — 5/17 20:53 创建
- `qwen06b_uniform_seed42` — 5/17 22:59 创建（即 PID 109024 所在）

---
