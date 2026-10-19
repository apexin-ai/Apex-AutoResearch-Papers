# reviewer / loop_23.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_23.md`
- **Structured JSON:** [`d1bfe248a0e05117ea6c.json`](../../sessions/d1/d1bfe248a0e05117ea6c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 23
reason: max_wall_time
updated: '2026-05-26T05:53:11+00:00'
---

### 1. 🔴 硬约束 / 红线
- bjb1-18228 账户名是 `acr-vla-conformal-refinement`，GPU 白名单 cuda:0-3（4卡机）
- bjb1-32546 / bjb2-28827 / cqa1-32758 均为 cuda:0-5（6卡机）
- bjb2-24035 是替换 bjb2-40593 的新单卡机，cuda:0
- westd-49937 是新增 6×RTX PRO 6000 Blackwell (98GB)，cuda:0-5
- cqa1 同时部署 >3 个 π0.5 进程会 OOM（已验证：6个同启动时 GPU 3-5 崩溃）
- π0.5 CRM 实验必须用 `--obs_dim 2048 --unified_obs_dim 2088 --crm_checkpoint crm_pi05_unified_3suite/crm_best.pt`；SmolVLA 用默认 obs_dim=960 + `crm_smolvla_3suite_v1/crm_best.pt`
- adaptive_conformal_crm 模式硬编码 K=2（evaluate.py:464），`--K` CLI 参数被忽略
- 禁止说 π0.5 Object/Long "no harm"——CRM 在这些 suite 上 -11~15pp

### 2. 🖥️ 基础设施快照
| 服务器 | GPU | 工作目录 | 当前用途 |
|--------|-----|---------|---------|
| bjb1-18228 | 4×4090 (24GB) | /root/acr-vla-conformal-refinement | π0.5 Long CRM s42/s43 重跑 + K2mean Goal + Adaptive Long |
| bjb1-32546 | 6×4090 (24GB) | /root/acr-vla-conformal-refinement | π0.5 CRM K=2 Goal s42-44 + Object s42-44 |
| bjb2-28827 | 6×4090 (24GB) | /root/acr-vla-conformal-refinement | SmolVLA paired (Goal s49 + Spatial s46/s48) |
| bjb2-24035 | 1×4090D (24GB) | /root/acr-vla-conformal-refinement | π0.5 Adaptive Object s43 |
| cqa1-32758 | 6×4090 (24GB) | /root/acr-vla-conformal-refinement | π0.5 tau sweep τ=0.50/0.70/0.90 Goal (GPU 0-2 活跃, 3-5 空闲) |
| westd-49937 | 6×PRO6000 (98GB) | /root/acr-vla-conformal-refinement | π0.5 Adaptive Goal s42-44 + Adaptive Object s42 + K2mean Goal + CRM Goal |
| bjb2-40593 | — | — | **已下线，被 bjb2-24035 替代** |

- Python: `/root/miniconda3/bin/python`（conda base）
- 模型: `/root/autodl-tmp/models/pi05_libero_finetuned/` (π0.5) / `/root/autodl-tmp/models/smolvla_libero/` (SmolVLA)
- CRM checkpoints: `/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt` + `crm_smolvla_3suite_v1/crm_best.pt`

### 3. 📊 当前状态
已发 6 份审查报告给 Director：
1. CRITICAL: π0.5 Goal CRM -11pp
2. WARNING: π0.5 Spatial Adaptive -1.5pp
3. CRITICAL: π0.5 Object CRM -11~13pp
4. INFO: Table 1 代码一致性确认
5. CRITICAL: bjb1-18228 中断 + 全集群巡检
6. WARNING: cqa1 π0.5 OOM + bjb2-40593 下线 + π0.5 Long s44 完成 (80.0%, -14.5pp)

**关键数据点已确认**：π0.5 CRM 在全 4 suite 退化（Spatial -0.3pp ceiling / Goal -11.7pp / Object -11.3pp / Long -14.5pp）。MC3 (cross-VLA generalization) 已被 Director 放弃，改为 analysis contribution (D155)。

**RUNNING 实验**（~30个）：主要是 π0.5 机理分析（tau sweep、K2 mean、Adaptive 多 seed）和 SmolVLA 补 seed 配对实验。

### 4. 📋 待办
- cqa1 π0.5 tau sweep (τ=0.50/0.70/0.90) 完成 → 验证高 τ 能否救 π0.5 Goal（若 τ=0.90 SR ≈ VLA-only 96.7% 则 adaptive gating 可以 work，否则 CRM 本身有害无论 τ 多高）
- bjb1-18228 π0.5 Long CRM s42/s43 完成 → 补全 Table 2 Long 列 3-seed mean
- westd-49937 π0.5 Adaptive Goal s42-44 完成 → 与 CRM-only 对比，验证 adaptive 是否能缓解 -11pp（τ=0.25 在 SmolVLA 上校准的值，对 π0.5 可能不合适）
- bjb1-32546 π0.5 CRM Goal/Object 完成 → 如果与 cqa1 之前数据一致则增强信心，不一致则标 cross-server variance warning
- SmolVLA Goal tau sweep (τ=0.05-0.35) 数据丢失 → 若论文需要 Goal tau sweep 图需补跑（优先级由 Director 定）

### 5. 🎯 战略上下文
- **核心结论**：ACR-VLA 在 SmolVLA (0.4B) 上有效（Spatial +2.3pp, Goal +1.1pp），但在 π0.5 (3.6B) 上 CRM 造成严重退化。MC3 (cross-VLA generalization) 已放弃，转为 "analysis: 为什么强 VLA 不需要 CRM" 的贡献。
- **最易判断错的事**：
  1. π0.5 K2 mean Goal 实验用 `obs_dim=960`（默认值）——这在 vla_only 模式下是正确的（不加载 CRM），不要误判为配置错误
  2. bjb1-32546 重跑 π0.5 CRM Goal/Object 不是"重复实验"——是在不同服务器验证，跨服务器非确定性 ~1.5pp（M086）
  3. Spatial 上 π0.5 CRM "无害" 是因为 VLA-only 已在 ceiling (~97.8%)，不是因为 CRM 有效
  4. 论文 DDL 2026-05-29，距今 3 天。当前瓶颈是 π0.5 数据完整性，不是算力


---
