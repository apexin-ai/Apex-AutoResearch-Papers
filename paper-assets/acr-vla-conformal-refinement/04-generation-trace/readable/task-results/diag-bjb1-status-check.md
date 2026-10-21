# diag bjb1 status check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_bjb1-status-check_20260513T231015_result.json`
- **Structured JSON:** [`21cb8a0ad769deedb623.json`](../../sessions/21/21cb8a0ad769deedb623.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### 1. evaluate.py P0 bug — **已修复**

`rollout_single`（第199-215行）中**没有 `env.reset()` 调用**：
```python
def rollout_single(env, init_state, action_fn, max_steps=300):
    obs = env.set_init_state(init_state)  # 第201行：直接设初始状态
    for _ in range(5):
        obs, _, _, _ = env.step(np.zeros(7))  # 5步warmup
```
`set_init_state` 是第一个调用，不会被 `env.reset()` 覆盖。Bug 已修复。

### 2. eval-acr-vla-spatial-v1 — **不在运行**

服务器上没有名为 `eval-acr-vla-spatial-v1` 的进程。取而代之的是 3 个**新的**评估实验（均使用修复后代码）：

| 实验 | 模式 | GPU | 状态 |
|------|------|-----|------|
| eval-spatial-v6-full | vla_only | 0 | 运行中，10 tasks 已加载 |
| eval-acr-spatial-v2 | acr_vla | 0 | 运行中，CRM 已加载 (337K params) |
| eval-reconvla-spatial-v3 | reconvla | 2 | 运行中，10 tasks 已加载 |

三个 eval 日志都只显示到模型/环境加载完成阶段，尚未输出 rollout 结果。

### 3. crm-train-a3-obs-only — **在运行**

PID 104611，GPU 3，`input_mode=obs_only`，spatial+object 合计 26737 样本。当前进度：

- Epoch 5/50，val_loss=0.018319
- 最佳 val_loss=0.018312（epoch 4）
- 训练收敛良好，loss 从 epoch 1 的 0.059→0.029 快速下降

**注意**：发现 PID 114104、114105 有两个重复的 `train_crm.py` 进程（07:10 启动），可能是误启动的副本，占用内存但 GPU 利用率低。

### 4. GPU 使用

| GPU | 显存占用 | 利用率 | 负载 |
|-----|---------|--------|------|
| 0 | 12040/24564 MiB (49%) | 22% | eval-v6-full + eval-acr-v2 |
| 1 | 1459/24564 MiB (6%) | 24% | 空闲（可能是重复 train_crm 进程） |
| 2 | 6732/24564 MiB (27%) | 21% | eval-reconvla-v3 |
| 3 | 565/24564 MiB (2%) | 10% | crm-train obs_only |

GPU 1 和 3 基本空闲，可调度新任务。建议清理 PID 114104/114105 两个重复的 train_crm 进程。

---
