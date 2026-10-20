---
loop: 2
reason: idle_timeout
updated: '2026-05-12T19:35:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 cuda:0 和 cuda:1 @ westd-16980，不可用其他设备
- analysis_gamma_sweep 是 **D008 final gate**——结果出来前不得启动任何新方向的实验，不得动 paper
- Gate 标准：任一 gamma beat random PPL ≥5% → continue；全部 fail → archive 整个项目
- EMNLP 2026 ARR DDL = 2025-05-25（13 天），gate FAIL 则无论如何不追这个 DDL
- recency baseline PPL=7.1758 几乎等于 full cache 7.1822（差 0.09%），任何 eviction 方法必须先 beat recency 才有意义

### 2. 🖥️ 基础设施快照
- **服务器**: westd-16980，工作目录 `/root/carc`
- **Python**: `/root/miniconda3/bin/python`，conda base 环境（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- **模型**: `/root/carc/models/DeepSeek-R1-Distill-Qwen-14B`
- **数据**: WikiText-2 (parquet cache in /root/carc), MATH-500 reasoning traces (embedded in scripts)
- **结果目录**: `/root/carc/results/`（heatmap_data.pt, inverted_ema_results.json, a2_attn_vs_ema.json, d003 results 等）
- **W&B**: 未配置（本项目所有实验用本地 JSON 记录）
- **HF cache**: 未显式设置（模型已本地下载）
- **活跃进程**: analysis_gamma_sweep PID=40063, tmux session, cron 监控中（reconcile 确认 still running）
- **GPU 1**: 空闲（analysis_heatmap 已完成）

### 3. 📊 当前状态
**刚做完**: 本 session 是被 WRITE HANDOFF 触发的新 session，尚未执行任何操作。上一 session 完成了：
- D007 决策：inverted EMA 双向否定（原始 ≈ random，反转 +15% worse），skip reasoning rerun
- D008 决策：gamma_sweep 定为 final gate
- analysis_heatmap 完成（success）：浅层不冗余，中层最冗余但不稳定，深层回落
- 清理了 carc_generate_rope_test（killed）和 inverted_ema_reasoning_v2（killed）

**Registry 状态**: 14 实验，13 DONE（10 negative / 1 success / 2 killed），1 RUNNING
- **RUNNING**: `analysis_gamma_sweep`（GPU 0, PID 40063）— 8 个 gamma 值 PPL sweep，gamma=0.1 已出 PPL=8.17（比 random 差 7%）
- 所有其他实验均已完成

**等待中**:
- gamma_sweep cron 回调（进程完成后系统自动通知）
- 无 Worker 在跑
- 无待处理 Director 决策

### 4. 📋 待办（条件触发式）
- **gamma_sweep cron 回调到达** → spawn Worker 读取 `/root/carc/analysis_gamma_sweep_results.json`，提取全部 8 个 gamma 的 PPL → 与 random PPL (7.6432) 对比
  - 任一 gamma beat random ≥5%（即 PPL ≤ 7.26）→ update_registry(conclusion=success) → 向 Director 汇报 continue，按 ROADMAP Phase 1 恢复
  - 全部 fail → update_registry(conclusion=negative) → 产出 red-section Framing 调整提案（或直接 archive 提案）→ 向 Director 汇报，附 pivot 备忘（exact mean 替代 EMA，O(B) 复杂度）
- **GPU 1 当前空闲** → ROADMAP 提到待做 "统一 literature_map.yaml 中 KeyDiff 描述"，可以 spawn 一个 CPU Worker 做这个文献整理（不需 GPU）
- **Director 决定 archive** → 备份代码和结果到 S3 → 关闭项目

### 5. 🎯 战略上下文
**项目核心结论链**:
- D001: cross-axis 假说（KV similarity → MLP sparsity）
- D002: MVP FAIL → pivot 到 O(1) KV eviction
- D003: sanity check FAIL（EMA ≈ random on WikiText-2 4K）
- D004: 最后一次尝试（32K + reasoning traces）
- D005: D003 expanded FAIL（EMA 在所有条件下劣于 random）
- D006: pivot 到 inverted EMA（驱逐高相似度 token）
- D007: inverted EMA 也 FAIL（+15% worse than random），双向否定
- D008: gamma_sweep 是最后的 gate

**易判断错的点**:
- gamma_sweep 几乎确定会 FAIL：D003 数据中 ema_0.9（最接近 optimal 的 gamma）vs random 仅差 1.77%，gamma=0.1 已确认差 7%。不要对结果抱有不切实际的期望
- 但**必须等结果出来**再做判断，不能提前 archive——这是 D008 的明确决策
- analysis_heatmap 是唯一 success，但它是可视化分析不是 eviction 实验，不改变整体 negative 结论
- KeyDiff 用 exact mean 有效而我们的 EMA 无效——区别在于 exact mean vs decayed running average，不是 centroid 思路本身有问题。如果 Director 问 pivot 方向，核心差异在这里
- recency baseline 极强（PPL 7.1758 vs full 7.1822），说明 token 重要性高度局部化，任何全局聚合信号（EMA/mean）天花板都很低
