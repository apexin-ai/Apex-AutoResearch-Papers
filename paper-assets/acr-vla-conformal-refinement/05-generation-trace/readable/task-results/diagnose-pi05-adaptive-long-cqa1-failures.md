# diagnose pi05 adaptive long cqa1 failures

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_pi05-adaptive-long-cqa1-failures_20260526T093202_result.json`
- **Structured JSON:** [`3e208aae94038aa1e7a3.json`](../../sessions/3e/3e208aae94038aa1e7a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### 根因：**误报。三个实验都在正常运行中，不是真的失败。**

监控系统报 "process dead 5× with no sentinel/W&B" 是因为这三个实验的启动方式（`bash -c ... | tee /tmp/...`）没有在 `/root/runs/acr-vla-conformal-refinement/` 下生成 run log 文件，也没有写 sentinel 文件或连接 W&B。监控系统无法检测到它们的存在，连续 5 次检查后判定为失败。

### 实验实际状态

| 实验 | PID | GPU | 进度 | 状态 |
|------|-----|-----|------|------|
| pi05-adaptive-long-s43 | 198442 | cuda:4 (12.7GB) | 完成 5/10 task，正在跑第 6 个 | **运行中** |
| pi05-adaptive-long-s44 | 199049 | cuda:5 (12.7GB) | 完成 5/10 task，正在跑第 5 个 | **运行中** |
| pi05-adaptive-object-s44 | 197917 | cuda:3 (10.8GB) | 已完成 8/10 task | **运行中** |

### 其他信息

- **GPU**: 6 张 4090D 全部占满，温度正常 (38-50°C)
- **磁盘**: 根分区 14% 使用，无空间问题（注：`/autodl-pub` 94% 但那是共享存储）
- **无 OOM**: 进程 RSS 内存均在 11-15GB，无异常
- **输出 JSON 尚未生成**: 脚本在全部 task 跑完后才写 JSON，属正常
- **其他 3 个实验也在跑**: crm_obs_only-long-s44 (GPU 0)、adaptive-object-s42 (GPU 1)、adaptive-goal-s42 (GPU 2)

### 建议

不需要重跑。等实验自然完成即可。long benchmark 每个 seed 有 10 tasks × 20 rollouts × 520 max_steps，耗时很长属正常。如需让监控系统识别，后续启动时应通过标准框架提交，确保生成 run log 和 sentinel。

---
