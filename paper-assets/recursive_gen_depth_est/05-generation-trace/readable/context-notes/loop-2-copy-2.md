# agent / loop_2.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`3e1344791081cb56898e.json`](../../sessions/3e/3e1344791081cb56898e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: idle_timeout
updated: '2026-05-14T19:34:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westb-52439 的 cuda:0 和 cuda:1（项目配置白名单）
- 模型目录用 `olmo-1b-hf`（不是 `olmo-1b`），之前踩过坑
- Qwen2.5 系列不能用（代码占比过高，LoRA 无法覆盖，MVP 阶段已验证两次失败）
- submit_training_job 的 command 必须自带环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/recursive_gen_depth_est && bash scripts/run_pipeline_xxx.sh`

### 2. 🖥️ 基础设施快照
- 服务器：westb-52439（2× RTX PRO 6000 Blackwell 98GB），account: root
- 工作目录：`/root/autodl-tmp/recursive_gen_depth_est`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 模型路径：`/root/autodl-tmp/models/`（pythia-1.4b/, gpt2-xl/, olmo-1b-hf/）
- 数据路径：`/root/autodl-tmp/recursive_gen_depth_est/data/depth_0.jsonl`（5000 条 Wikipedia）
- 日志目录：`/root/autodl-tmp/recursive_gen_depth_est/logs/`
- Checkpoint 目录：`/root/autodl-tmp/recursive_gen_depth_est/checkpoints/`
- 活跃进程：cross_model_gpt2xl_001 (PID 123650, cuda:1, tmux 管理)

### 3. 📊 当前状态
**我刚做完**：收到 pythia_temp09_001 CRON 完成回调，派了两个 Worker：
1. `worker_analysis_pythia_temp09_001_20260514T163125` — SSH 读日志提取 metrics，与 baseline 对比
2. `worker_submit_cross_model_olmo_002_20260514T163144` — 准备在 cuda:0 提交 OLMo-1B 重跑

**正在等待**：两个 Worker 的 [WORKER DONE] 回调均未返回。已向 Director 汇报了初步状态。

**Registry 状态**：
| exp_id | 状态 | GPU | 说明 |
|--------|------|-----|------|
| pythia_temp09_001 | ANALYZING | cuda:0(完成) | temp-only τ=0.9，Worker 正在提取 metrics |
| cross_model_gpt2xl_001 | RUNNING | cuda:1 | GPT-2 XL pipeline，预计 ~19:00 UTC 完成 |
| cross_model_olmo_002 | PREPARING | — | Worker 正在准备提交到 cuda:0 |
| pythia_topk50_001 | PREPARING | — | 等 cuda:1（GPT-2 XL 完成后） |

**还收到了一条重复 CRON 回调**（pythia_temp09_001 第二次），无需处理。

### 4. 📋 待办
- analysis Worker 回调 → 读 metrics → update_registry(conclusion, metrics) → 更新 report.md → 向 Director 详细汇报（含 vs baseline 对比 + 反思实验计划 + 文献联动）
- OLMo Worker 回调 → 确认提交成功 → 更新 ROADMAP 状态
- cross_model_gpt2xl_001 CRON 完成回调 → 派 Worker 分析 → cuda:1 释放 → 提交 pythia_topk50_001 (plan_001c)
- plan_001b + plan_002 + plan_003 全部完成 → 可启动 plan_004 (DCOL) 和 plan_006 (Atlas)
- 如果 pythia_temp09_001 conclusion = negative → 按 red-section skill 产出 Framing 调整提案，禁止直接跑下一个

### 5. 🎯 战略上下文
- **D001**：MVP PASS — Pythia-1.4B nucleus p=0.95，4-class acc 78.2%，3-class (d1-d3) 70.8%。递归深度可区分。
- **D002**：Dream 审稿完成，Best=3.0/Median=3.0/Worst=2.5。Atlas/EDD 为 primary contribution，DCOL 为 secondary。6 项结构性必修已写入 paper_framing.md。
- **核心 baseline 指标**：4-class acc 78.2%, filtered 81.6%, 3-class 70.8%, d1v2 AUC 0.861, top features = var_surprisal/p90_ppl/mean_ppl
- **易错点**：pythia_temp09 的 hypothesis 是"跨解码策略泛化"——如果 metrics 与 nucleus 接近（±5pp），这本身就是 success（证明策略无关性）。不要因为没有"显著提升"就判 negative。
- **pipeline 结构**：每个实验是 3 轮 LoRA finetune + 3 轮 generate + feature extraction + classification 的完整管线，wall clock ~1.5-2h per pipeline
- **GPU 预算**：P0 预估 45 GPU·h (~1 day on 2 GPUs)，P0+P1 共 83 GPU·h


---
