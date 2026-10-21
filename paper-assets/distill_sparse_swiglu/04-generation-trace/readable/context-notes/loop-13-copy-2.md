# reviewer / loop_13.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_13.md`
- **Structured JSON:** [`bcdf1f0e541fa730f3b2.json`](../../sessions/bc/bcdf1f0e541fa730f3b2.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_wall_time
updated: '2026-05-23T19:50:49+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-34887 cuda:0, cuda:1（2× RTX PRO 6000 Blackwell 96GB）。westd-41718 已释放不可用。
- qwen14b_kl30_s123_gsm8k 结果文件在 westd-41718 上，已无法访问验证。该数据完整性存疑（运行时间仅同类实验一半，conclusion=killed，无 sample_len）。如论文引用此数据需标注或改为 2-seed。
- EMNLP 2026：主文 8 页硬限、abstract ≤200 words、Limitations 必须在正文（不在 appendix）、ethics 已移除。

### 2. 🖥️ 基础设施快照
- 服务器：westd-34887 (root)，代码根目录 `/root/distill_sparse_swiglu/`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型：`/root/autodl-tmp/models/llama-3.1-8b`、`/root/autodl-tmp/models/qwen2.5-14b/`
- HF cache：`/root/autodl-tmp/.hf_cache`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/`
- 活跃进程：无（所有实验已完成，GPU 全部空闲）
- W&B：未配置（本项目不检查 W&B）

### 3. 📊 当前状态
刚完成 R28 提交前全量数据一致性审查 + Figure 3 修复验证。具体：
- **数据审查**：80+ 数字交叉验证，发现 1 处精度错误（Table 3 s42 KL PPL 8.80→8.82）已由 Agent 修正 ✅
- **Figure 3 修复**：Caption 百分比与图注冲突（14.5% vs 18%）→ Caption 改为描述性文字 ✅；KL 50% PPL 从 12.00 修正为 11.79（统一 s42）✅
- **ROADMAP 审查**：方向合理，覆盖度充分，无阻塞问题 ✅
- Registry：无 RUNNING/PREPARING 实验。成功 258 / 总 405。
- 等待中：无 Worker/Cron 回调。下一步应是 Director 提交 R28 审稿。

### 4. 📋 待办
- R28 提交审稿请求到达 → 按 §5 审查模式 B 执行全文对抗审查（必须先 Read paper-quality-lessons.skill.md + reviewer-audit-checklist §7）
- 如收到 paper_agent_request_review → 使用 §5.3 迭代评分模板返回维度评分
- 如 Agent 修改论文数字 → 重新交叉验证修改处与 registry 一致性
- Qwen s123 GSM8K 如果 Agent 决定补跑 → 验证新实验是否在 westd-34887 上且 GPU 在白名单内

### 5. 🎯 战略上下文
- **核心结论**：output-distribution KL 是 PPL 主导设计维度（signal type gap 25:1 vs coupling breadth）。C1 target-swap 确认 mask pattern 可迁移。Knowledge regression (MMLU/GSM8K) 是系统性限制。
- **R27→R28 改进链**：D104→D107→D108。K-curve 从 single-seed 升级到 full 3-seed（K=1/2/4/8/16/32），C4 control 确认 regression 非数据问题，8 处 overclaiming 修复。
- **易错点**：
  1. 论文中存在两种 allocation 比较基准（uniform vs global），正文 14.5% 是 matched-actual-sparsity uniform 比较，Figure 3 是 global 比较——不要混淆。
  2. TEAL 是确定性方法但不同 seq_len 产出不同结果——eval 必须带 `--seq_len 2048` 才匹配论文协议。
  3. Registry 中 metric 命名不统一（有些叫 `arc_challenge`，有些叫 `arc_challenge_acc_norm`）——比较前必须确认指标含义。


---
