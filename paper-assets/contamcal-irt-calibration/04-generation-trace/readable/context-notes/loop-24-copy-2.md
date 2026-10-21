# reviewer / loop_24.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_24.md`
- **Structured JSON:** [`69d8fb363c1bd71f3c93.json`](../../sessions/69/69d8fb363c1bd71f3c93.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 24
reason: max_wall_time
updated: '2026-05-23T19:49:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 `cqa1-21977`，GPU 白名单见 `execution.gpu_ids`——审查训练实验时必须核对 CUDA_VISIBLE_DEVICES 是否越界
- 论文 MDES 数值已统一为 1.25--2.05pp（之前 Intro/Conclusion 写 1.2--2.0 被我标 info，已修复）——不要再改回去
- Collapse/V-recovery 必须标 "preliminary"/"await replication"——6 处 hedging 已验证一致，任何新增文本必须延续此用词
- Table 3 ContamCal 不如 baselines（MAE 0.009 > Raw 0.006, τ 0.731 < Emperor 0.789）——这是已知弱点，防线是 "aggregate calibration is not primary goal"，不要试图改数据或重新 frame 成 ContamCal 赢了

### 2. 🖥️ 基础设施快照
- 服务器：`cqa1-21977`，远程代码根目录 `/root/contamcal-irt-calibration`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/`
- 论文源文件：`docs/paper/` 下 main.tex + 各章节 .tex + appendix.tex + references.bib
- 图表脚本：`figures/paper/gen_fig_*.py`（本地）和 `docs/paper/figures/gen_*.py`（本地）
- 活跃进程：无。实验全部完成，GPU 无分配。无 cron/tmux。

### 3. 📊 当前状态
**项目处于 Pre-submission 等待用户 OpenReview 提交（DDL 2026-05-25）。**

本轮 session 完成的审查：
1. 图表质量全面审计（6 figures 数据准确性、色板统一性、页面布局） — PASS
2. 提交前全文终审（叙事一致性、数据一致性、交叉引用、Limitations、AI 痕迹、EMNLP 格式） — 1 warning（双 "demonstrating" AI 痕迹）已修复
3. 提分空间评估 — 建议仅加 1 句 SFT 实践相关性（已完成）
4. Claim 强度 vs 证据覆盖深度审查 — 全部 contribution 无 overclaim
5. 最终 coherence 快检（Discussion 重写 + Appendix AD 新增） — PASS

Registry 无 RUNNING/PREPARING 实验。无等待中的回调。

### 4. 📋 待办（条件触发式）
- 用户完成 OpenReview 提交 → 确认提交成功，项目进入 review-waiting 阶段
- 收到 ARR 审稿意见 → 加载 `rebuttal` skill，按四维度逐条审查审稿意见合理性，提补实验清单给 Director
- Director 要求 rebuttal 期间补实验 → 加载 `ai-time-discipline` skill 评估 GPU-hours 可行性
- 如果审稿人攻击 "ContamCal 不如 baselines"（Attack #2） → 已准备好的防线："aggregate calibration is not primary goal; unique value = domain-level γ_d with credible intervals; no baseline provides this"
- 如果审稿人攻击 "SFT ≠ pretraining"（Attack #1） → Discussion 已加 balloccu2024leak 引用 + SFT 实践相关性论点

### 5. 🎯 战略上下文
- 论文核心 story：contamination 不是 uniform inflation，而是 family-specific spectrum（Immune/Benefit/Collapse/V-recovery）。2+2 framing：2 replicated + 2 preliminary。
- ContamCal 的价值不在 aggregate calibration（输给 baselines），而在 domain-level γ_d diagnosis（Social Sciences 负 / STEM 正，pooled γ 不显著）。
- 最容易判断错的事：(1) 看到 Table 3 以为 ContamCal 失败——它设计上就不追求 aggregate metrics；(2) 看到 S2-removal ablation 的 γ 符号翻转以为是 bug——根因是 ablation 脚本用了不同的 exposure 构建方式（raw RRF vs dosage-weighted）和不同的 τ 定义（kendall(dosages, calibrated) vs kendall(calibrated, ground_truth)），Appendix 已正确说明；(3) 不要混淆 J=16（文本中 τ/γ 数值）和 J=13（Figure 6 domain gamma 图），两者差 <10% 但来源不同。
- 决策链关键节点：D211 (Round 9, 3.5→优化) → D213 (Round 10, P(γ<0) 根因=模型池) → D215 (Falcon3 结果直接提交) → D219 (Volume control 45%/55%) → D220 (Round 13 framing 重写)。


---
