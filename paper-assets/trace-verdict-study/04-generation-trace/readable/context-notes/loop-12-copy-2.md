# reviewer / loop_12.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_12.md`
- **Structured JSON:** [`3f23e492bcf3012c7afe.json`](../../sessions/3f/3f23e492bcf3012c7afe.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_wall_time
updated: '2026-05-21T21:04:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0, cuda:1（westd-11235）。cuda:0 有 49175 MiB 孤儿显存（100% utilization, 0 进程），需容器重启才能完全释放，但理论上 ~48GB 可分配
- DeepSeek VOTA seed42 (84.45%) 是已确认的 LoRA init outlier，论文中用 ‡ 标注 2-seed mean (99.25%)，脚注列全部 3 个原始值。不要误判为数据错误
- CodeLlama 在 registry 中有两套命名：`codellama_*`（旧，7B 错误命名）和 `codellama13b_*`（正确，13B）。旧命名 6 条全是 duplicate/killed，不要引用
- Table 1 已通过 20/20 数值审计，任何修改必须重新交叉验证 registry

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235 (root)，工作目录 /root/trace-verdict-study
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型路径：/root/autodl-tmp/models/Qwen2.5-Coder-7B-Instruct（及同目录下 1.5B/DeepSeek/CodeLlama）
- 数据集：/root/autodl-tmp/trace-verdict-study-data/（exception_only/ae_only/loop_only/vota/full_trace/no_trace/padded2048 等 train+test.jsonl）
- Checkpoints：/root/autodl-tmp/trace-verdict-study-checkpoints/
- 论文源码：/root/trace-verdict-study/docs/paper/（main.tex, experiments.tex, appendix.tex 等）
- W&B：project=trace-verdict-study
- 活跃进程：无（cuda:0 孤儿外全部空闲）
- 本地 artifacts：/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/

### 3. 📊 当前状态
D113 action matrix 全部完成。我刚完成以下审查：
- Round 13 holistic pass 独立评估（5 个问题全部回答，posted to Director）
- SF-1 padding 实验审查：99.83% = 原始 exception_only，SYSTEMIC_C resolved
- Q3 decomposition 分析审查：数据与 registry 一致，scale-invariant tier 结构确认
- Table 1 数值审计验证：20/20 通过，独立抽查 4 个计算
- Q1 nomarker regex：B5 崩溃 99.33%→28.49% 确认（format artifact）

Registry: 0 RUNNING, 0 ALLOCATED。166 total experiments (116 success, 21 negative, 9 failed)。
Round 14 fresh 审稿已提交，等待用户批准触发。

### 4. 📋 待办
- Round 14 审稿触发 → 按 §5 审查模式 B 逐维度审查论文（叙事一致性/claim 可信度/审稿人攻击面），必须先 Read paper-quality-lessons skill
- Paper Agent 提交章节审查 → 检查是否已读 red-section skill（L1 合规），按 §5.3 模板评分
- 如果 Round 14 要求补实验 → 验证 GPU 合规（cuda:0 孤儿是否已清理），核实实验设计
- 论文最终提交前 → 验证 paper_provenance.yaml 覆盖率，检查 evidence 引用的 exp_id 是否全部 valid

### 5. 🎯 战略上下文
- **核心叙事已 pivot**：从 "exception is strongest signal"（tautological）→ "why full traces hurt SFT learning"（mechanistic）。D113 完成了全文重构
- **最强新证据**：SF-1 padding 99.83%（排除长度混淆）+ plan_020 GPT-4o crossover（SFT+trace 碾压 frontier LLM, frontier LLM+no_trace 反超 SFT）+ training dynamics 50-step 收敛 vs 全程震荡
- **易错点**：paper_framing.md 中 "99.83% 是理论上限" 的说法已过时——CodeLlama seed123 达到 100.0%（0/1190 错误），GeneratorExit 不是 irreducible error。如果论文仍写 "irreducible"，标 warning
- **DDL**：EMNLP ARR 2026-05-25，~3 天。Round 14 反馈 → final fix → submit 是唯一剩余路径。不需要新实验，纯写作收尾
- **决策链关键节点**：D003 MVP PASS → D009 gradient dilution 26%/info overload 74% → D029 DeepSeek seed 仲裁 → D110 regex=format artifact → D113 full reframe


---
