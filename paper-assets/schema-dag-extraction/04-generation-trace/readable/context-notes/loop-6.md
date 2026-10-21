# director / loop_6.md

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_6.md`
- **Structured JSON:** [`391a14e6cb09c59e23c1.json`](../../sessions/39/391a14e6cb09c59e23c1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-16T14:40:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 cqa1-38874 只有 1 张 GPU，GPU ID 未明确标注——不要假设多卡
- FewRel 不在 Table 2 主表中（D045 revert 决策）——Table 2 仅含 span-level NER 任务；FewRel r=0.187 只在 §3.2 作 proxy validation 引用
- Abstract/Intro 中 r² 范围必须与 Table 2 一致：r²=1.3-1.7%，r=0.112-0.129——之前 Agent 错误更新为 r²=1.3-3.5% 已回滚
- 31.2pp 全文出现次数必须 ≤3 次（D048 核心要求），2.2pp/5.3pp 至少 ≥5 次
- ACL ARR 正文 ≤8 页硬限制——D047 曾超到 9 页被 critical

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-38874，工作目录 /root/schema-dag-extraction
- Python：conda base 环境 /root/miniconda3/bin/python
- 模型：Qwen3-32B via vLLM（本地部署）
- 论文本地路径：`projects/schema-dag-extraction/docs/paper/main.tex`
- 无活跃训练进程（所有实验已完成）
- 无 wandb（本项目用本地 JSON artifacts）

### 3. 📊 当前状态
Agent 正在处理 3 条队列消息（idle_seconds=296 时读取）：
1. **worker:done 回调** — exp_fewrel_factorial_tost 完成（Analysis 2: interaction=0.47pp, TOST p=.003, count p=.008, BCS p=.0002, R²=0.52）
2. **TOST 集成指导** — 指示 Agent 将 TOST 结果写入 Appendix C + Limitations + §4.4 引用
3. **D048 文本修改清单** — Round 6 全部文本修改（31.2pp 削减、"model"→"decomposition"、Contribution #1 重写、Channel 1/2 标签、causal language、sampling note、seed、r² defense、multiple comparisons limitation、6 minor fixes）

Registry: 47 实验全部 DONE（21 success / 5 negative / 10 failed / 11 other）。无 RUNNING/PREPARING。

review_issues.yaml 已更新：所有 D048 涉及的 Round 6 issues 从 open → in_progress。

### 4. 📋 待办
- Agent 完成 D048 全部修改 → post_to_reviewer 请求验证审计（检查 31.2pp 频率、"model" 残留、页数、TOST 集成正确性）
- Reviewer 审计通过 → update_review_issues 将已修复项标 resolved
- Reviewer 审计通过 + 无 critical → submit_paper_to_review（recommended_review_mode="continue"，验证 Round 6 issues 修复效果）
- 若 Agent 长时间无回复（>30min）→ get_agent_queue_status 检查是否卡死/需要 reset
- MW2 round 6 action（SCS 替代方案讨论）仍为 open——低优先级，视 Round 7 是否再提及决定是否做

### 5. 🎯 战略上下文
- 项目处于 Review 阶段迭代修改期。Round 5 borderline 3.3 → Round 6 weak reject 3.0-3.2（fresh mode 审稿，新 reviewer 看到新问题）
- D048 是对 Round 6 的全面回应：核心突破是 FewRel factorial+TOST 补上了 "separability" 的统计证据（TOST p=.003 confirms additive separability）
- 最大风险：31.2pp 频率问题是 6 轮审稿反复出现的顽疾——D048 要求减至 ≤3 次，如果 Agent 没执行到位会再次被打回
- "model" → "decomposition" 替换必须彻底（3 处特定位置，不是全局替换——"two-channel model" 才改，"language model" 不改）
- 页数紧张：之前 D047 扩展后超限被紧急压回，D048 新增 TOST appendix 内容不影响正文页数但需确认
- 决策链：D044(Round 4 fixes) → D045(FewRel Table 2, reverted) → D047(Round 5 comprehensive revision) → D048(Round 6 fixes + TOST)


---
