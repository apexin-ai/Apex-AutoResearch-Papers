# ops westd checkpoint inventory and ood

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_checkpoint_inventory_and_ood_20260521T224524_result.json`
- **Structured JSON:** [`c6ee6729d667c7a2b37f.json`](../../sessions/c6/c6ee6729d667c7a2b37f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 4 张卡已全部用上。

---

## 产出汇总

### 1. 完整 Checkpoint 清单

| 路径 | 格式 | 身份 | Step | OOD 状态 |
|------|------|------|------|----------|
| `qwen_exp029_seed4_step15_hf` | HF | seed 4 | 15 (final) | ✅ 30.60% |
| `qwen_exp029_seed5_step10_hf` | HF | seed 5 | **10 (final, confirmed)** | ✅ 29.10% |
| `qwen_exp029_seed6_step15_hf` | HF | seed 6 | 15 (final) | ✅ 29.10% |
| `qwen_exp029_seed8_step5_hf` | HF | seed 8 | **5 (final, confirmed)** | ✅ 11.94% |
| `qwen3_exp021_ragen_sft_v4` | HF | SFT baseline | — | ✅ 5.97% |
| `intervention_c_hard_cap_step7_hf` | HF (FSDP 转换) | intervention-C (seed=999) | 7 (final) | 🔄 cuda:0 |
| `intervention_c_hard_cap_step5_hf` | HF (FSDP 转换) | intervention-C (seed=999) | 5 | 🔄 cuda:1 |
| `exp029_seed7_high_kl_step7_hf` | HF (bjb1→westd 传输) | seed7 high-KL | 7 (final) | 🔄 cuda:2 |
| `exp029_seed7_high_kl_step5_hf` | HF (bjb1→westd 传输) | seed7 high-KL | 5 | 🔄 cuda:3 |
| `qwen3_8b_sft_v1/checkpoint-231` | HF | Qwen3-8B (不同架构) | 231 | N/A |
| `exp029_seed3` | 空目录 | — | — | ✅ 已做 |
| `gae_baseline`, `7b-*`, `8b-cell-c` | 空目录 | — | — | — |

**关键确认**：
- Seed 5 step 10 = final step（`latest_checkpointed_iteration.txt` = 10）
- Seed 8 step 5 = final step
- Seed 7 base checkpoint 在两台服务器上均未找到（仅有 high-KL 和 hard-cap 两个 intervention 变体）
- Seed 2 checkpoint 两台服务器上均不存在

### 2. 已启动的 OOD Eval

| exp_id | GPU | PID | Checkpoint |
|--------|-----|-----|-----------|
| `intervention_c_step7_ood` | cuda:0 | 895615 | intervention-C step 7 (final, collapsed) |
| `intervention_c_step5_ood` | cuda:1 | 903154 | intervention-C step 5 (pre-collapse) |
| `seed7_high_kl_step7_ood` | cuda:2 | 924058 | seed7 high-KL step 7 (final) |
| `seed7_high_kl_step5_ood` | cuda:3 | 935129 | seed7 high-KL step 5 (mid-training) |

### 3. 空闲卡

**0 张空闲** — 全部 4 卡均在运行 OOD eval。

### 额外工作

- FSDP→HF 转换：intervention-c step 5/7（westd 本地）、seed7-high-kl step 5/7（bjb1 上）
- 跨服务器传输：通过建立 westd→bjb1 的 SSH key 认证，SCP 了 2 个 checkpoint（各 ~3.8GB）到 westd
- 全部 4 个 eval 的 registry 条目已创建（hypothesis + parent）

---
