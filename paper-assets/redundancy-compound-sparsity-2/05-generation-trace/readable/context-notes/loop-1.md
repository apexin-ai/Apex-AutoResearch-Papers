# director / loop_1.md

**redundancy compound sparsity 2** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`47c6fbb7a330e6560c16.json`](../../sessions/47/47c6fbb7a330e6560c16.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-12T14:19:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 cuda:0, cuda:1 @ westd-16980。不得使用其他卡。
- 模型本地路径：`/root/carc/models/DeepSeek-R1-Distill-Qwen-14B`。HF Hub 在该服务器上网络不通，所有模型/数据加载必须用本地路径或先 `source /etc/network_turbo`。
- D003 是 EMA eviction 信号的最后一次验证机会。如果 FAIL → 不再尝试 EMA，直接转 analysis paper。不要再给 EMA 第四次机会。
- 部署前必须 2-sample smoke test。该项目已因启动崩溃浪费 3 次部署（网络/API 兼容/CUDA 映射）。不准直接 submit_training_job。

### 2. 🖥️ 基础设施快照
- 服务器：westd-16980 (connect.westd.seetacloud.com)，2×RTX PRO 6000 Blackwell 96GB
- 工作目录：/root/carc/
- 代码文件：carc_utils.py, carc_calibrate.py, carc_mvp.py, carc_generate.py, carc_kv_eviction.py, sanity_check_eviction.py, eval_kv_eviction.py, merge_results.py
- 模型：/root/carc/models/DeepSeek-R1-Distill-Qwen-14B（BF16, ~28GB）
- MVP 数据：/root/carc/results_seed42/, /root/carc/results_seed1337/（60 条 MATH-500 reasoning traces）
- kvpress 已 pip install（baseline 框架）
- 活跃进程：D003 两个实验可能在跑也可能已崩（第三次部署后未最终确认存活状态）
  - d003_reasoning_traces (cuda:0): 20 条 reasoning traces × 6 strategies
  - d003_wikitext_32k (cuda:1): 32K prefill × 6 strategies
- 无 wandb / 无 git remote

### 3. 📊 当前状态
**D003 time-boxed retry 是当前最高优先级**。两个实验第三次部署后 Agent 报 93-95% GPU util，但系统后续又报 0%，最终存活状态未确认。接手后第一件事：ssh_read_only 查 nvidia-smi + 日志 tail。

Registry 实验：
- carc_mvp_seed42: DONE (FAIL, |r|=0.12, diff=5.7%)
- carc_mvp_seed1337: DONE (FAIL, |r|=0.11, diff=5.3%)
- sanity_kv_eviction: DONE (FAIL, EMA vs random gap 0.9%)
- d003_reasoning_traces: RUNNING（可能已崩）
- d003_wikitext_32k: RUNNING（可能已崩）

等待中：D003 结果 → 决定 Path C (KV eviction) 还是 analysis paper。
Reviewer 已完成 Plan B (analysis paper) 叙事框架，Director 已审阅并给出反馈。
Agent 被派了 baseline 代码准备任务（kvpress + eval_baselines.py），未确认是否完成。

### 4. 📋 待办
- D003 进程存活 → 等结果（reasoning ~3-4h, wikitext ~2-3h from 3rd deploy）
- D003 又崩了 → 第四次修复并确保 smoke test 通过再提交
- D003 PASS（reasoning 上 EMA vs random ≥5% 或 32K 上 EMA beat recency）→ 复活 Path C KV eviction 论文，继续 baseline 对比 + full eval
- D003 FAIL → 立即启动 analysis paper：
  - 优先级最高：A2（attention-score vs EMA 信号对比，用 kvpress 的 knorm/expected_attn）→ 决定 claim 范围是 "EMA fails" 还是 "no O(1) signal suffices"
  - A1（per-layer heatmap 可视化 spatial decoupling）— 用已有 MVP 数据，0 GPU
  - A3（tau sensitivity sweep）— ~2h GPU
  - A4（information decay curve）— ~2h GPU
  - B1（Qwen2.5-7B 第二个模型验证）— ~8h GPU，与上述并行
  - 论文目标：EMNLP 2026 Findings，workshop fallback
- carc_generate.py 的 RoPE position bug 已知但可能未修复 → 任何 autoregressive generation eval 前必须确认修复

### 5. 🎯 战略上下文
- 决策链：D001（MVP 定义 cross-axis 验证）→ D002（MVP FAIL, pivot to KV eviction）→ D003（sanity check FAIL on WikiText 4K, time-boxed retry on reasoning+32K）
- 核心发现：Spatial decoupling — 高 EMA-perturbation 相关层 (L30-33) 与高 perturbation-diff 层 (L41-45) 完全不重叠。这是论文最有学术价值的发现，不管走哪条路都要突出。
- 易错点 1：不要把 sanity check 的 WikiText 4K 结果等同于 D003 的 reasoning+32K 结果。两者测试条件不同，D003 是在正确动机场景下测试。
- 易错点 2：如果走 analysis paper，A2 实验（attention-score vs EMA）的结果直接决定 claim 范围（窄 vs 宽）。这是最关键的额外分析，不能跳过。
- 易错点 3：该服务器 HF Hub 不通。所有 HF 下载操作必须先 `source /etc/network_turbo` 或用本地缓存。已因此崩过 2 次。
- EMNLP ARR DDL 2026-05-25，剩 ~13 天。时间极紧，每个小时都重要。


---
