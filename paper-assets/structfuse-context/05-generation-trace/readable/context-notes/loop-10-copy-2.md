# agent / loop_10.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_10.md`
- **Structured JSON:** [`366125fecbf612619fda.json`](../../sessions/36/366125fecbf612619fda.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_wall_time
updated: '2026-05-15T12:53:58+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（bjb1-42106 的 2× RTX PRO 6000 96GB）。不可用其他 GPU。
- s42 regime 特殊：3 epochs, no early stopping（提供完整 overfitting curve）。s43/s44 及后续：2 epochs, patience=2。BM25 watcher 脚本已统一为全部 2 epochs + patience=2（D050 修改，但 Worker 回调尚未确认）。
- 数字精度：所有指标从日志原值取 4 位小数，禁止 3 位四舍五入再补零（之前 s42 精度事故教训）。
- embedding mining 各 encoder 用自己的 base model：Qwen 用 Qwen2.5-Coder-3B，StarCoder 用 StarCoder2-3B（Director 已确认 A 方案）。
- paper_framing.md D049 是当前 agreed framing：Claim 1 用 "reliable improvement at zero additional cost"，Claim 2 是 exploratory observation，禁止 "significant"/"challenges assumption"/"fundamentally different"。

### 2. 🖥️ 基础设施快照
- **服务器**：bjb1-42106（~/.ssh/config 已配置），2× RTX PRO 6000 96GB
- **工作目录**：远程 `/root/structfuse/`（训练代码）+ `/root/structfuse-context/`（评估脚本）
- **数据**：`/root/autodl-tmp/structfuse/full_m2_training_data/`（train/val × 3 策略 × 3 seeds × 2 encoders）
- **模型**：Qwen `/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B`，StarCoder `/root/autodl-tmp/models/bigcode/starcoder2-3b`
- **M1 输出**：`/root/autodl-tmp/structfuse/full_m1_data/all.jsonl`（注意：不是 `/root/structfuse/outputs/m1_reextract_v2/`）
- **活跃进程**：
  - Qwen M2 chain: PID 337267, cuda:0, cron 监控中
  - StarCoder M2 chain: PID 519791, cuda:1, cron 监控中
  - M1 reextract v2: 4 CPU workers, cron 监控中
  - BM25 tmux watchers: PID 560714 / 560676（等 M2 完成后自动触发 Phase 2）
- **BM25 Phase 1 数据已就绪**：`/root/autodl-tmp/structfuse/full_m2_training_data/{train,val}_bm25_s{42,43,44}.jsonl`

### 3. 📊 当前状态
**刚做完**：Method v1 §3.2 数字修正（34.3% / 15,153 自洽）、Related Work v1 通过 Reviewer 最终审查（3 轮修正 + 1 轮微调）、训练进度检查、random_s44 训练详情核实（非 "early-stopped at step 500"，实际训练 1500 steps）。

**RUNNING 实验**：
| exp_id | 状态 | 摘要 |
|--------|------|------|
| m2_full_qwen_continued | embed_s44 step 950/2816 | eval@500 R@1=0.5942, 4/9 done, ETA ~May 17 |
| m2_full_starcoder_resumed | random_s44 step 400/2816 | 2/8 done, ETA ~May 20 |
| m1_reextract_v2 | MONAI 67%, moto 19% | 44,173 lines, ETA ~22:00 CST May 15 |

**PREPARING**：plan_005_stratified（脚本就绪，等 M2 checkpoint）

**等待中**：
- BM25 watcher regime fix Worker（worker_ops_bm25-watcher-regime-fix-d050）回调尚未到达
- M2 完成 cron 回调 → 自动触发 BM25 Phase 2 + plan_005 + D045 统计分析

### 4. 📋 待办（条件触发式）
- **BM25 watcher Worker 回调到达** → 确认脚本修改成功，汇报 Director
- **m1_reextract_v2 cron 回调（ETA 今晚）** → 更新 registry，汇报最终数字，可能需要更新论文中的数据管道数字
- **Qwen M2 全部完成（~May 17）** → on-experiment-done 流程：D045 统计分析（best_by_R@1 主表 + leave-one-out + s44 训练动态 + seed variance）+ BM25 watcher 自动启动 Phase 2
- **StarCoder M2 全部完成（~May 20）** → 同上 + 跨 encoder 对比分析
- **plan_005 正式启动时** → 加入第 6 层分析：per-seed val set 难度校验（s44 outlier 排查）
- **experiments_v1.md 中 random_s44 描述** → 需修正 "early-stopped at step 500" 为 "early-stopped at step 1500; best checkpoint at step 500"（Director 已收到数据，待指令）

### 5. 🎯 战略上下文
- **核心结论**：embedding-distance mining 提供 reliable improvement（pilot +1.6-2.0pp，M2 s43 +0.52pp best_by_R@1），但 effect size 随数据规模缩小。D049 将 narrative 从 "challenges gradient-based assumption" 软化为 "reliable zero-cost baseline"。
- **s44 outlier 是最大统计风险**：R@1=0.6009 比 s42/s43 高 ~4.5pp，且是 transient peak（step 500 best，后续持续下降到 0.5542）。跨 seed 方差远大于 strategy treatment effect。plan_005 第 6 层分析（per-seed val set 难度）专门排查这个。
- **时间线紧张**：ARR May 25 deadline，StarCoder ETA May 20，post-M2 窗口仅 ~5 天。
- **论文章节状态**：Abstract v1 ✅ / Intro v1+v2 ✅ / Method v1 ✅(PASS) / Related Work v1 ✅(PASS) / Experiments v1 骨架 ✅(待审) / Discussion v2 初稿 / Conclusion ❌ / Appendix ❌
- **易错点**：(1) introduction 有 v1 和 v2 两个版本（v2 含 LaTeX），需确认主版本；(2) StarCoder 数据构建中 random/dataflow_aware 数据是从 Qwen 目录复制的（只有 embedding_distance 重新生成）；(3) val set 的 embedding_distance negatives 未用 StarCoder 重新生成（从 Qwen 复制），这可能是 Reviewer 攻击点。


---
