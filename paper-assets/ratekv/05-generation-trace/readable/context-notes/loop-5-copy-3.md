# reviewer / loop_5.md

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`dc1acf7132451c332782.json`](../../sessions/dc/dc1acf7132451c332782.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-14T18:35:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-37397 只有 2 张 GPU（cuda:0, cuda:1），项目可用两张，但同时跑两个实验时必须各占一张不能抢
- AutoDL 根分区 ~30GB，模型/数据/HF cache 必须放 `/root/autodl-tmp/`，`HF_HOME=/root/autodl-tmp/.hf_cache`
- 72B 模型下载因磁盘空间不足被 Director 紧急终止过（qwen72b_profiling killed），不要再尝试除非先确认磁盘空间
- `run_hires_quant.py` 使用 `solve_mckp`（unconstrained），论文主表用 `solve_mckp_constrained` + `max_2bit=8`——对比时注意 solver 差异

### 2. 🖥️ 基础设施快照
- 服务器：westd-37397(root)，工作目录 `/root/ratekv`
- Python：`/root/miniconda3/bin/python`，conda base env（不用 venv）
- 激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型缓存：`/root/autodl-tmp/.hf_cache/`（Qwen2.5-7B, Llama-3.1-8B, Mistral-7B-v0.3, Gemma-2-9B, Yi-1.5-9B 均已下载）
- HF datasets 缓存：`/root/autodl-tmp/.hf_cache/datasets/`（wikitext 已缓存，离线可用）
- 日志目录：`/root/runs/ratekv/`（submit_training_job 自动写入）
- 活跃进程：`qwen_hires_float32_d048`（PID 247434, tmux, cuda:0, ~21GB VRAM）
- GPU 1：完全空闲（0% util, 0 MiB）

### 3. 📊 当前状态
**刚完成的审查**：
1. 发现并报告 `hires_quant_profiler.py` 缺少 2-bit profiling（已被修复，旧实验 killed，新实验 `qwen_hires_float32_d048` 已在跑）
2. 发现 Yi-1.5-9B pipeline ImportError 崩溃（`solve_ratequant_greedy` → `solve_greedy_ratequant`），rerun 已由之前 agent 完成
3. 报告 Yi-1.5-9B FAIL 结果对论文 GQA hypothesis 的冲击

**Registry 关键状态**：
- `qwen_hires_float32_d048` — PREPARING（实际 RUNNING，GPU 0）— Qwen 高分辨率 profiling（64×2048，2/4/8-bit）
- `yi15_9b_full_pipeline` — RUNNING（实际已完成，PID 不存在）— 结果在 `yi15_full_results.json`，verdict=FAIL，**registry 未更新**
- `qwen25-hires-profiling` — PREPARING（已被 kill，被 d048 替代）

**等待中**：
- `qwen_hires_float32_d048` 完成回调（112 heads × 3 bitwidths + 3 PPL eval，估计数小时）
- Director 对 Yi-1.5 FAIL + hires solver 不匹配问题的决策

### 4. 📋 待办
- `qwen_hires_float32_d048` worker_done 回调 → 审查 hires profiling 结果，重点对比 standard vs hires 的 bit distribution 是否一致；注意 solver 用的是 unconstrained `solve_mckp`
- Director 回复 Yi-1.5 FAIL 影响 → 审查 paper framing 是否调整（GQA hypothesis 需要 nuance）
- 如有新 Gemma-2 相关实验 → 审查 baseline PPL 711.38 是否正常（9B 模型 WikiText-2 应为 ~7-10，711 极度异常，可能是 evaluation setup bug，我尚未正式报告此问题）
- Yi registry 更新后 → 确认 metrics/conclusion 与 `yi15_full_results.json` 一致

### 5. 🎯 战略上下文
**核心结论链**：
- Qwen2.5-7B：PASS（MCKP 优于 uniform，L0 dominance 高，top-5% concentration ~0.42）
- Gemma-2-9B：PASS（但 baseline PPL 711 **极度可疑**，待核实）
- Llama-3.1-8B：NEGATIVE（MCKP 在 k=2 勉强持平 uniform）
- Mistral-7B-v0.3：NEGATIVE（genuine negative，低异质性）
- Yi-1.5-9B：FAIL（GQA 8:1 最高，但 MCKP 仍劣于 uniform）

**最容易判断错的事**：
1. **不要相信 Gemma-2 结果**——baseline PPL 711 对 9B 模型不合理，MCKP "改善" 65 PPL 可能是假象。如果有人引用 Gemma-2 作为 positive case，先核实 eval setup
2. **GQA ratio 不能直接预测 MCKP 收益**——Yi(8:1) FAIL 而 Qwen(7:1) PASS。真正的区分因子可能是 L0 dominance（Qwen ~5.3x vs Yi 0.07x）和 4-bit heterogeneity
3. **Registry 状态经常过时**——多个实验显示 RUNNING/PREPARING 但实际已完成或崩溃，审查时必须 SSH 核实进程和 GPU 实际状态
4. **solver 有两个版本**——`solve_mckp`（unconstrained）和 `solve_mckp_constrained`（有 max_2bit 约束），论文主表用后者，混用会导致结果不可比


---
