# ssh urgent status check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_status_check_20260522T021156_result.json`
- **Structured JSON:** [`5e7933099e5d4682fbd6.json`](../../sessions/5e/5e7933099e5d4682fbd6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 服务器: westd-19183 — 在线

| 资源 | 状态 |
|------|------|
| **GPU 0** | 空闲 (0%, 0 MiB / 97887 MiB, 30°C) |
| **GPU 1** | 占用 (84%, 15293 MiB / 97887 MiB, 57°C) |

---

### 实验状态

**openvla_goal_standardized_v1** (PID 591230, GPU 1) — **运行中**
- 运行时间: 1h39m
- 当前: TRAINED → Phase 6 (counterfactual analysis) → `paraphrased` 条件 2400/5000
- 已完成 Phase 1-5 (trained)，Phase 6 已完成 wrong / empty / shuffled，正在跑 paraphrased
- 已产出文件 (trained): `action_r2_probing.json`, `l1_attention_profile.json`, `cross_instruction_classification.json`, `rsa_analysis.json`
- **还剩**: paraphrased 剩余 ~20min → 然后跑整个 UNTRAINED 管线 (~110min)
- **预估总剩余: ~2h**

**openvla_spatial_standardized_v1** (PID 594575, GPU 0) — **运行中（下载模型中）**
- 运行时间: 35min
- 当前: 下载 checkpoint，已下载 ~5.6GB，速度波动
- GPU 0 空闲因为还没开始计算
- **预估**: 下载还需 30-60min，之后完整管线 ~2h

**cf_batch_missing_v1** (PID 584349) — **已完成 ✓**
- 退出码: 0，耗时 44.9min
- 产出: `/root/autodl-tmp/vla-ssd/results/tracvla_long/untrained/counterfactual_combined.json`

---
