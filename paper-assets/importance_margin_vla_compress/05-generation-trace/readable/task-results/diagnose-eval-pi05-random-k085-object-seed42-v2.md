# diagnose eval pi05 random k085 object seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_random_k085_object_seed42_v2_20260521T232037_result.json`
- **Structured JSON:** [`150ef6d9b4962ec8d140.json`](../../sessions/15/150ef6d9b4962ec8d140.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完毕。

## 诊断结论

### 根因：**误报（false positive）——两个实验都已正常完成**

监控系统报 "process dead 5× with no sentinel/W&B — auto-resolved as failed"，但实际情况是：

| 实验 | 实际状态 | 结果 |
|------|---------|------|
| `eval_pi05_random_k085_object_seed42_v2` | **正常完成** | SR=5.0%, 500 episodes, 108.5min, 结果已保存 |
| `eval_pi05_l2norm_k07_spatial_seed42` | **正常完成** | SR=67.0%, 500 episodes, 98.8min, 结果已保存 |

**失败原因分析：sentinel 文件缺失**

- 这两个实验的 sentinel 文件（`/tmp/agent-ml-exit/eval_pi05_random_k085_object_seed42_v2.exit` 和 `eval_pi05_l2norm_k07_spatial_seed42.exit`）均不存在
- 可能原因：这两个实验的启动方式没有通过标准的 job wrapper（对比正常的 sentinel 格式 `0|2026-05-21T21:00:05Z`），或者 job name 与 sentinel 文件名不匹配
- 进程完成后，监控系统检测到进程已死、又找不到 sentinel，就判定为失败

### westd-38929 系统状态：正常

- GPU：4× RTX PRO 6000 (96GB)，状态正常
- 磁盘：根分区 29%，数据盘 80%（52GB 可用），没有空间问题
- 无 OOM 或硬件错误迹象

### 当前运行的 eval_pi05_l2norm_k0925_object_seed42 (pid=985039/985048)

**无风险**。该实验：
- 运行在 GPU 2 上，已跑 17 分钟，正在 Task 2，SR 保持 ~97%
- 使用标准 job wrapper 启动（有 trap/sentinel 机制），所以 sentinel 文件会正确生成
- 不会遇到同样的误报问题

### 修复建议

不需要修任何东西，也不需要重跑。两个实验的结果文件已完整保存：
- `/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.85_libero_object_seed42.json`
- `/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.70_libero_spatial_seed42.json`

只需在监控系统中将这两个实验的状态从 "failed" 改为 "completed"。

---
