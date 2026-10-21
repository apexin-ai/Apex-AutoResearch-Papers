# director / loop_2.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`9309db11c71207d876b3.json`](../../sessions/93/9309db11c71207d876b3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-14T02:19:51+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-47453 的 cuda:0/1/2/3（项目配置 `execution.gpu_ids`）
- output 目录已 symlink：`/root/provenance_weight_training/output` → `/root/autodl-tmp/provenance_weight_training/output`，所有 checkpoint 写入数据盘。**不要再报磁盘溢出风险**——Reviewer 已确认误报 3 次，已澄清
- TF-IDF detector 的 ECE=0.048 极接近 0.05 gate，温度 T=0.204 很激进。如果下游 scoring 在新数据上 ECE 超 0.05，需要重新校准而非换方案
- Grid-b baseline 定义：b ∈ {0.5, 1.0, 1.5, 2.0, 3.0, 5.0}，3 seeds（D004 协议），不可删减
- MVP pass/fail 标准：adaptive b* 均值 ≥ 90% grid-search 最优 perplexity 改善量（跨 3 seeds）

### 2. 🖥️ 基础设施快照
- 服务器：westd-47453，`ssh -p 47453 root@connect.westd.seetacloud.com`，密码 gOfvuw6gV7Mf
- 工作目录：`/root/provenance_weight_training`
- Python：conda base 环境（`/root/miniconda3/bin/python`），aml-train 镜像
- 数据盘：`/root/autodl-tmp/`（226GB 可用）
- 模型：`/root/provenance_weight_training/models/`（Qwen3-0.6B）
- 数据：`scored_data.jsonl`（371,499 docs，含 q_score 字段），`eval_holdout.jsonl`（67,823 行纯人类文本）
- TF-IDF detector：`combo_degrade` 配置，AUC=0.939，模型文件在项目目录
- 训练参数：`--save_total_limit 2 --save_only_model`（已修复磁盘问题）

### 3. 📊 当前状态
刚完成：TF-IDF detector 训练 + scoring + 磁盘修复 + uniform 重提交 + grid-b seed42 启动 + 实验避坑指南更新（symlink 教训）

Registry RUNNING：
- `uniform_seed42` (cuda:1)：从 ckpt-500 恢复，~58% 完成，ETA ~1.5h
- `uniform_seed123` (cuda:2)：同上
- `uniform_seed456` (cuda:3)：同上
- `grid_b_seed42_batch` (cuda:0)：b=0.5 进行中（37%），6 个 b 值串行，ETA ~10h 全部

已完成：`datagen_synthetic_4gpu` (success), `detector_tfidf_lr` (PASS)

Agent 已有 Phase 2 计划：uniform 完成后 kill grid-b 串行脚本，4 卡并行跑剩余 b 值。

### 4. 📋 待办
- uniform 3 seeds 完成回调 → Phase 2：kill grid-b 串行，保留已完成 b 值，剩余 b 值分配到 4 GPU 并行
- grid-b seed42 全部 6 个 b 完成 → 选 best b → 只跑 best b 的 seed 123/456（2 runs）+ 3 个 adaptive-b* runs
- 全部 24 runs 完成 → eval pipeline（perplexity + HellaSwag/MMLU + Self-BLEU）→ MVP pass/fail 判定
- eval 时注意 `CUDA_VISIBLE_DEVICES` 隔离（Reviewer 警告 device_map="auto" 会抢训练 GPU）
- MVP PASS → `complete_mvp()` → post-mvp-kickoff skill → paper_framing.md + experiment_plan.yaml + dream_simulate

### 5. 🎯 战略上下文
- 投稿目标：EMNLP 2026 ARR May 25（主攻，D003），AAAI 2027 后备
- 核心假设：adaptive b*（从 α_eff 推导）无需网格搜索即可匹配/超越 grid-searched b
- 决策链：D001(AAAI) → D003(改 EMNLP) → D002(MVP 设计) → D004(3 seeds+gate+kill criteria) → D005(q-score 极化风险) → D006(10% 数据重训失败) → D007(TF-IDF LR 弱检测器，成功)
- 关键转折：Qwen3-0.6B 合成文本对神经网络检测太容易（AUC>0.999），改用 TF-IDF 弱检测器是正确选择，mid_range 46.3%
- 易错点：(1) 不要因为 grid-b 串行太慢而删减 b 值——D004 协议 6 个 b 值不可变；(2) adaptive b* 代码已通过 smoke test（b*=3.311），但实际训练效果未验证；(3) eval 时必须用 left-padding（decoder-only 模型）


---
