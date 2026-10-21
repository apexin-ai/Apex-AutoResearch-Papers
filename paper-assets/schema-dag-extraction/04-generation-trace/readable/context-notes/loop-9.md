# director / loop_9.md

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_9.md`
- **Structured JSON:** [`e4c1c76de34b607827aa.json`](../../sessions/e4/e4c1c76de34b607827aa.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_messages
updated: '2026-05-21T06:26:51+00:00'
---

### 1. 🔴 硬约束 / 红线
- 论文使用官方 ACL 模板，`acl_natbib.bst` 必须与 GitHub master 保持 byte-identical（MD5: 3d1af46d62cc9172ef6e42b56c1cd613），禁止修改 bst 文件
- EMNLP 2026 严格 8 页主文限制（Limitations/references 不计），Conclusion 必须在第 8 页内结束
- 本项目无 GPU 分配（纯分析论文，实验已全部完成），不要申请/分配 GPU
- anonymous repo URL 已移除（返回 403），footnote 改为 "Code and data will be released upon acceptance."，不要再加匿名链接

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-38874（SSH host），实验代码目录 `/root/schema-dag-extraction/`
- 本地论文目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/`
- 产出目录：`projects/schema-dag-extraction/artifacts/`
- 无活跃进程、无 tmux session、无 cron 任务
- 68 个实验全部完成（33 成功 / 9 阴性 / 10 失败 + 工程类）

### 3. 📊 当前状态
v23 论文已完成并上传用户，处理了程正翔 7 条审稿建议：
1. §3.4 补充 RE none evaluation 定义（gold 始终在 candidate set，in-schema acc ≡ original acc）
2. Limitations 移除所有具体数字，改为定性描述 + Appendix 引用
3. Practical implications 区分 typical（2-4pp）vs extreme（25-31pp）效果
4. References "and 1 others" 修复（Gemini → Gemini Team，Llama → 10 authors 无 `and others`）
5. Checklist A2: N/A → Yes（SCS/BCS 误用风险声明）
6. 因果措辞全文收紧（confusability-driven → confusability-associated）

**刚提交 C 群审稿**（apr_20260521T062559_5s7u），推荐 fresh review，等用户在审批卡确认。
无 RUNNING/PREPARING 实验。无等待中的 Worker 回调。

### 4. 📋 待办
- 用户确认审稿模式 → C 群 Review Director 接手审稿流程
- C 群审稿报告返回 → 按 review-report-action skill 逐条处理，派 Agent 修改
- 用户确认最终版 → 提交 ARR（DDL 2026-05-25）
- 如用户提出额外修改 → 重置 Agent 后执行

### 5. 🎯 战略上下文
- 论文定位：**分析型论文**（非方法论文），核心贡献是隔离 count 和 confusability 两个维度对 LLM IE 的影响
- 核心发现：BCS 预测 RE（R²=22-58%）但 NER 无信号（结构性任务不对称），SDGD 分解失败（merge amplification + routing failure）
- RE none evaluation 是用户认为最关键的点——代码验证证实 gold 始终在 candidate set 中，count-curve 解释基础稳固，rebuttal TP14 已准备
- rebuttal_talking_points.md 已更新至 14 条，rebuttal_response_template.md 覆盖 13 条
- 易错点：不要把 Reviewer 之前签字的"GPU marginal value=0"当成永久结论——那是 v22 之前的判断，如果审稿报告指出新的实验需求需重新评估
- 易错点：编译后必须 pdf_to_images 验证页面布局（Conclusion 结束位置对 8 页限制极敏感，差 1 行就溢出）


---
