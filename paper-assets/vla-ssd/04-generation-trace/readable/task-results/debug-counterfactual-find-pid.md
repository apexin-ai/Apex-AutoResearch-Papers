# debug counterfactual find pid

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_counterfactual_find_pid_20260518T171606_result.json`
- **Structured JSON:** [`1dc2cb9a79ef15c9d371.json`](../../sessions/1d/1dc2cb9a79ef15c9d371.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

**进程状态：正在运行**

| 角色 | PID | 命令 |
|------|-----|------|
| 主进程 | **66746** | `python -u scripts/counterfactual_instruction.py` |
| resource tracker | 66878 | multiprocessing resource tracker |
| GPU worker 0 | 66879 | multiprocessing spawn (cuda:0) |
| GPU worker 1 | 66880 | multiprocessing spawn (cuda:1) |

**GPU 使用：**
- GPU 0: 15474MiB / 97887MiB, 81% util, 340W
- GPU 1: 15474MiB / 97887MiB, 82% util, 336W

**结果文件：**
- 6 个预期输出文件（`counterfactual_{correct,wrong,empty,shuffled,paraphrased,combined}.json`）**均不存在**
- 日志文件 `counterfactual_instruction.log` 存在（910 bytes），最后修改时间 `2026-05-19 01:06:42`（约 10 分钟前）
- 日志内容显示两个 GPU worker 刚完成模型加载（checkpoint shards 3/3），推理尚未开始写入结果

**结论：** 实验刚启动不久，模型加载完成，正在推理阶段。结果文件可能在所有条件评估完毕后一次性写入。

---
