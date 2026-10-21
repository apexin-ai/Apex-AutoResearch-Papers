# reviewer / loop_1.md

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`8d145bd0e34a275adfbc.json`](../../sessions/8d/8d145bd0e34a275adfbc.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-14T20:52:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- 所有 GPU 任务必须 --device cuda:0，依赖 submit_training_job 的 CUDA_VISIBLE_DEVICES 隔离（之前 shard 1-3 用 cuda:1/2/3 全部 CUDA error）
- plan-001 结果文件曾被 worker 误删一次（plan-002 代码 worker 导致），后续 worker 修改代码时不得清空 results/ 目录
- perplexity_by_depth.json 当前是旧版（642 bytes，缺 median/clean_mean/degenerate_examples），registry 中 ppl_gen0_median=13.5 等指标来自已丢失的修复版（3866 bytes）——引用这些数据前需重跑 Part C
- Qwen 模型名与 experiment_plan 不一致：plan 写 Qwen3.5-2B/0.8B，实际下载 Qwen3-1.7B-Base/0.6B-Base，尚未正式记录替代理由

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090 (root)，4× RTX 5090 (32GB each)
- 工作目录：/root/gen-depth-fingerprint
- Python：/root/miniconda3/bin/python（conda base 环境，非 venv）
- 模型路径：
  - 生成器：/root/autodl-tmp/models/pythia-2.8b, pythia-1b/EleutherAI/pythia-1b, olmo-2-1b-hf/allenai/OLMo-2-0425-1B, Qwen/Qwen3-1.7B-Base (symlink Qwen3-1___7B-Base), Qwen/Qwen3-0.6B-Base
  - 参考模型：/root/autodl-tmp/.hf_cache/EleutherAI/pythia-410m (+ models/pythia-410m/... snapshot)
- 数据：/root/gen-depth-fingerprint/data/（wiki_seed_1000.jsonl, features.csv, generations.jsonl, pythia-1b/ 子目录已完成）
- HF_HOME=/root/autodl-tmp/.hf_cache
- 无 wandb 配置

### 3. 📊 当前状态
**刚完成**：plan-002-pythia1b-s0/s1 审查（数据合规，但 Pythia-1B 深层退化严重——repetition loops at d3/d4）；D005 framing 变更四维度审查（PASS，level/diversity vs shape 科学上更准确）；plan-001 ablation 全量结果审查（3 轮：初始 CRITICAL → 修复后 WARNING → 10-fold bootstrap 最终版确认）。

**Registry 活跃实验**：
- plan-002: RUNNING — cross-generator 数据生成。round1 pythia-1b 已完成，OLMo-2-1B 在 cuda:2/3 运行中。round2 (qwen3-1.7b + qwen3-0.6b) 待启动
- plan-002-olmo2-s0/s1: PREPARING — OLMo generation 进行中（~50% GPU util）
- plan-001-restore: PREPARING — 结果恢复任务

**等待中**：OLMo-2-1B shard 完成回调 → 审查数据质量 → round2 启动后审查 Qwen 生成质量

### 4. 📋 待办
- plan-002-olmo2 shard 完成 → 审查输出记录数 + 检查是否有类似 Pythia-1B 的退化
- round2 (qwen3) 启动 → 验证 GPU 分配 + --device cuda:0 + 模型路径正确
- plan-002 全部 5 生成器数据完成 → 审查特征提取 + leave-one-generator-out CV 结果，**重点关注：per-generator depth signal 是否因退化程度不同而差异巨大**
- plan-003 启动 → 核心检验：换参考模型后 entropy_mean 是否仍 drift（若否则 D005 level/shape framing 崩塌）
- perplexity_by_depth.json 修复版未恢复 → 论文引用 median PPL 数据前必须重跑 Part C

### 5. 🎯 战略上下文
**决策链**：D001(MVP方案) → D002(MVP PASS进研究) → D003(预注册 Plan B: complementary signal) → D004(surface>reference, dual dynamics) → D005(level/diversity vs shape 分界，entropy_mean 是关键证据)

**核心结论**：surface_only (0.76) > reference_only (0.72)，原 Claim 2 "Fingerprint Independence" 被否定。新 Claim 2 "Dual Dynamics" 已通过四维度审查。full (0.82) 显著优于两个子集（Bonferroni-corrected bootstrap p=0.0）。

**最容易判断错的事**：
1. 不要把 surface/reference 的来源区分等同于 H1/H2 的分界——entropy_mean 是 reference 特征但呈 H2 drift，这是新 framing 的核心证据
2. Pythia-1B 深层文本严重退化（repetition），分类准确率可能虚高——不能因为 per-generator F1 高就断言方法在所有生成器上都有效，需看退化程度是否人为放大了 depth signal
3. plan-001 的 ablation 跑了 3 次（初始 5-fold → 修复版 5-fold → 最终 10-fold bootstrap），最终版数字略有不同（ref=0.716 vs 初始 0.719），以 results/ablation_results.json 中 10-fold 版为准


---
