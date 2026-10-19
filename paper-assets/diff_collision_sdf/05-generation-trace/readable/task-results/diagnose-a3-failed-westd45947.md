# diagnose a3 failed westd45947

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_a3_failed_westd45947_20260520T073616_result.json`
- **Structured JSON:** [`cae72724413f5820da88.json`](../../sessions/ca/cae72724413f5820da88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 核心发现：实验**没有失败**，但在 CPU 上跑

| 项目 | 状态 |
|------|------|
| spatial_bowl (PID 55321) | **运行中** — `Training: 10% \| 3000/30000`，85+ 分钟 |
| object_pudding (PID 55399) | **运行中** — `Training: 8% \| 2500/30000`，80+ 分钟 |
| Exit 文件 | **不存在** — 进程未退出 |
| GPU 显存 | **0MiB** — 两块 RTX PRO 6000 (98GB) 完全空闲 |
| 模型设备 | `device=cpu`（日志 DIAG 行明确显示） |
| 系统内存 | 充足（~975GB 可用） |
| 磁盘 | 充足（216GB/250GB 可用） |

### 根因分类：**环境/代码 bug — 模型未迁移到 GPU**

日志中的 `DIAG: BEFORE load - action_in_proj.weight device=cpu` 和 `DIAG: AFTER load - action_in_proj.weight device=cpu` 明确显示模型始终在 CPU 上。

**JAX `CUDA_ERROR_NO_DEVICE` 是红鲱鱼** — 这是 JAX 自身的 CUDA 初始化失败（`jax_plugins.xla_cuda12` 不兼容 CUDA 13.2），但项目用 PyTorch 训练，PyTorch CUDA 工作正常（`torch.cuda.is_available()=True, gpus=2`）。

### 影响

在 CPU 上跑 30000 步预计需要 **~14 小时**（vs GPU 约 30-60 分钟），浪费 GPU 资源。

### 建议

1. **立即 kill 这两个进程**，在 CPU 上继续跑没有意义
2. **查 `train_loop` / `train_pytorch.py` 中的 device 分配逻辑**，确保 `model.to("cuda")` 被执行。可能是 `on_model_created` 回调中 `device` 参数本身就是 `cpu`
3. **排查 `--resume` 路径**是否绕过了 `.to(device)` 调用
4. 修复后重新提交实验

是否需要我 kill 这两个进程并进一步排查代码？

---
