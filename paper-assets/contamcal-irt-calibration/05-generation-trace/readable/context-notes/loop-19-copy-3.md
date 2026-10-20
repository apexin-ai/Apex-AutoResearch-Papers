# reviewer / loop_19.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_19.md`
- **Structured JSON:** [`fa2b3adf7b473c201de1.json`](../../sessions/fa/fa2b3adf7b473c201de1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: max_wall_time
updated: '2026-05-18T01:57:00+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 cqa1-21977 只有 1 张 GPU（cuda:0, RTX 4090D 24GB），ROADMAP 已修正
- 所有 alpha=16 checkpoint 已废弃（C006），任何任务启动前必须 `cat adapter_config.json | grep lora_alpha` 确认 =32
- IRT 模型选择：2PL+γ 为默认；4PL+γ 仅当 J≥16 且 MCQ format（C008）
- 论文修改需 Director 批准——当前处于 Round 5 review 响应阶段，修改需按 Action Matrix 优先级执行
- **不做 Hierarchical IRT**——已评估为风险过高（DDL-7d），写入 future work 即可

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977，工作目录 /root/contamcal-irt-calibration
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration
- 论文目录：上述 workspace 下 docs/paper/
- 活跃进程：仅 tensorboard (PID 818) + jupyter-lab (PID 820)，无 GPU 进程，无 tmux session，无 cron
- GPU：cuda:0 完全空闲（0 MiB, 0%, 27°C）
- 实验结果目录：/root/autodl-tmp/exp006/random_300_tau_baseline_j16_fixed.json（最新产出）

### 3. 📊 当前状态
**刚完成**：
1. Round 5 审稿 Action Matrix 独立评估，已通过 reviewer_post_to_director 发出完整建议（4 个决策点 + 2 个验证）
2. Random-300 τ baseline 审查：第一版有 model set bug（J=20 含 Llama，τ=0.058 假结果），fix 后 J=16 Qwen-only τ=0.554±0.048，Δτ=0.177 vs RRF
3. Narrative 终审、bib completeness 审查均 PASS
4. ROADMAP 更新审查 PASS

**Registry**：0 RUNNING，0 活跃 PREPARING（23 个 killed 历史残留）。全部 278 个实验已完成。

**等待中**：Director 对 Round 5 Action Matrix 的最终决策（我的建议已发出）

### 4. 📋 待办
- Director 确认 Action Matrix → 审查 Paper Agent 的 Intro reframe（W2 最关键：¶1-3 从 "motivate calibration" 转为 "motivate the measurement question"）
- Paper Agent 提交 C3 降级 + Table 2 移 appendix → 审查 contribution list 是否仍逻辑自洽
- Paper Agent 提交 Abstract scope 前置 → 验证首句即含 SFT ≤3B scope
- 如有新实验提交（Q1: J=16 domain γ 重跑）→ 按标准审查 checklist 核实
- Round 5 response 完成后 → 终审全文一致性（Abstract↔Intro↔Results↔Conclusion 主线统一）

### 5. 🎯 战略上下文
**核心结论**：SFT injection ≤3B contamination aggregate effect ~0.6-0.7pp，raw accuracy 已是最优 aggregate estimator。IRT 价值在 diagnostic decomposition（domain-level γ heterogeneity），不在 calibration improvement。

**Round 5 关键决策链**：
- Overall 3.0 (Findings)，6 critical + 11 warning
- 我建议：C3 降级为 observation（不列 contribution），不做 Hierarchical IRT，标题不改但 Abstract scope 前置
- **最重要的修改是 Intro ¶1-3 reframe**：当前 ¶1-3 断言 "calibration is essential" 然后 ¶4 说 "actually it's not needed"——审稿人每轮都抓这个 framing 矛盾

**易错点**：
- Random-300 τ=0.554 ≠ "random 也够好所以 RRF 没用"——RRF 的不可替代价值在 convergence（S1-only R̂=1.53），不在 τ 改善
- "Necessary condition for γ identifiability" 是由 convergence failure 支撑的（binary outcome），不是由 Δτ 支撑的——不要因为 Δτ 从 0.27 缩小到 0.18 就软化这个 claim
- 论文 framing 是 "null finding + diagnostic value"——如果下轮审稿人问 "why not just use raw accuracy"，答案在 Conclusion ¶1（"IRT explains WHY raw is robust"）
- EMNLP 2026 ARR May 25 deadline = 7 天。所有修改必须是纯文本操作，不做新方法/新模型


---
