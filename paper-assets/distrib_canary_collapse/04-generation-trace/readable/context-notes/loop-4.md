# director / loop_4.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`8a3a027fd24a656813ea.json`](../../sessions/8a/8a3a027fd24a656813ea.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_messages
updated: '2026-05-14T23:44:16+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-19828 的 cuda:0 / cuda:1（2× RTX PRO 6000 Blackwell 96GB）
- submit_training_job 服务器名必须写 `westd-19828`（不是 autodl-rtx6000）
- canary→perplexity 通道已被差分 Granger 确认为伪回归（F→0），论文 claim 硬限：只能声称 "canary predicts diversity collapse"，**绝不能**声称 "canary predicts perplexity"
- TY（Toda-Yamamoto）已正式降级为辅助指标（D015），核心分析框架是 cross-corr + permutation Granger（差分版）+ BH FDR
- HF 下载用 `HF_ENDPOINT=https://hf-mirror.com`，不用 network_turbo 代理（会卡死）
- kill_job 只杀 tmux session 不杀子进程，kill 后必须 `ps aux | grep python` 确认进程全部死亡

### 2. 🖥️ 基础设施快照
- 服务器：westd-19828 (connect.westd.seetacloud.com)，账户 root
- 工作目录：/root/autodl-tmp/distrib_canary_collapse
- Python：conda base, Python 3.12.3, PyTorch 2.10.0+cu128（绝对路径 /root/miniconda3/bin/python）
- GPU：2× RTX PRO 6000 Blackwell 96GB (cuda:0, cuda:1)
- 关键脚本路径：`iterative_train.py`（主训练）、`analyze_mvp.py`（MVP 分析）、`permutation_granger.py`（差分 Granger）、`method_ablation.py`（5-method ablation）、`analyze_alpha_sweep.py`（α-sweep 分析）、`detrending_utils.py`（待用）
- 结果路径：`results/mvp/analysis/`（MVP 分析产物）、`results/bootstrap_ty_results.json`（plan_009）
- 活跃进程：plan_006_s42 + alpha_sweep_a025_s42_v3（各占一张卡）
- W&B / 弹性 GPU / Git：均未配置

### 3. 📊 当前状态
**刚做完**：
- D017-D020 一连串决策——差分 Granger 确认 perplexity 伪回归、ECE 升级 co-primary、BH FDR 零翻转、Claim 1 措辞升级为 "Granger-causal precedence"
- plan_009 bootstrap TY power analysis 完成（T=10 power 仅 5-20%，TY 正式降级）
- 5-method ablation 完成排序：naive 100% > diff 88% > threshold 56% > permG 38% > TY 25%
- α-sweep a000 (α=0.0 null control) 完成（success）
- mix_datasets 双向 subsample bug 修复已部署

**RUNNING**：
- `plan_006_s42`：Pythia-410M × α=1.0 × 20 gen extended run，验证 diversity lead 在更长序列下的稳健性
- `alpha_sweep_a025_s42_v3`：α=0.25 第一个 seed

**PREPARING（9 个排队）**：plan_006_s43、alpha_sweep 剩余 4 个 α 点（a010/a050/a060/a075）、alpha_sweep_a025 旧版本 v1/v2、mvp_rep44/v2_rep44

**Agent 队列**：空闲（depth=0）

**审稿阶段**：已进入 Review，Group C 团队并行处理论文评审（review_chat_id 已配置）

### 4. 📋 待办（条件触发式）
- plan_006_s42 完成 → 用 `analyze_extended.py` 做 full series cross-corr (max_lag=10) + rolling-window + permutation Granger，对比 MVP 10-gen 结果。**预期 perplexity 不会变显著**，focus 是 diversity lead 稳健性
- alpha_sweep_a025_s42_v3 完成 → 启动下一个 α 点（优先 a050/a075 极端点），确保两张卡始终满载
- α-sweep 6 点全完成 → 绘制 predictability regime map + 启动 plan_002 Phase 2 (pooled panel + permutation Granger)
- α-sweep 首批结果出来 → 运行 detrending_utils.py + 2σ onset threshold sensitivity + α* uncertainty interval（Dream 观察项）
- α-sweep 确认 canary→perplexity lead 在 α=0.50 存在 → 启动 plan_004 (C4 跨域验证)
- PREPARING 中的 alpha_sweep_a025_s42/v2 和 mvp_rep44/v2_rep44 是历史残留，不需要再跑，可以清理

### 5. 🎯 战略上下文
**核心结论链**：MVP STRONG PASS (D009) → token_entropy+ECE lead diversity 1-2 代 → perplexity channel 是伪回归 (D017/D018) → 方法选择决定 75% 的结论 (D011) → 论文 framing = "delineating predictability boundaries"，三个 claim 并行：(1) Granger-causal precedence of canary→diversity, (2) regime-dependent predictability (α-sweep), (3) 方法论陷阱是文献空白

**Dream 评分现状**：best 3/6, median 3/6, worst 2.5/6。5 项结构性修复中 4 项已完成（BH FDR、effect size、TY power analysis、permutation Granger），最后一项是 α-sweep 数据（正在跑）

**最容易判断错的事**：
- 不要期望 plan_006 的 perplexity channel 会突破——差分后 F→0 是决定性证据，更长序列不改变伪回归本质
- PREPARING 队列里有历史残留实验（mvp_rep44 等早期版本），不要盲目启动
- ECE 的地位取决于用哪种方法：TY 下只有 3/4 seed pass，permutation Granger 下 4/4 pass。论文需要同时报告两者，不能只挑好看的
- 目标 AAAI 2027 (~Aug 2026)，还有 ~2.5 个月，P0 实验预计 ~57 GPU·h，当前累计 ~8.4h，节奏合理但不能空卡


---
