# infra westd34685 checkpoint cleanup

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd34685_checkpoint_cleanup_20260520T165454_result.json`
- **Structured JSON:** [`d49e25549fcf5c170a75.json`](../../sessions/d4/d49e25549fcf5c170a75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。报告：

## 部署结果

| 项目 | 状态 |
|------|------|
| **磁盘** | 350G 总量，22G 已用，329G 可用 (7%) |
| **现有 checkpoint** | 尚无（训练刚到 ~1200 step，首个 checkpoint 在 step 2500） |
| **滚动删除** | nohup 后台循环部署成功（PID 32353），每 20 分钟执行一次，每个 seed 目录保留最新 2 个 `*_chkpt` 目录 |
| **训练状态** | 3 个 seed 均正常运行：s0 ~step 1238, s1 ~step 1197, s2 ~step 1175，速度 ~1.09 it/s |
| **occ_loss** | s0 最新: step=1200, occ_loss=0.0153, action_loss=0.2412 |
| **Failed to load occ label** | 3 个 seed 均为 0 次错误 |

注：crontab 不可用（该服务器未安装），改用 nohup 后台 sleep 循环实现。清理脚本路径 `/root/autodl-tmp/cleanup_checkpoints.sh`，checkpoint 命名格式为 `{run_dir}--{step}_chkpt`。

---
