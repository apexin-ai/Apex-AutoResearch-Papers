# reviewer / loop_3.md

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`d0d4324427942c41695a.json`](../../sessions/d0/d0d4324427942c41695a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-14T10:07:32+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（westd-37397），两张均已分配给 ratekv
- 模型路径必须用 `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B`（注意双下划线），HF_HOME=/root/autodl-tmp/.hf_cache
- experiments.tex 现在有两套 profiling 分辨率：hires (64seq×2048tok, PPL=10.91) 和 standard (16seq×512tok, PPL=11.23)。Table 1 用 hires（带†），Tables 2-3 用 standard。审查时必须分清数据来源
- Table 3 Mistral MCKP 值待修：当前 7.32 对应 k=18 但 caption 写 k=16，正确值应为 7.31（k=16, PPL=7.3106）。已通知 Director，可能已修复也可能还没

### 2. 🖥️ 基础设施快照
- 服务器：westd-37397 (root)，工作目录 /root/ratekv
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型：/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B（Qwen2.5-7B），Llama/Mistral 同目录下
- W&B：未配置（不检查 W&B）
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/
- 论文文件：docs/paper/{experiments,method,analysis}.tex + references.bib
- 活跃进程（截至 handoff）：
  - GPU 0: PID 199409, run_multi_seed.py (nohup, 45.7GB)
  - GPU 1: PID 210299, run_c4_rerun.py (tmux c4_rerun_d032, 67.2GB)

### 3. 📊 当前状态
**已完成审查**：
- experiments.tex CRITICAL 修复验证 → PASS（Mistral k=16/18 minor 残留）
- method.tex → PASS（数据全部验证通过）
- analysis.tex → PASS（diagnostic threshold n=3 弱，K compressibility 解释可商榷）
- runtime_benchmark 结果 → WARNING（simulate-only, MCKP 比 bf16 慢 36%，只有 solver cost 5ms 和 theoretical memory 对论文有用）
- bib 修复 → PASS
- GPU1 自动重启调查 → PASS（无自动重启机制）
- Mistral bit dist 确认 → WARNING（k=18/k=16 不一致已确认）

**RUNNING 实验**：
- multi_seed_error_bars：GPU 0，多 seed 验证，提供 error bars
- c4_rerun (c4_cross_dataset_eval_v2 替代)：GPU 1，真 C4 数据 + cal/eval 分割 + concatenation

**PREPARING**：
- cross_domain_calibration_v2：等 GPU 空闲

### 4. 📋 待办
- multi_seed 完成 → 核查 error bars 数据，验证 Table 1 的 single-seed 结果是否在 confidence interval 内
- c4_rerun 完成 → 核查 (1) MCKP allocation 与 WT2 profiling 的 agreement rate，(2) C4 eval PPL 改善幅度是否与 WT2 一致，(3) C4 baseline PPL=12.65 下的 MCKP 相对收益
- 论文新章节写作提交审查 → 按 Section 5 标准做对抗审查（Introduction/Related Work/Conclusion 尚未写）
- paper_agent_request_review 触发 → 必须用 §5.3 维度评分模板（Originality/Clarity/Soundness/Significance/Presentation + Overall 1-10）
- Director 转发 Framing 调整提案 → 立即 Read negative-framing-review skill，四维度审

### 5. 🎯 战略上下文
- 项目目标：EMNLP 2026 ARR（截稿 May 25），核心贡献是 cardinality-constrained MCKP for KV cache quantization
- 核心结论链：MSE falsified (D005) → pivot to quant-only MCKP (D007) → cardinality constraint (D009) → MVP PASS (D010) → Plan B framing (D015)
- **关键 narrative**：MCKP 仅在高 GQA ratio 架构上有效（Qwen 7:1 → +29.3%），低 GQA 无效（Llama +0.2%, Mistral -0.4%）。这是 honest negative result，论文已正确框架
- **最容易判断错的事**：10.91 vs 11.23 不是 bug，是 hires vs standard profiling 的差异。论文已通过†标注和 footnote 解决。不要重复 flag 这个问题
- **GPU 预算**：两张 RTX PRO 6000 (98GB each)，弹性扩容可通过 Manager 申请。当前两张都被占满，c4_rerun 完成前无法启动新 GPU 实验
- **数据污染教训**：c4_calibration.json 曾混入 WikiText 数据（"@-@" tokenization artifact），v1 实验结果全部 invalidated。c4_rerun 使用验证过的真 C4 数据


---
