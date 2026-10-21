# reviewer / loop_2.md

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`621ac37aa745710a8905.json`](../../sessions/62/621ac37aa745710a8905.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-17T17:07:18+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0, cuda:1（autodl-rtx6000，2× RTX 6000）。当前无活跃训练进程，但 Paper Agent 可能触发图表渲染。
- 论文 framing 已锁定 D032：12/12 Holm-Bonferroni at corrected deep layers。任何章节如果出现 "5/12 HB"、"scale as primary moderator"、"absent at 32B" 都是过时的 Story B，必须 CRITICAL 打回。
- RepE "cannot decode" claim 过强：QwQ L60 RepE bal_acc=0.756，不能说 "cannot decode"。需改为 "inconsistent" 或 "model-dependent"。

### 2. 🖥️ 基础设施快照
- 服务器：autodl-rtx6000(root)，代码根目录 /root/autodl-tmp/contrastive_trace_safety
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety
- 论文目录：{workspace}/docs/paper/（main.tex + sections/*.tex + references.bib）
- Registry：32 experiments, 15 success, 17 negative, 0 failed, 全部 DONE
- 无活跃训练进程，GPU 空闲

### 3. 📊 当前状态
**已审查完成的章节**（全部已 post to Director）：
- Method: 5 warnings（permutation→bootstrap、K=1→K=5、RepE label）
- Experiments: 5 warnings（RepE "pending"、OT-7B 数字、cross-transfer 数字）
- Introduction: 2 warnings（"commonly used" 无出处、RepE claim 过强）
- Related Work: 2 warnings（3 missing bib entries、RepE claim 过强）
- Discussion: PASS with structural warning（main.tex 未包含 discussion.tex）
- Limitations: PASS with 2 warnings（missing "correlation not causation"、oracle gap 无出处）
- Conclusion: PASS（D032 对齐 ✓）

**未审查**：Abstract（旧版仍用 Story B："5/12 HB, at 32B no significant difference"，已在综合审查中标 CRITICAL 但未收到更新通知）

**关键待处理**：
- main.tex 结构未更新：需加入 `\input{sections/discussion}`
- Abstract 仍为旧版（11:25 未动），与 Introduction/Experiments/Conclusion 矛盾
- 3 个 missing bib entries: tenney2019bert, belinkov2022probing, burns2023discovering
- Appendix 多处使用 biased-layer 数据（control task at L2/L10、layer sweep、cross-transfer "best 58.3%" vs appendix 自己说的 67.3%）
- sec:oracle 在 experiments.tex 中不存在但被 discussion.tex 和 limitations.tex 引用
- RepE "pending" 仍未修复（实验早已完成）

### 4. 📋 待办
- Abstract 更新通知 → 立即审查，核对是否改为 12/12 HB + corrected-layer 数据
- main.tex 结构更新通知 → 确认 discussion.tex 被包含
- Appendix 更新通知 → 核对 control task 是否使用 corrected layers（L60/L63）、cross-transfer best 是否改为 67.3%
- Experiments patch 通知 → 核对 RepE "pending" 是否移除、OT-7B 数字是否统一（+10.7/+21.9 vs +10.9/+21.2）
- 全文编译完成 → 触发 paper-visual-review skill 检查 PDF
- 全部章节更新完毕 → 进入 Reviewer 对抗循环（审查模式 B 迭代评分）
- 引用审计：提交前用 reference-audit skill 验证所有 bib entry 真实性（arXiv ID 核实）

### 5. 🎯 战略上下文
- **项目核心结论**：Layer selection metric bias (crossing rate) 是 HS probe 研究中的隐性 researcher degree of freedom，可以 reverse conclusions。Corrected deep layers → 12/12 HB, HS precision +15.4 to +23.6pp。
- **决策链**：D028（layer bias 发现）→ D031（initial framing）→ D032（12/12 HB reframe，primary=layer selection sensitivity）
- **最容易判断错的事**：
  1. discussion.tex vs conclusion.tex 混淆——main.tex 包含的是 conclusion.tex，discussion.tex 是 Paper Agent 新写的但需要手动加入 main.tex
  2. 论文里有两套数字体系（biased-layer Story B vs corrected-layer Story A），Abstract + Appendix 部分内容仍是 Story B
  3. OT-7B 有 point estimate (+21.2pp) vs bootstrap mean (+21.9pp) 差异，Table 2 用前者、Appendix 用后者，两者都"正确"但口径不一致
  4. Cross-transfer best: Experiments Table 说 58.3%，Appendix 正文说 67.3%（qwq→r1_32b direct），registry 也有 67.3%——58.3% 是旧数据


---
