# ops bjb2 40593 diagnose deploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb2-40593-diagnose-deploy_20260515T051900_result.json`
- **Structured JSON:** [`28dd92c382f123f6ef68.json`](../../sessions/28/28dd92c382f123f6ef68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断与部署结果

### 服务器状态（bjb2-40593）

| 资源 | 状态 |
|------|------|
| GPU (RTX 4090 D) | 已有进程占用：`eval-reconvla-object` (PID 211962, 5573MiB, 运行3.5h) |
| 代码目录 | `/root/acr-vla-conformal-refinement/` 完整（src, logs, scripts, tests） |
| Git | `.git/` 存在，master 分支 |
| crm_v3_norm checkpoints | `obs_only/crm_best.pt` + `perdof/` 均存在 |
| SmolVLA 模型 | 存在 |
| LIBERO 数据 | 完整（spatial/object/goal/10/90） |
| Python/Conda | `/root/miniconda3/bin/python` 存在 |
| 磁盘 | 152GB 可用 |

### 环境修复
无需修复——之前报告的问题已不存在（git repo 已初始化，所有资源就位）。

### 实验部署
**已提交 `eval-mag-obsonly-norm003-b2`**（与 reconvla-object 并行运行，共享 cuda:0）：
- 模式：`crm_obs_only`，benchmark：`spatial`，norm=0.03
- 正在初始化中（SmolVLA 权重加载完成，正在加载本地权重）
- 日志：`~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm003-b2.log`

### 注意事项
- 已有的 `eval-reconvla-object` 任务进度很慢（10 tasks × 20 rollouts，当前在 task 0 的 rollout 10/20），预计还需数十小时
- obs_only 模式不使用 VLA 做推理，VRAM 开销很小，并行运行应无问题

---
