# diagnose exp029 failed

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp029_failed_20260516T161158_result.json`
- **Structured JSON:** [`3ff7f67fa159a323df54.json`](../../sessions/3f/3ff7f67fa159a323df54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到根因了。诊断结果如下：

---

## exp029_episode_level 训练失败诊断

### 直接原因

训练在 `trainer.fit()` 的 `logger.log()` 阶段崩溃，错误信息：

```
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpzicbifxf'
```

wandb 在记录 Table artifact 时调用 `tempfile.mkdtemp()`，因 `/tmp` 目录不存在而失败。

### 根因分析

**`cleanup_loop.sh` 脚本误删了整个 `/tmp` 目录。**

该脚本（PID 878019）内容：

```bash
while true; do
    find /tmp -maxdepth 1 -name "tmp*" -mmin +5 -exec rm -rf {} \; 2>/dev/null
    sleep 300
done
```

关键 bug：`find /tmp -maxdepth 1 -name "tmp*"` 会匹配 `/tmp` 自身（basename 为 `tmp`，匹配 `tmp*` 模式），且 `/tmp` 修改时间必然超过 5 分钟，因此 `rm -rf /tmp` 被执行，**连带删除了整个 `/tmp` 目录**。

已确认 `ls /tmp` 返回 `No such file or directory`。

### 训练进度

- **0 步完成**：日志显示训练刚进入第一轮 rollout 后的 logging 阶段就崩溃
- **无 checkpoint**：exp029 目录只有 `train_restart.log`，无 checkpoint 文件
- **无 wandb 数据**：wandb 本地目录不存在

### 当前服务器状态

- GPU：2× RTX PRO 6000 空闲，0MiB 显存占用
- 磁盘：`/root/autodl-tmp` 78% 使用（57GB 剩余），非磁盘问题
- 训练进程全部退出，`cleanup_loop.sh` 仍在运行（但已无害，因 `/tmp` 已不存在）

### 建议下一步

1. **立即修复**：重建 `/tmp` 并杀掉有 bug 的 cleanup 脚本
   ```bash
   mkdir -p /tmp && chmod 1777 /tmp
   kill 878019 878071
   ```

2. **修复 cleanup_loop.sh**：加 `-mindepth 1` 防止匹配 `/tmp` 自身
   ```bash
   find /tmp -maxdepth 1 -mindepth 1 -name "tmp*" -mmin +5 -exec rm -rf {} \;
   ```

3. **重新启动 exp029**：`/tmp` 恢复后可直接重跑，无需额外修改。训练配置和代码本身没有问题。

---
