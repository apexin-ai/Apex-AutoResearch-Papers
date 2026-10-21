# diag openvla random k095 w41

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_openvla_random_k095_w41_20260528T063539_result.json`
- **Structured JSON:** [`2b67983587a10dd04110.json`](../../sessions/2b/2b67983587a10dd04110.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：进程正常运行中，是误报

**进程状态**：PID 700653 **仍在运行**，GPU 1 上 73% SM 利用率、41% 显存占用，活跃且健康。

**为什么 cron 报 miss**：实验未注册到 registry（registry 查询返回 0 条记录），cron 监控找不到对应的注册条目所以报进程消失。

**日志只到 Task 1 Ep 40/50 的原因**：输出缓冲。进程 13:56 启动，日志文件 14:31 最后修改，仅 17 行 1245 字节。实际进程已运行约 40 分钟，CPU 时间 263 分钟（多线程），应该已经推进到更后面的 task。stdout 缓冲区未刷新到日志文件。

**注意**：该实验 suite 是 `libero_10`（10 tasks × 50 episodes），命令中 `--suite libero_10`。名称里虽然有 "long" 但实际运行的是 libero_10 suite。另外 `CUDA_VISIBLE_DEVICES=0` 但实际跑在 GPU 1 上，说明环境变量传递有问题，但不影响运行。

**不需要任何操作**，等待进程自然完成即可。如需注册到 registry 以便 cron 正确追踪，需要补注册。

---
