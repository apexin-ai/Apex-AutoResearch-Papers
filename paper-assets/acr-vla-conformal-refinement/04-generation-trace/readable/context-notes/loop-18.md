# director / loop_18.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_18.md`
- **Structured JSON:** [`9ed45cd4a6f867888d44.json`](../../sessions/9e/9ed45cd4a6f867888d44.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: max_messages
updated: '2026-05-22T23:14:38+00:00'
---

# Director Handoff — Loop #18 → #19

## 刚做完什么
- Agent 完成 context rotation 后空闲，我立即发了 P0 CRM eval 部署指令（om_x100b6e3a7f2c84a8b4a59af2c70cd56）
- 用户已通知当前状态

## 等待中的关键事项

### 1. SmolVLA CRM Eval 部署（P0，论文 critical path）
- CRM 3-suite 训练在 bjb2-28827 cuda:0，ETA ~23:00 UTC May 22，应已完成
- Checkpoint: `/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt` (1.3MB, obs_only, unc_dim=0, obs_dim=960)
- 部署脚本: `artifacts/deploy_smolvla_crm_eval.sh`（Reviewer PASS）
- 18 个 eval：9 CRM (crm_obs_only mode) + 9 VLA-only baseline，3 suites × 3 seeds
- GPU 分配：bjb2-28827 cuda:1-5 (5)，bjb1-32546 cuda:0,1,2,4 (4)
- 已给 Agent 发了完整部署指令，等 Agent 回复确认执行

### 2. SmolVLA Baseline 收集（部分完成）
| Suite | Seed42 | Seed43 | Seed44 | Mean |
|-------|--------|--------|--------|------|
| Object | 66.5% | 66.5% | 65.0% | **66.0%±0.9%** ✅ |
| Spatial | 59.5% | running? | 60.0% | — |
| Goal | 75.5% | running? | running? | — |
| Long | 49.5% | 53.5% | 49.5% | **50.8%±2.3%** ✅ |

bjb1-32546 上可能还有 baseline eval 在跑，Agent 部署 CRM eval 时需避让。

### 3. π0.5 相关（P2 背景任务）
- π0.5 precompute 2048D 在 bjb1-18228 cuda:0,1,2 跑 3 suites，~37-44h 每个，best-effort
- bjb1-32546 cuda:3 有 SmolVLA 4-suite CRM 训练（crm_cache_v5 确认是 SmolVLA 960D，不是 π0.5），ETA ~08:20 UTC May 23
- π0.5 VLA-only baseline 已全部完成且饱和（94-100%），见 ROADMAP

## 关键决策上下文
- **D124**: 2-model paper（SmolVLA 0.4B + π0.5 3.6B），OFT 已放弃
- **D125**: crm_cache_v5 确认是 SmolVLA 960D（之前误标为 π0.5）
- **D126**: π0.5 precompute 降级为 best-effort，defer to rebuttal if not done by May 24
- **D077**: Adaptive K 是核心贡献（用户最高权限指令），CRM magnitude calibration pending

## CRM Eval 结果出来后的决策树
1. **CRM positive**（SmolVLA SR 有提升）→ 立即部署 adaptive_conformal_crm eval（核心贡献验证）→ Paper Agent 补数据到论文
2. **CRM neutral/negative** → 方法改进诊断（先看 CRM 预测误差分布，再决定改进方向）

## 不能做/教训
- M058: 不要仅凭 GPU 空闲就判断 eval 是 ghost entry（SmolVLA 0.4B eval 只需 19min）
- M059: 同一服务器最多 2 个 lerobot eval 并行，否则 1000 子进程崩溃
- Wrapper eval 和 lerobot-eval 有 6x SR gap，不可混比，CRM eval 必须用 wrapper + VLA-only 对照
- bjb1-32546 cuda:3 上的训练是 SmolVLA 4-suite CRM（不是 π0.5），不要误解

## Paper Writing
- Paper Agent 已完成 Method + Related Work 初稿（Step 1-2）
- 剩余章节（Intro/Experiments/Abstract/Conclusion）依赖 CRM eval 结果
- 投稿目标 CoRL 2026，DDL 2026-05-29，剩余 ≤7 天

## 服务器列表
| 服务器 | GPU | 用途 |
|--------|-----|------|
| bjb2-28827 | 6×4090 | CRM 训练(cuda:0) + CRM eval 部署(cuda:1-5) |
| bjb1-32546 | 6×4090 | baseline eval + CRM eval 部署 + 4-suite CRM(cuda:3) |
| bjb1-18228 | 4×4090 | π0.5 precompute 2048D(cuda:0-2), cuda:3 空闲 |
| bjb2-40593 | 1×4090D | excluded |


---
