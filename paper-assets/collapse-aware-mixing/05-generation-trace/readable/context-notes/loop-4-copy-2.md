# agent / loop_4.md

**collapse aware mixing** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_4.md`
- **Structured JSON:** [`bf7c0e5fc750e5b21ded.json`](../../sessions/bf/bf7c0e5fc750e5b21ded.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-14T02:41:40+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单只有 `cuda:0`（cqa1-38874），禁止使用其他 GPU 编号
- D018 已判定 MVP FAIL，三条路径全封——禁止在未获 Director 决策前启动任何新的 eff_rank leading indicator 实验
- 当前仅剩两个选项：Q2 negative result paper（EMNLP 2026 Findings）或 archive，由 Director/用户决策
- submit_training_job 命令必须包含 conda 激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，tmux 不继承环境
- AutoDL 根分区 30GB，所有大文件写 `/root/autodl-tmp/`

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-38874，1× RTX PRO 6000 96GB
- 工作目录：`/root/collapse-aware-mixing/`
- Python：`/root/miniconda3/bin/python`（conda base 环境，Python 3.12, PyTorch 2.10.0, transformers 4.57.6）
- 模型：EleutherAI/pythia-1b（HF cache `/root/autodl-tmp/.hf_cache`）
- 数据：wikitext-103-raw-v1（HF Hub）
- v7 输出：`/root/autodl-tmp/output_v7/`（G0/G1/G2 全 18 checkpoint + pivot 分析）
- v5 输出：`/root/autodl-tmp/output/`（仅 G0 完整）
- 活跃进程：mvp_seed0_replication_r2（PID 122208，tmux session，cuda:0）— 无 cron 监控（reconcile 返回 0）
- Worker 池：空（0 running）
- flash-attn 不可用，用 sdpa 回退

### 3. 📊 当前状态
**刚做完**：D018 MVP 最终判定 FAIL。三条路径结论：
1. C1 holdout eff_rank 在 collapse 中反向上升 +0.96%（FALSIFIED）
2. Pivot B generated eff_rank 与 n-gram entropy 同时检测（G1 step 152），噪声高 573 倍（NO ADVANTAGE）
3. Direction C 所有层变化 <1%（DEAD）

**RUNNING**：
- `mvp_seed0_replication_r2`：seed=0 复现实验，验证 holdout eff_rank 上升是否 seed-robust（支撑 Q2 negative result paper）。已提交但无 cron 监控，需要手动检查或注册 cron。

**PREPARING（全部废弃/搁置）**：mvp_pilot_v8, v8_r2, v3, v2 — 均为历史遗留，从未实际执行，可忽略。

**等待**：Director 对 Q2 vs archive 的决策。

### 4. 📋 待办（条件触发式）
- mvp_seed0_replication_r2 完成 → 检查 seed=0 下 holdout eff_rank 是否同样上升（预期是），更新 registry，汇报 Director
- Director 选择 Q2 → 需补实验：multi-seed（再跑 seed=1,2）+ multi-scale（Pythia-410M, 2.8B），估算 3-4 天 GPU
- Director 选择 archive → 释放 cqa1-38874 GPU，关闭项目
- **注意**：mvp_seed0_replication_r2 没有 cron 监控 → 启动后应立即注册 cron 或手动 poll

### 5. 🎯 战略上下文
- **核心发现**（有论文价值的 negative result）：holdout spectral eff_rank 与 mode collapse 完全解耦，模型生成崩塌到 1 个 unique token 时 holdout eff_rank 反而上升。这挑战了 SIGMA 等工作的隐含假设。
- **决策链**：D001(MVP设计) → D003(数据切换) → D005(lr修复) → D007(降规模) → D011(G1反常) → D014(C1 falsified) → D016(Pivot B GO→) → D018(推翻D016, MVP FAIL)
- **易错点**：
  - D016 曾基于 3 checkpoint 不公平对比误判 Pivot B GO，后被 D018 全 18 checkpoint 数据推翻——不要重蹈覆辙，任何对比必须用公平的数据量
  - PREPARING 状态的实验（v8/v8_r2/v3/v2）都是废弃的，不要试图恢复它们
  - memory.md 中 PI controller 的 r_target=50.0 是旧 bug 值（实际 eff_rank ≈ 677），已在 experiment_plan.yaml 修为 auto-infer
  - 论文中 SVD vs Gram Matrix 命名不一致待修（代码用 SVD 奇异值，framing 写 Gram 特征值）
  - SIGMA 已占据"谱分析检测 collapse"位置，我们的差异化是"闭环控制"——但 MVP FAIL 后这个 framing 需要完全重写


---
