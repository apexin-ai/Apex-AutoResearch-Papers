# reviewer / loop_14.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_14.md`
- **Structured JSON:** [`fe3788d114bc70d356bf.json`](../../sessions/fe/fe3788d114bc70d356bf.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_messages
updated: '2026-05-17T10:44:55+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 `[0,1,2,3]`（cqa1-22115 4×4090D 24GB）。越界进程必须 `[severity: critical]` 打回 + kill
- exp-026 feature stability 数据源必须是 **prompt-chain**（K*=2）。v1 曾误用 retrain-chain（K*≥4）导致 trivially pass，已被我拦截修正为 v2
- Appendix dose-response 表格（tab_dose_response）已用 v3 数据替换。旧 v1/v2 数据全错（差 0.5-1.3pp），如果看到旧数字（no_filter 10%=0.6009 等）说明回滚了
- pp 单位：1pp = 0.01。我之前两次犯 10× 错误，报告前必须二次核验

### 2. 🖥️ 基础设施快照
- 服务器：`cqa1-22115(root)`，代码根目录 `/root/autodl-tmp/gen-depth-contamination`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/`
- 论文源文件：`docs/paper/` 下 main.tex + 各 section .tex
- 主要数据目录：`/root/autodl-tmp/gen-depth-contamination/data_exp016_qwen_base/`（prompt-chain 主数据）
- exp-009 v3 结果：`/root/autodl-tmp/gen-depth-contamination/results/exp_009_dose_response/ratio_{10,30,50}/`
- 活跃进程：无（GPU 全部空闲，所有实验完成）

### 3. 📊 当前状态
**刚完成**：实验覆盖度最终审查。35 成功 / 7 失败 / 0 method-negative。所有实验 DONE。

**论文状态**：
- D053 patch 4/4 完成（C3 "converge" → "binary retains advantage, graduated ≈ no_filter"）
- Appendix table 25 已更新 v3 数据，全部 18 个数值已验证 ✓
- Limitations (7) 已更新 ✓
- Table 6 截断问题已修复 ✓
- Figure 1 pipeline 图已修复 ✓
- 最终 PDF 已编译（artifacts/main.pdf, 10:36 UTC）
- **exp-026/027 结果尚未写入论文**——已向 Director 建议放置位置（exp-026 → Appendix + Limitations (5) 引用；exp-027 → Discussion retrain-chain 段落加 CI）

**Registry RUNNING/PREPARING**：无

### 4. 📋 待办
- Director 批准 exp-026/027 写入方案 → 验证 Paper Agent 是否正确写入数据（exp-026: 8D min=0.6056, 5D=2/5 pass; exp-027: 3v4 CI=[0.7903, 0.8051]）
- Paper Agent 提交章节审查 → 按 §5 模板做维度评分 + claim 校验
- 最终 PDF 视觉审查请求 → 用 pdf_to_images 全页检查排版
- Group C 审稿报告到达 → 按审查 checklist 逐条验证 claim 与 evidence 对应
- Director 如果要求补跑 1024-token segment length → 可在 cuda:0 跑（CPU-bound LightGBM），但我已建议不补（趋势从 128/256/512 已清晰）

### 5. 🎯 战略上下文
**核心结论**：K*∈{1,2,3}，domain-dependent bounded saturation。Web text K*=2（7/8 configs），arXiv K*=3（2 models），Mistral K*=1。Binary filtering 在全 contamination spectrum 优于 graduated（graduated ≈ no_filter 是 K*=2 的 theory-confirming 结果）。

**关键决策链**：D047（Modified Option B framing）→ D049（arXiv K*=3 升级 framing）→ D051（retrain-chain 措辞修正）→ D053（C3 dose-response framing 修正）

**易错点**：
1. C3 framing 不能说 "universally beneficial"——30% MMLU binary 优势不显著（p=0.074）。当前 "binary retains consistent advantage" 是已审定的安全措辞
2. exp-026 的 8D margin 极薄（0.6056 vs θ=0.60，仅 +0.56pp），写论文时措辞应为 "≥8 features suffice" 而非 "robustly robust"
3. MMLU binary 优势在 10%（+0.21pp）大于 30%（+0.13pp），非单调。HellaSwag 才是单调的。不要把两个指标混为一谈
4. 论文文件在本地 workspace（`docs/paper/`），不在远程服务器。之前因为只读远程误判 "worker 未改文件"


---
