# reviewer / loop_8.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_8.md`
- **Structured JSON:** [`69928b4f9525d8cc5ace.json`](../../sessions/69/69928b4f9525d8cc5ace.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_wall_time
updated: '2026-05-15T14:02:05+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0, cuda:1 on westd-16980 only。其他 GPU 编号或其他服务器 → critical
- `llama_docred_full_s1_mt6144` 有变量混淆（同时改了 CF fallback 代码 + max_tokens 6144），其 CF 数据不能用于纯 CF ablation 对比。纯 CF ablation 必须控制 max_tokens=4096
- registry `exp_id` 精确过滤器不工作（返回空），必须用 `limit=0` 全量拉取后手动筛
- `ssh_read_only` 不支持管道符 `|`，需拆成多次调用
- 论文数字 "is consistent with" 不能写 "explains"（n=4 dual-factor，overclaiming 已被修正过一轮）

### 2. 🖥️ 基础设施快照
- 服务器：westd-16980(root)，工作目录 `/root/schema_semantic_constrained_ie`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型：Llama `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct`；Qwen 路径同级目录
- 数据：`data/docred/dev.json`（998 docs）、`data/scierc/`（551 samples）
- 输出：`outputs/` 目录下所有 .jsonl + violation_report_*.json
- 项目配置：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/projects/schema_semantic_constrained_ie.yaml`
- 无 W&B 配置（不检查 W&B）
- 活跃进程（截至 handoff 时）：PID 247492 = `llama_docred_full_s1_mt6144`，GPU 1，tmux session

### 3. 📊 当前状态
- 刚收到 `llama_docred_unconstrained_mt6144` 完成通知，状态 ANALYZING（Agent 正在跑 violation checker + F1）。998/998 输出已完成，但 metrics 尚未写入 registry。我验证了输出文件完整性和 GPU 合规，尚未发出审查报告（等 metrics 入 registry）
- `llama_docred_full_s1_mt6144`：RUNNING，862/998 (86.4%)，预计 1-2h 完成
- 4 个 W1 CF fallback 实验全部 PREPARING：`w1_cf_fallback_scierc_pilot`、`w1_cf_fallback_docred`、`w1_cf_fallback_llama_scierc`、`w1_cf_fallback_llama_docred`——等 GPU 空闲后启动
- 已完成的审查：Round 2 全文预审（6 维度）、Paper Agent 修复复查（4 warning fix + dual-factor appendix）、story 强度评估、两次 W1 dryrun 审查、Q8 FP paired analysis、mt6144 进度审查、ROADMAP 审查——全部 PASS/warning 级

### 4. 📋 待办
- Agent 将 `llama_docred_unconstrained_mt6144` metrics 写入 registry → 审查：与原 `llama_docred_unconstrained`(mt4096) 对比，验证 max_tokens 提升是否改善 parse failure / truncation；核实 violation rates 变化是否合理
- `llama_docred_full_s1_mt6144` 完成通知到达 → 审查：同上对比 + 注意变量混淆问题（CF fallback + mt6144 双变量），不可将 CF 改善归因于单一因素
- W1 CF fallback 实验（4个）启动 + 完成 → 核心审查任务：验证 CF 减少幅度、DR trade-off、是否支持升级论文 W1 叙事（从 TODO 变为实际数据）
- 如果 W1 fallback 效果好 → 检查 Paper Agent 是否按 main.tex 中 TODO 注释（lines 66-71）更新 Limitations 段和 §7 conclusion
- 所有 mt6144 + W1 完成后 → 论文数据一致性全量复查（新数字是否正确写入 .tex 文件）

### 5. 🎯 战略上下文
- 核心结论链：DR violations 普遍(15-18%) → prompt 不可靠 → OntoCoDec 两层约束(grammar+semantic) → SciERC DR↓94%, DocRED DR↓45-90% → 残余 DR 由 tightness×baseline_RV 双因子预测(R²=0.886, n=4)
- W1 CF violations 是论文最大未解决弱点（最高 12.02%）。W1 fallback 实验结果决定论文 Limitations 段的措辞强度——这是当前最关键的待审数据
- dual_factor_data.json 中 Qwen DocRED residual_DR_pct=10.19% vs registry 10.21%，差 0.02pp，之前已标 info 级，非阻塞
- 论文 8 页主体 + unlimited appendix (ACL ARR format)。当前 18 页总，主体刚好卡 8 页——任何新增内容都可能 spill，需警惕
- 易错点：不要把 `llama_docred_full_s1_mt6144` 的 CF 数据当作纯 CF ablation 引用——它同时改了 max_tokens，Agent 已在 registry notes 标注但容易被忘记


---
