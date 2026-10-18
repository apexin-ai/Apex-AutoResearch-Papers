# reviewer / loop_7.md

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_7.md`
- **Structured JSON:** [`cd7636a0d25965db2a5b.json`](../../sessions/cd/cd7636a0d25965db2a5b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_wall_time
updated: '2026-05-16T14:28:20+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 cqa1-38874，项目无 GPU 白名单限制（纯 CPU 分析 + vLLM 推理已全部完成）
- 论文数字必须与 registry 交叉验证——之前发现 §5 sdgd_zero F1 混用了 v1/v2 值（0.241 vs 0.251），已修正
- BCS 定义已统一为 MEAN pairwise SCS（D038/D039），不得回退到 MAX
- 因果语言禁令：所有 "drives"/"causes" 已替换为 "predicts"/"associated with"，不得重新引入
- 31.2pp 是 extreme-batch methodological upper bound，不是 typical effect——论文 headline 数字是 2.2pp（typical）和 −5.3pp（quartile）

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-38874 (root)，工作目录 /root/schema-dag-extraction
- Python：/root/miniconda3/bin/python（conda base）
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/
- 论文 tex 文件：{workspace}/docs/paper/（main.tex, results.tex, sdgd_negative.tex, discussion.tex, introduction.tex, abstract.tex, experimental_setup.tex, related_work.tex, checklist.tex）
- 关键远程 artifacts：/root/schema-dag-extraction/artifacts/（fewrel_formal/, fewrel_40rel_r4/, fewrel_16rel_bootstrap/, fewrel_80pool_16sub/, fewrel_factorial_tost/）
- 无活跃进程，无 tmux session，无 cron 任务——全部实验已完成

### 3. 📊 当前状态
刚完成 FewRel factorial + TOST 实验审查并提交报告给 Director。核心发现：
- Worker 跑了三重分析，仅 Analysis 2（回归 TOST, p=.003）确认 additive separability，另两个 ANOVA 功效不足 TOST inconclusive
- Worker overclaim "三重分析均支持"，我已标 WARNING 并建议仅以 Analysis 2 为主体
- 论文文件未被 worker 修改（最后修改时间均为 May 16 13:xx），registry 未注册新实验

Registry PREPARING 状态（均已有 metrics，只是未转 DONE）：exp_aggregation_monte_carlo, exp_scs_name_def_ablation, exp_fewrel_contamination_check, exp_cross_embedding_sensitivity, exp_fewrel_v2_n25, bcs_max_to_mean_fix, exp017_gpt4o_mini_fewrel (killed)

等待中：Director 对 Round 6 action matrix 的后续决策（D048），特别是：
- W2: 31.2pp 出现次数从 9→4 的编辑
- W3: "model"→"decomposition" 术语修改
- Appendix C 重写（集成 factorial TOST 结果）
- Should-Fix items (W5-W10)

### 4. 📋 待办
- Director 派 worker 集成 factorial TOST → 审查 Appendix C 重写是否正确引用 Analysis 2 数据（interaction=0.47pp, TOST p=.003, R²=0.52）；检查 Limitations item 3 是否更新；确认 ±3pp margin 有 justification
- 31.2pp 削减 worker 完成 → 核对剩余出现次数（目标 ≤4 次 main body）；确认 headline 数字仍以 2.2pp/−5.3pp 为主
- "model"→"decomposition" worker 完成 → grep 全文确认无遗漏 overclaim
- 任何新的 tex 修改 → 检查页数仍 ≤8 页（Conclusion 须在第 8 页内结束，之前 line 694 确认）
- 如收到 Round 7 审稿报告 → 独立评估并提交策略建议

### 5. 🎯 战略上下文
**核心结论链**：D005 MVP PASS → D012/D013 pairwise 升主证据 → D019 SDGD 降为 negative → D031 跨模型强复现 → D043 oracle routing +1.4pp n.s. → D044 framing 全面降调 → D047 Round 5 大修 → D048 Round 6 factorial + TOST

**论文定位**：分析型论文（诊断 schema-induced degradation），非方法型。两通道 separability 是核心 claim，decomposition 是 negative/inconclusive result 诚实报告。投 EMNLP 2026 ARR May 25 Main track。

**易错点**：
1. Analysis 1（2×2 ANOVA）BCS 不显著——不要把这当成"BCS 无效"的证据，是 power 不足。但也不能忽略它
2. Analysis 3 interaction p=.098 是 borderline——如果审稿人追问"cross-pool interaction"，需要准备好回应（BCS 范围差异导致效应量不同，非真正交互）
3. 论文中 FewRel pairwise r=0.187 在 §3.2 但不在 Table 2（D046 决定保留这个张力 + caption 交叉引用），不要试图"修复"
4. MAVEN 正向 BCS-F1 相关是 centrality confound（D012），不是 Channel 2 失败——pairwise SCS 在 MAVEN 上仍显著（r=0.129）


---
