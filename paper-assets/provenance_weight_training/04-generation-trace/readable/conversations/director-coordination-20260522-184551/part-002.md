# Director coordination (archived snapshot) — Part 2 of 2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../director-coordination-20260522-184551.md) · [Structured JSON](../../../sessions/86/862db3a725cf645bf417.json)

## Round 133

### User

_source line 632 · 2026-05-22T18:45:07.875713+00:00_

[WRITE HANDOFF] 请立即写你的 handoff。

**格式硬约束**:
- 整条回复**只能**是 &lt;handoff>...&lt;/handoff> 标签包裹
- 禁止在标签外写任何寒暄 / 说明 / 确认（"好的"/"我开始写"/"写完了"等）

**必须覆盖以下 5 个 section（缺一不可，无内容写 N/A）**:

### 1. 🔴 硬约束 / 红线
  本项目特定的不可违反约束（GPU 设备号、服务器名、账号、路径限制等）。
  写本项目特定的，不要抄 CLAUDE.md 通用 L1 红线。
  下一个"你"第一眼看到的就是这里，写错了会被 Director CRITICAL。

### 2. 🖥️ 基础设施快照
  - 服务器名 + 工作目录 + Python 路径 + conda env
  - 模型路径 / 数据集路径 / wandb config / HF cache
  - 活跃进程：PID + tmux session + cron 任务 ID
  写一次就稳定，下一个"你"不用再 SSH 探查。

### 3. 📊 当前状态
  - 你刚做完什么 / 正在做什么
  - registry 里 RUNNING/PREPARING 的实验列表 + 一句话摘要
  - 等待中的 Worker 回调 / Cron / Director 决策

### 4. 📋 待办（条件触发式）
  格式 "条件 X 满足 → 动作 Y"。例如:
  - "Falcon-H1R 下载完成 → sed 修 MODEL_PATH → dry-run → 提交"
  - "pilot_011 出 GC4 结果 → ≥2pp 转架构 narrative，<2pp 写 null-result"

### 5. 🎯 战略上下文
  - 项目核心结论 / 决策链（D001..）
  - 下一个"你"最容易判断错的事 / 容易踩的坑

**写作原则**：
- 第 1 节必须是项目特定的（不是通用 L1 红线）
- 第 2 节让下一轮 BOOT 后能立即开工，避免重新 SSH 探查
- 简洁 > 完整：每节 5-10 行足够，长 handoff 不等于好 handoff

示例格式:
&lt;handoff>
### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:4 / cuda:5（之前两次违规 cuda:0 被 Director CRITICAL）
- submit_training_job 不支持 shell builtin（source/conda activate 全不行）

### 2. 🖥️ 基础设施快照
- 服务器：westd-8x6000，工作目录 /root/autodl-tmp/hybrid_reasoning_phases
- Python：/root/miniconda3/bin/python（绝对路径，不走 conda activate）
- 模型：/root/autodl-tmp/qwen35_4b_direct
- 活跃：pilot_011 (PID 203221, tmux=pilot_011, cuda:4)

### 3. 📊 当前状态
我刚完成 pilot_010 分析，正在等 pilot_011 (Falcon-H1R) CoT 生成完成（6/50）。
registry: pilot_011 RUNNING；其他全 DONE。

### 4. 📋 待办
- pilot_011 cron 回调 → spawn worker 跑 probe + GC4 计算
- GC4 ≥2pp → 转架构 narrative；<2pp → null-result paper outline 已就绪

### 5. 🎯 战略上下文
Falcon-H1R 是最后一个数据点。已知 4B/9B GC4 都 FAIL。
易错：不要把 GC4-par (Falcon parallel) 和 GC4-seq (Qwen sequential) 直接对比。
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_2b6c9bea33a70c93bf4bf04ac36b8df9:director",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 633 · 2026-05-22T18:45:51.066665+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-41312 cuda:0/1/2/3（4× RTX PRO 6000 96GB），不得使用其他服务器的卡
- eval 必须用 bfloat16（不是 float16）——float16 max=65504 在 wiki 数据上会 NaN overflow，这个 bug 修过一次（eval_perplexity.py:92）
- n_min/B 耦合规则：n_min 必须 ≈ B/2（B=4 → n_min=2, B=8 → n_min=4, B=16 → n_min=8）
- ρ=0.4 的统计语言：只能用 "directionally consistent" + "bootstrap CI excludes zero"，**不能**用 "significantly"（p_BH=0.078 未过 0.05）。ρ=0.6 可以用 "significant"（p_BH≤0.018）
- 所有 t/p 值必须从 Table 1 的 3dp 数值推导，确保精度一致（之前因 full-precision vs 3dp 被 Reviewer 抓过）
- EMNLP 2026：checklist 在 OpenReview 表单填，不在 PDF 里（已移除）；主文 ≤8 页

### 2. 🖥️ 基础设施快照
- 服务器：westd-41312 (root)，4× RTX PRO 6000 Blackwell 96GB
- 工作目录：/root/provenance_weight_training（远程代码/训练）
- Python：conda base 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 论文本地路径：`projects/provenance_weight_training/docs/paper/`（main.tex → main.pdf，15 页总，~7 main + appendix）
- artifacts：`projects/provenance_weight_training/artifacts/`（review_issues.yaml, alpha_eff_variance_decomposition.md, figures/, review_reports/）
- ρ=0.3 数据已生成：远程 `data/scored_data_rho03.jsonl`（235K 行，712MB）
- 活跃进程：无（Agent 刚被派去启动 ρ=0.3 训练但可能还没提交 job）

### 3. 📊 当前状态
- **Round 11 审稿**：已 `submit_paper_to_review`（apr_20260522T180015_o4tj），pending 用户审批卡片
- **ρ=0.3 防御性实验**（D120）：数据就绪，Agent 已收到指令在 cuda:0/1 启动 adaptive+uniform seed42 训练，但训练可能尚未实际启动（registry 无 RUNNING）
- **13/13 Round 10 issues resolved**：包括最后的 M3 α_eff 方差分解（定量结果已写入 §6 Discussion）
- **M3 定量结果**：未解释方差 ~70% 检测器噪声 / ~30% b* 变换设计；B=4→B=16 方差降 10.25× 但 R² 不变（0.47→0.44）
- 论文编译通过，0 critical warnings

### 4. 📋 待办
- Agent 回复 ρ=0.3 训练启动确认 → 检查 registry 状态 + GPU 分配正确性
- ρ=0.3 训练完成 → eval（holdout + OWT + Wiki, bfloat16）→ 汇报 Δ(adaptive−uniform)
- ρ=0.3 结果出来 → 如果 Δ negative（works）→ Paper Agent 加 appendix 条目 + 更新 rebuttal；如果 Δ positive（fails）→ 写入 rebuttal 作为 boundary evidence（transition 在 [0.3, 0.4]）。**不改变主文核心叙事**
- Round 11 审稿结果回来 → 按 review-report-action skill 做 Holistic Pass + Action Matrix
- review_issues.yaml M3 的 Paper Agent action 还标 in_progress → 审稿回来前改 completed

### 5. 🎯 战略上下文
- **论文定位**：Analysis paper，不是 method paper。4 个贡献：(1) epoch confound >95% (2) detector calibration+discrimination requirements (3) 4-tier mechanism decomposition (4) adaptive b* as practical corollary
- **审稿轨迹**：Round 8: 2.5 → Round 9: 3.0 → Round 10: 3.0 → Round 11: target 3.5+
- **关键决策链**：D115 reframe → D116 LR confound confirmed → D117 Round 9 action matrix → D118 Round 10 action matrix → D119 Round 11 提交 → D120 ρ=0.3 补跑
- **易错点**：
  - ρ=0.3 结果不管正负，都**不能**改主文 claim 或核心叙事——只作 appendix/rebuttal 储备，DDL 3 天不允许结构性改动
  - Reviewer 报告 simulation mean b*=0.90 vs 论文 actual training mean b*=1.4 有差异，rebuttal 中引用方差分解数据时注意区分来源
  - 效应量极小（Δ=−0.020 PPL ≈ 0.11% relative），downstream 完全 null——这是结构性弱点，不可修复，只能靠诚实讨论赢好感
  - 论文 page budget 紧张（~7 main pages），加内容必须同时砍别处
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_2b6c9bea33a70c93bf4bf04ac36b8df9:director"
}
```

</details>

---
