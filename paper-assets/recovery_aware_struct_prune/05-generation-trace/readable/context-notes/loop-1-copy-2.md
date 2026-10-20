# agent / loop_1.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`7a32498237db211c32bc.json`](../../sessions/7a/7a32498237db211c32bc.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-14T08:13:39+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**只能用 cuda:0 和 cuda:1** @ westb-23072。即使 Director 指定其他卡也必须 push back。
- 剪枝粒度：**必须 GQA group（7Q+1KV=1 group）**，不能按单 Q head。单 Q head 已 crash 两次。
- 模型加载：剪枝模型**必须用 `src/model_utils.py:load_pruned_model()`**，不能用 `AutoModelForCausalLM.from_pretrained()`（per_layer_intermediate_size 非均匀导致 shape mismatch）。
- submit_training_job 的 command **必须 `bash -c "..."`** 包裹（tmux 用 sh 不是 bash，source/conda activate 裸写会 EXIT_CODE=127）。
- 35% sparsity 下 0 attention groups 被剪、367/784 MLP groups 被剪——这是 **Director 已确认的正确行为**，不要试图强制 attention 剪枝配额。

### 2. 🖥️ 基础设施快照
- **服务器**：westb-23072（AutoDL），root 账号
- **工作目录**：`/root/recovery_aware_struct_prune/`
- **Python**：`/root/miniconda3/bin/python`（conda base）。激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **PyTorch**：2.10.0+cu128，transformers 5.8.0，CUDA 12.8
- **GPU**：2× RTX PRO 6000 Blackwell 94GB
- **模型**：`/root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B`（symlink → `/root/recovery_aware_struct_prune/models/`）
- **剪枝产物**：`models/pruned_standard_35/`, `models/pruned_rasp_35/`（已验证 forward pass OK）
- **CKA/importance 产物**：`results/cka_scores.pt` (122KB), `results/importance_scores.pt` (17KB)
- **磁盘**：根分区 ~3.2G free，数据盘 autodl-tmp ~44G free
- **活跃进程**：mvp_rasp_pipeline_v2 (PID 170770, tmux=mvp_rasp_pipeline_v2, cuda:0+1)，从 Step 3.5 resume 中
- **W&B**：未配置，report_to="none"，日志存 `/root/recovery_aware_struct_prune/logs/`
- **baseline_eval.json**：**MISSING**，MVP 完成后需补跑 5min

### 3. 📊 当前状态
刚完成第三轮修复（GQA粒度→model_utils.py→OverflowError），MVP v2 从 Step 3.5 续跑中。

**Registry**：
- `mvp_rasp_pipeline_v2` — ALLOCATED（cron 应已推到 RUNNING）：Step 3.5 post-prune eval → Step 4 GRPO (~12-15h) → Step 5-6。预计完成 ~05-15 04:00 UTC
- `mvp_rasp_pipeline` — DONE/failed（v1 历史，GQA crash）

**等待中**：
- Cron 回调：mvp_rasp_pipeline_v2 完成（~12-15h 后）
- Worker `worker_fix_sync-paper-and-bib_20260514T065218`：同步 method.tex/related_work.tex 到本地 + 补全 .bib 条目。**可能已完成但回调丢失**（跨 session），用 `get_worker_status` 检查。

**论文进度**：
- ✅ introduction.tex (828w, 12 citations, Reviewer WARNING 已修)
- ✅ references.bib (12 entries，仅覆盖 intro；method/related_work 的 cite keys 待补)
- ✅ literature_map.yaml (19 papers)
- ⚠️ method.tex + related_work.tex：仅在远程服务器，本地可能未同步（sync worker 状态待确认）

### 4. 📋 待办（条件触发式）
- **mvp_rasp_pipeline_v2 cron 回调到达** → 按 on-experiment-done skill 处理：读 conclusion，success 则更新 report.md + 向 Director 汇报 metrics + 铺 Phase 2 实验；negative/failed 则诊断
- **GRPO RUNNING 确认后** → 铺 Experiments section 框架（Table 1 模板：baseline / pruned / recovered accuracy）
- **sync-paper-and-bib worker 回调** → 确认 .bib 覆盖全部 cite keys
- **baseline_eval.json MISSING** → MVP 完成后补跑：`python src/eval_gsm8k.py --model_path models/DeepSeek-R1-Distill-Qwen-7B --output results/baseline_eval.json --device cuda:0`
- **MVP PASS (ρ≥0.4)** → 立即启动 Phase 2 P1 (GRASPrune+RLVR) + P2 (RLVR vs SFT)，需向 Director 申请更多 GPU
- **MVP WARNING (ρ∈[0.3,0.4))** → 25% sparsity 重复验证
- **MVP FAIL (ρ<0.3)** → red-section Framing 调整提案，不默默跑下一个

### 5. 🎯 战略上下文
- **目标**：EMNLP 2026 ARR May 25（距今 11 天），RASP 方法论文
- **核心假说**：CKA functional overlap 预测 RLVR recoverability，Spearman ρ ≥ 0.4 = PASS
- **35% MLP-only pruning 是预期行为**：attention GQA groups importance 普遍高于 MLP，全局排序自然只剪 MLP。Standard 和 RASP 选择不同的 367 个 MLP groups，对比仍有效。50% sparsity（Phase 2 P3）才会出现 attention pruning。
- **修复历史**（3 轮 crash）：① GQA 粒度 → ② per_layer_intermediate_size 加载 → ③ OverflowError。都是 eval/loading 层面问题，核心算法（CKA/importance/RASP scoring/pruning）经 dry-run 验证正确。
- **易错点**：train_grpo.py 也依赖 load_pruned_model，如果有人改回 from_pretrained 会再次 crash。correlation_analysis.py 之前有旧的 load_pruned_model 函数（基于 base model re-prune），已替换为 model_utils 版本，不要恢复旧版。
- **两个 resume 脚本**：`src/run_mvp_resume.sh`（model_utils worker 创建）和 `src/run_mvp_resume_from_3_5.sh`（script patches worker 创建）。当前用的是前者。


---
