# reviewer / loop_3.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`66755cce1932b5907f1e.json`](../../sessions/66/66755cce1932b5907f1e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-14T17:38:55+00:00'
---

### 1. 🔴 硬约束 / 红线
- 项目未配置 gpu_ids 约束，但实际分配 4 张 5090（cuda:0-3）。exp_017 曾因未指定 CUDA_VISIBLE_DEVICES 默认跑 cuda:0，已被我标 warning。**所有训练/推理命令必须显式指定 CUDA_VISIBLE_DEVICES**。
- exp_017_llama_conll 曾被 Agent 错误标记为"never started"（搜索路径太窄），我发 critical 后已修正。**审查 Agent 的"未运行/失败"结论时，必须自己 SSH 验证 checkpoints/ 和 logs/ 目录，不信 Agent 的搜索结论。**
- WNUT-17 数据 54% F1=0，logprob full rho=-0.411（强负相关），这个 benchmark 可能需要 Director 决策是否继续投入。

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090(root)，工作目录 `/root/autodl-tmp/struct_self_consist_ie`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 模型 checkpoints：`/root/autodl-tmp/struct_self_consist_ie/checkpoints/`
  - qwen3-8b-scierc-merged-v2（主力模型，SciERC）
  - qwen3-8b-wnut17-merged（WNUT-17）
  - llama3.1-8b-conll2003-merged（CoNLL2003，刚 merge）
  - llama3.1-8b-scierc-merged（SciERC Llama）
- 数据：`data/scierc/processed_data`、`data/wnut17`、`data/conll2003`
- 输出：`output/` 下按 exp_id 分目录
- W&B：未配置（report_to: none），不检查 W&B
- 活跃进程（截止 handoff）：exp_017_llama_conll_infer PID 98932 子进程（vLLM），GPU 0，~7% 进度

### 3. 📊 当前状态
我刚完成三轮审查：
1. 发现 3 个 RUNNING 实验（exp_003_wnut17_v2 训练、exp_001_seed456_v2 推理、exp_017_llama_conll 训练）全部已完成但 registry 未更新 + 4 GPU 空闲 → warning 已发
2. exp_017_llama_conll 被 Agent 误标失败 → critical 已发，Agent 已修正 registry 并启动 merge+inference
3. exp_003_wnut17_v2_infer（FAIL）和 exp_001_seed456_v2_ner（MARGINAL）结果已审查 → warning 已发

当前 registry RUNNING：
- **exp_017_llama_conll_infer**：Llama-3.1-8B CoNLL2003 推理，GPU 0，N=8，~7%，预计还需 ~7min
- **exp_001_seed456_v2_ner**：实际已完成（output 有 report.json），registry 未更新
- **exp_003_wnut17_v2**：ANALYZING，推理实际已完成，registry 未更新

等待：exp_017_llama_conll_infer 完成后 Agent 应收集结果并更新 registry。

### 4. 📋 待办
- exp_017_llama_conll_infer 完成通知到达 → 审查结果（N=8 的统计功效是否足够、structural_beats_surface 结论、与 Qwen 对比是否公平）
- Agent 更新 exp_003_wnut17_v2 和 exp_001_seed456_v2_ner 的 registry → 核实 metrics 是否与 report.json 一致
- Agent 对 3-seed NER 做一致性分析（seed42/123/456）→ 审查方差是否合理、结论是否过强
- Director 决策 WNUT-17 是否继续 → 如果继续，审查新方案（调 T？调 prompt？）；如果放弃，确认 paper narrative 是否需要调整
- 新实验铺排（队列里还有 exp_008_re_n16_full 等 8 个）→ 审查 GPU 分配和 CUDA_VISIBLE_DEVICES

### 5. 🎯 战略上下文
- 核心假设：structural consistency（Fleiss kappa / soft Jaccard）比 surface-level 信号（logprob）更能预测 LLM IE 输出质量
- SciERC 上 structural_beats_surface=true（3 seed 中至少 seed456 确认），这是论文核心 claim 的支撑
- WNUT-17 是反例（FAIL），CoNLL2003 待定（exp_017 推理中）。如果 CoNLL2003 也 FAIL，claim 范围将受限于"科学文献 NER"
- **最容易判断错的事**：Agent 声称实验"失败/未运行"时不要直接信——本轮已发生一次误判（exp_017）。永远自己 SSH 验证。
- **n_samples 不一致**：exp_017 用 N=8 而其他用 N=16，跨实验对比时必须注意这个差异，不能直接比较 rho 值。
- 项目总计 44 个实验（成功 27 / 负向 15 / 失败 1），处于 research 中后期，接近论文写作。


---
