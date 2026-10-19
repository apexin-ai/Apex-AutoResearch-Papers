# ops gpu collision check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_collision_check_20260515T202601_result.json`
- **Structured JSON:** [`12de5b1488d14b26c232.json`](../../sessions/12/12de5b1488d14b26c232.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### cuda:0
- **PID 129187** — `python src/train.py` (bce_isocompute_v2_s42), 占用 90938 MiB
- 状态：**仍在运行**（stat: Rl），已完成 step 500/1000，约 1.05s/step，预计还需 ~9 分钟

### cuda:1
- **nvidia-smi 显示：空**，无 GPU 计算进程
- **PID 131619** — `python src/train.py` (kl_sparsity**30**_s42, `--gpu 1`) 刚启动，正在加载模型权重 + 初始化 data loader，尚未分配显存

### plan_005 (PID 129873)
- **已正常完成**，EXIT_CODE=0
- 最终结果：Linearity ratio=0.2644, Weak subsumption detected
- 进程已退出，无 GPU 碰撞风险

### kl_sparsity70_s42 (PID 130683)
- **已死亡**，进程不存在，无日志文件
- 服务器上没有任何 kl_sparsity70 相关进程或日志，只有 kl_sparsity**30**_s42

### 结论
**无 GPU 碰撞。** plan_005 已正常结束释放资源，PID 130683 (kl_sparsity70) 不存在。当前 cuda:1 上实际跑的是新提交的 kl_sparsity30_s42 (PID 131619)，正在初始化中。

---
