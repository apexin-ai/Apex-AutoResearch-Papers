# agent / loop_13.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_13.md`
- **Structured JSON:** [`c01dbce7ea81520beff5.json`](../../sessions/c0/c01dbce7ea81520beff5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: idle_timeout
updated: '2026-05-19T12:17:45+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: westd-34887 cuda:0,1 + westd-41718 cuda:0,1，共 4 张 A6000。禁止使用任何白名单外 GPU
- HF 必须离线模式: `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache`，否则网络请求超时
- 论文 mask visualization 数据必须引用 **64-sample** 版本（Jaccard@50%=0.682, @30%=0.463），不是早期 16-sample
- C1@50% max Δ 已被 D073 修正为 **0.79pp**（非旧值 0.59），且仅 1-seed 非 2-seed。论文中若残留旧值必须改
- 14B Qwen 实验只能在 westd-34887 跑（98GB VRAM 需求，41718 不够）
- submit_training_job 命令必须自带 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不能假设 .venv

### 2. 🖥️ 基础设施快照
- **westd-34887**: 2×A6000, 工作目录 `/root/distill_sparse_swiglu/`, Python `/root/miniconda3/bin/python`, conda env=base
- **westd-41718**: 2×GPU, 同一工作目录结构, checkpoints 包含 kl_sparsity25/30, mvp_kl_norm_v2, c1_ablation 系列
- 模型路径: `/root/autodl-tmp/models/llama-3.1-8b` (LLaMA), Mistral/Qwen 路径在各实验 spec 中
- HF cache: `/root/autodl-tmp/.hf_cache`
- 活跃进程:
  - `qwen14b_kl30_s123_eval_v4` PID=100832 on westd-34887, cron 监控中
  - `qwen14b_kl30_s456_eval_v2` PID=100060 on westd-34887, cron 监控中
- 活跃 Worker: `worker_analysis_flops-overhead-table_20260519T121505` (running, turn 11, 在做 FLOPS overhead 表格分析)
- 本 session 无 CronCreate 记录，但 reconcile_crons 确认两个 eval 实验仍在跑

### 3. 📊 当前状态
**刚做完**: Round 12 审稿 (D073) 产出 action matrix + Mistral HellaSwag/PIQA 补全（`mistral_kl30_hellaswag_piqa` HS=0.6892 PIQA=0.7519, dense baseline HS=0.832 PIQA=0.8188, 均 DONE）。Paper tex 文件最后修改 08:29-08:31 UTC 今天，已整合 Round 11 多数 patch。

**正在跑的实验** (2 RUNNING):
- `qwen14b_kl30_s123_eval_v4`: 14B s123 multi-seed eval (WikiText-2 PPL + 5 downstream), v2/v3 都因 OOM 失败, v4 是杀掉 orphan PID 93142 后的重试
- `qwen14b_kl30_s456_eval_v2`: 14B s456 multi-seed eval, 同样配置

**ANALYZING 未完结** (2):
- `qwen14b_kl30_s456`: 训练完成 conclusion=success, 但 eval 结果还在上面两个 RUNNING 实验里
- `qwen14b_kl30_s123`: 训练完成但 conclusion 未设

**等待中**:
- FLOPS overhead table Worker 完成回调
- 两个 Qwen-14B eval cron 回调

### 4. 📋 待办（条件触发式）
- `qwen14b_kl30_s123_eval_v4` cron 回调 → 提取 metrics → update_registry → 与 s42 eval 对比确认 MMLU 反转是否跨 seed 一致
- `qwen14b_kl30_s456_eval_v2` cron 回调 → 同上处理 → 三种子齐备后向 Director 汇报 14B multi-seed 完整结论
- 14B 三种子齐备 + MMLU 反转确认 → 更新论文 14B 段落（experiments.tex 14B section）
- FLOPS overhead table Worker 完成 → 整合到论文 appendix 或 method
- **D073 action matrix 执行**（Round 12 修复，部分可能已被上一轮 session 做了，需核实）:
  - N1: C1@50% max Δ 改为 0.79pp, 标注 1-seed → 检查 experiments.tex + appendix.tex
  - N2: Table 2 "BCE+comp" 标签改为 "BCE (staged)" 或删除; Table 4 删除 BCE+Comp 行
  - C1 → "Target-Swap Ablation" 全文 rename
  - Taxonomy 软化（"suggestive" 而非 "proves"）
- Mistral HellaSwag/PIQA 数据（已 DONE）→ 补入 Mistral cross-arch 对比表（experiments.tex Table）
- 所有数据整合完 → Round 12 review（continue mode）→ 最终 ARR 提交

### 5. 🎯 战略上下文
- **DDL: 2026-05-25 ARR May cycle，还剩 6 天**
- **当前审稿评分: 3.0 Findings**，目标冲 4.0 Main Conference
- **核心结论链**: KL distillation 发现了与 magnitude-based oracle 本质不同的 neuron importance pattern (53% Jaccard divergence)。C1 causal ablation 证明 target quality 是 KL 优势的唯一来源（gradient coupling = 0 贡献）。跨架构 (Mistral) + 跨 scale (Qwen-14B) 验证
- **最易判断错的事**:
  1. 14B MMLU 反转 (KL < TEAL) 是真实的 scale-dependent 现象，不是 bug。论文定位为 "valuable negative finding revealing loss × allocation × scale three-way interaction"，不要试图修复它
  2. Mistral downstream 表格现在有 6 个 task（ARC/WG/MMLU/GSM8K/HS/PIQA），但 HS/PIQA 来自独立实验 `mistral_kl30_hellaswag_piqa`（不是 `mistral_kl30_downstream`），合并时注意来源
  3. `qwen14b_kl30_s123` 的 conclusion 字段还是空的（ANALYZING 状态），别误以为它失败了
  4. 论文中 BCE+Comp 相关内容是 D073 要求删除/修正的重灾区——Table 2 标签虚假（实际无 compensation）、Table 4 protocol 不一致（per-token vs TEAL），必须彻底清理
  5. C1 ablation 有两套数据：旧 oracle（s42 max Δ=7.85pp 异常）vs retrained oracle（s123/s456 max Δ=1.70pp）。论文只能用 retrained 版本


---
