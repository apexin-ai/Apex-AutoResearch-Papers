# agent / loop_1.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`fa83f0f98a1cbdbdf1c4.json`](../../sessions/fa/fa83f0f98a1cbdbdf1c4.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-14T15:59:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: cuda:0, cuda:1 on westb-52439。不要用其他 GPU 编号
- OLMo 必须用 `allenai/OLMo-1B-hf`（路径 `olmo-1b-hf`），不是 `OLMo-1B`（后者需 hf_olmo 自定义代码）
- OLMo LoRA targets 是 **3 个模块** `q_proj,k_proj,v_proj`，不是 2 个
- Pipeline 脚本提交前必须 `bash -n script.sh` 验证语法（olmo_001 因未闭合引号崩溃浪费一个 GPU cycle）
- submit_training_job 不会自动推进 registry 状态到 RUNNING——需要手动走 PREPARING→QUEUED→ALLOCATED→RUNNING（带完整 spec）
- Checkpoint 目录按模型/策略隔离（data/olmo/, data/gpt2xl/, data/pythia_temp09/, data/pythia_topk50/），不要混写

### 2. 🖥️ 基础设施快照
- 服务器: westb-52439（SSH config alias，实际 hostname autodl-rtx6000），2× NVIDIA RTX PRO 6000 Blackwell 98GB
- 工作目录: `/root/autodl-tmp/recursive_gen_depth_est`
- Python: conda base — `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型路径:
  - Pythia-1.4B: `/root/autodl-tmp/models/pythia-1.4b/` (LoRA: query_key_value)
  - OLMo-1B: `/root/autodl-tmp/models/olmo-1b-hf/` (LoRA: q_proj,k_proj,v_proj)
  - GPT-2 XL: `/root/autodl-tmp/models/gpt2-xl/` (LoRA: c_attn,c_proj)
- 种子数据: `data/depth_0.jsonl` (5000 Wikipedia samples, 共享)
- 活跃进程（截至 14:55 UTC）:
  - cuda:0: Pythia temp09 pipeline, PID 125067 (bash wrapper) → 125083 (python finetune), tmux=pythia_temp09_001
  - cuda:1: GPT-2 XL pipeline, PID 126022 (generate depth-1), tmux=cross_model_gpt2xl_001
- Cron: cross_model_gpt2xl_001 有 120s 间隔监控；pythia_temp09_001 由 submit_training_job 注册

### 3. 📊 当前状态
**刚做完**:
- 处理了 Director CRITICAL: rogue GPT-2 XL 进程（PID 122428/122434）已自行退出，无 checkpoint 污染
- 修复 OLMo 脚本: MODEL_PATH→olmo-1b-hf, TARGET_MODULES→q_proj,k_proj,v_proj, SYNTAX_OK
- 创建并启动 Pythia temp09 pipeline on cuda:0 (registry RUNNING)
- 创建 Pythia topk50 pipeline 脚本（就绪待启动）
- 修复 experiment_plan.yaml: plan_002→olmo_002, plan_003→gpt2xl_001, plan_006b→done, 拆分 plan_001b/001c
- OLMo crash 分析: olmo_001→failed (脚本bug), 创建 olmo_002 (PREPARING)

**Registry 活跃实验**:
- `pythia_temp09_001` RUNNING — Pythia temp-only τ=0.9, cuda:0, ~2h
- `cross_model_gpt2xl_001` RUNNING — GPT-2 XL nucleus, cuda:1, ~4h total from 14:42 UTC
- `cross_model_olmo_002` PREPARING — 等 cuda:0 释放
- `pythia_topk50_001` PREPARING — 等 cuda:1 释放

**等待中**: 两个 cron 回调（pythia_temp09 完成 / gpt2xl 完成）

### 4. 📋 待办（条件触发式）
- pythia_temp09_001 cron 回调(~17:00 UTC) → 启动 cross_model_olmo_002 on cuda:0（脚本已修复, depth-0 checkpoint 可复用跳过 ~5min）→ submit_training_job → 推 registry 到 RUNNING
- cross_model_gpt2xl_001 cron 回调(~19:00 UTC) → 分析结果 + domain consistency check → 启动 pythia_topk50_001 on cuda:1（脚本 run_pipeline_pythia_topk50.sh 已就绪）
- cross_model_olmo_002 完成(~19:00 UTC) → 分析 OLMo 结果 + 与 Pythia MVP 对比 → 汇报 Director
- 所有 4 条 pipeline 完成(~21:00 UTC) → plan_004 (DCOL DeBERTa) + plan_006 (Atlas) 可启动，向 Director 提交 P0 下半段审批
- 每次实验完成 → 按 on-experiment-done skill 分叉处理(success/negative/failed)

### 5. 🎯 战略上下文
- **核心发现**: 递归生成深度可从统计特征高精度区分。MVP Pythia-1.4B 4-class acc=78.2%, 3-class=70.8%, top features: var_surprisal > p90_ppl > mean_ppl
- **决策 D001**: MVP PASS，进入 research phase (2026-05-14)
- **论文目标**: EMNLP 2026 ARR DDL 5/25。3 个 Claims: (1) DCOL ordinal depth estimation, (2) Depth Degradation Atlas, (3) depth-graduated curation
- **P0 关键路径**: 3 模型(Pythia/OLMo/GPT-2 XL) × 3 策略(nucleus/temp/topk) 数据生成 → DCOL 训练 → leave-one-model-out → Atlas。数据生成是瓶颈，预计今天 21:00 UTC 全部完成
- **易错点**:
  - OLMo 用 `olmo-1b-hf` 不是 `olmo-1b`，后者有 aria2 残留且需自定义代码
  - GPT-2 XL 的 Conv1D 特殊性——PEFT 自动处理但 LoRA targets 必须是 c_attn/c_proj
  - 代码污染随深度增加（d1=17.8%→d3=27.4% 宽标准），但过滤后 acc 反而提升（78.2→81.6%），信号是真实的
  - Registry 状态推进不能跳步（PREPARING→QUEUED→ALLOCATED→RUNNING），每步都要调 update_registry
  - DDL 紧迫（11 天），不要在任何地方留 buffer，全速推进


---
