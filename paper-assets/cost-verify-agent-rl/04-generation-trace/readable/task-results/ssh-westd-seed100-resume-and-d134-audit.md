# ssh westd seed100 resume and d134 audit

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd_seed100_resume_and_d134_audit_20260522T215650_result.json`
- **Structured JSON:** [`4586d30bc7c2939645d8.json`](../../sessions/45/4586d30bc7c2939645d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。

---

## 汇报

### seed100 resume checkpoint
- **存在**, 路径: `/root/autodl-tmp/checkpoints/exp029-seed100/global_step_5/`
- 大小: **21GB**（含 optimizer states，符合 FSDP 完整 checkpoint 预期）
- 含 optimizer states: **是**
  - `actor/model_world_size_2_rank_{0,1}.pt`
  - `actor/optim_world_size_2_rank_{0,1}.pt`
  - `actor/extra_state_world_size_2_rank_{0,1}.pt`
- **可以 resume**（world_size=2, .pt 格式, optimizer + model + extra_state 齐全）

---

### D134 审计

**base.yaml 默认值**: enable_think=True, enable_response_mask=**True**, context_window_mode=full, val T=0.5

**D134 协议要求**: enable_think=True, enable_response_mask=**False**, context_window_mode=full, T=**0.4**

所有 eval config 使用 `defaults: - base`，以下为逐项审计（全部 134 episodes）：

| 数据点 | config 文件 | enable_think | enable_response_mask | context_window_mode | val T | 合规 |
|--------|------------|-------------|---------------------|--------------------|----|-----|
| seed4 step15 | `_alfworld_exp029_seed4_ood_eval.yaml` | True (继承base) | **False** (显式) | full (显式) | **0.4** (显式) | ✅ |
| seed4 step15 v2 | `_alfworld_seed4_step15_ood_eval_v2.yaml` | True (继承base) | **False** (显式) | full (显式) | **0.4** (显式) | ✅ |
| seed5 step10 v2 | `_alfworld_exp029_seed5_ood_eval_v2.yaml` | True (继承base) | **False** (显式) | full (显式) | **0.4** (显式) | ✅ |
| seed6 step15 | `_alfworld_exp029_seed6_ood_eval.yaml` | True (继承base) | **False** (显式) | full (显式) | **0.4** (显式) | ✅ |
| seed6 step15 v3 | `_alfworld_seed6_step15_ood_eval_v3.yaml` | True (继承base) | **False** (显式) | full (显式) | **0.4** (显式) | ✅ |
| seed2 step15 | `_alfworld_seed2_step15_ood_eval.yaml` | True (继承base) | **False** (显式) | full (显式) | **0.4** (显式) | ✅ |
| seed42 step5 | `_alfworld_seed42_step5_ood_eval.yaml` | True (继承base) | **False** (显式) | full (显式) | **0.4** (显式) | ✅ |
| seed100 step5 | `_alfworld_seed100_step5_ood_eval.yaml` | True (继承base) | **False** (显式×2†) | full (显式) | **0.4** (显式) | ✅ |
| seed200 step5 | `_alfworld_seed200_step5_ood_eval.yaml` | True (继承base) | **False** (显式) | full (显式) | **0.4** (显式) | ✅ |
| seed300 step5 | `_alfworld_seed300_step5_ood_eval.yaml` | True (继承base) | **False** (显式) | full (显式) | **0.4** (显式) | ✅ |
| SFT baseline | `_alfworld_sft_baseline_ood_eval_v3.yaml` | True (继承base) | **False** (显式) | full (显式) | **0.4** (显式) | ✅ |
| intervention-c step5 | `_alfworld_intervention_c_step5_ood_eval.yaml` | True (继承base) | **False** (显式) | full (显式) | **0.4** (显式) | ✅ |
| intervention-c step7 | `_alfworld_intervention_c_step7_ood_eval.yaml` | True (继承base) | **False** (显式) | full (显式) | **0.4** (显式) | ✅ |
| seed7-high-kl step5 | `_alfworld_seed7_high_kl_step5_ood_eval.yaml` | True (继承base) | **False** (显式) | full (显式) | **0.4** (显式) | ✅ |
| seed7-high-kl step7 | `_alfworld_seed7_high_kl_step7_ood_eval.yaml` | True (继承base) | **False** (显式) | full (显式) | **0.4** (显式) | ✅ |
| C' step5 | `_alfworld_c_prime_step5_ood_eval.yaml` | True (继承base) | **False** (显式) | full (显式) | **0.4** (显式) | ✅ |
| seed2048 step5 | `_alfworld_seed2048_step5_ood_eval.yaml` | True (继承base) | **False** (显式) | full (显式) | **0.4** (显式) | ✅ |

†seed100 config 有两处 `enable_response_mask: false`（一处在 `actor_rollout_ref.model` 下，一处在顶层），不影响结果，均为 False。

**需要重跑的: 无。全部 17 个 eval config 均 D134 合规。**

---

### GPU 状态 (westd-47453)

| GPU | 显存使用 | 总显存 | 利用率 |
|-----|---------|-------|--------|
| 0 | 0 MiB | 97887 MiB | 0% |
| 1 | 0 MiB | 97887 MiB | 0% |
| 2 | 0 MiB | 97887 MiB | 0% |
| 3 | 0 MiB | 97887 MiB | 100%* |

*GPU 3 显示 100% utilization 但 0 MiB 显存占用，无 train.py 进程运行，无 tmux session。可能是驱动残留状态，实际空闲。

4 卡全部可用，无训练进程。checkpoint watchdog 后台运行中（PID 118781）。

---
