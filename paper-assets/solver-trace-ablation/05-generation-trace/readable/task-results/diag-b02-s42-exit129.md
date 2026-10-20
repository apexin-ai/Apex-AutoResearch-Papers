# diag b02 s42 exit129

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_b02-s42-exit129_20260516T050113_result.json`
- **Structured JSON:** [`eed246eff40f77ec639b.json`](../../sessions/ee/eed246eff40f77ec639b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### b02-s42 失败原因

**Exit 129 (SIGHUP) 发生在第一次运行的 step 80**，写到 `sweep_isr_b02_s42/`（只有 checkpoint-50 + 80 行 reward_log）。原因大概率是 SSH session 断开或 tmux 被杀，不是 OOM。

**已成功重跑为 v2**：`sweep_isr_b02_s42_v2/` 包含完整结果：
- 500/500 步完成，final model 已保存（~15GB safetensors）
- checkpoint-500 存在
- eval/ 目录已存在（已做过评估）
- reward_log.jsonl 126KB（完整）

**结论：b02-s42 不需要重跑。** v2 已经成功完成。旧的 `sweep_isr_b02_s42/`（15GB）可以清理。

### 当前双跑状态

| 指标 | GPU 0 (b02-s43) | GPU 1 (b02-s44) |
|------|-----------------|-----------------|
| PID | 633515 | 659716 |
| 显存 | 85430/97887 MiB (87%) | 80318/97887 MiB (82%) |
| 利用率 | 90% | 94% |
| 温度 | 59°C | 60°C |

- **RAM**: 77GB / 1TB used，922GB available — 完全安全
- **磁盘**: 212GB / 250GB (85%)，剩余 39GB — 两个 run 各需 ~15GB，勉强够用。训练完成后建议清理 `sweep_isr_b02_s42/`（废弃的 v1）释放 15GB。

### 结论

- b02-s42 ✅ 已完成（v2），无需重跑
- 双跑安全 ✅，RAM 充裕，GPU 温度正常
- 唯一风险是磁盘（39GB free），两个 run 完成后会到 ~9GB，建议跑完后立即清理 v1 废弃目录

---
