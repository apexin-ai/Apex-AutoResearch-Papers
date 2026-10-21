# agent / loop_14.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_14.md`
- **Structured JSON:** [`a68b5543c7d9b06c82c3.json`](../../sessions/a6/a68b5543c7d9b06c82c3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: idle_timeout
updated: '2026-05-15T21:20:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 `westd-39279:cuda:0` 和 `westd-39279:cuda:1`，禁止用其他设备
- D095 Narrative A 已批准生效，paper_framing.md 已按 D095 改写——**不可回退到旧 framing**（D057 之前的 "ISR has structural advantage" 已被 premise-count-matched 1.06x 推翻）
- Genuine rate ISR 6.06% vs Random 9.54% **p=0.182 不显著**——任何论文文本不可 claim genuine rate 有显著差异
- Random H7 pooled 13.7% 由 s43-r3 单 seed 贡献（38.3%），s42/s44-r2 均 0%——论文必须同时报 per-seed 和 pooled，显著标注单 seed 来源
- D051: 2.4x ISR 倍率已作废，premise-count-matched 1.06x 是定论
- H7b (obfuscated tautology) 仅存在于 ISR s44 的 12 个样本——不可泛化到其他条件
- classify_h7.py D086 版本是 taxonomy ground truth，不可用旧版本输出
- genuine = proved − |H7 ∪ H1 ∪ H8|（C013 集合排除公式），不是简单减法

### 2. 🖥️ 基础设施快照
- **服务器**: westd-39279 (2×RTX PRO 6000 96GB)，account: root
- **工作目录**: `/root/solver-trace-ablation`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，非 venv）
- **环境激活**: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型**: Qwen2.5-3B-Instruct，路径在服务器 `/root/autodl-tmp/` 下（具体路径需 SSH 确认，多次实验用过）
- **数据**: `proofwriter_fol_100.jsonl` (eval), FOLIO 500 (train)
- **HF cache**: `/root/autodl-tmp/.hf_cache`
- **W&B**: 项目有 wandb 集成，具体 project name 见实验 spec
- **Checkpoints**: 各实验 checkpoint 在 `/root/autodl-tmp/outputs/&lt;exp_id>/` 下
- **活跃进程**: 无（0 RUNNING, 0 cron, 0 worker）
- **论文**: `projects/solver-trace-ablation/paper/` 目录，TeX 编译正常（17页 PDF, 0 errors）
- **Provenance**: 36/36 完成

### 3. 📊 当前状态
所有 86 个实验已完成（success 26 / negative 28 / failed 26 / killed 6）。无运行中实验、无活跃 Worker、无活跃 Cron。

**刚完成的**:
- D095 Narrative A 批准 + paper_framing.md 全文改写（H7a GRPO-general ISR-amplified + H7b ISR-specific + genuine n.s.）
- Random 3-seed pooled stats: H7 p=1.3×10⁻³⁹, Genuine p=0.182
- TeX 编译环境就绪，Provenance 36/36
- 论文已有部分 TeX 内容（experiments.tex 等），但需要全量数据同步到最新 D095 framing

**等待中**: 无 Worker 回调、无 Cron、无 Director 决策待处理

### 4. 📋 待办（条件触发式）
- 立即可做 → 启动 Paper Agent 全文写作（DDL 2026-05-25，剩 10 天）
- TeX 数据同步 → 将 D095 最终数字（pooled stats, per-seed 表格, Wilson CI）更新到 experiments.tex / appendix.tex 所有表格和正文
- paper_framing.md 改写已完成 → 按 framing-reaudit skill 做全文 re-audit（逐章节 diff），确保 intro/abstract/method/experiments/discussion/conclusion 全部与 D095 Narrative A 一致
- 写作完成 → reference-audit（引用验证）+ paper-visual-review（排版检查）
- 如果 Reviewer 反馈要补实验 → GPU 空闲可立即跑（2×RTX PRO 6000 96GB 全部空闲）

### 5. 🎯 战略上下文
**核心结论**: ISR 是有效的 reward hacking 诊断工具（Claim 1），但作为优化目标时展现 meta-level Goodhart 效应（Claim 2），且跨逻辑泛化（Claim 3）。这是一篇 **诊断/分析论文**，不是 "ISR 改善了训练" 的正面结果论文。

**决策链关键节点**:
- D051: 2.4x 作废 → 1.06x premise-count-matched
- D057: ISR 无结构优势闭环
- D079: SFT 零 hacking 对照
- D085: H7b obfuscated tautology 发现（meta-Goodhart 直接证据）
- D089/D090: exec-only 1000步 hacking mode seed-dependent
- D093: Random H7≠0%（推翻 "H7 is ISR-specific"）
- D095: 最终 Narrative A（H7a GRPO-general + H7b ISR-specific）

**最容易判断错的事**:
1. 不要把 H7a 说成 ISR-specific——它是 GRPO 通用现象，ISR 只是放大了频率（5x）
2. 不要直接对比 ISR pooled H7 70.6% vs Random 13.7% 而不标注 Random 的 single-seed concentration
3. exec-only 不同 seed 收敛到不同 hacking 策略（s42=H1, s43=H7a, s44=H1+H8），不要说 "exec-only 总是 H1"
4. SFT baseline 的 genuine=92.2% 是重要对照——它证明 Goodhart 是 RL(GRPO) 特有现象，不是模型能力问题
5. 写作进入全速推进——DDL 只剩 10 天，Paper Agent 应立即启动多 Worker 并行写各章节


---
