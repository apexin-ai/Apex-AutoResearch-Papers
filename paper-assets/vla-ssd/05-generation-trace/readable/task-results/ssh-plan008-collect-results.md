# ssh plan008 collect results

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_plan008-collect-results_20260516T000152_result.json`
- **Structured JSON:** [`e93013a101b60c655ce4.json`](../../sessions/e9/e93013a101b60c655ce4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个进程都在运行，都在第 1/10 个 task 的约 60% 处。

状态汇总：

- **random_s0** (cuda:0): task 1/10 `open_the_middle_drawer_of_the_cabinet`, 4173/7027 steps (59%), ~38 step/s
  - 控制指令：固定随机字符串 `"civoq tixe mef wugi di wapon"`
  - 输出文件：`open_the_middle_drawer_of_the_cabinet.h5` (1.69 GB, 写入中)

- **shuffled** (cuda:1): task 1/10 `open_the_middle_drawer_of_the_cabinet`, 4245/7027 steps (60%), ~38 step/s
  - 控制指令：打乱词序如 `"of middle the open the drawer cabinet"`
  - 输出文件：`open_the_middle_drawer_of_the_cabinet.h5` (1.75 GB, 写入中)

**进度估算**：
- 每个 task 约 7027 步，~38 step/s 平均（有周期性 GPU 争抢降速），约 5-7 分钟/task
- 10 tasks 总计约 **50-70 分钟**
- 当前约 6% 完成，已运行 ~4 分钟
- **预计完成时间：约 50-65 分钟后**（约 UTC 09:05-09:20）

RSA 结果目录中尚无 random_s0 或 shuffled 的结果，需要等特征提取完成后运行。

要我稍后再来检查进度，还是在预计完成时间附近设定定时检查？

---
