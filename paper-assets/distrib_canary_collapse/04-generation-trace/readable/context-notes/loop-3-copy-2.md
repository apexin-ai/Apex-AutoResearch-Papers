# agent / loop_3.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`b605282df027b6f0e639.json`](../../sessions/b6/b605282df027b6f0e639.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: idle_timeout
updated: '2026-05-15T00:40:55+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**只能用 westd-19828 的 cuda:0 和 cuda:1**。无其他服务器/GPU 分配。Director 指定白名单外 GPU 也必须 push back
- 服务器名是 `westd-19828`（不是 autodl-rtx6000，旧名已废弃），submit_training_job 必须用此名
- kill_job 只杀 tmux session 不杀子进程——kill 后必须 `ps aux | grep python` + `kill -9` 确认子进程死亡，否则旧进程写同一输出目录导致数据损坏（a025_v2 事故教训）
- canary→perplexity 已被差分 Granger **决定性证明为伪回归**——论文 claim 硬限为 "canary predicts diversity collapse"，禁止声称 predict perplexity
- HF 下载用 `HF_ENDPOINT=https://hf-mirror.com`，不用 network_turbo 代理（会卡死）；pip install 可以用 network_turbo

### 2. 🖥️ 基础设施快照
- **服务器**: westd-19828，2× RTX PRO 6000 Blackwell 96GB
- **工作目录**: `/root/autodl-tmp/distrib_canary_collapse`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，Python 3.12.3, PyTorch 2.10.0+cu128）。激活方式：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。**无 .venv**
- **HF cache**: `/root/autodl-tmp/.hf_cache`（设 `HF_HOME`）
- **模型**: EleutherAI/pythia-410m（HF cache 已下载）
- **数据**: `data/wikitext103_5k/`（5000 条，train split，MVP + α-sweep 共用）；`data/wikitext103/`（full，plan_006 用）
- **活跃进程**:
  - plan_006_s42: PID 68368, tmux session, cuda:0, 20-gen extended run (α=1.0, 10k steps/gen)
  - alpha_sweep_a025_s42_v3: PID 53069, tmux session, cuda:1, 10-gen (α=0.25, 5k steps/gen)
- **Cron**: 两个实验各有 cron 监控（reconcile 确认均 still running）
- **W&B**: 未配置（指标通过 all_metrics.json 本地采集）

### 3. 📊 当前状态
**刚做完**: 上一个 session 完成了 D014-D020 的全部结构性修复——5-method ablation、permutation Granger 差分版、BH FDR 集成、bootstrap TY power analysis、null control (α=0.0)、ECE 地位评估。ROADMAP 和 memory.md 已更新。

**RUNNING (2)**:
- `plan_006_s42` (cuda:0): α=1.0, 20-gen extended, 验证 diversity lead 在更长序列下是否更稳健。预估 ~8.7h 总时长（从 2026-05-14T23:41 开始）
- `alpha_sweep_a025_s42_v3` (cuda:1): α=0.25, 10-gen，测试低污染下 canary signal 是否可检测。第三次尝试（v1 killed 参数修复, v2 failed 旧进程数据损坏）

**PREPARING (7，等 GPU 空出来串行跑)**:
- α-sweep 剩余 4 点: a050_s42, a075_s42, a010_s42, a060_s42
- plan_006_s43 (20-gen 第 2 seed)
- 历史残留: alpha_sweep_a025_s42_v2, alpha_sweep_a025_s42, mvp_v2_rep44, mvp_rep44（已完成/废弃，状态未清理）

**等待**:
- 两个 RUNNING 实验的 cron 完成回调
- 无待处理的 Director 决策请求

### 4. 📋 待办（条件触发式）
- **alpha_sweep_a025_s42_v3 完成回调到达** → spawn worker 跑 `analyze_alpha_sweep.py`（cross-corr + permutation Granger 差分版 + BH FDR），更新 registry metrics → 对比 α=1.0 MVP 结果判断 signal 衰减程度 → 汇报 Director
- **a025 分析完成 + cuda:1 空出** → 立即提交 α-sweep 下一个点（优先 a050_s42，中间点信息量最大）
- **plan_006_s42 完成回调到达** → 按 memory.md 中的 plan_006 分析 checklist 执行：full series cross-corr (max_lag=10) + rolling-window + 与 MVP 10-gen 对比 + permutation Granger（差分版）。**预期 perplexity channel 不会变显著**，focus 在 diversity lead 稳健性
- **plan_006_s42 分析完成 + cuda:0 空出** → 提交 plan_006_s43（第 2 seed）或 α-sweep 下一个点
- **α-sweep 6 点全完成** → 执行 plan_002 Phase 2 (pooled panel + permutation Granger)；运行 detrending analysis（`detrending_utils.py` 已就绪）；计算 α* onset threshold + uncertainty interval
- **任何实验 conclusion=negative** → 按 red-section skill 产出 Framing 调整提案，**禁止默默跑下一个**

### 5. 🎯 战略上下文
**项目核心**: 迭代合成数据训练中，token_entropy 和 ECE 作为 canary 指标能以 1-2 代的领先量预测 diversity collapse（distinct_1/2/3）。方法论贡献是核心 differentiator——naive correlation 给出 100% 显著率，实际 75% 是伪回归。

**三个 parallel claims** (D013-D020):
1. token_entropy Granger-causes diversity collapse（差分后 24/24 FDR-sig，Cohen's f² large）。ECE 为 conditional secondary canary（差分版比 TY 更一致）
2. 可预测性是 regime-dependent 的（α-sweep 正在验证）
3. 分析方法选择决定结论——5-method ablation 揭示方法论陷阱（naive 100% → TY 25%），这是文献空白

**目标**: AAAI 2027 (~Aug 2026)

**最容易判断错的事**:
- **不要对 perplexity channel 抱希望**——差分 Granger 已经终局证明是纯趋势驱动。plan_006 更长序列不会改变这个结论
- **TY 在短序列下 power 极低** (T=10: 5-20%)——TY 只能做 Claim 3 的方法敏感性展示，不能作为核心证据
- **α-sweep a025 已经失败两次**（v1 参数修复 killed, v2 旧进程数据损坏）——v3 如果又 fail，检查是否有残留进程
- **report.md 里的 PREPARING 实验有历史残留**（mvp_rep44, mvp_v2_rep44 等）——不要试图提交这些，它们是旧版本的废弃记录
- **ECE 地位经历过波动**：从 co-primary (D019) → conditional secondary (D020)，因为 TY 下只 3/4 sig，但差分版 permutation Granger 下 4/4 sig 又回升。当前定位是 "conditional secondary canary"，plan_006 结果可能再次调整


---
