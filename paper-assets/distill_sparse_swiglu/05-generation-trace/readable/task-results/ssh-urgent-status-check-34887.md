# ssh urgent status check 34887

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_status_check_34887_20260520T205249_result.json`
- **Structured JSON:** [`747e88de52b086551981.json`](../../sessions/74/747e88de52b086551981.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. GPU 状态
| GPU | 利用率 | 显存 |
|-----|--------|------|
| cuda:0 | 0% | 0 / 97887 MiB |
| cuda:1 | 0% | 0 / 97887 MiB |

**两卡完全空闲。**

### 2. MSE 50% s123 进程
**PID 235945 和 235955 均已死亡。**

### 3. 训练状态：已完成 1000/1000 步
- 最终 step: `[Step 1000/1000] loss=185.000015 mse=0.000017 constraint=185.000000 sparsity=0.051 lambda=1000.00 tau=0.100`
- Checkpoint 已保存: `checkpoints/mse50_s123/predictor_mse.pt` (145MB, May 21 03:11)

### 4. Eval 状态：**失败**
- `benchmark_eval.py` 在 lm_eval 加载数据集时崩溃
- 错误: `RuntimeError: Cannot send a request, as the client has been closed.` — HuggingFace Hub httpx client 连接问题
- `mse50_s123_eval/` 目录为空，**无结果产出**

### 5. 问题分析
训练正常完成但 **sparsity 收敛到 0.051（~5%）而非目标 50%**，MSE loss 约束项主导了优化。Eval 因 HF Hub 网络问题失败，需要重新启动 eval（先 `source /etc/network_turbo` 修复网络）。

**注意**: sparsity=0.051 严重偏离 50% 目标——MSE loss 训练出的 predictor 几乎不做稀疏化，这个 checkpoint 可能无法直接用于论文对比。

---
