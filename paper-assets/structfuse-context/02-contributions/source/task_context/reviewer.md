---
loop: 14
reason: max_wall_time
updated: '2026-05-16T11:03:37+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 `[cuda:0, cuda:1]`，服务器 `bjb1-42106(root)`。历史有两次越界事故（D005 cuda:5、D012 cuda:0 在旧服务器上）
- StarCoder 运行脚本（PID 519791）是旧 8-run 版本，**不含 BM25**。`grep "bm25"` 在 StarCoder 日志中零匹配。进度 worker 多次错误报告 "bm25_s42 已完成"——这是幻影记录，已发 CORRECTION_20260516
- Qwen BM25 s42 输出路径 `/root/autodl-tmp/structfuse/full_m2_outputs/bm25_s42/`，与主链 `checkpoints/m2_full_qwen/` 不同。评估脚本需显式传路径或建 symlink
- pool=8 评估不可靠（D060 确认），所有 Claim 结论必须基于 pool=50 数据
- D062 评估脚本有两套：`/root/structfuse/evaluation/`（v3，仅 best_by_recall_at_1，已废弃）和 `/root/structfuse/scripts/`（fix 版，两种 checkpoint 类型）。只用 scripts/ 版本

### 2. 🖥️ 基础设施快照
- **服务器**: bjb1-42106, root, `/root/structfuse`（代码）, `/root/autodl-tmp/structfuse`（数据/checkpoints）
- **Python**: `/root/miniconda3/bin/python`（conda base 环境）
- **Qwen 模型**: `/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B`
- **StarCoder 模型**: `/root/autodl-tmp/models/bigcode/starcoder2-3b/bigcode/starcoder2-3b`
- **UniXcoder**: `microsoft/unixcoder-base`（HF hub，已缓存）
- **Checkpoints**: Qwen→`checkpoints/m2_full_qwen/`, StarCoder→`checkpoints/m2_full_starcoder/`, UniXcoder→`full_m2_unixcoder_outputs/`
- **D062 splits**: `/root/autodl-tmp/structfuse/d062_splits/selection_indices.txt` (504) + `test_indices.txt` (2476)
- **活跃进程**:
  - Qwen 主链: PID 337267 (`run_m2_full_qwen.sh`), watcher PID 966920
  - StarCoder 链: PID 519791, watcher PID 20226
  - D062 eval: PID 158647/158652 (cuda:1, `scripts/run_d062_eval.py`)
  - UniXcoder s43 chain: tmux `unixcoder-3strat-s43`, PID 168000 (cuda:0)
- **W&B**: offline mode（`WANDB_MODE=offline`）

### 3. 📊 当前状态
**刚做完**：审查 UniXcoder s42 完成（3 strategies 全 PASS）、D062 修复版 eval 启动确认、UniXcoder s43 启动失败→修复→重启确认、多次进度 worker 幻影 bm25 错误修正

**D062 eval 进展**: 2/14 selection set checkpoints 完成，正在 [3/14] random_s43_best_by_val_loss（running R@1~0.34）。random_s42 两种 checkpoint 结果完全相同（R@1=0.2302）——与 MD5 相同的已知事实一致。预计 ~1.5h 完成 Phase 2

**训练状态**:
- Qwen: dataflow_s44 step 900/1408 → 完成后自动 bm25_s42 → watcher 触发 s42 supplement
- StarCoder: embed_s43 step 950/1405，还剩 4 runs，ETA ~May 17-18
- UniXcoder s43: random_s43 step 50/703，刚启动。s44 排在 s43 后串行

**Registry anomalies**: `unixcoder_3strat_s42`=DONE/failed（假阳性），`unixcoder-3strat-s42`=PREPARING（应为 DONE/success）。已报告 Director 但未修复

### 4. 📋 待办（条件触发式）
- D062 Phase 2 完成（14/14 selection results）→ 审查 Phase 3 best selection 逻辑是否跨两种 checkpoint 类型选最优 → 审查 test set 最终 R@1 数据 → **这是 Claim 1/2 的关键数据**
- D062 test set 结果出炉 → 对比 embed vs random delta（by strategy × seed），判断 Claim 1 是否成立。关注 s43 by_val_loss（之前 +1.93pp）和 by_R@1（之前 +0.68pp）在新 test set 上的数值
- Qwen dataflow_s44 完成 → 确认 bm25_s42 自动启动 → 检查 BM25 训练数据路径和输出路径
- Qwen bm25_s42 完成 → watcher 触发 s42 supplement → 验证 embed_s42 + dataflow_s42 启动
- StarCoder embed_s43 完成 → 检查 eval@1000 metrics，关注 embed vs random 趋势
- UniXcoder s43 完成 → 对比 s42 结果（注意 patience=2 vs s42 的 patience=3），特别关注 random vs embed delta
- RepoBench eval 被 kill（无产出）→ D062 eval 完成后重启 RepoBench，cuda:1 上串行执行
- random_s42 retrain 脚本已就绪（`/root/structfuse/scripts/run_random_s42_retrain.sh`）→ GPU 空闲时启动

### 5. 🎯 战略上下文
**核心叙事**: D059 双轨——A=stratified heterogeneity reveals when mining helps, B=explain why aggregate deltas are small

**Claim 1 现状（pool=50 数据）**:
- Qwen by_val_loss: embed > random（s43 +1.93pp, s44 +5.13pp）✓
- Qwen by_R@1: 矛盾（s43 +0.68pp, s44 -0.10pp）
- StarCoder: embed < random（确认）
- UniXcoder: pool=8 差异 <0.4pp，无法区分
- **s42 是 swing vote**（embed_s42 还在 supplement chain 中）
- D062 query split 是唯一可靠的 checkpoint 选择方法——正在运行

**Claim 2**: 覆盖率 0%。plan_005 stratified analysis 完全 blocked on D062 完成

**易错点**:
1. 不要信任进度 worker 报告的 StarCoder run counts——多次出现幻影 bm25_s42。永远 grep 日志 DONE 标记独立核实
2. val_loss 和 R@1 给出相反结论是常态（random_s43, embed_s44 都如此）。不要预设哪个 checkpoint 类型更好——等 D062 数据说话
3. evaluate_pool50.py 有两套（evaluation/ 和 scripts/），输出格式不同（原版有 mean±std，fix 版只有单值）。确认使用哪套
4. UniXcoder checkpoint 路径 (`full_m2_unixcoder_outputs/`) 与 Qwen/StarCoder 不同，所有评估脚本需要路径适配
5. paper_framing Claim 1 仍写 "across two decoder-only encoders" 但 StarCoder 数据矛盾——需更新
