# ops westd check round2 and seed investigation

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_check_round2_and_seed_investigation_20260522T100715_result.json`
- **Structured JSON:** [`a2674f52736e8f151e34.json`](../../sessions/a2/a2674f52736e8f151e34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

v3 config 已就绪。汇总：

---

### 1. Round 2 eval 状态

| GPU | 任务 | 状态 | 显存 |
|-----|------|------|------|
| 0 | intervention_c_step7 | ✅ 运行中（vLLM 已加载，开始 rollout） | 90 GB |
| 1 | high_kl_step5 | ✅ 运行中（wandb 连接，model loading） | 8 GB |
| 2 | high_kl_step7 | ✅ 运行中（wandb 连接，model loading） | 8 GB |

3 个 Round 2 eval 全部正常启动，wandb runs 已创建。

### 2. intervention_c_step5 Round 1 (GPU 3)

**已完成**，GPU 已释放（0 MiB）。结果：
- **success = 19.4%**（pass@1 = 19.4%，134 tasks）

### 3. seed.val 一致性汇总

| Config | seed.val | 状态 |
|--------|----------|------|
| **seed5** | **789** | ❌ 不一致，需要重跑 |
| seed6 | 321 | ✅ |
| seed4 | 321 | ✅ |
| intervention_c (step10) | 321 | ✅ |
| intervention_c_step5 | 321 | ✅ |
| intervention_c_step7 | 321 | ✅ |
| high_kl_step5 | 321 | ✅ |
| high_kl_step7 | 321 | ✅ |
| c_prime_step5 | 321 | ✅ |
| seed2048_step5 | 321 | ✅ |
| **SFT baseline v1** | **123** | ❌ |
| **SFT baseline v2** | **123** | ❌ |

**问题**：seed5 用了 seed.val=789，SFT baseline 用了 seed.val=123。两者都与标准 321 不一致。seed5 需要重跑 eval。

### 4. SFT baseline v3 config

`_alfworld_sft_baseline_ood_eval_v3.yaml` 已创建：
- seed.val: 123 → **321** ✅
- enable_response_mask: (默认 True) → **False** ✅
- experiment_name / log dirs 已更新为 v3
- **未启动**，等 Round 2 完成后再跑

### 待处理
- seed5 需要用 seed.val=321 重跑 eval（需创建 v2 config）
- SFT baseline v3 等 GPU 空闲后启动

---
