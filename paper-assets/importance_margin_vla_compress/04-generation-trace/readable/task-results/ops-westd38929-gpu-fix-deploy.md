# ops westd38929 gpu fix deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd38929-gpu-fix-deploy_20260522T021517_result.json`
- **Structured JSON:** [`403ab7783be5a4fdc081.json`](../../sessions/40/403ab7783be5a4fdc081.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

---

### GPU 0: 无冲突（纠正）
任务描述的 v1/v2 冲突**实际不存在**。PID 227008 和 227018 是同一实验 `eval_pi05_l2norm_k085_spatial_seed42` 的父子进程链（bash wrapper → timeout → python）。只有一个实验在跑，没有 v2 进程。当前进度：Task 5/10 完成，running SR=88.8%，已跑 33 分钟。**未执行 kill 操作**。

### GPU 1: 已部署
`eval_pi05_l2norm_k095_spatial_seed42` 已提交（PID 260890），模型正在加载中。之前失败原因是缺 `HF_HUB_OFFLINE=1`。

### GPU 2: 空闲（实验已完成）
`eval_pi05_random_k0925_object_seed43` — exit code 0，**SR=30.0%**
结果文件: `pi05_random_k0.93_libero_object_seed43.json`

### GPU 3: 空闲（实验已完成）
`eval_pi05_random_k085_spatial_seed42` — exit code 0，**SR=58.4%**
结果文件: `pi05_random_k0.85_libero_spatial_seed42.json`

### 4 GPU 状态表

| GPU | 状态 | 实验 | 进度/结果 |
|-----|------|------|-----------|
| 0 | 运行中 | eval_pi05_l2norm_k085_spatial_seed42 (PID 227018) | Task 5/10, SR=88.8%, ~33min |
| 1 | 刚启动 | eval_pi05_l2norm_k095_spatial_seed42 (PID 260890) | 加载模型中 |
| 2 | 空闲 | eval_pi05_random_k0925_object_seed43 | 已完成, SR=30.0% |
| 3 | 空闲 | eval_pi05_random_k085_spatial_seed42 | 已完成, SR=58.4% |

---
