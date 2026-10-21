# 诊断报告：westd-41312 实验失败分析

## 核心结论

**这些不是真正的训练失败——是监控系统的误判。** 实际情况分两层：

1. **原始实验 (seed123/456)** 被 SIGTERM 杀死（GPU 调度重分配），但已在其他服务器或重试中跑完
2. **r2 重试实验**当前正在 westd-41312 上正常运行，但 registry 在启动后 ~4 分钟就将它们标记为 "failed"（因为 WANDB_MODE=disabled 导致无 sentinel/heartbeat）

---

## 实时状态（截至 2026-05-18 05:48 CST）

| 实验 | Registry 状态 | 实际状态 | GPU | 进度 |
|------|--------------|----------|-----|------|
| ess_only_seed123_r2 | DONE/failed (05:04 CST) | **正在运行** | GPU 2 | 55% (3343/6103) |
| ess_only_seed456_r2 | DONE/failed (05:04 CST) | **正在运行** | GPU 1 | 63% (3841/6103) |
| random_reweight_seed456 | DONE/failed (05:30 CST) | **正在运行** | GPU 3 | 25% (1507/6103) |
| grid_b0_3_seed123_r2 | DONE/failed (05:00 CST) | **未在此服务器启动** | — | — |
| grid_b0_3_seed456 | killed (registry) | **已完成** EXIT_CODE=0 | — | 100% |

---

## 失败原因分析

### 第一层：原始实验被 SIGTERM (EXIT_CODE=143)

**时间线证据：**
- `ess_only_seed123`: 被杀于 May 18 04:55:28 CST
- `ess_only_seed456`: 被杀于 May 18 04:55:29 CST (同一秒！)
- `adaptive_fix_seed42`: 被杀于 May 17 23:04 CST

**原因**：实验管理系统主动 SIGTERM 杀进程以腾出 GPU，不是 OOM/崩溃。证据：
- 两个实验在同一秒被杀 → 系统操作
- 日志中无错误/traceback，仅 "Terminated"
- 紧接着新实验被调度到释放的 GPU

**注意**：registry 显示 `ess_only_seed123` 和 `ess_only_seed456` 已在 westd-47453 上成功完成 (conclusion=success)。所以这些实验的结果已经有了。

### 第二层：r2 重试被监控系统误判为 failed

**关键发现：**
- r2 重试在 05:00 CST 启动，registry 在 05:04 CST（仅 4 分钟后）就标记为 failed
- `random_reweight_seed456` 在 05:30 启动，registry 在 05:30 同秒标记 failed
- 实验设置了 `WANDB_MODE=disabled` → 无 W&B heartbeat
- Registry 无 server 字段 → 监控系统不知道去哪台机器检查进程
- 监控系统：无 sentinel + 无法确认进程存活 → "process dead 5×" → auto-resolve as failed

**这是监控系统的 bug，不是训练的 bug。**

### 第三层：grid_b0_3_seed123_r2

- 在 westd-41312 上无日志、无进程
- Registry 标记 failed (05:00 CST)，无 server 字段
- 推测：调度时 4 GPU 全被占用，从未实际启动

---

## 系统健康检查

| 检查项 | 状态 |
|--------|------|
| GPU 显存 | 正常 (46.5/97.8 GB per card) |
| GPU 利用率 | 100% (4 卡全满) |
| 磁盘空间 | 充足 (autodl-tmp 145GB 可用) |
| Checkpoint 完整性 | 正常 (所有实验都有有效 checkpoint) |
| OOM killer | 无法确认 (dmesg 无权限)，但无迹象 |
| GPU 错误 | 无 |

---

## 行动建议

### 立即行动
1. **不要重启任何实验** —— ess_only_seed123_r2, ess_only_seed456_r2, random_reweight_seed456 都在正常跑
2. **手动更新 registry** —— 将这 3 个实验状态改回 RUNNING，关联 server=westd-41312
3. **调度 grid_b0_3_seed123_r2** ��— 需要等某个 GPU 空出（预计 ess_only_seed456_r2 最先完成，~1.3h）

### 预计完成时间
- ess_only_seed456_r2: ~1.3h (最先)
- ess_only_seed123_r2: ~1.6h
- random_reweight_seed456: ~2.6h

### 根因修复（防止再发）
- 监控系统需要支持 WANDB_MODE=disabled 场景（通过 PID 文件或进程检查 fallback）
- 提交实验时应设置 server 字段，让监控能正确定位进程
- 或改为 `WANDB_MODE=online` 以恢复 heartbeat 机制

---

## 总结

| 问题 | 是否系统性 | 是否需要代码修复 |
|------|-----------|----------------|
| SIGTERM kill | 是（GPU 调度） | 否，是运维行为 |
| 监控误判 | 是（WANDB disabled） | 需修复监控逻辑 |
| grid_b0_3_seed123_r2 未启动 | 个案（GPU 资源不足） | 需要手动调度 |
| 训练代码 bug | 不存在 | — |
