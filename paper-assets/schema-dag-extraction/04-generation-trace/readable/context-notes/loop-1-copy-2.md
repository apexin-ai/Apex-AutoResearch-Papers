# agent / loop_1.md

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`978d826d9cbd4324228d.json`](../../sessions/97/978d826d9cbd4324228d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-14T23:11:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cqa1-38874 cuda:0（唯一分配的 GPU）
- 模型和 HF cache 必须放 `/root/autodl-tmp/`（根分区仅 9GB 可用）
- 实验用 `--max_samples 1000`（不是 test set 全量 37648）
- vLLM 当前是 0.20.2（Director 曾要求回滚到 0.18.1 但未执行，0.20.2 实际可用，不要再动）
- 代码修复已通过 Director 确认（5 个 fix），不要再改 BCS/random samples/solo baseline/ΔF1/dynamic enum 相关逻辑
- Exp 1 count curve 方向反了（F1 随 count 上升），Director 已知晓，正在等 evaluation 诊断结果再决策

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-38874，账户 root
- 工作目录：`/root/schema-dag-extraction/`（代码 `src/`，数据 `data/`，结果 `results/`，日志 `logs/`）
- Python：`/root/miniconda3/bin/python3`（conda base，不是 venv）
- 激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache`
- 模型：Qwen3-32B-FP8 at `/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/`（7 shards，完整）
- 数据：Few-NERD parquet at `/root/schema-dag-extraction/data/parquet/{train,test,validation}.parquet`
- Type configs：`configs/few_nerd_types.json`（66 types），`data/few_nerd_type_stats.json`
- Embeddings：`data/type_embeddings.pt`（Qwen3），`data/type_embeddings_e5.pt`（E5 ablation）
- Heatmaps：`data/heatmap.pdf`（Qwen3），`data/heatmap_e5_*.pdf`（E5）
- 活跃进程：Exp 2 PID 197321（`run_experiment.py --mode exp2`，cuda:0）
- Cron：`exp002_confusability_controlled`（每 180s 监控 PID 197321）
- 等待回调的 Worker：`worker_ssh_eval-diagnosis-b2_20260514T231026`（evaluation 诊断，CPU only）

### 3. 📊 当前状态
- **exp001_count_baseline**: ANALYZING。94/94 batches 完成。结果异常——relaxed F1 随 count 上升（0.067→0.247）。Exact F1 全部 < 0.02。已派 Worker 做 evaluation 诊断（B 方案 2）
- **exp002_confusability_controlled**: RUNNING（PID 197321）。54 batches（count=6/12 × 25 random + low/high BCS），预计 ~1.5-2h。第一个 batch `count_6_low_bcs` 已开始
- **Worker `eval-diagnosis-b2`**: 正在运行，读代码 + 抽样对比模型输出 vs gold。诊断 relaxed match 逻辑、type 过滤、P/R 分拆、预测数量 vs count。Director 说这个结果优先于 Exp 2 汇报

### 4. 📋 待办（条件触发式）
- `eval-diagnosis-b2` Worker 回调 → **立即汇报 Director**（优先于一切）。如果发现 evaluation bug → 派 Worker 修复 evaluate.py → 用修复版重新计算 Exp 1 指标 → 更新 registry
- `exp002` cron 回调（进程退出）→ SSH 检查 log → 判断成功/失败 → 更新 registry → 如成功：运行 analyze_results.py（Δ(solo_F1 - batch_F1) vs BCS，Pearson r）→ 汇报 Director
- 如果 evaluation 诊断发现 type 过滤 bug → Exp 2 结果也需要用修复版 evaluate.py 重算
- 如果 Pearson |r| ≥ 0.3 且 p < 0.05 → PASS，推进 SDGD 框架实现
- 如果 |r| < 0.3 → NEGATIVE，按 red-section skill 产出 Framing 调整提案，禁止默默跑下一个实验
- Director 提过：如果 Exp 2 在 count=6 上因 BCS variance restriction 不显著 → 追加 count=2 和 count=4 数据点

### 5. 🎯 战略上下文
- 项目核心：验证 type confusability（BCS）是否独立驱动 LLM IE 质量下降。EMNLP 2026 ARR May 25（距今 11 天）
- D001：项目立项 MVP。D002：统计效力修正（random 10→25，加 solo baseline，改用 ΔF1）
- **当前最大风险**：evaluation 可能有 bug（count curve 反转 + exact F1 ≈ 0 + 预测数远超 gold）。如果 evaluation 确认有问题，Exp 1/2 结果都不可信，需要修复后重跑。这是下一步所有决策的前提
- BCS 用 Qwen3 mean-pool（已验证优于 E5）。BCS 定义是 max pairwise similarity（不是 mean）
- 易错点：few_nerd_utils.py 用 `fine_ner_tags`（66 细粒度），不是 `ner_tags`（9 粗粒度）。之前有过这个 bug
- 易错点：实际只有 64 active types（不是 66），代码中 `min(66, len(active_types))` = 64
- 易错点：不要在未分配的 GPU 上启动实验。本项目只有 cuda:0


---
