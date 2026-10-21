# exp official checkpoint sr test

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_official_checkpoint_sr_test_20260519T170946_result.json`
- **Structured JSON:** [`65df82ed51c460d61c93.json`](../../sessions/65/65df82ed51c460d61c93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**OVERALL SR = 0.00 (0/15)**

| Task | Name | SR |
|------|------|----|
| 0 | open_the_middle_drawer_of_the_cabinet | 0/5 |
| 3 | open_the_top_drawer_and_put_the_bowl_inside | 0/5 |
| 7 | turn_on_the_stove | 0/5 |

所有 15 个 episode 全部跑满 400 步，R=0.000，没有任何一个 episode 获得部分奖励。

**关键日志观察**：
- Action 输出范围合理（[-1, 1]），gripper 在 -1/+1 间切换
- 每个 episode ~57s（400步），说明推理速度正常
- 不同 seed 没有产生任何差异——模型在所有初始条件下都无法完成任务

**Path B 彻底死亡。** 官方 checkpoint 在我们的 LIBERO 环境中 SR=0，这意味着要么环境/管线还有我们未发现的不兼容问题，要么 OpenVLA 在这些特定 task 上本身就很弱。无论哪种情况，Path B 作为闭环评估管线已不可行。

---
