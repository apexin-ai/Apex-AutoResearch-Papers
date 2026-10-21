# reviewer / loop_22.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_22.md`
- **Structured JSON:** [`0eb9e1134e03c1341fb8.json`](../../sessions/0e/0eb9e1134e03c1341fb8.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 22
reason: max_wall_time
updated: '2026-05-23T19:47:21+00:00'
---

### 1. 🔴 硬约束 / 红线
- Object Adaptive s45 在 bjb2-40593 上因 CRM checkpoint 缺失崩溃过两次（`eval-supp-obj-adapt-tau025-s45` failed, `s45-r2` killed）。该实验已转到 bjb2-28827。**bjb2-40593 上没有 3-suite CRM checkpoint**（`/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt` 不存在），只能跑 VLA-only 或需要先同步 checkpoint
- Long suite 使用 **4-suite CRM checkpoint**（`crm_unified_4suite_r4/crm_best.pt`），Spatial/Object/Goal 使用 **3-suite CRM checkpoint**（`crm_smolvla_3suite_v1/crm_best.pt`），混用会导致结果不可比
- cqa1-32758 PID 199664（Long VLA-only s43）是孤儿进程——registry 指向 bjb2-28827 的新部署，但 cqa1 上的旧进程未被 kill（运行 5h+）。另两个孤儿（PID 345585/345660）已被 kill

### 2. 🖥️ 基础设施快照
- **bjb2-28827** (6x 4090): GPU 0-5 全忙。Object s45 Adaptive + s46 Adaptive + Object VLA-only s45 + Long s43 VLA-only + Long s44 Reconvla + Long s44 K2mean
- **bjb1-32546** (6x 4090): GPU 0-5 全忙。Object VLA-only s46 + Long s43 ×4 (Adaptive/CRM/Reconvla/K2mean) + Long VLA-only s44
- **cqa1-32758** (6x 4090D): GPU 1,5 跑 Long s44 Adaptive+CRM。GPU 4 跑 Long K2mean s42。GPU 0/2/3 有 backfill 部署（worker 刚完成，具体实验需查 registry）。PID 199664 孤儿仍在
- **bjb2-40593** (1x 4090D): 跑 Object CRM s45（worker swap 部署）
- **bjb1-18228**: π0.5 precompute，ETA 5/24-25
- 代码根目录均为 `/root/acr-vla-conformal-refinement`，conda base 环境
- 本地 workspace: `/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/`

### 3. 📊 当前状态
**已完成审查并报告**：
- Long s42 全套（VLA-only 58.0%, Adaptive 59.0%+1.0pp, CRM 56.5%-1.5pp, Reconvla 56.5%-1.5pp）→ 已 post info
- τ-sweep 消融（Goal s42, 4 点倒 U 型）→ 已 post info
- bjb2-40593 崩溃 → 已 post critical，已修复
- cqa1 孤儿进程 → 已 post warning，部分清理
- ROADMAP D133 叙事审查 → 已 post info，通过
- p<0.05 移除 → 已提醒需确认替代表述

**RUNNING 实验（~16 个）**：全部是 Long s43/s44 多种子 + Object s45/s46 额外种子。预计 5-7h 完成。

**等待中**：Paper Agent D133 narrative pivot patch 提交后的 Step 5 re-review

### 4. 📋 待办
- Long s43/s44 结果到齐 → 计算 Long 3-seed mean±std，验证 D133 "Adaptive ≥ VLA-only on ALL 4 suites" 是否在 Long 上成立。若 Long 3-seed Adaptive ≤ VLA-only → **立即 CRITICAL**，D133 叙事需再次调整
- Object s45/s46 结果到齐 → 计算 5-seed Object Adaptive mean±std，评估方差是否收窄到可接受水平
- Paper Agent 提交 D133 narrative patch → 按 Step 5 模板做写作对抗审查（评分 + checklist）
- Long trigger_rate 3-seed 数据到齐 → 若一致偏低（<5%），post warning 要求 Limitations 披露 "confidently-wrong" 局限
- π0.5 precompute 完成 → 验证 cross-model 实验设计

### 5. 🎯 战略上下文
**核心叙事 D133**："Gating prevents harmful correction + improves where VLA shows uncertainty"。这是 Object 3-seed Δ=0.0pp 崩塌后的 pivot，从 "positive across all suites" 转向 "gating is the mechanism"。叙事的核心支柱是 **Adaptive ≥ CRM on ALL suites**（+1.0 to +2.5pp），这比 Adaptive vs VLA-only 更稳固。

**最容易判断错的事**：
1. **Long 1-seed 的 +1.0pp 不可信**——参照 Object（s42=+2.0pp → 3-seed=0.0pp），Long 完全可能翻转。在 Long 3-seed 到齐前不要对 Long 数据做任何论文级结论
2. **CRM always-on 用 ε=0.05/K=10，Adaptive 用 ε=0.2/K=2**——τ-sweep 讨论中容易混淆。τ=0.10 的 81.0%(-2.5pp) 不能和 CRM always-on 的 85.5%(+2.0pp) 直接比较，因为 ε 不同
3. **Registry 中有重名/近名实验**（如 `eval-supp-obj-adapt-tau025-s45` vs `eval-supp-adapt-tau025-obj-s45`），查数据时要核对 server+seed+conclusion，不要只看 exp_id 前缀
4. **Goal VLA-only 3-seed = 83.7±1.3%**（s42=83.5, s43=82.5, s44=85.0）——之前多次修正，最终值已稳定。Goal CRM 3-seed 也恰好 = 83.7%（delta=0.0pp），这不是 bug
5. **Memory 文件 `object_adaptive_3seed_zero_delta.md`** 记录了 Object 崩塌的完整数据，是 D133 pivot 的关键证据


---
