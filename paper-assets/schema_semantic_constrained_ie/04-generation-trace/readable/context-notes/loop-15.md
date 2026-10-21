# agent / loop_15.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_15.md`
- **Structured JSON:** [`de60e44f8cb2ef0f16f1.json`](../../sessions/de/de60e44f8cb2ef0f16f1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: idle_timeout
updated: '2026-05-16T19:51:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-16980 cuda:0/1，westd-21461 cuda:0/1。其他设备/卡号禁止使用
- 论文投稿目标：EMNLP 2026 ARR May 25，距今 9 天
- w9 sampling 实验（已提交 PREPARING）是为论文补充的 temperature sampling 对比，不是核心实验——不要因为它们 block 论文进度
- Mistral DocRED residual DR 33.2% 如实报告，不 normalize，不 cherry-pick
- Post-hoc framing 已调整（D032）：constrained decoding 价值 = 生成时硬保证 + composability + 极端鲁棒性，不再 claim "F1 preservation"

### 2. 🖥️ 基础设施快照
- **服务器**: westd-16980 + westd-21461
- **工作目录**: `/root/schema_semantic_constrained_ie`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，非 venv）
- **模型路径**: `/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B`（两台服务器均有）
- **数据**: `data/docred/dev.json`, `data/processed_data/test.json`(SciERC)
- **活跃进程**:
  - w9_qwen_docred_zs_sampling: PID 40367, westd-21461 cuda:0, tmux session
  - w9_qwen_scierc_zs_sampling: PID 382074, westd-16980 cuda:0, tmux session
- **Cron**: reconcile 返回 0（两个 PREPARING 实验刚提交，cron 应已注册但尚未触发状态推进）
- **W&B**: 项目内实验用 wandb 记录（参考 wandb-guide skill）
- **论文目录**: `artifacts/` 下有已注册产出

### 3. 📊 当前状态
**刚做完**: 全部 54 个核心实验完成（46 success / 1 negative / 3 killed / 4 misc）。FT ablation 8/8 ✅。残余 DR error analysis ✅。论文 Round 4 = 7/10。

**正在进行**:
- w9_qwen_docred_zs_sampling (PREPARING, westd-21461 cuda:0) — ZS temperature sampling 对比
- w9_qwen_scierc_zs_sampling (PREPARING, westd-16980 cuda:0) — ZS temperature sampling 对比
- 两个实验状态为 PREPARING（已 submit_training_job，等 cron 推进到 RUNNING）

**等待**:
- w9 两个 sampling 实验完成 → 分析结果
- ft_ablation_analysis.md 数据错误修正（Reviewer critical 指出）— 状态不明确，需确认是否已修
- Paper Agent patch: DocRED FT ablation 最终数据 + error analysis → Round 5
- Round 5 Reviewer 评估（目标 ≥8/10）

**Worker 池**: 0 running（空）。论文定稿阶段，主要 block 在 w9 结果 + paper patch

### 4. 📋 待办（条件触发式）
- w9 cron 回调（DONE）→ spawn worker 分析 sampling 结果（对比 greedy vs sampling 的 violation rate + F1），更新 registry，汇报 Director
- ft_ablation_analysis.md 确认修正 → 若未修，spawn worker 修正数据错误
- Paper patch 就绪 → spawn worker 执行 Round 5 论文更新（DocRED FT ablation 数据 + error analysis 写入 paper）
- Round 5 完成 → dream_simulate(review_mode="full") 最终模拟评估
- 模拟 ≥8/10 → submit_paper_to_review 交 Group C

### 5. 🎯 战略上下文
- **核心结论**: OntoCoDec 两层约束有效——grammar 消 ET/RV，semantic 是 DR 唯一 defense（FT 后 grammar 对 DR 冗余）。Composability 成立（ΔF1<0.6pp）。Post-hoc 在低 violation rate 下可行但高 violation rate 场景崩溃（Mistral DocRED 73.7% rejection）
- **决策链**: D030(Mistral 选型) → D031(不加 NYT29) → D032(post-hoc framing 调整) → D033(Mistral crossover) → D034(Qwen tokenizer warning 忽略) → D035(进入最终定稿)
- **易错点**:
  - w9 sampling 实验是补充性质，即使结果 negative 也不 block 论文（greedy 已是主结果）
  - ft_ablation_analysis.md 数据错误是 Reviewer critical，必须在 Round 5 前确认修复
  - 论文中 Constrained decoding 不再 claim "F1 preservation superiority over post-hoc"——只 claim 硬保证 + composability + 鲁棒性
  - Residual DR 分析中 Qwen 残余全是 schema gap（不可消除），Llama 残余 92% 是 entity typing 弱——这是 limitation 不是 failure


---
