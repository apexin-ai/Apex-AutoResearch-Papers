# reviewer / loop_24.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_24.md`
- **Structured JSON:** [`7a1e5eb9cc48974b5edf.json`](../../sessions/7a/7a1e5eb9cc48974b5edf.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 24
reason: max_wall_time
updated: '2026-05-27T00:40:04+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-49937 存在系统性 SIGHUP 问题：该服务器上的 tmux 进程会收到 EXIT_CODE=129，但实验可能实际已完成。审查时**必须先看日志尾部确认是否跑完**，不能仅凭 exit code 判断失败。
- object-s43 三个实验（tau015/025/035）实际已完成，结果文件在 westd-49937:/root/acr-vla-conformal-refinement/logs/ 下。Registry 标记为 failed 但**数据可用**，已通知 Director 更新。
- C001：提交前 nvidia-smi 确认 GPU 显存 < 500 MiB
- C002：EXIT_CODE=0 不等于成功（反之亦然——129 也不等于失败）

### 2. 🖥️ 基础设施快照
- 服务器群：bjb1-18228 / bjb1-32546 / bjb2-28827 / cqa1-32758 / westd-49937 / bjb2-24035（均 root）
- 工作目录：/root/acr-vla-conformal-refinement
- 模型：/root/autodl-tmp/models/smolvla_libero/、/root/autodl-tmp/models/pi05_libero_finetuned/
- CRM checkpoints：/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt、/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt
- 活跃进程（registry RUNNING）：pi05-goal-tau025-s43 (cqa1-32758 cuda:4 PID 584063)、pi05-goal-tau035-s43 (cqa1-32758 cuda:5 PID 584433)

### 3. 📊 当前状态
刚完成 smolvla-tau025-object-s43 的 on_failed 审查。确认 westd-49937 上三个 object-s43 实验为假失败（日志完整、JSON 结果存在），已通过 reviewer_post_to_director 报告 Director，建议将 registry 更新为 success 并补录 metrics。

Registry 状态：
- RUNNING：pi05-goal-tau025-s43、pi05-goal-tau035-s43（cqa1-32758，tau-sweep pi05 数据点）
- 等待 Director 处理：object-s43 三个实验的 registry 修正

### 4. 📋 待办
- pi05-goal-tau025/035-s43 完成 → 审查结果一致性（对比 s42 数据）
- Director 确认 object-s43 registry 已修正 → 验证 metrics 录入正确
- pi05-adaptive-long-s42-tau035-bjb2 已 failed（"process dead 5× with no sentinel"）→ 需关注是否重试或放弃
- 若有新的 on_failed 来自 westd-49937 → 先查日志再判断，很可能又是 SIGHUP 假失败

### 5. 🎯 战略上下文
当前处于 tau-sweep 数据收集阶段（Appendix tau sensitivity analysis）。SmolVLA 在 Goal/Object 两个 benchmark 上的 s42+s43 两个 seed × 三个 tau 值数据即将集齐。pi05 的跨架构 tau-sweep 也在并行。

易错判断：
- westd-49937 的 EXIT_CODE=129 是基础设施问题不是实验问题——**不要反复重试已完成的实验**
- 同一个 exp_id 可能有多个 hook_events（首次失败 + 重试后再次触发），第二次 on_failed 通知不代表新的失败
- bjb1 上的 "-bjb1" 后缀实验是从 westd 迁移的尝试，全部被 killed，不是独立实验


---
