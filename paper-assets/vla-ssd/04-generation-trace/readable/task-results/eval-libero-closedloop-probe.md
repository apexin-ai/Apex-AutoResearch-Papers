# eval libero closedloop probe

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_libero_closedloop_probe_20260520T123214_result.json`
- **Structured JSON:** [`d9c77dc8d299a0e4f706.json`](../../sessions/d9/d9c77dc8d299a0e4f706.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report written and registered as artifact `art_20260520_1caea8`.

## 结果摘要

**OpenVLA LIBERO-Goal 闭环评估：全部 0% 成功率**

| 已完成任务 | SR |
|---|---|
| Task 0: open the middle drawer | 0/10 |
| Task 1: put the bowl on the stove | 0/10 |
| Task 2: put the wine bottle on cabinet | 0/10 |
| Task 3-9: 仍在运行 | 预期 0/10 |

**关键发现**：
- 模型**不是**输出固定 action——a0 跨 trial 有多样性，说明模型在读观测
- 所有 trial 都在 400 步超时，没有提前终止或崩溃
- 0% SR 与之前 Path B 结果一致（0/9, 0/15）

**失败根因分析**（按可能性排序）：
1. **256-bin 动作量化精度不足** + 自回归 7-token 解码的复合误差
2. **MuJoCo 版本不匹配**（3.8.1 vs 原论文可能用的 ≤3.1.x）
3. **图像预处理差异**（PIL vs TensorFlow）
4. transformers 版本微差（4.40.2 vs 4.40.1）

**结论**：确认了 vla-ssd 项目的核心动机——VLA 模型的动作精度是闭环控制的瓶颈。

eval 仍在 westd-19183 上运行（PID 461520），预计 ~22:30 完成全部 10 个任务。完成后 results.json 会自动写入 `/root/autodl-tmp/vla-ssd/results/libero_closedloop_probe/`。

---
