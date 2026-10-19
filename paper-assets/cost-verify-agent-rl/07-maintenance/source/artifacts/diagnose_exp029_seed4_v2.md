# exp029_seed4_v2 诊断报告

## 结论：实验仍在正常运行，Cron 监控误报

**实验未失败。** 所有进程活跃，无错误、无 OOM、无崩溃。Cron 的 "process dead 5×" 是误判。

## 证据

### 1. 进程状态（正常）
- PID 302056（主 bash）: 存活，tmux session `exp029_seed4_v2` 在线
- PID 305302（ray::TaskRunner.run）: 97.4% CPU，102 线程，~3GB RSS，状态 S（sleeping=正常等待 I/O）
- PID 305501（ray::WorkerDict GPU:0）: 33.6% CPU，38940MiB VRAM
- PID 305502（ray::WorkerDict GPU:1）: 33.3% CPU，38682MiB VRAM
- wandb-core (PID 305813): 存活
- 无退出哨兵文件 `/tmp/agent-ml-exit/exp029_seed4_v2.exit`（确认进程未退出）

### 2. 日志分析（无错误）
- `exp029_seed4_v2.log` (3264 行): grep 无 ERROR/Exception/Traceback/OOM/killed
- 日志最后内容: `Training Progress: 0%| | 0/15 [00:00<?, ?it/s]`
- 初始验证已完成: 279.4s，success=9.375%，140 games eval
- 训练循环刚开始（step 0/15），正在执行第一个训练 step 的 rollout 收集

### 3. Ray 日志活跃度
- Ray session 目录 `logs/` 中 monitor.log、raylet.out、python-core-worker 日志均在 16:54-16:55 更新
- TaskRunner 已发送 400 task attempts，WorkerDict 已发送 163 task attempts，无发送失败
- Ray GCS 通信正常，无 dropped events

### 4. Cron 误报原因分析
Cron 检查逻辑为 "no sentinel/W&B"：
- **No sentinel**: 正确——进程未退出，所以没有哨兵文件。但这不代表进程死亡。
- **No W&B**: 初始验证指标已在 step 0 记录，之后训练循环第一步尚未完成，尚无新的 W&B 指标。初始验证耗时 279s，训练 rollout（3553 games）耗时更长。
- Cron 将 "无新 W&B 指标 + 无哨兵" 误判为 "进程死亡"，实际上进程只是在执行耗时长的第一个训练 step。

## bjb1-17606 当前资源状态

| 资源 | 状态 |
|------|------|
| 磁盘 (/) | 8.3G/30G (28%) |
| 磁盘 (数据盘) | 18G/879G (3%) |
| GPU 0 (RTX PRO 6000) | 38940MiB/97887MiB, 0% util (rollout 间隙正常) |
| GPU 1 (RTX PRO 6000) | 38691MiB/97887MiB, 0% util (rollout 间隙正常) |
| 内存 | TaskRunner ~3GB + WorkerDict ~14GB = 正常 |
| SHM | 80M/110G |

## 建议

1. **无需重试，无需干预。** 实验正在正常训练。
2. **Cron 监控需修复**：当前逻辑仅依赖 sentinel + W&B 新指标判断存活，缺少进程 PID 存活检查。建议增加 `kill -0 <PID>` 或 `ps -p <PID>` 作为存活判断条件，在 sentinel/W&B 条件不满足时先验证进程是否真的死亡。
3. **后续观察**：第一个训练 step 完成后（预计再需 5-15 分钟），日志应输出 step 1/15 进度并更新 W&B 指标。届时可验证训练是否正常推进。
