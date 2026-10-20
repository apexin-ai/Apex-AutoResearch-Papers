# reviewer / loop_6.md

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_6.md`
- **Structured JSON:** [`94bd44efba94da354b58.json`](../../sessions/94/94bd44efba94da354b58.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_wall_time
updated: '2026-05-16T02:17:58+00:00'
---

### 1. 🔴 硬约束 / 红线
- 项目 GPU 白名单：cuda:0-3（autodl-5090 四卡 RTX 5090）。无越界历史，但需持续监控。
- `paraphrastic_chains.py` 的 `load_generations()` 用 glob `"generations_shard*.jsonl"` 加载数据——如果目录里有多个 shard 文件会全部混入。任何往 `data/pythia-2.8b-paraphrase/` 放文件都要注意命名。
- plan-012 系列的 `end_to_end_classifier*.py` 无 sentinel/W&B，cron monitor 会误标 failed——这是已知模式，不要信 cron 的 failed 状态，必须独立验证结果文件。
- Discussion vs Limitations 关于 instruct entropy reversal 存在方法不一致（Discussion 混用 partial_corr_rho + length_matched_rho 得出 "two of three"，Limitations 用 partial_corr_rho 一致得出 "all three"），已报两次 WARNING，尚未修复。

### 2. 🖥️ 基础设施快照
- 服务器：`autodl-5090`（SSH 账号 root），代码根：`/root/gen-depth-fingerprint`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型缓存：`/root/autodl-tmp/models/`（Qwen3 系列）、`/root/autodl-tmp/.hf_cache/`（Pythia/OLMo）
- 参考模型：`/root/autodl-tmp/models/pythia-410m/models--EleutherAI--pythia-410m/snapshots/9879c9b...`
- 结果目录：`/root/gen-depth-fingerprint/results/`
- 无 W&B 配置，无活跃 tmux session
- 当前无活跃进程（所有 GPU 空闲 0%）

### 3. 📊 当前状态
**刚完成**：plan-006-confound-fix 数据污染发现 → 报 CRITICAL → Worker 修复 → 我验证 clean 结果并报告。这是本轮最重要的发现：rp=1.3 confound 导致的 feature direction reversal 被证伪，clean 数据显示 paraphrastic 与 continuation chains depth signal 方向一致、幅度可比。

**Registry 状态**：全部 DONE，无 RUNNING/PREPARING 实验。最近完成的：
- plan-012-qwen06b (DONE): QLoRA Qwen3-0.6B r=16, 5-class F1=0.583
- plan-012-pythia410m (DONE): QLoRA Pythia-410M, 5-class F1=0.556
- plan-012-qwen06b-v2 (DONE): QLoRA Qwen3-0.6B r=32, 5-class F1=0.587（与 r=16 差异 <0.5pp，LoRA rank 不敏感）
- plan-006-confound-fix (DONE): **registry metrics 仍为污染版**（para_3class_f1=0.727），实际 clean 结果为 0.742
- plan-012-xgboost-matched (无独立 registry): matched baseline HGBT 5-class F1=0.497, 3-class F1=0.805

**等待中**：无 Worker 回调。等待 Director 决策：
1. plan-006-confound-fix registry 更新（metrics + plan-006-paraphrastic 的 spearman_signs_reversed: true 需标注 invalidated）
2. Discussion vs Limitations instruct 段落不一致修复
3. Method section "architecturally independent" 措辞修复

### 4. 📋 待办（条件触发式）
- plan-006-confound-fix registry 被更新 → 验证 metrics 是否为 clean 版本（para_3class_f1 应为 0.742 非 0.727）
- 任何新实验启动 → 检查 GPU 白名单合规 + 验证 CUDA_VISIBLE_DEVICES
- Worker 修改 Discussion instruct 段落 → 核对是否统一用 partial_corr_rho（entropy_mean: Qwen3-0.6B=+0.103, Qwen3-1.7B=+0.161, OLMo=+0.364），"all three" 而非 "two of three"
- 论文如拟引用 paraphrastic 对比 → 必须用 clean 数据，确认无 rp=1.3 artifact
- 新论文章节提交审查 → 按 §5 维度审查（claim 可信度 / 叙事逻辑 / 审稿人攻击面），先查 Agent 是否读过 red-section skill

### 5. 🎯 战略上下文
- **项目核心**：ordinal depth estimation（gen-0/gen-1/gen-2+ 三分类），7-feature ensemble 在 LOGO 下 3-class F1=0.789，binary gen-1 vs gen-2+ F1=0.723。QLoRA end-to-end 方法在 matched protocol 下比 handcrafted features 高 6-10pp（3-class）。
- **已证伪的结论**：plan-006-paraphrastic 的 "feature direction reversal in paraphrastic chains" 和 "paraphrastic chains lose depth signal faster" 是 rp=1.3 artifact。Clean 数据显示两种 chain 信号可比。原始 registry 条目 `spearman_signs_reversed: true` 错误。
- **最容易判断错的事**：
  1. 不要相信 cron on_failed 事件——plan-012 系列三个实验全部被误标 failed，实际都成功了
  2. plan-006 有两个版本的结果：`plan006_paraphrastic_comparison_old_rp13.json`（旧，confounded）和 `plan006_paraphrastic_comparison.json`（新，clean）。引用时必须用后者
  3. plan-012 结果 JSON 中的 `baseline_xgboost` / `delta_vs_xgboost` 引用的是 LOGO baseline（plan-009），不是 matched baseline。公平对比应用 `plan012_xgboost_matched.json`（HGBT 5-class 0.497, 3-class 0.805）
  4. `instruct_length_confound.json` 中 Qwen3-0.6B 的 partial_corr_rho entropy_mean = +0.103 **是**正值（reversal），Discussion 混用 length_matched_rho 将其 dismiss 为"all partial |ρ| < 0.02"是 cherry-picking 方法


---
