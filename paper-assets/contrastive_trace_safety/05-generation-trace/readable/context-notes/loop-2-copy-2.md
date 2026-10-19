# agent / loop_2.md

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`a1ada775d9ad18da24f2.json`](../../sessions/a1/a1ada775d9ad18da24f2.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-17T20:21:29+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目当前 GPU 分配为 0（无 GPU），所有实验必须 CPU-only 或等 Director 分配
- 服务器 autodl-rtx6000 上 hidden states 已预提取，但 safe trace .pt 文件可能只包含 jailbreak traces（正在确认中）
- 32B 模型 layer index 映射：QwQ L60 = tensor index 60, R1-32B L63 = tensor index 63（已在多个实验验证），但 worker 对 32B 做 PCA-256 降维后跑 LR 是一个 confound，需注意
- references.bib 中的引用已经过 arXiv ID 验证（5/5 confirmed），不要再质疑这些

### 2. 🖥️ 基础设施快照
- 服务器：autodl-rtx6000，工作目录 `/root/autodl-tmp/contrastive_trace_safety`
- Python：`/root/miniconda3/bin/python3.12`
- 包：sklearn 1.8.0, torch 2.10.0+cu128, sentence-transformers 5.4.1
- HF_ENDPOINT=https://hf-mirror.com（必须设置）
- Hidden states 路径：
  - R1-8B: `artifacts/hidden_states/` (LAYERS=[12..24], L14=idx 2, dim=4096)
  - OT-7B: `artifacts/hidden_states_ot7b/` (28 layers, L16=idx 16, dim=3584)
  - QwQ-32B: `artifacts/hidden_states_qwq_32b/` (64 layers, L60=idx 60, dim=5120)
  - R1-32B: `artifacts/hidden_states_r1_32b/` (64 layers, L63=idx 63, dim=5120)
- 本地项目：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/`
- 活跃进程：worker_code_safe_trace_fpr_multimodel_20260517T201744 正在运行（检查 safe trace 可用性）

### 3. 📊 当前状态
**刚完成 Round 5 审稿修复三大任务：**
- Task 1 (PCA-384d): DONE, conclusion=success. 10/12 Holm-Bonferroni reject，modality advantage persists at matched dimensionality. exp_r5_pca384_control 已注册。
- Task 2 (AUROC layer sweep): DONE, conclusion=negative. AUROC 选 mid-depth (~50%) 而非 deep layers (>90%). exp_r5_auroc_layer_sweep 已注册。已报 Director，等决策（加 appendix or 不提）。
- Task 3 (8 references): DONE, 7/8 添加到 references.bib + related_work.tex。Paper 4 "Towards Fully Exploiting LLM Internal States" 未找到。引用总数 38 条。
- arXiv ID 验证：5/5 全部 VERIFIED，无需修改。

**等待中：**
- worker_code_safe_trace_fpr_multimodel_20260517T201744：检查 OT-7B/QwQ/R1-32B 是否有 safe trace hidden states，如有则计算 per-model safe-trace FPR
- Director 对 AUROC negative 结果的决策
- Director 对 PCA-384d 结果写入论文位置的指示

**Registry 状态：** 37+ experiments, 全部 DONE。无 RUNNING/PREPARING。

### 4. 📋 待办
- safe_trace_fpr worker 回调 → 如果有数据：注册 exp，报 Director per-model FPR breakdown，填 experiments.tex TODO；如果无数据：报 Director 需要 GPU 推理
- Director 决策 AUROC → 如果加 appendix：spawn writer worker 写 AUROC layer profile 段落
- Director 指示 PCA-384d 写入位置 → spawn writer worker 写 subsection/appendix
- 论文 experiments.tex L65 有 `[TODO: verify per-model breakdown from artifacts]` 待填（依赖 safe_trace_fpr 结果）
- Bootstrap 10k 用了旧 config（R1-8B L2 W=3 非 L14 W=15），Director 已知，决定不重跑，论文报 1000-resample p-values

### 5. 🎯 战略上下文
- **论文核心发现**：layer selection methodology 可以 reverse 结论。bal_acc × crossing_rate 在 32B 模型系统性选 shallow layers，masking HS advantage。corrected layers 后 12/12 Holm-Bonferroni 显著。
- **DDL**：EMNLP 2026 ARR May 25（8天后）
- **PCA-384d 是本轮最强新证据**：直接反驳 dimensionality confound，precision gains +17-23pp persist at matched 384d
- **AUROC negative 不是坏消息**：它强化了 "layer selection is metric-sensitive" 的主线，但不能 claim "three metrics converge"
- **易错点**：
  - 不要混淆 safe-trace FPR（benign traces 的整条 trace false alarm）和 pre-CP FPR（unsafe trace 在 commitment point 前的 step-level 误报）。论文 caveats 段要的是前者
  - 32B 模型 LR probe 在原始 5120d 时用 solver='liblinear'（saga/lbfgs 太慢），PCA 后可用默认 solver
  - OT-7B 的 Window=3 是 corrected config，不是 W=15
  - R1-32B W=1 coverage 只有 25%（5/20 test traces），这是已知 caveat


---
