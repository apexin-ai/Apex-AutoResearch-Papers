# reviewer / loop_1.md

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`939b1f1b99cac8d45533.json`](../../sessions/93/939b1f1b99cac8d45533.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-14T21:53:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:0（cqa1-38874 上唯一分配的 GPU）
- 模型必须放 `/root/autodl-tmp/`，根分区仅 9GB 剩余，禁止往根分区写大文件
- BCS 定义必须用 **max** pairwise cosine similarity（非 mean），已修正过一次，代码在 `compute_bcs.py:44`
- exp2 random samples 必须 25/档（非 10），已修正过一次，代码在 `run_experiment.py:120`
- Few-NERD 必须用 `fine_ner_tags`（66 细粒度类型），非 `ner_tags`（8 粗粒度），已修正过一次

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-38874(root)，工作目录 `/root/schema-dag-extraction/`
- Python：`/root/miniconda3/bin/python3`（Python 3.12，conda base env，不是 venv）
- torch 2.10.0+cu128, vLLM 0.20.2
- 模型：`/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/`（Qwen3-32B-FP8, 32GB 权重）
- 数据：`/root/schema-dag-extraction/data/parquet/{train,test,validation}.parquet`（Few-NERD）
- Type defs：`/root/schema-dag-extraction/configs/few_nerd_types.json`（66 types）
- Embeddings：`data/type_embeddings.pt`（Qwen3）+ `data/type_embeddings_e5.pt`（E5-large-v2，两个变体）
- Sim matrix：`artifacts/sim_matrix.pt`
- 活跃进程：exp1 via vLLM EngineCore PID 188307（cuda:0, 94GB VRAM）
- 磁盘：根分区 9GB free / 30GB，数据盘 31GB free / 250GB
- 无 W&B（`--no_wandb`），无 tmux session 记录

### 3. 📊 当前状态
- **exp001_count_baseline**: RUNNING。count=[1,2,6,12,22,44,66]，37648 test samples，PID 188307。Dry run 已完成（100 samples），full exp1 日志最后可见在跑 count_1 的 solo batches（66 个 type 各跑一次）。预估还需 1-2h。
- **exp002_confusability_controlled**: PREPARING。等 exp1 完成后启动。
- **E5 alternate embeddings**: 已计算完毕（`data/type_embeddings_e5.pt`），但 BCS 分布对比数值未持久化到 log 文件——需要 Agent 确认 E5 vs Qwen3 的 BCS range，决定 exp2 用哪个 embedding。
- **等待中**: exp1 完成回调 → 审查结果 → exp2 启动决策

### 4. 📋 待办
- exp1 完成 → 审查 eval_exp1.json：(1) count-quality curve 是否单调递减？(2) solo baseline per-type F1 分布是否合理？(3) exact F1 是否仍 <5%（dry run 仅 0-3%，如果 full exp 也这样，需要切到 relaxed F1 或审查 prompt）
- exp1 审查通过 → 确认 exp2 用哪套 embedding（E5 vs Qwen3），看 BCS range 是否足够宽
- exp2 完成 → 核心审查：Pearson |r| ≥ 0.3 且 p < 0.05？Δ(solo_F1 - batch_F1) vs BCS 的相关性？
- |r| ≥ 0.3 → go，推进 Contribution B（SDGD 实现）
- |r| < 0.3 → pivot 到 negative result study，需要审查 framing 提案（加载 negative-framing-review skill）

### 5. 🎯 战略上下文
- 核心假设：type confusability（非 count）独立驱动 training-free LLM IE 质量下降。Day-3 go/no-go gate。
- 决策链：D001 立项 → D002 统计修正（25 random/档 + solo baseline + BCS max）
- ARR May 25 DDL = 距今 11 天。MVP 3h GPU，全项目 170h。单卡 11 天理论上限 264h，够用但无 buffer。
- **最容易判断错的事**：(1) dry run 的 exact F1 极低（0-3%）不一定是 bug——LLM 不擅长精确 char offset 是已知问题，relaxed F1（9-14%）说明模型确实在抽取实体。需要关注 full exp 的结果再判断。(2) BCS range 窄（0.88-0.92 with Qwen3 embedding）可能使 exp2 correlation 不显著——E5 embedding 是 Plan B，但数值对比还没确认。(3) 不要因为"11 天很紧"就发 deadline warning——AI Agent 速度与人类不同，只看 GPU-hours 够不够。


---
