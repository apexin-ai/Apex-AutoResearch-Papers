# reviewer / loop_7.md

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_7.md`
- **Structured JSON:** [`b8e041d5744abf68b841.json`](../../sessions/b8/b8e041d5744abf68b841.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_wall_time
updated: '2026-05-15T05:00:02+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 `westd-37397`，项目代码目录 `/root/ratekv`，模型/数据在 `/root/autodl-tmp/`
- W2 unconstrained baselines 用了 **2bitonly profiles**（只有 d_h(2)），导致 solver 退化为 {2,16} 二分法——**不能直接放入 Table 2 unconstrained 列**，与 Qwen 的 full-profile 数据不可比。已发 critical 给 Director，等决策
- 论文 baseline PPL 全文用 **eval set = 9.81**（Qwen），W9 实验用 calibration set = 8.20，不能混用
- hires profiling 的 concentration 以 `qwen_hires_float32_d048` 的 **float32 值 0.6104** 为准（P0 统一过）

### 2. 🖥️ 基础设施快照
- 服务器：`westd-37397(root)`，项目路径 `/root/ratekv`
- Python：conda base `/root/miniconda3/bin/python`
- 模型路径：Qwen `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B`，Yi `/root/autodl-tmp/.hf_cache/01ai/Yi-1___5-9B`，Llama `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B`，Mistral `/root/autodl-tmp/models/Mistral-7B-v0.3`，Gemma-2 `/root/autodl-tmp/.hf_cache/google/gemma-2-9b`
- Calibration data：`/root/ratekv/calibration_hires.json`（64 seq × 2048 tok）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/`
- 论文 tex：`docs/paper/`（main.tex, method.tex, analysis.tex, experiments.tex, related_work.tex）
- 无活跃训练进程，无 cron，无 wandb

### 3. 📊 当前状态
**已完成审查并发报告给 Director 的**：
- ✅ method.tex W6+W8 写作审查 → PASS（info 级，建议 W9 formal transition 补充）
- ✅ related_work.tex W7 写作审查 → PASS（warning: "Don't Waste Bits!" 引用遗漏）
- ✅ W2 unconstrained baselines 审查 → **CRITICAL**（profile 类型不一致，{2,16} 退化）
- ✅ W9 compounding scaling 审查 → **WARNING**（Layer-0 饱和伪信号，非渐进 compounding；大 n PPL 非单调）
- ✅ 论文全数字一致性审计 → PASS（无实质不一致）
- ✅ Gemma-2 hires profiling 审查 → PASS
- ✅ 图表（heatmap + scatter）数据一致性审查 → PASS
- ✅ Director Action Matrix 独立审查（7 点反馈）

**Registry 状态**：
- `w2_unconstrained_baselines`: PREPARING（实际已完成但 registry 未更新）
- `w9_compounding_scaling`: PREPARING（同上）
- 其余实验全 DONE

**等待中**：
- Director 对 W2 critical 的决策（选项 A/B/C）
- 更多 writing worker 完成通知（W1 新模型、W3 downstream、W10 headline switch 等）

### 4. 📋 待办
- W2 Director 回复选项 A（full profile 重跑）→ 审查新实验设计是否用了 {2,4,8,16} full profiling
- W2 Director 回复选项 B（改叙述为 stress test）→ 审查论文措辞是否准确反映实验设计
- W9 如有重跑（solver marginal benefit ranking 选 head）→ 审查是否排除 Layer 0 heads、是否用 eval PPL
- 新 writing worker 完成 → 按 §5 章节审查维度审查（特别注意 Table 2 unconstrained 列填入什么数字）
- experiments.tex 更新 → 核实 "11.23±0.06" 混用问题是否修复（W10 要求 headline 改为 10.99±0.06）
- 任何新实验结果 → 标准审查流程（registry vs 代码 vs 论文声明交叉验证）

### 5. 🎯 战略上下文
**项目核心**：Per-head KV cache quantization with cardinality constraint。5 个 7-9B 模型中仅 Qwen 受益（-27.3%），其余 4 个 negative result（Flat/Spike 分类）。Round 1 审稿 Weak Reject 2.25/5，正在逐条 rebuttal。

**最容易判断错的**：
1. **W2 数据看起来很震撼（PPL 672-1220）但不能直接用**——profile 类型不一致导致 86% 2-bit 是人为产物，不是 solver 真实行为。Qwen 用 full profile 只有 60% 2-bit。
2. **W9 的 ratio 300-500× 听起来很强但是 Layer-0 饱和伪信号**——n=4 刚好是 Layer 0 全部 4 个 KV head，这是层级灾难不是渐进 compounding。有价值的只有 n=1 (ratio=1.0) 和 n=2 (ratio=3.84)。
3. **"2bitonly" profiles 与 "full" profiles 的区别**：2bitonly 只测了 d_h(2)，没有 d_h(4)/d_h(8)。full profile 测了所有 bit-width。Qwen 的已有数据（Table 4/Fig 2）都基于 full profile。用 2bitonly 跑 solver 会让 4-bit/8-bit distortion = 0，solver 被误导。
4. **"Don't Waste Bits!" 引用**被 W7 worker 跳过，reviewer 原文提了这篇。


---
