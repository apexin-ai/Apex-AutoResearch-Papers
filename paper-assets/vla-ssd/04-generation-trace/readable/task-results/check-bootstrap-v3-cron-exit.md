# check bootstrap v3 cron exit

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bootstrap_v3_cron_exit_20260523T070749_result.json`
- **Structured JSON:** [`b96586ebd0d8697ff54d.json`](../../sessions/b9/b96586ebd0d8697ff54d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### 1. 进程状态：两个 GPU 都还在跑

Cron 报告的 PID 724283 是启动器进程（非实际 batch 脚本），子进程仍在活跃运行。

| GPU | 当前任务 | 阶段 | 实时进度 |
|-----|---------|------|---------|
| cuda:0 | `openvla / goal / untrained` | 特征提取 | 1750/5000 samples |
| cuda:1 | `tracvla / goal / trained` | Bootstrap | 1000 iterations (100 workers)，已跑 ~6 min |

### 2. 完成进度：1/20

**cuda:0** 负责 12 条件：openvla×4suites×2cond (8) + nora×2suites×2cond (4)
**cuda:1** 负责 8 条件：tracvla×4suites×2cond (8)

已完成并保存 JSON 的仅 1 个：`openvla_goal/trained.json`

### 3. 已完成结果

**openvla_goal / trained**:
| 指标 | 值 |
|------|-----|
| peak_layer | L1 |
| peak_r2 | 0.4177 |
| exit_r2 (L31) | 0.3313 |
| delta | 0.0864 |
| CI_95 | [-0.056, 0.1064] |
| boot_mean | 0.0173 |
| delta 在 CI 内？ | **是** ✅ |

### 4. 无错误

两个 GPU 日志均无错误或异常，正常推进中。按目前速度（每条件 ~20 min），全部 20 条件预计还需约 6-7 小时完成。

---
