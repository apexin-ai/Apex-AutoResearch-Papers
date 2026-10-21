## exp029_seed6_v3 失败诊断

**根因**: 监控系统误判——实验实际并未失败。初始 validation 阶段（~6 分钟）期间，训练输出由 Ray worker 进程处理，主日志文件停止写入，监控系统在多次检查中未检测到 sentinel/W&B 活动，误判为 "process dead" 并自动标记为 failed。同时，监控在首次尝试仍在运行时就触发了重启（16:16 的第二次尝试），导致多个 Ray session 和 GPU 竞争的级联失败。

**日志证据**:
1. **首次尝试（16:12, Ray session 889240）**: 完成 validation（success=9.375%），到达 "Training Progress: 0/15"，然后在 16:22:28 被外部 kill——两个 WorkerDict 同时输出 `[rank0/rank1]: WARNING: destroy_process_group() was not called before program exit`，无 Python traceback
2. **第二次尝试（16:16, Ray session 901204）**: 在首次尝试 Ray workers 仍占用 GPU 时启动，初始化后被 kill
3. **第三次尝试（16:24, Ray session 920754, pid 920754）**: **当前仍在运行**，GPU 2: 38617 MiB / GPU 3: 37639 MiB，wandb run `2bbyvsdr` 已连接，TaskRunner/WorkerDict 进程活跃

**路径问题**: 不存在。`/root/cost-verify-agent-rl` 是指向 `/root/autodl-tmp/cost-verify-agent-rl` 的符号链接，两个路径等价。

**修复建议**:
1. **立即**: 无需修复，当前第三次尝试（pid 920754）正在运行，应将监控状态从 "failed" 更新为 "running"
2. **防止复发**: 监控系统检查进程存活时，应检查实际 PID（`ps -p <pid>`）而非仅依赖日志写入活动或 W&B metrics 出现时间。RAGEN 初始 validation 需要 ~6 分钟，此期间主日志无输出是正常行为
3. **清理**: 旧 Ray session（16:12、16:16）的残留文件可安全删除：`rm -rf /root/autodl-tmp/ray_tmp/ray/session_2026-05-21_16-12-25_668804_889240 /root/autodl-tmp/ray_tmp/ray/session_2026-05-21_16-16-29_525229_901204`
