# reviewer / loop_9.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_9.md`
- **Structured JSON:** [`d696da5b9701209c1bb8.json`](../../sessions/d6/d696da5b9701209c1bb8.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_wall_time
updated: '2026-05-15T20:17:46+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**cuda:0, cuda:1** only（C001 约束）。exp027 PID=789790 正确占用这两张卡，已核实。
- 服务器账号：`root@bjb1-17606`，不得用其他服务器/账号提交训练
- eval 最低标准：C003 要求 ≥16 episodes validation
- 预检约束：C002 pre-flight check 在提交训练前必须执行
- experiment_plan.yaml 和 paper_framing.md 被 worker 写到了 `artifacts/` 非标准路径（`artifacts/_project/report/experiment_plan.yaml` 和 `artifacts/docs/framing_draft.md`），不在项目根目录标准位置。已两次 WARNING 要求迁移，未修复。

### 2. 🖥️ 基础设施快照
- 服务器：`bjb1-17606`，代码根目录 `/root/cost-verify-agent-rl`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型：SFT checkpoint `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4`（Qwen3-1.7B）
- 框架：RAGEN + verl（`/root/cost-verify-agent-rl/RAGEN/`）
- W&B run：`y7jiibqk`（exp027）
- Ray session：`/root/autodl-tmp/tmp/ray/session_2026-05-15_22-33-13_032304_789790/`
- Ray worker log：`worker-1c0c3125f578501ad5705c524bd19adcfcd41768c1d59d6194d73f97-01000000-793046.out`
- 活跃进程：exp027_stable_grpo PID=789790（tmux），双 GPU 100% 利用率，~51GB/98GB 显存

### 3. 📊 当前状态
**刚完成**：联合审查 worker_research_gigpo_feasibility + worker_writing_method_draft，已 post 到 Director。核心发现：参考论文 GRPO baseline 72-73% vs 我们 10%，存在 62pp recipe gap，GiGPO +13pp 外推不可靠。

**exp027 进度**：Step 3 已完成（success 10.16%，KL 0.248 绿区），Step 4 rollout 进行中。Step 5 将触发首次 val eval（save_freq=5, test_freq=5）——这是 MVP 决策点。

**Registry RUNNING**：仅 exp027_stable_grpo

**待处理 worker 回调**：无积压

**等待 Director 决策**：
- GiGPO 预期要不要下调（我 WARNING 了 baseline gap）
- Method draft Self-Guide Integration 节保留还是推迟
- 非标准文件路径是否迁移

### 4. 📋 待办
- Step 4 metrics 出现在 Ray worker log → 提取 success/KL/entropy/pass@16，按 D040 三层判定框架评估，趋势对比 step 2→3→4
- Step 5 val 结果出现 → **MVP 关键决策点**：val success ≥20% → 绿灯继续 Phase B；10-20% → 建议 recipe 调整（LR/iterations 对齐参考论文）或 GiGPO；<10% → 严重警告，需要根本性 recipe 重新评估
- 新 worker_done 通知 → 按 audit checklist 审查
- Director 转发 framing 调整提案 → Read `negative-framing-review.skill.md` 后四维度审查

### 5. 🎯 战略上下文
**核心问题不是 RL 算法选择，是 recipe gap**。GiGPO 论文（Qwen2.5-1.5B）和 Self-Guide 论文（Qwen3-1.7B）的 GRPO baseline 都在 72-73%，我们同模型 exp027 仅 10%。这意味着瓶颈在 SFT checkpoint 质量 / 训练配置 / 环境设置，不在 episode-level vs step-level advantage。GiGPO 是合理的低成本改进但不是银弹。

**最容易判断错的事**：
1. 不要被 GiGPO worker 的 "+13pp" 数字误导——那是从 72.8% baseline 的增益，10% baseline 下增益未知
2. exp027 的 success 从 step 1（35.94%）暴跌到 step 2-3（10.16%），step 1 的高值可能是 SFT checkpoint 的残留表现而非真实学习。连续两步持平在 10% 更像真实水平
3. pass@16 在下降（62.5% → 50%），如果继续下降到 <50% 说明策略多样性在丧失
4. KL step 2 黄区（0.413）→ step 3 绿区（0.248）是好迹象，但 success 未随 KL 恢复而提升，说明 KL 稳定性 ≠ 学习进展
5. Method draft 写得不错但有若干"假定为事实"的假说（confirmatory verification、Self-Guide integration），审查时注意区分 hypothesis vs verified finding


---
