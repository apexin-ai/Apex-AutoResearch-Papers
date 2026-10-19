# director / loop_2.md

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`10ca9abf67d3aa0ab1c5.json`](../../sessions/10/10ca9abf67d3aa0ab1c5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-17T17:07:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 autodl-rtx6000 的 cuda:0, cuda:1（项目独占，但当前全空闲——所有实验已完成）
- paper_framing.md 是论文数据的权威源，Paper Agent 必须以此为准，不能从旧 writing_plan.yaml meta 段取数字（writing_plan.yaml 的 meta.core_claim 仍是旧 framing "modality matters little"，未更新）
- OT-7B precision 差值用 +21.9pp（bootstrap mean, artifact 为准），不是 +21.2pp（point estimate）。这个数字已在 paper_framing.md 和 Holm-Bonf summary 表中统一修正
- R1-8B FPR Holm-Bonferroni 是 ✅（rank 12, threshold=0.0500, p=0.044），不是 ❌。详情段已修正

### 2. 🖥️ 基础设施快照
- 服务器：autodl-rtx6000，2× RTX 6000
- 远程工作目录：通过 `load_project_config("contrastive_trace_safety", section="execution")` 获取
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/`
- 论文目录：`docs/paper/` (main.tex + sections/*.tex)
- Artifacts：`artifacts/` (实验结果、dream reports、review reports)
- Registry：32 个实验（15 success / 17 negative / 0 failed），全部 DONE
- 活跃进程：无 RUNNING 实验，无活跃 cron（GPU 全空闲）
- Paper Agent session 活跃：`paper_agent` key，queue depth ~5（正在处理积压的 patch 指令）

### 3. 📊 当前状态
**Paper Agent Reframe 执行中**（D032: 12/12 Holm-Bonferroni + layer selection sensitivity）。

已完成章节（Reviewer 审查通过 + patch 派发）：
- Method: PASS w/ 5 warnings（permutation→bootstrap, K=1→K=5, RepE label — patches 已派）
- Experiments: PASS w/ 5 warnings（RepE pending→实际数据, OT-7B 数字, temporal>modality claim 方向修正, cross-transfer 数字统一 — patches 已派）
- Introduction: PASS w/ 2 warnings（"commonly used" 归因, RepE claim 过强 — patches 已派）
- Related Work: PASS w/ 2 warnings（3 missing bib entries, RepE claim — patches 已派）
- Discussion: PASS w/ 1 warning（main.tex 不包含 discussion.tex — patch 已派）
- Limitations: PASS w/ 3 warnings（oracle gap 出处, 恢复 correlation≠causation, 25% 措辞 — patches 已派）
- Conclusion: PASS（数据一致，主线断裂已解决）

**CRITICAL 已解决**：Abstract/Conclusion/Limitations 的 Story B（5/12 HB, "32B 不显著"）vs Introduction/Experiments 的 Story A（12/12 HB）主线断裂——Conclusion 已全面重写，Abstract+Limitations 重写 patch 在 Paper Agent 队列中。

**Paper Agent 队列深度 ~5**：积压 patches 包括 Experiments 修复、Discussion 结构修复（main.tex 需加 `\input{sections/discussion}`）、Limitations 修复、bib entries、RepE 数据更新。

### 4. 📋 待办（条件触发式）
- Paper Agent 处理完所有 patches → 检查 main.tex 编译结构：确认 `\input{sections/discussion}` 在 `\input{sections/conclusion}` 前
- Abstract 重写完成（从 Paper Agent 回报）→ 验证 12/12 HB, layer selection as primary, 无 "5/12" 残留
- 全部章节 patch 完成 → `submit_paper_to_review` 提交完整论文给 Review Director 做最终审查
- Review Director 返回审稿报告 → 按 `review-report-action` skill 处理（先 Holistic Pass 再逐条 Action Matrix）
- 引用验证：提交前用 `reference-audit` skill 检查 bib 真实性（Reviewer 建议）
- Oracle Gap 决策：已指示 Paper Agent 放入 Appendix，确认 sec:oracle label 存在且 Discussion/Limitations 的 \cref 指向正确

### 5. 🎯 战略上下文
**项目核心结论（D028→D032 决策链）**：
- D028: `bal_acc × crossing_rate` metric 有 mechanistic bias（crossing_rate 在浅层更高）
- D029: Scale-dependent claim 证伪——HS 优势在 4/4 模型存在，被 layer selection 掩盖
- D030: paper_framing.md 全面重写（scale-dependent → universal + layer selection）
- D031: Reviewer 打回 "universal" overclaim，降级为 qualified + layer selection 升为 primary
- D032: 12/12 Holm-Bonferroni 全部通过，precision +15-24pp 跨 4 模型一致

**易错点**：
- writing_plan.yaml 的 meta 段（core_claim, 各种 constraints）仍是旧 framing（"modality matters little", "3 models"），**不要从这里取叙事方向**。权威源是 paper_framing.md
- Cross-transfer best accuracy：PCA best=59.5%, direct best=67.3%（qwq→r1_32b, 但 crossing_rate=1%）。论文两处报告不同数字的问题 patch 已派但需验证修复
- main.tex 结构：当前只 include conclusion.tex 不 include discussion.tex，patch 已派但是最关键的编译修复
- RepE 不是 "unsupervised"——需要 CP 标签计算 mean difference，标注为 "direction-based supervised"
- CCS 不是 "unsupervised"——需要 CP 标签构建 pair，标注为 "weakly supervised / semi-supervised"
- DDL: EMNLP 2026 ARR May 25（~7-8 天），时间充裕但需要完成 Paper Agent patches + final review cycle


---
