# ssh check gpu conflict

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_gpu_conflict_20260514T025148_result.json`
- **Structured JSON:** [`97b17a7622168dde44c9.json`](../../sessions/97/97b17a7622168dde44c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 进程状态

| 实验 | 原始 PID | 当前状态 |
|------|---------|---------|
| exp_006_graduated_filtering | 46129 (bash wrapper) → 55665 (python3) | **存活**，正在训练 `binary-ours_s456`，step 2583/2814 (92%)，~1.26 it/s |
| exp_015_neural_probe | 56559 | **已死**，exit code 129 (SIGHUP) |

### GPU 显存

- GPU: RTX 4090D，24564 MiB 总量
- 当前占用: PID 55665 (exp_006) → **15504 MiB** (63%)，GPU-Util 82%
- exp_015 已不在 GPU 上

### exp_006 进度

总计 50 runs（6 strategies × 5 seeds，graduated 额外 ×5 alphas）。已完成：
- `base_model` — 基线 eval ✓
- `no-filter` × 5 seeds — 全部完成 ✓
- `binary-ours_s42`, `binary-ours_s123` — 完成 ✓
- `binary-ours_s456` — **训练中 92%**，约 3 分钟内完成训练，之后还有 eval

**7/50 runs 完成，1 个在跑**。剩余 42 runs，按每 run ~25 min 估算还需 ~17.5 小时。

### exp_015 死因

日志显示 exp_015 在做 Qwen 模型推理时遇到 **OOM**（两个进程同时占 GPU：exp_006 用 13.36 GB + exp_015 子进程用 9.09 GB → 超出 24 GB）。但 OOM 后脚本用了 fallback 路径（可能用预计算的 embeddings），**成功完成了全部 probe 分析**，输出了结果文件后收到 SIGHUP 退出。

结果已保存: `artifacts/exp015_neural_probe_results.json`
- K\*(neural probe) = 3, K\*(lgbm) = 2
- 分类准确率 = 0.4335
- 相邻 AUC: 0v1=0.987, 1v2=0.698, 2v3=0.620, 3v4=0.593, 4v5=0.575

### 结论

**不需要 kill 任何进程。** exp_015 已自然结束且结果完整保存。exp_006 独占 GPU 正常运行，15.5 GB 显存无压力。

---
