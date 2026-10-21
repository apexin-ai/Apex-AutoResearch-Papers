# agent / loop_1.md

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`a327a990081ae26cad59.json`](../../sessions/a3/a327a990081ae26cad59.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-22T00:31:53+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 分配：cuda:0,1 = Qwen3-32B vLLM (port 8000)，cuda:2,3 = Llama-70B vLLM (port 8003)。不可挪用、不可停 vLLM
- OpenRouter API key = `tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8`，model = `google/gemini-2.5-flash`，endpoint = `http://47.94.22.126/v1`
- BT 分析必须用 ALL pairs（含 inconsistent），choix.ilsr_pairwise，10000 bootstrap，seed=42。不可只用 consistent pairs
- GEE 数字源统一用 `csd_pipeline/gee_diagnostics.py` 的 NLI≥0.90 过滤结果（D041 决策）
- EMNLP 2026 deadline: May 25 AoE

### 2. 🖥️ 基础设施快照
- 服务器：westb-29275，SSH `ssh -p 29275 root@connect.westb.seetacloud.com`
- 环境：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 工作目录：`/root/causal_style_decomp_judge`
- 数据盘：`/root/autodl-tmp/`（模型在此）
- Qwen3-32B：`/root/autodl-tmp/models/Qwen3-32B/`，Llama-70B：`/root/autodl-tmp/models/LLM-Research/Llama-3.3-70B-Instruct/`
- NLI：`/root/autodl-tmp/models/nli-deberta-v3-large/`
- 活跃进程：vLLM Qwen3-32B (port 8000, GPU 0,1)，vLLM Llama-70B (port 8003, GPU 2,3)
- HF 网络必须 `TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1`

### 3. 📊 当前状态
**刚完成：**
- Gemini Flash 4th judge 实验：DONE/success，两轴 Blindspot confirmed（8/8 矩阵）
- Forest plot 重新生成（4 judges），已放 `docs/paper/figures/forest_plot.pdf` + `artifacts/figures/paper/`
- Figure 1 候选提取完成（`artifacts/figure1_candidates.json`），推荐 mvp_0048
- experiment_plan.yaml 更新 5 个 stale 条目（exp-020~024 → done）
- Paper tex 文件已含 Gemini 数据（7 文件 patch + GEE 数字修正 by Director）

**Registry 非 DONE 实验：**
- `register_100_cf`: QUEUED — blocked on API 402（register axis scoring），低优先级

**无等待中的 Worker/Cron 回调。**

### 4. 📋 待办（条件触发式）
- Director 选定 Figure 1 候选 → 按选定 example 生成正式 Figure 1 图（可能需 draw-paper-figure skill）
- Director 要求 Gemini register axis → spawn worker 跑 `gemini_flash_scoring.py` 加 register 数据
- Director 要求 debiased Gemini → spawn worker 跑 correction PoC on Gemini（同 API key）
- 论文 compile 失败 → 检查 tex 语法（Gemini patch 可能引入格式问题）
- `register_100_cf` API 恢复 → 重启 scoring

### 5. 🎯 战略上下文
**核心结论链：** C1 Blindspot 8/8 confirmed (4 judges × 2 axes) → C2 measurement attenuation (bootstrap d≈0 + 100pt + power analysis) → C3 axis gradient (verbosity=Pure Style OR 8-13, formality=Mixed, register=judge-dependent) → C4 correction resistance (5/5 still sig after debiasing)

**Gemini 的 nuance：** formality Style OR=1.64 NS（唯一 GEE style 不显著的 cell），但 BT 仍 sig (p=0.0306)。论文措辞："BT detects in all 4 judges, GEE attributes primarily to originality in Gemini"——不要说 Gemini has no formality bias

**易错点：**
- Verbosity 数据 mvp_0041 缺 1 trial（Gemini API 返回 None），171 comparisons not 172
- Placebo 检测的是 rewriting artifact ≠ format amplification（概念区分，Director/Reviewer 多次纠正）
- experiment_plan.yaml 中 exp-007b 和 exp-008 仍 in_progress（分别是 verbosity_32b 和 register_100_cf，均 blocked on old API issue）——这两个可能也需要 Director 确认是否该标 done


---
