# code exp014 naturalistic v2

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp014_naturalistic_v2_20260525T064459_result.json`
- **Structured JSON:** [`f5aa4f43bc54fda239a0.json`](../../sessions/f5/f5aa4f43bc54fda239a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已成功启动，正在执行 Phase 1 数据采样。

**已完成的操作：**

1. **脚本编写**：`scripts/exp014_naturalistic_v2.py`（1165 行），包含 5 个 Phase：
   - Phase 1：从 FineWeb CC 流式采样 50K docs（50≤words≤1000，<30% non-ASCII，截断 256 tokens）
   - Phase 2：Qwen2.5-1.5B-Instruct 提取 15D 特征（surprisal 9D + vocab 3D + tail 3D），self-BLEU 使用全局 100 篇 reference pool
   - Phase 3：加载 `exp_qwen_cont_10k/features.csv` 训练 5 个 binary LightGBM P(Y>k)，全量训练，OBD 预测 CC 数据
   - Phase 4：9 个独立质量指标（GPT-2 Large PPL、MAUVE、MTLD、HD-D、3/4-gram rep、Zipf、TTR、hapax）
   - Phase 5：Spearman/Kendall + Bonferroni、分层分析、Kruskal-Wallis/Mann-Whitney/Cliff's delta、Bootstrap CI、length-controlled correlation、3 个可视化

2. **依赖安装**：`lexical-diversity`、`mauve-text`（含 `faiss-cpu`）

3. **任务提交**：`exp_014_naturalistic_v2`，GPU cuda:1，tmux session，12h timeout，日志 `results/exp014_v2/run.log`

每个 Phase 开头有断点续跑检查，支持中断后重启。预计总运行时间 6-8h。

---
