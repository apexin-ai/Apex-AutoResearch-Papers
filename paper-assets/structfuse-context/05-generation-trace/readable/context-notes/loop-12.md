# agent / loop_12.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_12.md`
- **Structured JSON:** [`75b37d9c60206d20dec1.json`](../../sessions/75/75b37d9c60206d20dec1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_messages
updated: '2026-05-16T02:30:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：`gpu_ids=[cuda:0, cuda:1]`（bjb1-42106 双卡 RTX PRO 6000 96GB）。不存在 cuda:2+
- SWE-bench eval（embed_s43, dataflow_s43）已放 placeholder 暂停，Qwen chain 完成前**不要删除** `/root/autodl-tmp/structfuse/artifacts/swebench_retrieval_eval/{embedding_distance_s43_100,dataflow_aware_s43_100}/summary.json`
- E2E eval（LLM patch generation）推迟到 Qwen chain 完成后，Director 明确 kill 过一次（GPU 竞争降速 39%）
- plan_003 SWE-bench eval 论文定位：**外部泛化展示**，不做控制对比 claim（3 checkpoint 用了不同 seed s42/s43/s43，confound）
- BM25 Phase 1 数据已生成（3 seeds），Phase 2 训练等 Qwen chain 完成后由 watcher 自动触发

### 2. 🖥️ 基础设施快照
- **服务器**：bjb1-42106（~/.ssh/config 已配置直连）
- **环境**：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，Python `/root/miniconda3/bin/python`
- **项目代码**：`/root/structfuse/`
- **数据/checkpoint**：`/root/autodl-tmp/structfuse/`
  - M1 数据：`full_m1_data/all.jsonl` (44173 lines)
  - M2 训练数据：`full_m2_training_data/{train,val}_{random,embedding_distance,dataflow_aware,bm25}_s{42,43,44}.jsonl`
  - Qwen checkpoints：`checkpoints/m2_full_qwen/{strategy}_s{seed}/`
  - StarCoder checkpoints：`checkpoints/m2_full_starcoder/{strategy}_s{seed}/`
  - SWE-bench eval output：`artifacts/swebench_retrieval_eval/`
- **HF cache**：`/root/autodl-tmp/.hf_cache`
- **wandb**：offline mode，runs 在 `/root/structfuse/wandb/`
- **活跃进程**（上次采集）：
  - PID 337267 (bash wrapper) → PID 18427 (Qwen dataflow_s43 训练, cuda:0)
  - PID 519791 (bash wrapper) → PID 38016 (StarCoder embed_s42 训练, cuda:1)
  - PID 61328 (SWE-bench retrieval eval random_s42, cuda:0, 71/100 → 可能已完成)
  - M1 reextract: 4 workers (PID 209821+), moto 200/536
- **Cron**：m1_reextract_v2, m2_full_starcoder_resumed, m2_full_qwen_continued（3 active）
- **API**：OpenRouter `http://47.94.22.126/v1`，key=`tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8`（E2E eval 用）

### 3. 📊 当前状态
**刚做完**：4 个文献质量 warning 修复（GRACE 确认真实、literature_map 39→60、UniXcoder/dataflow 描述修正）+ neg_difficulty 机制分析图（r=−0.60, p=0.069）+ m2_eval_summary 汇总表 + related_work 21篇收集 + pool=50 pipeline 预检通过 + SWE-bench eval 暂停机制就绪

**RUNNING 实验**：
- `m2_full_qwen_continued`：dataflow_s43 (5/7), step ~1000+, eval@1000 R@1=0.5174（退化中，early stop 1/2）。剩余 dataflow_s44 + bm25_s42。ETA ~May 18
- `m2_full_starcoder_resumed`：embed_s42 (4/9), eval@500 R@1=0.4372。ETA ~May 19-20
- `plan_003_swebench_eval`：random_s42 71/100（可能已完成），后续暂停
- `m1_reextract_v2`：81/82 repos, moto 200/536 (ETA May 17)

**QUEUED**：plan_018_bm25 (Phase 1 done, Phase 2 等 GPU), plan_015_dynamic (等 GPU)
**PREPARING**：plan_005_stratified (等 M2 checkpoints)

**等待中**：
- Worker `training-and-eval-status` 已派发但 handoff 前未返回——下一个"你"需要 `get_worker_status('worker_ops_training-and-eval-status_20260516T022911')` 读取结果
- Director 问了 3 个问题（SWE-bench 完成否、dataflow_s43 eval@1500、训练进度），上述 Worker 的结果就是答案

### 4. 📋 待办（条件触发式）
- `training-and-eval-status` Worker 回调 → 读取结果，向 Director 汇报 3 项数据（SWE-bench/dataflow eval@1500/训练进度）
- SWE-bench random_s42 完成 → 确认 summary.json 生成 + 后续 skip 生效 + 记录 R@1 到 registry
- dataflow_s43 early stop（eval@1500 不改善）→ 更新 registry，dataflow_s44 自动启动
- Qwen chain 全部完成（~May 18）→ 立即触发：(1) pool=50 eval (2) plan_005 stratified (3) plan_018 Phase 2 BM25 训练 (4) 恢复 SWE-bench eval 剩余 2 checkpoints (5) E2E eval
- StarCoder chain 全部完成（~May 19-20）→ pool=50 StarCoder + plan_005 StarCoder 分层
- m1_reextract_v2 完成 → 执行合并脚本 `python3 /root/structfuse/scripts/combine_m1_reextract.py`（可不等 moto，99.3% 已就绪）
- Director 说"写论文" → 读 paper_framing.md + writing_plan.yaml，所有 section v1 已有初稿

### 5. 🎯 战略上下文
**核心危机**：Claim 1（embedding > random）2-seed mean Δ ≈ 0（−0.08pp）。embed_s42 缺失是 swing vote。翻盘路径：(1) embed_s42 结果 (2) pool=50 instance-level cluster bootstrap (3) D052 C/D 应急措辞。**不提前 pivot**（D018/D019 原则）。

**Claim 1 Δ 现状**（Qwen）：s43 +0.52pp, s44 −0.67pp, s42 缺失。StarCoder embed_s42 也是负向（−2.32pp）。

**A/B 双轨**：A轨=embed improves（需 Δ>0 + CI），B轨=difficulty-mechanism insight（r=−0.60 已有证据）。两轨 related work 和实验基本共享，不冲突。

**易错点**：
- plan_018 BM25 Phase 1 已完成（数据在 `full_m2_training_data/`），Director 可能不记得——不要重跑
- SWE-bench eval 暂停靠 placeholder 文件，误删会导致批量脚本继续跑下一个 checkpoint 抢 GPU
- Qwen watcher PID 966920 负责 s42 supplement（embed_s42+dataflow_s42+bm25_s42），主链完成后自动触发——验证它是否还活着
- dataflow negatives = ¬reachable_G(x,q)（不连接的文件），之前写反过一次
- 论文 framing 已软化（D049）：不再 claim "consistently improves"，改为 dual-track reporting


---
