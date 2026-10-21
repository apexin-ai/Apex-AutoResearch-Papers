# reviewer / loop_7.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_7.md`
- **Structured JSON:** [`8a37d6388c1825207ac0.json`](../../sessions/8a/8a37d6388c1825207ac0.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_wall_time
updated: '2026-05-15T15:25:40+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：autodl-5090 的 cuda:0/1/2/3 均可用（execution.gpu_ids 未限制，但当前无 GPU 实验需求）
- Registry 中 3 个实验已添加 `rho_note` 修正（exp_001_n16_seed456, exp_017_llama_conll_n16_r1024, exp_017_llama_conll_n16_s456_r1024），其余 ~80 个实验的 ρ 值仍为旧管道数据——**不要引用未修正实验的 CoNLL FK ρ（如 0.81）作为论文数据**，必须用 `analysis_unified_rho_full.json` 的值
- 论文数字来源必须是统一管道 JSON（`output/analysis_unified_rho_full.json`，12 个配置），不是 registry metrics（registry 大部分未批量更新）
- SciERC gold-empty=22/551，CoNLL gold-empty=697/3453——所有 ρ 计算必须排除 gold-empty 实例

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090(root)，工作目录 `/root/autodl-tmp/struct_self_consist_ie`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型：`checkpoints/qwen3-8b-scierc-merged-v2`、`checkpoints/llama3.1-8b-conll2003-merged`
- 数据：`data/scierc/processed_data`（551 inst）、`data/conll2003`（3453 inst）
- 论文 LaTeX：本地 `docs/paper/`（main.tex + sections/）
- 统一管道数据：`output/analysis_unified_rho_full.json`（12 配置，所有 sanity check pass）
- 活跃进程：无。4× RTX 5090 全部空闲（纯写作/审稿阶段）
- 无活跃 tmux/cron

### 3. 📊 当前状态
**刚收到 Director 的 Round 8 Action Matrix 审查请求**（R1=3.5/5, R2=2.5/5, overall borderline），我已读完论文全文 LaTeX + paper_framing.md + decisions D001-D083，正在撰写独立审查意见。**尚未发出 reviewer_post_to_director**。

Registry: 83 实验全部 DONE（46 success, 20 negative, 16 killed, 1 failed），无 RUNNING。
等待中：无 worker 回调。Director 等我的 Round 8 action matrix 审查意见。

### 4. 📋 待办
- **立即**：完成 Round 8 action matrix 审查并发 `reviewer_post_to_director`。Director 请求审查 4 方面：(1) 方案可行性（10 天 DDL），(2) 遗漏检查，(3) 优先级排序，(4) 技术判断（3 个分歧点）。我已读完所有材料，核心判断如下供下一个"我"直接使用：
  - **页数压缩 10-11→8**：提案可能只砍 ~2 页，如果实际 11 页需要砍 3 页则不够，需追加压缩 Method 或合并 tables
  - **ε=0.05 循环论证**：连续度量（Spearman ρ(LP_range, F1_range)=0.467）替代方案足够，但必须前置连续指标、CDF 降为辅助说明
  - **LP T=0.7**：纯写作修复可接受（free-form ablation std ratio 0.97 已证明 compression 是 intrinsic），但论证链要紧凑
  - **标题 "Struggle to Select"**：可接受但偏弱，"Do Not" 更匹配数据（p=0.39）；CoNLL N=16 有 +0.28pp 显著但极小的 gain 使 "Do Not" 略过强，"Struggle" 是合理折中
  - **R3-W2 分歧**：同意 Director 站 R1（definitional vs empirical 拆分已在 intro L23 和 discussion L9 明确声明），但需验证 experiments section 是否仍把 4/5 定义性失败当实证发现呈现
  - **遗漏**：AUROC 在 CoNLL 使用 median F1=1.0 阈值的局限性未在论文讨论；gold-empty 修正的透明度（论文是否解释了统一管道）
- Paper Agent 提交章节写作审查 → 按 §5 checklist 做对抗审查（重点检查 SYSTEMIC #1 的 scope 限定是否到位）
- Round 8 修复完成后 → 检查 tab:robustness appendix 的 CoNLL N=16 数字是否用统一管道值（之前发现需 +0.012 更新）

### 5. 🎯 战略上下文
- **核心结论**：5 类置信信号在 IE 中能预测质量（ρ≤0.45, AUROC≤0.82）但不能选择更好输出（correlation-selection gap）。Free-form ablation 证明这是 model/task intrinsic 而非 constrained decoding artifact（D072）。
- **决策链关键节点**：D072（universal gap framing）→ D075（Cannot→Do Not）→ D076（Round 7 strategy）→ D080（ρ 统一管道，消除 CoNLL FK 虚高 0.81→0.48）→ D083（N=8 缺口不补）
- **最容易判断错的事**：
  1. 不要把 registry 的 ρ 值当论文 ground truth——registry 大部分未更新，只有 `analysis_unified_rho_full.json` 可信
  2. 论文有两套 greedy F1：micro（registry, ~0.662）vs macro（selection analysis, ~0.618），同表内必须口径统一（D081）
  3. SYSTEMIC #1（Claim-Evidence Scope Mismatch）是从 Round 3 追踪到 Round 7 的顽固问题，Paper Agent 声称已修复但我尚未独立验证论文文本——这是下一个"我"最重要的验证任务
  4. R2 给 2.5/5 是最大风险——如果 R2 的核心关切（tautological framing）未被充分回应，整体评分不会上升


---
