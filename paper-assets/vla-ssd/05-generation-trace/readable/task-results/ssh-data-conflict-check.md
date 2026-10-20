# ssh data conflict check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_data-conflict-check_20260515T205901_result.json`
- **Structured JSON:** [`2d53d8e62628626a28e8.json`](../../sessions/2d/2d53d8e62628626a28e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 最终状态报告

**1. 进程排查**
- PID 658056（GPU 1）：untrained no-instruction 特征提取，运行 ~35 min，正常
- PID 659993：已不存在，无冲突
- 无重复进程，无需 kill

**2. 数据问题发现与修复**
- **trained_no_inst 每个文件只有 10 demos（应 50）**——全部 10 个文件已删除并重新提取
- 新进程 PID 661030 已在 GPU 0 启动，用 `--max_demos 50` 重新提取

**3. 四个特征目录状态**

| 目录 | 文件数 | Demos/文件 | 状态 |
|------|--------|-----------|------|
| trained_inst | 10/10 | 50 | 完整 |
| untrained_inst | 10/10 | 50 | 完整 |
| trained_no_inst | 0/10 → 提取中 | 50 | GPU 0 重新提取（PID 661030） |
| untrained_no_inst | 3/10 → 提取中 | 50 | GPU 1 进行中（PID 658056） |

**4. GPU 状态**
- GPU 0：RTX PRO 6000, 16.4GB/97.9GB, 63% util — trained_no_inst 提取
- GPU 1：RTX PRO 6000, 16.4GB/97.9GB, 68% util — untrained_no_inst 提取

**5. 预计完成时间**
- 每个 task ~3-4 min，两个进程并行
- untrained_no_inst：剩 7 个 task，约 25 min
- trained_no_inst：剩 10 个 task，约 35 min

---
