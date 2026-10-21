# director / loop_2.md

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`399edb479468b8e757e7.json`](../../sessions/39/399edb479468b8e757e7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-15T12:14:29+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:0 @ cqa1-38874（gpu_ids 白名单只有这一张）
- SDGD 实验必须用两阶段架构（CPU decompose → GPU extract），单进程会 vLLM fork 死锁（exp-008 已踩过）
- MAVEN 实验必须用 Qwen3 embeddings（`maven_bcs_matrix_qwen3.pt`），不要用 MiniLM 版本做正式实验（MiniLM 仅用于 ablation 对比）
- LLaMA 模型来自 `nvidia/Llama-3.3-70B-Instruct-FP8`，绝不能用 `neuralmagic` 版本恢复下载（shard 不兼容，会损坏模型）
- output_seed0 目录（92GB）不动——可能是别的项目的

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-38874 (connect.cqa1.seetacloud.com)，root 用户
- 工作目录：`/root/schema-dag-extraction`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- Qwen3-32B-FP8：`/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/`
- LLaMA-3.3-70B-FP8：`/root/autodl-tmp/.hf_cache/llama-3.3-70b-instruct-fp8/`（15/15 shards，72.7GB，已验证）
- MAVEN 数据：`valid.parquet`（8042 sentences, 149 active types）
- FewRel 数据：80 relations，configs/fewrel_relation_types.json
- 活跃进程：FewRel formal exp1 (PID 263125, tmux, cron 监控中)
- Dream 运行中：`dream_20260515T113743`（full review mode），等回调

### 3. 📊 当前状态
**刚做完**：exp-008 SDGD-zero 诊断（负面结果 F1=0.251 < baseline 0.445）+ SDGD v2 改进方案实现（min_batch_size + confidence merge）+ 2×3 embedding ablation 矩阵完成 + paper_framing.md 多次精化到 D013

**运行中**：
- `exp_fewrel_formal` (PID 263125, cuda:0) — FewRel formal exp1+exp2，~5.5h
- `dream_20260515T113743` — full review，等回调
- SDGD v2 代码已就绪（CPU decompose 脚本 + GPU extract 脚本），等 GPU

**等待**：
- FewRel formal cron 回调 → 三层分析
- Dream 回调 → 按 dream-report-action skill 处理
- Agent 刚 RESET，新 session 会读 handoff 继续

### 4. 📋 待办
- FewRel formal 完成 → 立即跑 `analyze_fewrel_results.py` 三层分析 → 汇报 go/no-go
- FewRel 分析完 → 启动 exp-012 LLaMA multi-model（脚本已就绪，`max_model_len=4096`）
- exp-012 完成 → SDGD-zero v2 重跑（min_batch_size=8 + confidence merge），对比 baseline
- SDGD v2 后 → SDGD MAVEN MiniLM（CPU decompose 已完成，GPU extract 待跑）
- Dream 回调到 → 按 dream-report-action skill 逐条处理
- 所有实验完成 → 激活 Paper Agent 写初稿

### 5. 🎯 战略上下文
**决策链**：D005(MVP pass) → D008(证据重构 pairwise 为主) → D009(BCS proxy task-specific) → D011(方案A: aggregation confound narrative) → D012(pairwise primary, per-type secondary) → D013(centrality confound 精化) → D014(SDGD-zero 失败,需改进)

**核心结论**：Pairwise confusability 跨 NER/ED/RE 三任务普遍存在（Few-NERD Qwen3 r=0.156, MAVEN MiniLM r=0.120, FewRel batch Δ=-50pp）。Per-type aggregation 在同域 schema 有 centrality confound（MAVEN per-type 两种 embedding 都正向）。SDGD-zero v1 因 merge amplification 失败，v2 待验证。

**易错点**：
- 不要把 batch-level 正相关（BCS→高 F1）当作支持假设的证据——那是 frequency/centrality confound
- 不要混淆 per-type mean BCS（有 centrality confound）和 pairwise SCS（干净信号）
- SDGD 实验必须用两阶段架构，否则 vLLM fork 死锁
- FewRel pilot 用了 MiniLM embedding，正式实验已切 Qwen3
- `run_fewrel_formal.py` 默认 model_path 已修正为正确路径，但要确认 `--mode` 参数不能漏
- Dream 之前崩过一次（infra bug），已自动重试，当前 dream 是第二次


---
