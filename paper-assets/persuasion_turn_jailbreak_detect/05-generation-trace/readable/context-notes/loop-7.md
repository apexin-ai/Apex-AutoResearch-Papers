# reviewer / loop_7.md

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_7.md`
- **Structured JSON:** [`4777750ce8a8c43ae361.json`](../../sessions/47/4777750ce8a8c43ae361.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_wall_time
updated: '2026-05-23T20:02:14+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-33183 的 cuda:0-3（C001）。exp67 用了 cuda:0 已验证合规。
- 匿名 repo：`anonymous-nlp-2026/persuasion_turn_jailbreak_detect`。当前环境 SSH key 无写权限，push 需要用户提供 PAT 或手动操作。
- EMNLP 2026：正文严格 8 页（Limitations 不计入）；Abstract ≤200 词（当前约 180）；Ethics Statement 不放 PDF（在 OpenReview form）；一篇文章只能有一个 Limitations section 在正文。
- `\graphicspath{{../../}}`：LaTeX 从项目根 `figures/paper/` 找旧图，从 `docs/paper/figures/paper/` 找新图（fig3/fig4）。两个路径都有效但不统一。

### 2. 🖥️ 基础设施快照
- 服务器：westd-33183(root)，代码根目录 `/root/persuasion_turn_jailbreak_detect`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/`
- 论文源码：`docs/paper/`（main.tex + 各章节 .tex）
- PDF：`docs/paper/main.pdf`（26 页，含 AI disclosure section）
- 匿名 repo commit：`2eef235`（但 AI disclosure 的 push 失败，本地 `/tmp/anon_repo` 有两个未推送 commit）
- GPU：cuda:0 空闲保留应急。AutoDL / gpu-5090 已释放。
- 无活跃训练进程、无 cron、无 RUNNING 实验。

### 3. 📊 当前状态
**项目处于提交前最终修复阶段。** DDL 2026-05-25。

刚完成的工作：
- R18-R22 共 5 轮审稿全部处理完毕，评分 3.0-3.5（Findings/Borderline Conference），已决定停止审稿循环
- 3 个 pre-submission audit workers 完成：(1) appendix-consistency, (2) abstract-body-crosscheck, (3) table-registry-traceability
- RoBERTa-large seed check 完成：确认 3-seed 数据完整，Table 4 声明有效
- 匿名 repo re-push 完成（但 AI disclosure 那次 push 因权限失败）

**审计发现的 must-fix 清单（10 项文本修正，我已合并两个 audit worker 的结果发给 Director）：**
1. introduction.tex:22 "60pp" 对比基准错（vs vanilla 非 vs MLM）
2. conclusion.tex:21 "DD/AA Δ≤2.5pp" 与 -57.9pp 自相矛盾
3. abstract.tex "base scale (125M-184M)" 应为 125M-355M
4. conclusion.tex:14 MLM "F1≥0.97" 缺 "at K≤5" 限定
5. experiments.tex:217 OASST2 FPR "1.0%" 应为 1.5%
6. conclusion.tex:18 "≥40pp" 应为 "≥18pp"
7. conclusion.tex:21 "zero-padding" 应为 "benign-turn padding"
8. conclusion.tex:32 tab:main_results 引用错误 → tab:evidence_hierarchy
9. conclusion.tex:25 "10 conversations" → "10-25 conversations"
10. experiments.tex:205 / conclusion.tex:18 "All DAPT" 含 Topic → "jailbreak-domain DAPT"

Registry 全部 DONE（无 RUNNING/PREPARING）。等待 Director 派 Worker 执行上述 10 项修复。

### 4. 📋 待办
- 10 项文本修复 Worker 完成 → 验证修复正确性 + 确认无新增不一致
- S3 备份重试完成 → 确认备份成功
- AI disclosure 匿名 repo push 解决（用户提供 PAT 或手动 push）→ 确认 remote HEAD 包含 AI disclosure
- 最终 PDF 编译后 → 视觉审查确认仍为 8 页正文
- 用户提交 ARR → 无需 Reviewer 动作

### 5. 🎯 战略上下文
- 论文核心：DisPeD 两轴分解（attack-side DAPT + benign-side few-shot），13 encoder configurations 的系统消融
- 评分天花板 3.0-3.5 已确认：三个结构性限制（合成数据、ToxicChat 反转、vs Gururangan 2020 novelty）不可通过写作修复
- TOST 已用 n=10 seeds（exp41_tost_10seed），DD/FITD confirmed equivalent，AA not（d=0.44）。之前 Appendix Table 16 显示 n=3 已修正为 n=10
- **最容易判断错的事**：(1) 不要再启动审稿循环——振荡说明已到天花板；(2) Appendix full_prefix 表的 DD-Full .994 vs 主表 .997——seed-level 验证确认 .997 正确，full_prefix 表需更新但属 info 级别；(3) Table 3 Binary DD-Full 显示 1.000±.000 但 seed42 可能为 0.990（来自 plan_013 可能不同数据版本），需 Agent 确认后决定是否修正；(4) Table 3 Dual-OOD 4 个 cell 无 registry 来源——数据可能正确但未注册


---
