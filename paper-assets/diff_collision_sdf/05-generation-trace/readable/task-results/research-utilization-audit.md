# research utilization audit

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_utilization_audit_20260528T191058_result.json`
- **Structured JSON:** [`0a76ac085a48f2b17bbc.json`](../../sessions/0a/0a76ac085a48f2b17bbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。产出已注册为 `art_20260528_9360ac`。

**核心发现：**

- **利用率 70.8%**（51/72 实验被论文引用），29.2% 未引用的实验中 57% 是因 180° 旋转 bug 被废弃的 pre-fix 评估，属于合理排除。
- **仅 3 个实验有未被利用的价值：**
  1. `eval_multiseed_sdf_l01_s0_eseed256`（λ=0.1 第4个 eval seed，CAR=57%）— 可直接加入 appendix eval-seed 表，修复当前 3 vs 5 的不对称
  2. `reeval_lora_s0_30k_v2`（同一模型重复评估，CAR=57% vs 56.5%）— 量化了 run-to-run 噪声，可支撑 MDE 讨论
  3. `train_phase2_lambda0_extra_seed`（Phase 2 消融第2个 seed）— 如果做过 eval，可将 Phase 2 消融从 n=1 升至 n=2

- **17 个溯源缺口：** 论文中的 Pi0 Full-FT（83%）、Pi0 LoRA（82%）、Oracle 系列、A3、spatial_bowl SDF 评估、以及 stepwise 16K/20K/24K/28K 数据均无对应 registry 实验记录。

---
