# check 022b startup verify

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_022b-startup-verify_20260517T111024_result.json`
- **Structured JSON:** [`0ab79682fe7b1a79bffa.json`](../../sessions/0a/0ab79682fe7b1a79bffa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_022b_no_curriculum 状态报告

**启动成功** ✓

| 检查项 | 状态 |
|--------|------|
| 进程存活 | PID 670559，运行中，已累计 242 分钟 CPU 时间 |
| GPU 占用 | cuda:1 占用 3265 MiB，GPU-Util 21% |
| 训练进度 | 已到 step 15000（目标 105000），eval_return 从 37.4→167.3 |
| logdir | 已创建，含 latest.pt (235MB)、metrics.jsonl、tfevents |
| 报错 | 仅 FutureWarning（torch.cuda.amp.autocast 弃用警告），无实际错误 |

### Gate 参数验证

| 指标 | 期望 | 实际 (step 15000) | 判定 |
|------|------|-------------------|------|
| gate_scale | 1.0 | 1.0 | ✓ curriculum 关闭，gate 全程激活 |
| gate_empirical_entropy | > 0 | 2.0 | ✓ gate 在主动学习 |
| gate_dt_1_frac | < 1.0 | 0.1 | ✓ 仅 10% 选择 dt=1，gate 积极探索长步长 |
| gate_dt_mean | — | 4.6 | gate 偏好中等步长 |
| gate_dt 分布 | 非退化 | dt1~dt8 均匀分布 (0.1~0.2) | ✓ 探索充分 |

### 早期表现

- eval_return: 37.4 (5K) → 167.3 (15K)，学习曲线正常上升
- gate 无退化迹象，entropy_ratio=0.9 接近最大熵，gate 仍在充分探索

**结论：exp_022b 启动正常，gate 行为符合预期（无 curriculum 约束下自由探索多种 dt），训练在正常推进。**

---
