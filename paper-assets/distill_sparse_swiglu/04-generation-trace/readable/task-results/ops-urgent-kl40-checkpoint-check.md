# ops urgent kl40 checkpoint check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-kl40-checkpoint-check_20260518T190135_result.json`
- **Structured JSON:** [`e6f572f6aa6ec4c376f6.json`](../../sessions/e6/e6f572f6aa6ec4c376f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

关键信息找到了。

## 结果

### kl_sparsity40_s42 checkpoint

**不存在。** 两台服务器（westd-34887、westd-41718）的 `checkpoints/` 目录下都没有 `kl_sparsity40_s42/` 文件夹。

存在的相邻 sparsity checkpoints：`kl_sparsity35_s42`、`kl_sparsity45_s42`（均在 34887）。

### bench_kl40_global 用的 checkpoint

Registry 记录（`registry.yaml:3311`）显示命令行用的是：
```
checkpoints/kl_sparsity40_s42/predictor_kl_normalized.pt
```
这个实验在 2026-05-16 成功完成（PPL=10.117, MMLU=38.06%），说明 **checkpoint 当时存在但后来被删除了**。

### d030_kl40_uniform 也引用了 40% 

也有 `d030_kl40_uniform` 实验（DONE/success），同样使用了 40% sparsity 配置。

### 34887 GPU 状态

| GPU | 状态 | 显存 | 利用率 |
|-----|------|------|--------|
| cuda:0 | **占用** | 67.0 / 97.9 GB | 63% |
| cuda:1 | **空闲** | 0 / 97.9 GB | 0% |

GPU 0 有进程在跑（PID 47633），GPU 1 完全空闲可用。

### 总结

`kl_sparsity40_s42` checkpoint 曾经存在于 westd-34887 并被 `bench_kl40_global` 成功使用，但目前已不在两台服务器的磁盘上。如果需要重新评测（如 `kl_sparsity40_s42_eval_teal_uniform` 还在 PREPARING 状态），需要**重新训练**该 checkpoint。

---
