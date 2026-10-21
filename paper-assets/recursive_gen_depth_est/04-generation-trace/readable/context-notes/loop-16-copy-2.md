# reviewer / loop_16.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_16.md`
- **Structured JSON:** [`cc933d923c5575ca9064.json`](../../sessions/cc/cc933d923c5575ca9064.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: max_wall_time
updated: '2026-05-22T18:16:20+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **cuda:0**（服务器仅 1 张 RTX PRO 6000 Blackwell 96GB）。GPU 白名单 = [0]。
- accumulation 实验中 OLMo 使用 **temp0.9** 而非 nucleus——Tab 10 和行文已修正，不要再改回 "all nucleus"。
- Pythia accumulation 脚本 `baseline_full_replacement` 硬编码 0.8428 是**错误的**（那是 GPT-2 XL 的值），Pythia atlas = 78.7%。Registry 的 `delta_vs_full_replacement` 不可引用。
- D015 硬约束：Limitations 必须包含 per-strategy d1v2 reversal 数值（0.13 temp / 0.25 OLMo）——当前已在 conclusion.tex:9，勿删。

### 2. 🖥️ 基础设施快照
- 服务器：**gpu-6000pro-2**，工作目录 `/root/autodl-tmp/recursive_gen_depth_est`
- Python：`/root/miniconda3/bin/python`，conda base 环境
- 模型路径：`/root/autodl-tmp/models/qwen25_7b`（Qwen2.5-7B FP16）
- 数据：`/root/autodl-tmp/recursive_gen_depth_est/data/`（9-cell atlas 数据 + qwen25_7b/ 生成中）
- 论文源码（本地）：`projects/recursive_gen_depth_est/docs/paper/`
- 活跃进程：**qwen25_7b_selfref_001**（PID 825150, tmux=qwen25_7b_selfref_001, cuda:0）——Phase 3.1a LoRA finetune d0, ~94/939 steps @ 1.35s/step（截至上次检查，进程已运行 ~2.5h）

### 3. 📊 当前状态
**刚完成**：
- M3/M4/M5 闭环评估已提交 Director（M3 闭环、M4 部分闭环、M5-Bino 闭环、M5-seed 部分闭环）
- LLaMA-3 AUC 验证：Table 21 的 0.965/0.874 错误值已被修正为正确的 0.949/0.877，我已独立核实
- CPI Table 7 审查：发现 CI width "< 0.5" 声明与源数据矛盾（实际 0.78-3.67），已报 Director [warning]
- Tab 10 accumulation 策略标注已修正（"all nucleus" → 正确标注）
- Scale narrative 预评估：7B ≥60% 能将 R17-N2 从 critical 降为 warning，提升 ~0.25-0.5 分

**RUNNING**：qwen25_7b_selfref_001——Qwen2.5-7B FP16 self-ref 全管线（generate d0-d3 → LoRA finetune × 3 → feature extraction → RF classify），预计总 6-10h

**等待中**：qwen25_7b_selfref_001 完成 → 审查结果（target: 4-class acc ≥60%, EDD₀.₇₀ ≥2）

### 4. 📋 待办
- **qwen25_7b_selfref_001 完成** → 核实 4-class accuracy / pairwise AUC / EDD / top features，对比 14B self-ref (50.8% EDD=0) 和 1.5B self-ref (78.7% EDD=3)；若 ≥60% EDD≥2 → 报 Director "monotonic attenuation confirmed, R17-N2 partial mitigation"；若 <50% → 报 "7B self-ref fails, scale cliff earlier than expected"
- **CPI Table 7 修复后** → 核实新版表格 CI width 值是否与源数据 (`results/conditional_pi/summary.json`) 一致
- **论文新编辑出现** → 检查 Discussion scale 段落是否加入 7B 数据（取决于实验结果）
- **DDL 倒计时**（May 25, 3天）→ 监控是否有新实验启动，评估 GPU-hours 预算是否充足

### 5. 🎯 战略上下文
- **论文定位**：EMNLP 2026 ARR Findings（非 Conference），task formalization + empirical benchmark 为核心贡献，方法论零创新已 acknowledged
- **模拟审稿评分**：Overall ~3.0-3.5（Findings 门槛 3.0），Novelty 是最大弱点（R17-N5 critical）
- **R17-N2 是 P1 priority**：14B EDD=0 的 self-ref confound 是最重要的 open critical issue。qwen25_7b_selfref_001 是唯一在飞的实验来缓解它
- **易错判断**：
  - 不要将 Pythia 1.4B self-ref (78.7%) 与 Qwen 7B self-ref 做 "clean scale comparison"——跨了架构（Pythia vs Qwen），只有 Qwen 7B→14B 是 within-family
  - 7B 实验用 QLoRA 4-bit（早期）vs FP16（当前 selfref_001）——结果不可直接混用。Table 20 (tab:cross_scale) 的 Qwen2.5-7B 60.1% 是 QLoRA 版本
  - cross-seed table (B.16) 中 GPT-2 XL seed=42 的 84.28% 就是被错误复制到 Pythia accumulation baseline 的那个值
  - Registry 总量 152 条实验，大量是 invalidated/superseded，不要引用旧的 accum_mix50（feature-space mixing 错误版本）


---
