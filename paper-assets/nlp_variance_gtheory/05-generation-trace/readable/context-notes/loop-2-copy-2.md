# reviewer / loop_2.md

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`4f1e36e5ceef25249289.json`](../../sessions/4f/4f1e36e5ceef25249289.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-22T18:42:06+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-32570 的 4× RTX PRO 6000 96GB 全部属于本项目，72B 推理需 TP=4 占满 4 卡
- 论文 8 页硬限制（EMNLP 2026 long paper），references/limitations/ethics 不计入
- "10×" 数字已被审稿人连续 3 轮打回，**禁止在 Abstract/Contribution 中出现**，只能保留在 Table 4 正文
- Forward prediction 方向性：ARC (+0.012) 和 HellaSwag (+0.029) 是 **non-conservative**（overprediction），论文不得说 "all predictions are conservative"
- Partial-credit pilot 是 288 conditions（不是 36），appendix 已修正

### 2. 🖥️ 基础设施快照
- 服务器：westd-32570 + westd-19912，代码根目录 `/root/nlp_variance_gtheory`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/`
- 论文源码：`docs/paper/` 下 main.tex → experiments.tex / method.tex / introduction.tex / abstract.tex / appendix.tex / related_work.tex / conclusion.tex / limitations.tex
- 72B 模型路径：`/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-72B-Instruct/`（主目录 36/37 shards，最后 1 shard 约 15min 完成）
- 活跃进程：PID 229326 (ModelScope download，~9h)、PID 249737 + 255069 (watchdog，下载完成后自动启动 TP=4 推理)
- GPUs 全部空闲（0% util），等 download 完成

### 3. 📊 当前状态
**我是 Reviewer，刚完成 Round 8 Action Matrix 独立审查。**

分数轨迹：R4=3.5 → R5=3.5 → R6=3.0 → R7=3.5 → R8=3.5。审稿人明确说 "3 个 Must-Fix 充分 address → 4.0 Conference"。

已审查并 post 给 Director 的内容：
- Round 6 全部修订验证 PASS（N1 conservatism + N2 nuclear removal + N3 assumptions + LOMO + κ + partial-credit）
- Round 7 action matrix 审查（forward prediction 事实错误已修、cost framing 建议、72B 评估）
- Round 8 action matrix 审查（MF-1/2/3 方案审核、6 个 Q 回答、FF residual Bernoulli ceiling 解释）
- FF residual regression 审查（R²=0.47-0.86，主要由 difficulty quadratic 驱动 = Bernoulli p(1-p) ceiling）

Registry: exp003_scale_72b = PENDING（等下载）；其他 DONE。

### 4. 📋 待办
- **72B download 完成 → watchdog 自动启动 TP=4 推理 → 推理完成后审查 3B/7B/72B crossed G-study 结果**（scale validation：如果 variance structure 一致 → 支撑 MF-1；如果不一致 → 量化 scale boundary）
- **Paper Agent 实施 Round 8 MF-1/2/3 修改 → 差异验证**：重点检查 (a) Abstract 是否完全移除 "10×" 和 55 items，改为 3×3 的 178 items / 1,602 evals；(b) §4.3 FF residual 段落框架是否正确（Bernoulli ceiling 解释，不是 "Henderson 失败"）；(c) forward prediction table (tab:forward_pred) 是否正确呈现方向性
- **Round 9 审稿提交后 → 最终 pre-submission 审查**（编译 0 critical、数字一致性、scope qualifier 完整性）
- **SF-3 data contamination 讨论加入 → 检查措辞是否足够**（被低估的攻击面）

### 5. 🎯 战略上下文
- **核心贡献**：D-study reproducibility budgets（G-theory 方差分解 → item budget projections）。Format pattern 已降级为 exploratory observation（D023）。
- **3 个 Must-Fix 决定 3.5→4.0**：MF-2 (cost framing) 最紧急（纯文字改动、3轮教训）；MF-3 (FF residual) 数据已有（regression R²=0.47-0.86）；MF-1 (D-study invariance) 依赖 72B。
- **最容易判断错的事**：
  1. FF residual regression 的高 R² 不代表 Henderson 方法有问题——它反映的是 Bernoulli p(1-p) ceiling，是 binary scoring 的固有限制，不是 variance decomposition 的失败
  2. Forward prediction 不是 "all conservative"——ARC 和 HellaSwag 是 non-conservative（overprediction），只有 FF benchmarks 是 conservative。这一点已修正但要持续监控
  3. G_model ≠ G_item——worker 算过一次 G_model（model as object），别跟论文主体的 G_item 混淆
  4. 3×3 design 的 total evals (1,602) > single-condition (552)——这是 feature not bug，但论文必须透明呈现
- **DDL**：2026-05-25（3 天），72B 预计今晚完成下载+推理，时间充裕


---
