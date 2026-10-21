# ssh verify 4 new experiments

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-4-new-experiments_20260517T065156_result.json`
- **Structured JSON:** [`ef994843cdb595516c46.json`](../../sessions/ef/ef994843cdb595516c46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果汇总

| 实验 | 服务器 | tmux | 日志状态 | Rollout |
|------|--------|------|----------|---------|
| obs-only seed46 | bjb1-18228 | ✅ (tmux ls 可见) | CRM loaded, 10 tasks loaded | ❌ 未开始 |
| obs-only seed47 | bjb1-18228 | ⚠️ has-session 报 MISSING，但日志正常 | CRM loaded, 10 tasks loaded | ❌ 未开始 |
| perdof seed46 | bjb1-32546 | ✅ OK | VLM + CRM loaded, 10 tasks loaded | ❌ 未开始 |
| perdof seed47 | bjb2-28827 | ⚠️ session 名可能不同 | VLM + CRM loaded, 10 tasks loaded | ❌ 未开始 |

**状态**: 4 个实验均已成功加载模型和环境，无报错。但 90 秒内均未产生第一条 rollout 输出——可能 VLA 模型初始化 + 环境 reset 耗时较长。bjb1-32546 和 bjb2-28827 的日志显示完整的 SmolVLM2 权重加载过程，说明进程仍在正常推进。

建议再等 2-3 分钟后复查 rollout 进度。

---
