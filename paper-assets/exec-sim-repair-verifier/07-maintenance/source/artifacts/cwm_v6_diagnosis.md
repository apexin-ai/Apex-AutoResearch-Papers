# CWM v6 SIGTERM(143) 诊断报告

**时间**: 2026-05-13 04:55 CST  
**服务器**: seetacloud-westd-4x5090  
**进程**: PID 89516 (python3 train_repo_cwm.py), 父进程 PID 89511 (bash)  
**死亡点**: step 105/6633, 训练 ~14 分钟

## 根因：SeetaCloud 平台外部 SIGTERM

**SIGTERM 来源是平台层面，非容器内部。** 证据链：

1. **tmux server 被杀** — `tmux ls` 返回 "no server running"。tmux server 死亡后向所有 session 内进程发 SIGTERM，导致 bash→python 级联终止
2. **排除 OOM** — cgroup memory.events: `oom=0, oom_kill=0, high=0, max=0`。内存使用 ~43GB/360GB(cgroup limit)，远未触及上限
3. **排除 PID 限制** — pids.current=698, pids.max=20480, pids.events max=0
4. **排除 CPU 限制** — cpu.max=10000000/100000 (100 核配额)
5. **排除磁盘满** — 根分区 11GB 可用，数据盘 427GB 可用
6. **排除 swap 压力** — swap.max=0, swap.current=0
7. **无内部 kill 源** — 无 crontab、无 supervisor 日志、无 bash_history 中的 kill 命令
8. **dmesg/journalctl/syslog 不可用** — 容器权限限制，无法查看宿主机日志

**结论**: 宿主机或 SeetaCloud 编排系统发起了容器级 SIGTERM。可能原因：平台维护/调度、资源再分配、或计费相关操作。

## 历史 CWM 失败模式

| 版本 | 最大 step | 运行时长 | 退出码 | 死因 |
|------|----------|---------|--------|------|
| v1 | 694 | ~2h24m | 143 | SIGTERM（平台） |
| v2 | 0 | 立即崩溃 | 1 | 代码错误 |
| v3 | 119 | ~20m | 137 | SIGKILL（可能 OOM） |
| v4 | 386 | ~1h10m | 无记录 | 未知 |
| v5 | 0 | 立即崩溃 | 1 | CUDA OOM (GPU 0) |
| v6 | 105 | ~14m | 143 | SIGTERM（平台） |

**关键发现: 6 次训练的 checkpoint 目录全部为空。** save_steps=100，但从未成功保存过。v1 跑到 694 步理应有 6 个 checkpoint，但 `/root/autodl-tmp/checkpoints_repo_cwm/` 为空。

## 可用 Checkpoint

**无。** 所有 checkpoint 目录均为空：
- `/root/autodl-tmp/checkpoints_repo_cwm/` — 空
- `/root/autodl-tmp/checkpoints_repo_cwm_v4/` — 空
- `/root/autodl-tmp/checkpoints_repo_cwm_v6/` — 空
- 全局搜索 `checkpoint-*` 和 `adapter_model*` — 无结果

## 建议

### 1. checkpoint 保存失败是更紧迫的问题
训练被 kill 可以 resume，但 checkpoint 不保存意味着所有进度归零。需要排查：
- `train_repo_cwm.py` 的 Trainer 配置是否正确传递了 `save_strategy="steps"` 和 `save_steps=100`
- 是否有 callback 拦截了 save
- save 是否因权限/路径问题静默失败

### 2. 添加 SIGTERM 信号处理
在训练脚本中注册 `signal.SIGTERM` handler，收到信号时先保存 checkpoint 再退出。LoRA adapter 只有 ~12M 参数，保存耗时 <5 秒。

### 3. 平台 SIGTERM 不可控，需要容错
SeetaCloud 平台可能随时发 SIGTERM。建议：
- save_steps 从 100 降到 50 或更小
- 确认 save 真正写入磁盘后再继续训练
- 训练启动时检查是否有可用 checkpoint，自动 resume

### 4. 服务器选择
- **seetacloud-westd-4x5090**: 平台 SIGTERM 不稳定，但如果修复 checkpoint 保存 + 添加信号处理，可以 resume 式训练
- **换服务器**: 如果 SIGTERM 频率太高（6 次中 2 次），考虑迁移到更稳定的环境
- **优先级**: 先修 checkpoint 保存 bug，在任何服务器上都需要这个修复
