# ops westd38929 msh fix batch2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd38929-msh-fix-batch2_20260520T112926_result.json`
- **Structured JSON:** [`db8d06a92cb5febee33d.json`](../../sessions/db/db8d06a92cb5febee33d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果：Batch 2 已在运行，无需修复

**MSH 问题已修复：** pip 安装的 libero 包中 MSH 文件完好（1.5M-3.0M，May 16 日期），之前 15:24 报的 "empty MSH" 错误已被修复。

**Batch 2 已在 4 进程并行运行**（自 18:19 启动），当前进度：

| k 值 | 已完成 tasks | 当前 task | 中间成功率 |
|------|-------------|-----------|-----------|
| **0.5** | 9/10 | Task 9（最后一个） | 58%, 2%, 74%, 78%, 42%, 50%, 2%, 38%, 14% |
| **0.3** | 8/10 | Task 8 | 30%, 0%, 32%, 48%, 18%, 44%, 0%, 22% |
| **0.2** | 7/10 | Task 7 | 6%, 0%, 4%, 12%, 12%, 0%, 0% |
| **0.1** | 7/10 | Task 7 | 0%, 0%, 0%, 0%, 0%, 0%, 0% |

**预计全部完成时间：** ~30-40 分钟内（k=0.5 最快，约 10 分钟；k=0.1/0.2 最慢，约 30 分钟）。

注意事项：
- 4 个进程命令行都显示 `--gpu 0`，但 nvidia-smi 显示 4 卡各用 ~4.8GB，实际分布在 4 张卡上
- k=0.1 全部 task SR=0%，符合极端剪枝预期
- 无需额外操作，等待完成即可

---
