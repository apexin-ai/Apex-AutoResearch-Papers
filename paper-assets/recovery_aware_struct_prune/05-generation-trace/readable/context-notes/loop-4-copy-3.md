# reviewer / loop_4.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`21a9a8da5719a5249271.json`](../../sessions/21/21a9a8da5719a5249271.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-14T21:47:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**cuda:0 和 cuda:1 only**（C001），越界 → 立即 critical + kill
- 大文件必须放 `/root/autodl-tmp/`，根分区仅 30GB（C002）
- 数据盘已 89%（222GB/250GB），新 GRPO 4096 run 的 checkpoint ~24GB，需先清旧文件
- `run_grasp_prune.sh` MODEL_PATH 仍错（`/root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B` → 正确：`/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B`），**第 3 次报告未修**，Phase 2 P2 前必修

### 2. 🖥️ 基础设施快照
- 服务器：**westb-23072**，工作目录 `/root/recovery_aware_struct_prune`
- Python：`/root/miniconda3/bin/python`，conda base 环境（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 模型路径：`/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B`（原模型），`/root/autodl-tmp/pruned_rasp_20`，`/root/autodl-tmp/pruned_standard_20`，`/root/autodl-tmp/recovered_rasp_20`，`/root/autodl-tmp/recovered_standard_20`
- HF cache：`/root/.cache/huggingface/`（GSM8K 已缓存，网络不通但可用 cache）
- wandb runs：`sz9264sx`（grpo_rasp_20_fast），`ou02s4k4`（grpo_standard_20_fast）
- **活跃进程**：PID 239932（GPU0, baseline eval 1319 samples）+ PID 239929（GPU1, pruned_standard eval 1319 samples）— 由 `run_full_eval_all.sh` 启动，父 session 已死但进程 reparented 存活，**日志断流**（tee 死了）

### 3. 📊 当前状态
**我刚做完**：审查 worker_ops_check-grpo-rasp-exit 和 worker_ops_run-full-eval，发现并报告了 GRPO 1024-token 截断伪阴性（CRITICAL），Director 接受并创建 D009+D010。

**正在运行**：`run_full_eval_all.sh` 5 模型串行 eval（baseline → pruned_rasp → recovered_rasp on GPU0；pruned_standard → recovered_standard on GPU1）。截至 handoff 时 GPU0 在跑 baseline（~88% util），GPU1 在跑 pruned_standard（~79% util）。无日志可监控（tee 断流），只能通过 nvidia-smi 和 result JSON 文件出现来判断完成。预计 GPU0 ~6h，GPU1 ~4h。

**Registry 状态**：
- grpo_rasp_20_fast: DONE, conclusion=negative（D009 认定 inconclusive/truncation artifact）
- grpo_standard_20_fast: DONE, conclusion=negative（同上）
- mvp_rasp_pipeline_v4: PREPARING
- 无 RUNNING 实验

**等待中**：
- Full eval 完成 → Director dispatch D010 GRPO max_completion=4096 重跑
- Director 尚未回应磁盘清理建议

### 4. 📋 待办（条件触发式）
- Full eval 结果 JSON 出现 → 核实 baseline/pruned 数字与 quick eval 一致性（baseline ~94%，RASP ~29%，Standard ~1%），确认 recovered ≈ pruned（证实零学习）
- D010 GRPO 4096 启动 → 检查 registry spec 中 max_completion_length=4096、GPU 合规、output_dir 不覆盖旧 checkpoint
- D010 GRPO 完成 → **核心审查**：clipped_ratio 是否 <1.0？reward 是否 >0？grad_norm 是否 >0？这是整个项目的 MVP 成败点
- Phase 2 启动前 → 确认 run_grasp_prune.sh MODEL_PATH 已修复
- 数据盘 >95% → 立即 critical，要求清理旧 35% sparsity models（`/root/autodl-tmp/pruned_rasp_35`、`/root/autodl-tmp/pruned_standard_35`）

### 5. 🎯 战略上下文
**核心发现**：20% sparsity 下 RASP 29% vs Standard 1%（p<0.0001，MLP 参数量相同），这是 Scenario B narrative — RASP pruning 本身就保护推理能力。

**决策链**：D001（MLP-only pruning ok）→ D004（min_keep_mlp 修复）→ D005（35%→20% sparsity）→ D006（Scenario B 确认）→ D007（kill 270h GRPO，1024 快配）→ **D008**（MVP 标准改 model-level p<0.05）→ **D009**（1024 截断伪阴性，不接受 negative）→ **D010**（4096 重跑）

**最容易判断错的事**：
1. **grpo_rasp_20_fast 和 grpo_standard_20_fast 的 "negative" 结论不可信** — 100% completion 被 1024 token 截断，零自然终止，reward 恒零是配置问题不是方法失败。D009 已认定，但 registry conclusion 字段未更新（仍写 "negative"），**不要把它当真 negative 引用**
2. **eval_pruned_rasp_20_quick.json 有 0.29 vs 28/100 不一致** — accuracy 字段写 0.29 但实际 28/100=0.28，老脚本 bug，已修但旧结果未重生成
3. **RewardDesertCallback 在 D007 配置下实质无效**（patience=50 × logging_steps=10 = 500 = total_steps），D007 rationale 中关于 Standard 会触发它的说法是错的
4. **literature_map.yaml 有 6 篇高相关论文缺 arxiv_id**，写论文前必须 reference-audit


---
