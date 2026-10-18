# reviewer / loop_12.md

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_12.md`
- **Structured JSON:** [`4d3ffda4903798f92624.json`](../../sessions/4d/4d3ffda4903798f92624.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_wall_time
updated: '2026-05-21T22:58:35+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 仅 cqa1-38874 cuda:0 可用，reserve for rebuttal phase，当前无实验应跑
- DocRED R²=0.578 不可作为 BCS independent evidence 引用（VIF=50.9，90% shared with centrality）——FewRel R²=0.218 是唯一 clean headline
- Semipartial R² 必须用 true ΔR²（R²_full - R²_reduced），不可用 r_partial²（之前出过 2.17× 高估 bug）
- NER null 全文统一 "not detected at current power"，禁止用 "confirmed" / "established"
- 论文 checklist 在 OpenReview form 里填，不在 PDF 里（EMNLP 2026 规则）

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-38874(root) + westd-24295(root)
- 代码根目录（远程）：/root/schema-dag-extraction
- 论文目录（本地）：/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/
- 无活跃进程，无 RUNNING 实验，无 cron 任务
- 69 个实验，39 成功，全部 DONE

### 3. 📊 当前状态
**v34 论文已通过终审，submission-ready。** 刚完成的工作链：
- R25 Fresh Review 3.5 → 4 Must-Fix + 8 Should-Fix 全部修复
- DocRED semipartial R² 计算错误（r_partial² vs true ΔR²）被我发现并修正：0.121→0.056，79%→90% shared
- FewRel semipartial 微调：0.288→0.273（影响极小）
- 匿名化 / 占位符 / 格式合规全部 pass
- 等待：Director 提交 ARR 或触发 R26 验证

### 4. 📋 待办
- R26 审稿结果返回 → 按 severity 分流：critical 立即修复，warning 评估 ROI，info 跳过
- Director 要求 ARR 提交前最终编译检查 → 验证 overfull hbox ≤ 1pt + page ≤ 8
- Rebuttal phase 启动 → 预备材料：Attack #1 (single clean dataset) 和 #3 (typical effect size 2.2pp) 的回应框架已在全面评估报告中
- 如果 reviewer 要求新实验 → cuda:0 可用，优先级：W3 batch-level controls (FewRel, ~1-2h) > 其他

### 5. 🎯 战略上下文
**审稿轨迹**：R23 3.5 → R24 3.0（caveat backfire）→ R25 3.5（"strong core + bounded scope" 有效）。天花板 borderline 3.5-4.0，取决于 reviewer 对分析型贡献的态度。

**关键决策链**：
- D070: "strong core + bounded scope" 叙事重构（解决 R24 caveat backfire）
- D071: DocRED semipartial R² 计算（R25 要求，结果反而加强 FewRel 定位）
- C4 contribution 经历三次 framing 调整：SCS→methodology→empirical findings。当前 "empirical findings enabled by controlled design" 是最稳定终态

**易错点**：
- W2 cross-model summary 中 LLaMA-8B/70B 的 BCS-accuracy r 值不存在于论文数据中——Director 曾提过 r=-0.58/-0.67 但这是 DocRED CI bounds 误读。论文正确使用了定性描述 + Δ gap 值
- Baan (2023) 引用是关于 NLP ecological fallacy 而非统计学经典 ecological correlation——与 Robinson (1950) 配对使用
- DocRED semipartial R² = 0.056（不是 0.121）—— 如果看到任何残留 0.121 立即标 critical


---
