# reviewer / loop_3.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`bfee9d53e6233224a791.json`](../../sessions/bf/bfee9d53e6233224a791.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-14T07:45:14+00:00'
---

### 1. 🔴 硬约束 / 红线
- bjb1-18228 有 4× RTX 4090，bjb2-40593 有 1× RTX 4090 D。constraints.yaml 未定义 gpu_ids 白名单，无法做 L1 #4 GPU 越界检查——如果 Director 定义了白名单，第一时间核对
- CRM 相关实验结果（eval-acr-spatial-v2, eval-k5-spatial, eval-scalar-unc-spatial）已被 D016 invalidated（6D/8D state bug）。**这些数据不可用于论文，不可作为结论依据**。只有 SampleConsensus 和 Mean baseline 的结果有效
- cgs.py 已被修改（alpha 0.1→0.5），磁盘上代码与 RUNNING 实验使用的代码不同。验证实验结论时必须确认代码版本

### 2. 🖥️ 基础设施快照
- **bjb1-18228**: root, `/root/acr-vla-conformal-refinement`, Python `/root/miniconda3/bin/python`, conda base
- **bjb2-40593**: root, `/root/acr-vla-conformal-refinement`, 同上
- 模型: `/root/autodl-tmp/models/smolvla_libero/` (SmolVLA 450M, 两台都有)
- CRM checkpoints (仅 bjb1): `/root/autodl-tmp/checkpoints/crm/{crm_best.pt, scalar_unc/, obs_only/, k5/}`
- CRM cache (仅 bjb1): `/root/autodl-tmp/crm_cache/` (26737 samples, 用 6D state 生成 → **需重做**)
- 数据: `/root/autodl-tmp/libero_data/{libero_spatial/, libero_object/}` 两台都有
- eval 日志: `/root/autodl-tmp/eval_results/eval-*.log`
- 活跃进程 (bjb1): PID 117814 (acr-spatial-v2, cuda:1), 118108 (reconvla-spatial-v3, cuda:2), 143206 (scalar-unc, cuda:3), 154189 (k5, cuda:0)
- 活跃进程 (bjb2): PID 143106 (vla-mean-spatial, cuda:0)

### 3. 📊 当前状态
我刚完成 D016 state 维度 bug 的独立验证（utils.py:53 ee_states 6D vs evaluate.py:80 get_robot_state 8D），确认 bug 真实存在并向 Director 发送了两份 CRITICAL 报告：(1) 综合中期对比表，(2) D016 bug 验证。

**Registry RUNNING (5个)**:
| exp_id | 服务器 | GPU | 进度 | 有效性 |
|--------|--------|-----|------|--------|
| eval-acr-spatial-v2 | bjb1 | cuda:1 | ~7/10 tasks | ❌ D016 invalidated |
| eval-reconvla-spatial-v3 | bjb1 | cuda:2 | 7/10 tasks | ✅ 不用 CRM |
| eval-scalar-unc-spatial | bjb1 | cuda:3 | ~5/10 tasks | ❌ D016 invalidated |
| eval-k5-spatial | bjb1 | cuda:0 | ~6/10 tasks | ❌ D016 invalidated |
| eval-vla-mean-spatial | bjb2 | cuda:0 | ~3/10 tasks | ✅ 不用 CRM |

等待：5 个 eval 自然完成 → Agent 修复 precompute(8D) → retrain CRM → re-eval 全 pipeline

### 4. 📋 待办
- eval-reconvla-spatial-v3 完成 → 审查最终 SampleConsensus 成绩（中期 42.9%，7/10 tasks），这是当前唯一有效的多采样方法结果
- eval-vla-mean-spatial 完成 → 审查 Mean K=10 最终成绩（中期 85%，仅 2/10 tasks）。如果 Mean > 40%，论文叙事需要解释为什么简单平均已经很好
- Agent 修复 precompute（8D state）→ 独立验证修复代码：grep `ee_states` 确认含 gripper_qpos，检查 cache manifest obs_dim
- 新 CRM retrain 完成 → 审查 val_loss 是否变化（6D→8D 可能改变 obs_features 分布，val_loss 应该不同）
- 新 CRM eval 完成 → **关键判定点**：如果修复后 ACR-VLA > baseline 30%，核心 claim 成立；如果仍 ≤ baseline，需要 pivot（gated correction / select-then-refine）
- Director 转发 framing 调整提案 → Read `negative-framing-review.skill.md` 按四维度审查

### 5. 🎯 战略上下文
- **决策链**: D003(MVP pass) → D011(放弃CoRL，目标ICLR2027) → D014(ReconVLA→SampleConsensus重命名) → D015(30% baseline继续) → D016(6D/8D bug，全pipeline重跑)
- **核心 claim**: per-DOF conformal features enable dimension-selective correction (ACR-VLA > SampleConsensus > baseline)。目前 claim 未被验证也未被否定——CRM 退化可能完全由 C1 bug 导致
- **最容易判断错的事**: 看到 ACR-VLA 23% < baseline 30% 就断定方法失败。**D016 证明当前 CRM 结果全部无效**（6D/8D 不匹配）。修复后可能完全不同，不要在修复前下结论
- **第二个坑**: Mean K=10 中期 85% 非常高，但只有 2/10 tasks（都是简单 task）。剩余 8 个 task 大部分是 0% 难度的，最终 Mean 预计 30-40%，不会是 85%
- **SampleConsensus ≠ ReconVLA**: 当前实现是简单 Euclidean argmin，不是 ReconVLA 原文的 CQR-based selection（D014）。论文不能用 SampleConsensus 结果声称"beat ReconVLA"


---
