# director / loop_10.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_10.md`
- **Structured JSON:** [`3008e9b51248252405b1.json`](../../sessions/30/3008e9b51248252405b1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_messages
updated: '2026-05-23T00:04:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 仅限 westd-34887 cuda:0,1（westd-41718 已由用户释放，不可达）
- 论文路径在本地 `projects/distill_sparse_swiglu/paper/`，不在远程服务器
- paper_compile_and_check 必须传 `paper_dir=/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper`（默认路径 docs/paper/ 不存在）
- EMNLP 2026 主正文严格 8 页限制，当前刚好 8 页，任何新增内容必须同时削减等量文字
- Coupling 数字已从 10-47% 修正为 29-97%（R23），所有文件（paper/*.tex + paper_framing.md）已同步，不要回退

### 2. 🖥️ 基础设施快照
- 服务器：westd-34887 (connect.westd.seetacloud.com)，2× RTX PRO 6000 Blackwell 96GB
- 远程工作目录：/root/distill_sparse_swiglu/
- Python：/root/miniconda3/bin/python（conda base，不是 venv）
- 模型：LLaMA-3.1-8B / Mistral-7B-v0.3 / Qwen-2.5-14B（路径在远程 /root/ 下，具体路径需 Agent 确认）
- 活跃进程：无（所有实验已完成）
- W&B：未配置

### 3. 📊 当前状态
**刚做完**：R24 审稿报告（3.0 Findings, fresh review）的 Holistic Pass + Action Matrix，已提交 Reviewer 独立审视。
**等待中**：
- Reviewer 对 R24 Action Matrix 的反馈（post_to_reviewer 已发）
- 用户审批 R23 修正版（apr_20260522T190056_dgfo，可能已过期需重新提交）
- Registry 卫生：perlayer_kl_s123_downstream_v2 (PENDING→DONE), perlayer_kl_50_s42 (ANALYZING→DONE)，已派 Agent 但 Agent 被 reset 未执行

**Registry**: 378 实验，328 完成，251 成功，0 RUNNING。

### 4. 📋 待办
- Reviewer R24 反馈到达 → 综合定稿 Action Matrix → 派 Paper Agent 执行写作修复
- R24 核心写作修复（Reviewer 确认后执行）：
  - C1: Abstract/Conclusion "29-97%" → 定性描述（"coupling-dominated for commonsense, mismatch-dominated for reasoning"），§4.5 补 K=4 50% 反常假设
  - C2: §4.2 补机制假设段（WikiText-103 分布偏差 + forward KL mode-covering + Meng et al. 2022 引用）
  - W6: 全文 "dominant" → "substantially outperforms" / "critical design dimension"
  - W3: Limitations 加 "open-ended generation untested"
  - M4: 加代码释放声明
  - M5: Introduction 早期建立与 MaskLLM 的区分
  - Missing refs: Meng et al. 2022, GRASP, Li et al. 2023（需验证相关性）
- 写作修复全部完成 → 重新编译 → submit_paper_to_review（continue mode）
- DDL 2026-05-25 最终提交

### 5. 🎯 战略上下文
- **项目核心**: KL distillation 发现与 magnitude 46-68% 不同的 neuron importance patterns，PPL 降低 14.5-50%。C1 target-swap ablation 证明 mask 质量（不是 gradient coupling）是 quality driver。
- **卡在 3.0 Findings 的根本原因**: (1) per-layer KL 分解的 confound 使定量声明不可靠（但定性方向独立成立）；(2) MMLU/GSM8K 退步缺机制解释；(3) 无 wall-clock speedup。前两个可通过写作修复缓解，第三个是结构性限制。
- **易错点**：
  - 主正文恰好 8 页，任何增加文字必须配套删减——不要只加不减
  - "29-97%" 是 R22→R23 刚修正过的数字，现在 R24 又要软化——不要误以为数字本身错了，而是定量精度不够（仅 K=1/K=4 两个点）
  - K=4 50% PPL=44.23 > K=1 34.85 是真实数据，论文解读为 "coupling dominates at high sparsity"，但审稿人认为缺机制解释——需要假设性讨论不是新实验
  - review_issues.yaml 在 `artifacts/review_issues.yaml`，R24 的 issue 需要新增条目
  - R23 审批卡可能已过期（5/22 提交），修复后需重新 submit_paper_to_review


---
