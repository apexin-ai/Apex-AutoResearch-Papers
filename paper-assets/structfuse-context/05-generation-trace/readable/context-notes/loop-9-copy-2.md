# agent / loop_9.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_9.md`
- **Structured JSON:** [`e1791737a79cfcc27194.json`](../../sessions/e1/e1791737a79cfcc27194.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: idle_timeout
updated: '2026-05-15T04:12:20+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 **仅** `bjb1-42106:cuda:0, cuda:1`——历史上两次越界（D005, m2_early_pilot_v3 用 cuda:0 on cqa1）被 CRITICAL
- `submit_training_job` 的 command 必须自带环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && ...`。服务器用 conda，**没有 .venv**
- Dataflow-aware 策略论文描述已改为 **BM25 排序**（D041，匹配代码实现），不要描述为 embedding 排序
- Claim 2 已降级为 "exploratory observation with testable prediction"（D035），不可恢复为 core claim
- plan_005 分层分析的 R@1 值目前全是 **dry-run mock**，禁止引用为真实结果（D039）
- 服务器上残留旧进程 PID 465668（evaluate_pool50.py --pool-size 5 --gpu -1），需清理后再用

### 2. 🖥️ 基础设施快照
- **服务器**: bjb1-42106（2× RTX PRO 6000 96GB）
- **工作目录**: `/root/structfuse`
- **Python**: `/root/miniconda3/bin/python`（conda base env）
- **模型**: Qwen2.5-Coder-3B + StarCoder2-3B（pretrained 从 HF cache）
- **数据**: `/root/autodl-tmp/structfuse/full_m1_data/`（M1 提取）、`/root/autodl-tmp/structfuse/full_m2_training_data/`（M2 训练数据，含 BM25 negatives）
- **Checkpoints**: `/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/` 和 `/m2_full_starcoder/`（子目录按 strategy_seed/best_by_* 组织）
- **活跃进程**:
  - cuda:0: PID 337267（m2_full_qwen chain，当前 embedding_s43，3/9 完成）
  - cuda:1: PID 519791（m2_full_starcoder chain，当前 random_s43，1/8 resumed）
  - CPU: m1_reextract_v2（4 workers，87% 完成）
- **BM25 watchers**: 两个 tmux watcher 分别监控 PID 337267 和 519791，链完成后自动启动 BM25 训练
- **Cron**: 3 个活跃（m1_reextract_v2, m2_full_starcoder_resumed, m2_full_qwen_continued）
- **Worker**: worker_check_moto-codeql-propagation（running，检查 moto repo CodeQL timeout 传播）

### 3. 📊 当前状态
刚完成 session-start reconcile。三个 cron 均确认 job still running。

**RUNNING**:
- `m2_full_qwen_continued`: embedding_distance_s43 step 150/2810（刚开始）。random 三个 seed 全部完成（s42=0.5527, s43=0.5554, s44=0.6009）。剩 6 runs，ETA ~May 17
- `m2_full_starcoder_resumed`: random_s43 step 1500/2810（~53%）。R@1 trending up 0.4708→0.4780。剩 7 runs，ETA ~May 17-18
- `m1_reextract_v2`: 24624/28276 done（87.1%），ETA May 15 17:00-19:00 CST。moto repo 536 instances 全部 call_graph timeout（exit code 33，directCallEdge 超时），fallback to embedding-distance

**PREPARING**: plan_005_stratified（脚本 ready，dry-run v5 通过，等 M2 checkpoints）
**QUEUED**: plan_018_bm25（Phase 1 done，Phase 2 等 M2 完成 + GPU 释放，watcher 自动触发）、plan_015_dynamic（等 GPU）

**等待中**:
- Worker worker_check_moto-codeql-propagation 回调
- M2 两条链完成回调（~May 17）→ BM25 watcher 自动启动 Phase 2
- m1_reextract_v2 完成回调（今天）

### 4. 📋 待办（条件触发式）
- m1_reextract_v2 cron 回调 → 更新 registry（final data count）→ 汇报 Director 最终数据规模（预期 ~44K instances）→ 更新 report.md pipeline 数字
- worker_check_moto-codeql-propagation 完成 → 读产出，决定 moto 536 instances 是否需要特殊处理
- M2 Qwen chain 完成（~May 17）→ BM25 watcher 自动启动 BM25 Qwen 训练（cuda:0）→ 同时 spawn worker 跑 plan_005 分层分析（用真实 checkpoints 替换 --dry-run）+ evaluate_pool50.py（D042 独立评估）
- M2 StarCoder chain 完成（~May 17-18）→ BM25 watcher 自动启动 BM25 StarCoder 训练（cuda:1）→ evaluate_pool50.py StarCoder
- BM25 Phase 2 完成 → 对比 BM25 vs embedding/random R@1 → 决定 narrative（harm→correction / neutral→systematic comparison）→ 这是论文 story 的关键分叉点
- Post-M2 全部完成 → plan_003 SWE-bench eval（P0，40h，可能需要 LLM API key Qwen3.6-27B）+ plan_004 RepoBench + plan_019 pool sensitivity
- May 20-24: 论文写作窗口 → ARR May 25 deadline

### 5. 🎯 战略上下文
**核心结论链**: True embedding-distance mining consistently improves contrastive code retrieval (+1.6–2.0pp R@1, across Qwen pilot)。BM25 baseline 待验证。Structure-grounded (dataflow) negatives 是 conditional observation（n=2 encoder, D035 降级）。

**决策链要点**:
- D035: Claim 2 降级为 exploratory（dataflow 效果 encoder-dependent: Qwen +0.8pp, StarCoder -0.5pp）
- D036: 主 metric 改为 R@1（不是 val_loss）
- D041: Dataflow 策略描述改为 BM25 排序（匹配代码实现）
- D042/D043: pool=50 独立评估脚本（evaluate_pool50.py）替代训练时 pool=8 eval，所有 best checkpoints 需重新评估

**易错点**:
- Qwen random_s44 的 best R@1=0.6009 异常高（比 s42/s43 高 4-5pp），best_step=500——可能是 seed variance，不要过度解读单个 seed
- M2 的 `m2_full_qwen` registry 状态是 ANALYZING（cron 自动设的），但实际链通过 `m2_full_qwen_continued` 继续跑。两个 registry entry 描述同一条链的不同阶段
- `m2_full_starcoder` 状态 DONE(failed) 是旧 cron timeout 标记，实际通过 `m2_full_starcoder_resumed` 继续。同理
- BM25 overlap 分层数据显示大 repo top-7 Jaccard 仅 0.297（vs embedding），之前基于 87% 全候选重叠的预测（BM25 ≈ embedding）可能不成立——Phase 2 结果才是真正的区分点
- plan_003 SWE-bench 可能需要 LLM API key（Qwen3.6-27B），dry-run 确认中，提前准备 request_secret


---
