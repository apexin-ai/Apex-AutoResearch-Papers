# infra gpu status check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-status-check_20260516T021905_result.json`
- **Structured JSON:** [`4c71f56e75331bec4d78.json`](../../sessions/4c/4c71f56e75331bec4d78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 全局状态（4× NVIDIA RTX PRO 6000 Blackwell, 98GB each）

| GPU | 实验 | 显存占用 | GPU利用率 |
|-----|------|----------|-----------|
| **cuda:0** | contamination_60_tau07_seed42 (PID 282223) | 46514/97887 MiB | 99% |
| **cuda:1** | grid_b0_3_seed42 (PID 274309) | 46514/97887 MiB | 99% |
| **cuda:2** | contamination_60_ess_only_seed42 (PID 265017) | 46514/97887 MiB | 97% |
| **cuda:3** | detect_remove_baseline_seed42 (PID 276739) | 46514/97887 MiB | 99% |

### 训练进度

| 实验 | GPU | Step | 进度 | 速度 | ETA |
|------|-----|------|------|------|-----|
| contamination_60_ess_only_seed42 | cuda:2 | 4705/6103 | **77%** | 2.12s/it | ~49min |
| grid_b0_3_seed42 | cuda:1 | 1669/6103 | **27%** | 2.12s/it | ~2h36m |
| detect_remove_baseline_seed42 | cuda:3 | 1075/6103 | **18%** | 2.11s/it | ~2h57m |
| contamination_60_tau07_seed42 | cuda:0 | 283/6103 | **5%** | 2.20s/it | ~3h33m |

### cuda:0 冲突结论

- **contamination_60_tau07_seed42**：存活，正常运行（PID 282218 wrapper + 282223 python）
- **tau_05_nmin2_seed42**：**已死**。日志显示跑到 step 258/6103 (4%) 后被 SIGHUP 终止（EXIT_CODE=129）。PID 281298 不存在。它被杀掉为 contamination_60_tau07_seed42 让路了。

### detect_remove_baseline_seed42 状态

正常运行。WANDB_MODE=disabled，日志可见。weighting/b=0.0, ess=4.0（uniform weighting 符合预期），unweighted_loss ≈ weighted_loss。当前 epoch 0.11，step 1075/6103。

### 总结

4 个 GPU 全部满载运行，各跑 1 个实验，无冲突。tau_05_nmin2_seed42 需要重新调度到有空闲 GPU 时再启动。

---
