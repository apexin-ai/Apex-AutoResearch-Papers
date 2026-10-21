# ssh cf batch progress check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cf_batch_progress_check_20260522T000314_result.json`
- **Structured JSON:** [`6a08a0865937bc872218.json`](../../sessions/6a/6a08a0865937bc872218.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## CF Batch 实验进度报告

### cf_batch_part2_v1 (PID 585447, cuda:1) — ✅ 已完成

- 进程已退出，`EXIT_CODE=0`
- 两个任务全部完成：
  - **tracvla goal untrained** → 已保存
  - **tracvla long untrained** → 已保存 (`counterfactual_combined.json`)
- 总耗时 29.1 min
- GPU 1 已释放（0% 利用率，0 MiB 显存）

### cf_batch_missing_v1 (PID 584349, cuda:0) — 🔄 运行中

运行时间 01:19:37，GPU 0 利用率 54%，显存 9.5/96 GB

| # | 任务 | 状态 | 耗时 |
|---|------|------|------|
| 1 | openvla object untrained | ✅ 完成 | 27.6 min |
| 2 | tracvla spatial untrained | ✅ 完成 | 29.9 min |
| 3 | tracvla object untrained | 🔄 运行中 (4/5 conditions done, **paraphrased** 进行中) | ~35 min |
| 4 | tracvla goal untrained | ⏳ 排队 | ~29 min |
| 5 | tracvla long untrained | ⏳ 排队 | ~29 min |

**当前状态**：任务 3（tracvla object untrained）正在处理最后一个 condition（paraphrased），预计 ~7 分钟内完成本任务。

**注意**：PID 584349 的命令包含了 5 个任务（含 goal 和 long），与 part2 重叠。任务 4、5 的结果已由 part2 生成，missing batch 会再跑一遍覆盖。

**预估剩余时间**：
- 仅新结果（task 3 完成）：~7 分钟
- 全部跑完（含重复的 task 4+5）：~7 + 29 + 29 ≈ **65 分钟**

### 已生成的 CF 结果文件

新增关键结果（本次 batch 产出）：
- `/root/autodl-tmp/vla-ssd/results/libero_object_untrained/counterfactual_combined.json`
- `/root/autodl-tmp/vla-ssd/results/tracvla_spatial/untrained/counterfactual_combined.json`
- `/root/autodl-tmp/vla-ssd/results/tracvla_goal/untrained/counterfactual_combined.json`
- `/root/autodl-tmp/vla-ssd/results/tracvla_long/untrained/counterfactual_combined.json`

待生成：
- `tracvla_object/untrained/counterfactual_combined.json`（~7 分钟后）

---
