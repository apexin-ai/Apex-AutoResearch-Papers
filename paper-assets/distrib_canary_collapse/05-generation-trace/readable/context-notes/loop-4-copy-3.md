# reviewer / loop_4.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`fb9d41f8af5561ac6dcd.json`](../../sessions/fb/fb9d41f8af5561ac6dcd.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-14T23:43:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:0 和 cuda:1（westd-19828 两张 RTX PRO 6000 Blackwell 96GB）
- 之前发现过 orphaned dry-run 进程占用 cuda:0 共 14.9GB，已被 kill。审查训练实验必查 nvidia-smi 核对 CUDA_VISIBLE_DEVICES 是否在白名单内
- ssh_read_only 不支持 shell 元字符（`|`, `>`, `$()`），grep 带管道会被 block——用单独的 grep 命令或 tail/head 替代
- registry spec 字段已被分析 worker 错误修改过（a000_s42 的 data_path/data_count/command 被覆盖），核实实验配置时以远程 config.json 为准，不要只信 registry spec

### 2. 🖥️ 基础设施快照
- 服务器：westd-19828 (root)，工作目录 `/root/autodl-tmp/distrib_canary_collapse`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 数据集：`/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k/`（wikitext-103-raw-v1，train split 1.8M 条，Arrow 格式）
- HF cache：`/root/autodl-tmp/.hf_cache`
- 模型：EleutherAI/pythia-410m（从 HF cache 加载）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/`
- 活跃进程（截至 handoff）：a025_s42 (PID 53069, cuda:1, ~2.5h 运行，gen_6 完成中)；cuda:0 空闲
- 无 wandb 配置（本项目不检查 wandb）

### 3. 📊 当前状态
**刚完成**：
- 审查了 6 个 worker（code-analysis-unify、kill-dryrun-fix-comment、bh-fdr-integration、fix-method-ablation-spurious、d019-t3-f2-fix、analyze-a000-s42）+ 1 次深度审查（差分 Permutation Granger → Claim 3 结构）
- alpha_sweep_a000_s42 (α=0.0 null control) 已完成并审查，结论 PASS with WARNING（registry spec 被错误覆盖、趋势标签不精确）
- plan-006 训练准备 worker 已完成：plan_006_s42 (PENDING)、plan_006_s43 (PREPARING) 已注册

**Registry 状态**：
- DONE: alpha_sweep_a000_s42, method_ablation_phase1, bootstrap_ty_s42, 及 MVP 系列
- RUNNING: alpha_sweep_a025_s42_v3 (cuda:1, gen_6/10, ~63min 剩余)
- PENDING: plan_006_s42 (20-gen extended, 等 GPU)
- PREPARING: plan_006_s43, alpha_sweep_a010_s42, alpha_sweep_a060_s42

**等待**：
- a025_s42_v3 完成 cron 回调
- Director 对 GPU 0 空闲后的调度决策（plan_006 vs alpha_sweep 下一个 α）

### 4. 📋 待办
- a025_s42_v3 cron 完成回调 → 审查 α=0.25 结果，对比 α=0.0 和 α=1.0 的 canary signal 强度梯度；核实 GPU cuda:1 释放
- plan_006_s42 启动通知 → 核实是 20-gen 配置（非 10-gen）、synthetic_ratio=1.0、max_lag=10、种子正确
- 任何新 alpha_sweep 启动 → 核实 CUDA_VISIBLE_DEVICES 在白名单内，dry-run 无残留进程
- Director 转发 framing 提案 → Read negative-framing-review skill，四维度审查
- 章节写作审查请求 → 合规检查（Agent 是否看过 red-section skill）+ 维度评分

### 5. 🎯 战略上下文
**核心结论链**：
- D013/D015: TY Granger 在 T=10 power=0.05-0.20，已降级，不参与 robust/spurious 分类
- D019: ECE 升级为 co-primary canary（排除 TY 后与 token_entropy 等价）；Claim 1 升级为 "Granger-causal precedence"（非 "causal mechanism"）；f² 在 df_resid<20 时禁用 Cohen 基准
- D020: 2×2 差分对比表（channel × differencing）为 Claim 3 核心 figure；spurious_rate 报双版本（含 TY 75% / 排除 TY 62.5%）

**核心实验发现**：canary→diversity 稳健（diff F↑, 24/24 SIG_FDR），canary→perplexity 虚假（diff F→0, 0/8 SIG_FDR）。这个对比是 Claim 3 的支柱。

**易错点**：
- 不要把 f² 值（102-435）按 Cohen 基准解读——df_resid=5-6 时极端膨胀，代码已加 guard（f2_size="df_too_low"），但论文叙事中也不能引用这些数字
- report.md 资源状态是 stale 的（写着"空闲"但 GPU 实际在跑），不要信 report.md 的资源行
- alpha_sweep_analysis.json (05:58) 是 a000_s42 完成前生成的，不包含 a000 最终结果
- registry spec 可能被 worker 修改过——验证实验配置时必须对照远程 config.json


---
