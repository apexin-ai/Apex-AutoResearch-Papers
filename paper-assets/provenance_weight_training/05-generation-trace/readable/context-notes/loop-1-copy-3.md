# reviewer / loop_1.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`817f56cb1302a7d5f1c5.json`](../../sessions/81/817f56cb1302a7d5f1c5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-13T22:02:01+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-47453，GPU 白名单需确认（当前 detector 跑 cuda:0，datagen 用了 cuda:0-3，未见 execution.gpu_ids 配置文件）
- 合成数据目标 80M tokens（200M × 40%），worker 已从 132M 子采样到 ~80M 修正，旧版保留为 `mixed_data_old_67pct.jsonl`——不要用旧版
- D004 协议：3 seeds (42/123/456)，grid-b∈{0.5,1.0,1.5,2.0,3.0,5.0}，fixed-b per run（非 per-batch adaptive），detector gate AUC≥0.95 + ECE≤0.05
- run_mvp.sh 的 `$OUTPUT_DIR` 默认 `./mvp_output`，但实际数据在 `/root/provenance_weight_training/data/`——Agent 需要对齐路径或设 OUTPUT_DIR

### 2. 🖥️ 基础设施快照
- 服务器：westd-47453 (root)，4× RTX PRO 6000 Blackwell 96GB
- 工作目录：`/root/provenance_weight_training/`
- Python：`/root/miniconda3/bin/python`（conda base 环境，无 venv）
- 数据路径：
  - 人类数据：`/root/provenance_weight_training/data/human/{train,detector,eval_holdout}.jsonl`
  - 合成数据：`/root/provenance_weight_training/data/synthetic/depth_1_merged.jsonl` (340,992 docs, 132M tok)
  - 混合数据（已修正）：`/root/provenance_weight_training/data/mixed_data.jsonl` (371,499 docs, ~200M tok, 40% synth)
  - Detector 输入：`/root/provenance_weight_training/data/detector_input/{human,synthetic}/`
- Detector checkpoint：`/root/provenance_weight_training/output/detector/checkpoints/checkpoint-500/`
- W&B project：`provenance-weight-mvp`
- 活跃进程：detector 训练中 GPU 0（PID 未记录，需 `nvidia-smi` 查）

### 3. 📊 当前状态
**刚完成的审查**：
- datagen_synthetic_4gpu：PASS（132M tok 生成完成，退化率 0.87%）
- merge-and-assemble-mixed：PASS（子采样到 80M synth tok，40% contamination 修正）
- quality-check-run：PASS（仅 shard_0 有质量报告，可接受）

**当前运行**：
- Detector 训练（GPU 0, 98% util, step 500/10,194）——eval_auc 已达 0.9999
- Registry 仅 `datagen_synthetic_4gpu` (DONE)，detector 训练未注册

**等待**：
- Detector 训练完成 → gate check (AUC/ECE) → 温度校准 → scoring → 24 runs pretraining
- 无 pending worker 回调、无 cron

### 4. 📋 待办（条件触发式）
- Detector 训练完成通知 → 验证 `final_model/` 目录存在 + `temperature.pt` 已生成 + `calibration_results.json` AUC≥0.95 ECE≤0.05
- Gate check 通过 → 审查 scoring step（temperature scaling 是否正确加载，q-score 分布形态——如果高度极化需要标 warning）
- 24 runs pretraining 启动 → GPU boundary check + wandb 指标交叉验证
- compare_results.py 输出 → 核实 MVP pass/fail 判定逻辑

### 5. 🎯 战略上下文
- 项目核心：α_eff(b) 理论驱动的 importance weighting 是否优于 uniform baseline（含合成数据 pretrain）
- 决策链：D003 改 EMNLP primary → D004 定义 MVP 协议（200M tok, 3 seeds, grid-b, detector gate）
- **最容易判断错的事**：detector AUC=0.9999 看似利好，实际可能是问题——q-score 高度极化会让所有 b>0 的权重方案等效于直接删除合成数据，grid-b 细粒度对比退化为 "有 vs 无" 二元对比。MVP 仍能 pass（weighted > uniform），但不能证明 adaptive b* 的精细调优价值。温度校准后的 q-score 分布是判断关键
- **容易踩的坑**：run_mvp.sh 路径与实际数据路径不一致；report.md 和 registry 更新严重滞后（4 GPU 空闲 5h+ 才启动 detector）；shard_1-3 无质量报告但已合入混合数据


---
