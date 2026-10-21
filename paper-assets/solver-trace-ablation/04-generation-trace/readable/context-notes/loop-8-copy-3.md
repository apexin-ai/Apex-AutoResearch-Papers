# reviewer / loop_8.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_8.md`
- **Structured JSON:** [`1ba5536934154c8c95d6.json`](../../sessions/1b/1ba5536934154c8c95d6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_wall_time
updated: '2026-05-15T10:28:32+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（gpu_ids=[0,1]）。越界进程立即 CRITICAL + 要求 kill。
- Eval 数据必须用 `data/proofwriter_fol_100.jsonl`（C008/C009）。之前 SFT s44 首次 eval 误用 `test_100.jsonl` 已被我抓到并修正，Agent 可能再犯。
- 训练数据固定 `data/train_500_seed42.jsonl`（C001），所有实验共用。
- by_answer_type 正确分布：true:34 / false:25 / unknown:41。如果 registry 出现其他分布（如 50/44/6），说明用了错误 eval 数据集。
- genuine_rate 应以 fraction of proved 计算（genuine_count / n_proved），不是 fraction of total。plan002-b01-s42-1000 的 registry 用了 3/100=0.03 而非 3/90=0.033，口径不一致但未修正。

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279 (root)，代码根目录 `/root/solver-trace-ablation`
- Python：`/root/miniconda3/bin/python3`（conda base 环境，不用 venv）
- 模型：`/root/autodl-tmp/models/Qwen3-4B`
- 数据盘：`/root/autodl-tmp/`（250GB，清理后 ~112G used / 139G avail）
- Outputs：`/root/autodl-tmp/outputs/`
- 磁盘刚从 100% 满恢复（清理了 138GB），新实验保存 checkpoint 会再吃空间，注意监控
- 无 W&B 配置（所有实验用 --no_wandb）
- 活跃进程：exp1-isr-b03-s42-1000 可能在 GPU 0 运行（最后一次检查 GPU 0 = 87%/80GB）；plan018-random-b01-s42-1000-r2 训练完成、正在 ANALYZING

### 3. 📊 当前状态
**本 session 已提交 10 条审查报告**（5 条来自上一个 context window，5 条本轮）：

关键已完成审查：
- plan002-b01-s42-1000 eval：NEGATIVE，H7=92.2%，genuine=3.0%，tautological collapse confirmed ✓
- SFT s44 registry 修正：PR 0.14→0.17，by_answer_type 修正，genuine 12→15 ✓
- Wilson CI complete：3-seed pooled ISR genuine = Random genuine (p=1.0)，art_20260515_61b3a3 的 p=0.0001 是错误的（cross-seed 比较）✓
- 磁盘满危机：两个实验崩溃，清理后恢复 ✓
- plan018-random-b01-s42-1000-r2：训练完成但 **resume 语义有问题**——实际跑了 1350 步（350+1000），非 1000 步 resume。与 plan002 的 1000 步不可直接对比 ✓

Registry 状态（截至 handoff）：
- ANALYZING: plan018-additive-random-b01-s42-1000-r2（eval 待出）
- RUNNING: exp1-isr-b03-s42-1000（GPU 0，ISR β=0.3，从 base model 开始 1000 步）
- DONE: 69 experiments
- FAILED: plan018-additive-random-b01-s42-1000 (disk full), exp1-isr-b03-s42-1000 原始 (disk full)

### 4. 📋 待办（条件触发式）
- plan018-random-b01-s42-1000-r2 eval 完成 → 审查 H7/H1/genuine 分类，确认 hacking 模式（预期 H1-dominant，ISR≈0.333）。**关键：这是 1350 步模型，不是 1000 步，论文使用需注意**
- exp1-isr-b03-s42-1000 完成 → 审查 eval，对比 exp1-isr-b03-s43（500步：H7=2.3%，genuine=30.2%）。这是 β=0.3 的 1000 步版本，看是否也 collapse
- 任何新 eval 完成 → 检查 by_answer_type 是否为 34/25/41，防止再出 test_100.jsonl 错误
- 论文章节审查请求 → 先查 red-section skill 合规，再做内容审查。当前 abstract "92.9% SFT non-hacking" 需更新为 91.3%（3-seed pooled）
- GPU 空闲 > 15min → 主动提醒 Director 安排实验

### 5. 🎯 战略上下文
**论文 3 个核心 Claim**：
1. STA 作为诊断工具（ISR 分解 hacking 模式）
2. Goodhart / ISR 无结构优势（genuine rate parity: ISR≈Random at β=0.1）
3. 跨逻辑泛化（FOL→Prolog）

**Claim 2 是审查重心**。关键数据链：
- Wilson CI pooled：ISR b01 genuine=17.3% [13.0%, 22.7%] vs Random b01 genuine=17.4% [12.4%, 23.8%]，Fisher p=1.0
- Bootstrap 原始 p=0.637 结论正确但输入数据有误（genuine rate 与 registry 不匹配）
- art_20260515_61b3a3 声称 "corrects broken bootstrap p=0.637" 实际本身是错误的（cross-seed 比较），Director 已知悉
- 1000 步实验加强 Goodhart 叙事：ISR 500 步时最好的 seed (s42, 30.9% genuine) 延长训练后 collapse 到 3.0%

**最容易判断错的事**：
1. **不要被 ISR 数值高迷惑**。训练时 ISR=1.0 不代表 genuine——plan002-1000 的 ISR=1.0 全是 tautological (premise==conclusion)。
2. **Cross-seed heterogeneity 极大**。ISR b01 三个 seed：s42=32.1% genuine, s43=3.3%, s44=13.5%。Pooled 数据掩盖了 seed 间质变（s44 总是 collapse）。
3. **plan018-r2 是 1350 步不是 1000 步**。`--model_path checkpoint-350 --num_steps 1000` 是从 checkpoint 权重做新 1000 步，不是 resume。对比 plan002 (1000步) 不公平。
4. **SFT pooled genuine 已从 93.1% 改为 91.3%**（加入修正后的 s44）。论文数字可能尚未更新。


---
