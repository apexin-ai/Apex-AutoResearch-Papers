# reviewer / loop_10.md

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_10.md`
- **Structured JSON:** [`51854d5e9fd174f1c59f.json`](../../sessions/51/51854d5e9fd174f1c59f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_wall_time
updated: '2026-05-17T16:27:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- exp_schema_intervention 的 Qwen3 SCS 验证（Phase 1）使用了与实验（Phase 2-3）不同的 rename map（验证用 "civic registration land"/"birthplace domain"，实验用 "nationality"/"land of origin"）。**任何基于 qwen3_scs_verification.json 的结论都不能用于解释 v2 实验结果**。
- 论文数据必须用 unified protocol（reeval_text_match.py）的 micro 值，不能用旧 set-intersection 值（LLaMA NER 旧值 count_2=0.962 已被废弃，正确值 0.323）。
- FewRel RE batch size 相等，micro≈macro 无实际差异；NER 有 1-1.2pp 差异，paper 用 micro。

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-38874(root) + westd-24295(root)
- 代码根目录：/root/schema-dag-extraction（远程）
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/
- 论文 tex：本地 docs/paper/{main.tex, introduction.tex, discussion.tex, results.tex, ...}
- 模型：/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/（cqa1）
- 数据：/root/schema-dag-extraction/data/fewrel_parquet/、Few-NERD、MAVEN
- 实验产物：/root/schema-dag-extraction/artifacts/（cqa1）
- westd 日志已备份到 cqa1：/root/schema-dag-extraction/backup_westd/
- 无活跃 GPU 进程（schema_intervention 已完成，gemini_flash dry run 已失败退出）

### 3. 📊 当前状态
**刚完成**：对 D058 双实验（schema intervention + Gemini Flash）的 critical 审查并已提交 Director。

**Registry 状态**：
- exp_schema_intervention: ALLOCATED（Agent 尚未更新为 DONE，但实验已产出结果到 artifacts/exp_schema_intervention/）
- exp_gemini_flash_cross_model: PREPARING（dry run 失败，API Connection error，0/5 正确）
- 其他近期实验全部 DONE

**等待中**：
- Director 对我的 schema_intervention critical 报告的响应/决策
- Agent 更新 registry 中 exp_schema_intervention 的 conclusion/metrics
- Round 12 论文写作修复（S1-S9）的实施和审查请求
- Round 12 paper submission（submit_paper_to_review）

### 4. 📋 待办
- Agent 更新 exp_schema_intervention registry 结论 → 核查 Agent 是否将结果 frame 为 "inconclusive"（正确）而非 "renaming hurts"（rationalization）
- Director 决定是否在论文中提及 schema intervention → 确保以 inconclusive/negative 定位，不能作为 causal evidence
- Round 12 S1-S9 写作修复提交审查 → 逐项验证：(a) Introduction Finding(1) 拆句, (b) Conclusion 扩展到 5-8 句, (c) TOST 首次出现加 qualification, (d) main.tex L502/504/508/513/531 "driven" → "related"/"associated", (e) 3 个 orphan bib 条目删除, (f) missing references 添加
- Val-only SCS-confusion 结果（ρ=0.216, p=0.018）写入论文 → 核查措辞和位置
- Gemini Flash API 恢复 → 审查实验结果（但建议不再投入时间）

### 5. 🎯 战略上下文
- **DDL**：ARR May 25, 2026（~8 天）。论文核心 claim 已有足够实验支撑（Qwen3-32B + LLaMA-70B，4 数据集 3 任务）。
- **schema intervention 是最大的坑**：实验结果方向完全相反（treatment 全面降低准确率），且存在三重方法论缺陷（rename map 不匹配、rename count 共线性 r=-0.625、solo check 功效不足）。**绝对不能 frame 为 causal evidence**。如果 Agent 试图包装为"重要发现"，这就是 rationalization（§5 negative-framing-review skill 的典型场景）。
- **前瞻评估结论**（我已提交）：D058 实验的 realistic excitement 升级上限是 2.75→3.25-3.5。没有自动化工具/方案，很难进入 Main conference（Overall ≥4.0）。Findings 接收（Overall ≥3.0）是现实目标。
- **容易判断错的事**：(1) 不要被 interaction effect p≈0 误导——统计显著不等于因果有效，rename count 共线性是致命混淆；(2) Qwen3 SCS 验证文件的数据是旧 rename map 的，与实验不对应；(3) 论文 NER 值要用 unified protocol micro，不要混淆 macro 来源的 count_curve_summary.json


---
