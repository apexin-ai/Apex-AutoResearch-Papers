# agent / loop_2.md

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`c0c69d36bc974d36869d.json`](../../sessions/c0/c0c69d36bc974d36869d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: idle_timeout
updated: '2026-05-15T00:04:48+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0, cuda:1, cuda:2, cuda:3（autodl-5090），不可用白名单外的 GPU
- 实验 ID 命名：Qwen3-1.7B 的正确 exp_id 前缀是 `plan-002-qwen3-1_7b`，不是 `plan-002-qwen17b`（后者是之前的重复提交错误命名，已 kill）
- submit_training_job 的 GPU 编号始终从 0 开始（框架自动注入 CUDA_VISIBLE_DEVICES）
- 数据/模型/HF cache 必须放 `/root/autodl-tmp/`，根分区只有 ~30GB
- pip install / git clone 前必须 `source /etc/network_turbo`；HF 下载设 `HF_HUB_DISABLE_XET=1`

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090（4× RTX 5090 32GB），工作目录 `/root/gen-depth-fingerprint`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 激活命令：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 数据：`/root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl`（1000 条 wiki seed）
- 已完成生成数据：`data/pythia-1b/generations_shard{0,1}.jsonl`（各 ~2.5MB, ~2270 records）
- MVP 数据：`data/features.csv`（4609 条，Pythia-2.8B 生成链）
- 参考模型：EleutherAI/pythia-410m（所有实验共用）
- 生成脚本：`generate_chain.py`（支持 `--model-name`, `--shard-id`, `--num-shards`）
- 活跃进程（4 个，均 tmux backend）：
  - plan-002-qwen3-1_7b-s0: PID 111533, cuda:0
  - plan-002-qwen3-1_7b-s1: PID 111646, cuda:1
  - plan-002-olmo2-s0: PID 108242, cuda:2
  - plan-002-olmo2-s1: PID 108452, cuda:3
- Cron 监控：4 个活跃 cron 对应上述 4 个实验

### 3. 📊 当前状态
plan-002（跨生成器评估）Round 1 进行中：
- ✅ Pythia-1B 两 shard 完成（~2270 records/shard，gen0-gen4 深度分布正常，shard0: 497 seeds / shard1: 498 seeds）
- 🔄 OLMo-2-1B 两 shard RUNNING（cuda:2,3，PID 108242/108452，已运行 ~10h+）
- 🔄 Qwen3-1.7B 两 shard RUNNING（cuda:0,1，PID 111533/111646，刚启动不久）
- ❌ plan-002-qwen17b-s0/s1 是重复提交错误，已 kill 并记录，无需处理

等待中：
- 4 个 cron 回调（OLMo-2 和 Qwen3-1.7B 完成时触发）
- Round 2 待 Round 1 完成后启动：Qwen3-0.6B（需要两个 GPU）

plan-001（feature ablation）已完成：full_macro_f1=0.82, ref_only=0.72, surface_only=0.76，确认 Claim 2。
plan-001-restore 仍在 PREPARING 状态，是残留条目，可忽略。

### 4. 📋 待办
- OLMo-2 shard 0/1 cron 回调到达 → spawn worker 验证输出数据质量（records 数、深度分布）→ 更新 registry metrics
- Qwen3-1.7B shard 0/1 cron 回调到达 → 同上验证
- Round 1 全部 4 模型生成完成 → 用空出的 GPU 启动 Round 2：Qwen3-0.6B（cuda:0,1 两 shard）
- Round 2 完成 → plan-002 所有生成数据就绪 → spawn worker 做跨模型分类实验（特征提取 + 训练分类器 + 评估 macro-F1）
- plan-002 分类结果出来 → 与 MVP baseline (macro-F1=0.84) 对比 → 汇报 Director，确认 Claim 1 跨生成器泛化
- 分类完成后 → 推进 plan-003（cross_family_reference_model）或 plan-004（downstream_utility），视 Director 优先级

### 5. 🎯 战略上下文
- 核心 idea：用小参考模型（Pythia-410M）的分布特征检测文本"生成深度"（gen-0/1/2+）
- MVP 已验证单生成器场景（Pythia-2.8B，macro-F1=0.84），现在在验证 Claim 1 跨生成器泛化
- plan-001 确认了 Claim 2：参考模型特征（F1=0.72）独立于表面词汇统计（F1=0.76）有区分力，但表面特征略强，framing 已调整为"Dual Dynamics"（H1 = level/sharpness 特征, H2 = diversity 特征）
- Venue 目标：AAAI 2027 (DDL Aug 2) primary / EMNLP 2026 ARR (May 25) stretch
- 易错点：
  - OLMo-2 模型 ID 是 `allenai/OLMo-2-0425-1B`，不是旧版 OLMo
  - Qwen3 模型是 Base 版本（`Qwen/Qwen3-1.7B-Base`），不是 Instruct
  - generate_chain.py 的 `--model-name` 参数是短名（如 `qwen3-1.7b`），不是 HF full ID
  - 已有 5 个 PREPARING 状态的残留实验（mvp-001-gen-s0/s1/s2/s3, plan-001-restore），都是历史遗留，不要尝试重启


---
