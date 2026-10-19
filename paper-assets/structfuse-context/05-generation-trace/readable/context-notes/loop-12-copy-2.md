# reviewer / loop_12.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_12.md`
- **Structured JSON:** [`adf927d0648d7dc7286c.json`](../../sessions/ad/adf927d0648d7dc7286c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_wall_time
updated: '2026-05-15T18:13:51+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 分配：cuda:0 (Qwen 训练链) + cuda:1 (StarCoder 训练链)，两卡均已占满，不得在其上启动额外进程
- m1_reextract_v2 是纯 CPU 任务，不占 GPU，但 4 个 CPU worker 在跑，不要 kill
- `all.jsonl`（/root/autodl-tmp/structfuse/full_m1_data/all.jsonl）是 May 13 生成的旧文件（44173 行），reextract 完成后需要重新合并才能用——不要误以为它已包含新 structural 数据
- StarCoder 主链 PID 519791 的 supplement watcher (PID 20226) 只跑 BM25，不含 embed/dataflow——registry 中的 "DUPLICATE RISK" WARNING 是错误的，已向 Director 报告建议移除

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-42106 (root)，工作目录 /root/structfuse
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型：Qwen → /root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B；StarCoder → /root/autodl-tmp/models/bigcode/starcoder2-3b/bigcode/starcoder2-3b
- 数据：/root/autodl-tmp/structfuse/full_m2_training_data/（M2 训练），/root/autodl-tmp/structfuse/full_m1_data/（M1 提取）
- Checkpoints：/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/ 和 m2_full_starcoder/
- W&B：offline 模式，日志在 /root/structfuse-context/wandb/
- 活跃进程：
  - PID 337267 (tmux, Qwen 主链 cuda:0)，当前子进程 PID 18427 (dataflow_s43)
  - PID 519791 (tmux, StarCoder 主链 cuda:1)，当前子进程 PID 38016 (embed_s42)
  - PID 966920 (watch_and_chain_qwen_s42.sh, 等 Qwen 主链结束后跑 s42 supplement)
  - PID 20226 (watch_and_chain_starcoder_s42.sh, 等 StarCoder 主链结束后跑 BM25 only)
  - m1_reextract_v2: 4 CPU workers 处理 MONAI + moto 剩余实例

### 3. 📊 当前状态
刚完成两轮审查：m1_reextract_v2 进度核实 + M2 训练进度核实，均 PASS。

Registry RUNNING:
- **m2_full_qwen_continued**: dataflow_s43 (5/7)，eval@500 R@1=0.5495。remaining: dataflow_s44 → bm25_s42。ETA May 17 14:00-18:00 CST
- **m2_full_starcoder_resumed**: embedding_distance_s42 (4/8)，step 200/4242。remaining: embed_s43/s44 → dataflow_s42/s43/s44。ETA May 19-20 CST
- **m1_reextract_v2**: 98.6% done (27882/28276)。moto CodeQL call_graph 100% timeout (exit 33, 536 instances affected = 1.9%)，MONAI 正常处理。ETA May 16 10:00-12:00 CST

QUEUED: plan_018_bm25 (Phase 2 GPU 训练)、plan_015_dynamic
PREPARING: plan_005_stratified（分层评估脚本就绪，等 M2 checkpoints）

### 4. 📋 待办（条件触发式）
- m1_reextract_v2 完成 → 核实最终 JSON 计数 + moto 降级数据质量 → 提醒 Agent 触发 all.jsonl 合并 + M2 训练数据重新生成
- m2_full_qwen_continued 完成 → 审查全部 7 个 subrun 的 R@1 一致性，特别关注 s44 系统性偏高（val set 可能更容易），交叉验证 dataflow vs embedding vs random 策略差异
- m2_full_starcoder_resumed embed_s42 首次 eval (step 500) → 核实 embedding 策略是否 >random（random_s42 R@1=0.4604），这是 cross-encoder validation 的关键数据点
- Qwen supplement (PID 966920) 触发 → 核实 embed_s42 + dataflow_s42 是否正常启动在 cuda:0，无 GPU 冲突
- plan_005_stratified 正式启动 → 审查 confound 控制是否到位（pool_size / repo_size 分层），注意 s42 regime 差异（3ep vs 2ep）

### 5. 🎯 战略上下文
- 核心假设：structural negatives (embedding_distance / dataflow_aware) > random negatives，需在 Qwen + StarCoder 两个 encoder 上 3 seeds 统计验证
- Qwen 初步信号：embedding vs random 差异极小（~0.5pp），s44 seed 方差 (~4.5pp) 远大于策略 treatment effect——这是论文最大风险点，plan_005_stratified 必须排除 confound 后才能 claim
- StarCoder random 3 seeds 完成（R@1 ~0.46-0.49），比 Qwen (~0.55-0.60) 低约 10pp，符合 neg_difficulty_analysis 预期（StarCoder pretrained margin 2.6-4x Qwen）
- BM25 baseline 是 Dream 审稿认定的最大结构性缺陷，plan_018_bm25 Phase 1 (CPU mining) 已完成，Phase 2 等 GPU
- 易错点：不要把 registry 的 WARNING "StarCoder supplement DUPLICATE RISK" 当真——已验证 supplement 只跑 BM25，无重复


---
