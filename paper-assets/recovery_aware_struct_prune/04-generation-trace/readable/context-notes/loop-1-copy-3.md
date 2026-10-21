# reviewer / loop_1.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`a8096131d5acfc3a9535.json`](../../sessions/a8/a8096131d5acfc3a9535.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-14T06:15:40+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 cuda:0 和 cuda:1（westb-23072 的 constraint C001）
- 18944 / 28 = 676 余 16：MLP 分组有 16 个 orphan channels 被隐式丢弃，不影响结论但论文需注明
- correlation_analysis.py 用 `from prune import ...`，必须从 src/ 目录运行或确保 PYTHONPATH 包含 src/
- 服务器无外网（HF Hub 不可达），GSM8K 数据集依赖本地缓存 `/root/.cache/huggingface/datasets/openai___gsm8k/`

### 2. 🖥️ 基础设施快照
- 服务器：westb-23072 (root)，2× NVIDIA RTX PRO 6000 Blackwell 98GB
- 工作目录：`/root/recovery_aware_struct_prune`，Python：`/root/miniconda3/bin/python3`（conda base）
- 模型：`/root/recovery_aware_struct_prune/models/DeepSeek-R1-Distill-Qwen-7B` → symlink → `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B`（15GB, BF16, Qwen2ForCausalLM, 28层, 28Q/4KV heads）
- 论文文件在远程：`/root/recovery_aware_struct_prune/paper/{method.tex, related_work.tex}`（无 main.tex/bib）
- W&B 未配置（report_to="none"），日志走本地 logging_dir
- 活跃进程：**无**。两张 GPU 完全空闲。旧 pipeline 已清理，models/ 下只剩模型 symlink，results/ 已清空

### 3. 📊 当前状态
- **mvp_rasp_pipeline**: registry 标 DONE/failed。原因：旧 prune.py 逐 Q head 剪枝导致 GQA 违规 + RASP 零 attention 剪枝
- **代码修复已完成并通过审查**：prune.py（GQA group 粒度）、importance_score.py（GQA 聚合）、cka_overlap.py（GQA group CKA）、correlation_analysis.py（attention+MLP 双模式 recoverability）
- **run_mvp.sh 已更新**：CKA+importance 并行、增加 post-prune eval、修正 JSON 解析
- **论文 method.tex + related_work.tex 已审查**：写作质量好，引用全部真实，但有 4 个 warning（见下方战略上下文）
- **literature_map.yaml 已创建**：19 篇，缺部分已引用论文，优先级低
- **等待**：Director 确认重跑 MVP pipeline。GPU 空闲中

### 4. 📋 待办
- MVP pipeline 重启通知 → 核实 CUDA_VISIBLE_DEVICES 合规（cuda:0/1）+ 确认新 registry entry 创建
- Step 3 剪枝完成 → **立即检查** standard 和 RASP 各自的 attn/MLP 剪枝比例（RASP 可能仍然零 attention 剪枝，因 F(h) 分布偏差 MLP 0.88-0.99 vs attn 0.19-0.69 → RASP score 差 ~6 倍）
- RASP 零 attention 剪枝确认 → 这不是 bug 而是方法特性，correlation 走 MLP-only ρ 仍可验证 MVP 假设。但需提醒 Director：论文叙事要调整（不能 claim "recovery-aware 保护关键 attention heads"，应 claim "recovery-aware 识别高冗余 MLP 结构优先剪枝"）
- GRPO 训练完成 → 检查 GPU 利用率、loss 曲线、training steps
- correlation_results.json 出来 → 核实 ρ 值、CI、N 是否足够、MVP verdict
- baseline eval 仍缺 → run_mvp.sh 未加未剪枝模型评估，论文需要 baseline→pruned→recovered 三级对比数据

### 5. 🎯 战略上下文
- **核心假设**：Spearman ρ(CKA overlap, RLVR recoverability) ≥ 0.4。pass/fail 阈值：≥0.4 PASS，[0.3,0.4) → 25% sparsity 重复验证，<0.3 FAIL → pivot 到纯 empirical comparison
- **最容易判断错的事**：RASP 只剪 MLP 不是 bug。MLP overlap 极高（0.88-0.99）导致 RASP score 极低 → 被优先剪。这是方法的正常行为。Standard pruning（importance only）应该会产生混合 attn+MLP 剪枝，两者对比本身就是一个发现
- **论文 warning 跟踪**（method.tex 审查中标记的，修复后需回来校准）：
  1. Algorithm 1 伪代码用 structure-count sparsity，代码用 parameter-count sparsity
  2. "Self-calibrated reasoning traces" claim 但代码直接用 GSM8K 原始问题
  3. Stage 3 写 "GSM8K and MATH" 但代码只用 GSM8K
  4. 缺少 F(h) 分布偏差讨论（审稿人必问）
- **SparseGPT 仍未加入 related work**——审稿人可能当 obvious omission
- **目标**：EMNLP 2026 ARR May 25，距今 ~11 天


---
