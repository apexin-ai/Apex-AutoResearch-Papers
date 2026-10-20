# agent / loop_15.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_15.md`
- **Structured JSON:** [`bc942b70d56c41c1d1cd.json`](../../sessions/bc/bc942b70d56c41c1d1cd.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: max_messages
updated: '2026-05-17T12:04:11+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cqa1-22115 cuda:0/1/2/3，不可用其他 GPU
- **M002 教训**：每个实验必须使用独立 data 目录，禁止共享含中间生成文件的目录。run_pipeline.py 有 skip-if-exists 逻辑，共享目录会导致复用其他模型的生成数据（exp_wiki_pythia/olmo v1 已因此作废）
- submit_training_job 命令必须 `bash -c '...'` 包裹，绝对路径（不用 ~），脚本内 --device 始终 cuda:0（框架自动映射物理 GPU）
- 环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不要假设 .venv 存在
- 所有 HF 操作必须 offline 模式：`HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-22115，account=root
- 工作目录：`/root/autodl-tmp/gen-depth-contamination/`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- HF cache：`/root/autodl-tmp/.hf_cache/`
- 模型路径：
  - OLMo-1B: `/root/autodl-tmp/.hf_cache/allenai/OLMo-1B-hf`
  - LLaMA-3.1-8B: `/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B`
  - Pythia-1.4B: `/root/autodl-tmp/.hf_cache/models--EleutherAI--pythia-1.4b/snapshots/fedc38a16eea3bd36a96b906d78d11d2ce18ed79`
  - Qwen2.5-1.5B scorer: `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B`
- 数据路径：
  - arXiv seed: `data/exp_024_arxiv/`
  - Wiki seed: `data/exp_023_wiki/depth_0.jsonl`（只有 depth_0 是源数据，depth_1+ 是 Qwen 生成的）
  - Wiki v2 独立目录（Worker 创建中）: `data/exp_wiki_pythia/`, `data/exp_wiki_olmo/`
- 活跃进程：
  - exp_arXiv_olmo: PID 26733, cuda:0, RUNNING
  - exp_arXiv_llama8b: PID 27469, cuda:1, RUNNING
  - cuda:2/3: wiki v2 Worker 正在修复 pipeline + 准备提交
- 论文 PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/main.pdf`（510KB, 20页, 0 errors）

### 3. 📊 当前状态
**刚完成**：
- exp_wiki_pythia + exp_wiki_olmo kill + 标记 DONE/failed（data reuse bug M002）
- exp_wiki_pythia_v2 + exp_wiki_olmo_v2 注册（PREPARING）
- Theta 敏感性扫描表（Task A）✅ 完成，CSV + LaTeX 已在 artifacts/
- M002 教训已写入 memory.md
- 向 Director 汇报全局状态

**正在进行**：
- Worker `worker_code_exp_wiki_v2_fix_and_submit_20260517T120104`：修复 run_pipeline.py skip-if-exists + 创建独立 data 目录 + 提交 wiki v2 到 cuda:2/3
- Worker `worker_analysis_14d_ablation_bootstrap_20260517T120133`：14D vs 15D bootstrap CI 明细表，正在定位 features.csv 和 LightGBM 配置（turn 12）

**Registry RUNNING/PREPARING**：
- exp_arXiv_olmo: RUNNING (cuda:0, OLMo-1B on arXiv, ~1-2h)
- exp_arXiv_llama8b: RUNNING (cuda:1, LLaMA-8B on arXiv, ~3-4h)
- exp_wiki_pythia_v2: PREPARING (cuda:2, Worker 提交中)
- exp_wiki_olmo_v2: PREPARING (cuda:3, Worker 提交中)

**等待回调**：
- wiki v2 Worker done → 确认提交成功，更新 registry
- 14D ablation Worker done → 收割结果，register_artifact，汇报 Director
- 4 个 GPU 实验 cron 回调 → on-experiment-done 流程

### 4. 📋 待办（条件触发式）
- wiki v2 Worker 完成 → 确认 cuda:2/3 RUNNING，检查 pipeline 修复是否生效（结果不应与 exp-023 相同）
- 14D ablation Worker 完成 → 收割 per-model per-pair AUC+CI 表，register_artifact，向 Director 汇报完整明细
- exp_arXiv_olmo cron 回调（~1-2h）→ on-experiment-done：检查 K* 是否=3（与 exp-024 Qwen / exp-025 Pythia 一致），更新 registry+report.md，汇报 Director
- exp_arXiv_llama8b cron 回调（~3-4h）→ 同上，额外关注 8B scale 是否改变 K*
- exp_wiki_pythia_v2 / exp_wiki_olmo_v2 cron 回调 → 检查 K* 是否=2（与 exp-023 Qwen 一致），此时如果 K*≠2 是重要发现需要立即汇报
- 4 个域覆盖实验全部完成 → 汇总 domain × model 覆盖矩阵，更新论文 Table，向 Director 提交完整矩阵
- Group C 审稿最终报告到达 → 处理审稿意见，可能需要补实验

### 5. 🎯 战略上下文
- **项目核心**：首次系统测量递归合成文本的 K*（generational discrimination boundary）。K* 是 domain-dependent bounded：web K*=2 (7/8 configs), arXiv K*=3, Mistral K*=1
- **DDL**：EMNLP 2026 ARR May 25（8 天）
- **审稿**：Group C Round 2 进行中。三个 critical：overclaiming（已修）、theta sensitivity（Task A 已完成）、self_BLEU ablation（Task B 进行中）
- **当前 4 个实验目的**：补全 domain × model 覆盖矩阵——arXiv 需要第 3 个模型（OLMo）+ 大模型验证（LLaMA-8B）；Wikipedia 需要跨模型验证（Pythia + OLMo）
- **关键决策链**：D049（arXiv K*=3 升级 framing）→ D050（跨模型验证通过）→ D051（retrain K*≥4）→ D052/D053（dose-response 否定 graduated filtering）
- **易错点**：
  1. 不要再用共享 data 目录——M002 教训
  2. exp_wiki_pythia 的 exp_023_wiki/depth_0.jsonl 是真正的 seed 数据，depth_1+ 是 Qwen 生成的，v2 只复制 depth_0
  3. Theta 敏感性表已完成但 Director 可能还没看到结果——如果 Director 再追问，直接汇报 artifacts/ 路径
  4. 14D ablation 是 Reviewer 明确要求的 per-model 明细，不能只给 "K*=2 stable" 的定性结论
  5. arXiv 实验如果 K*≠3（特别是 LLaMA-8B），需要立即调整论文 framing 中 "structured domain K*=3" 的 claim scope


---
