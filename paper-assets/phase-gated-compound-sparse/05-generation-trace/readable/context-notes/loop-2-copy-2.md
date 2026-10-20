# agent / loop_2.md

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`14a8cb81f21029e95f63.json`](../../sessions/14/14a8cb81f21029e95f63.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: idle_timeout
updated: '2026-05-14T02:07:12+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 westd-22162 cuda:0/1/2/3，config 已锁定，Director 指令也不能覆盖
- 所有 v4 legacy importance 实验数据无效（NaN 中毒 + 位置偏差），禁止引用其 II 数值做任何结论
- 唯一可信的 baseline 数据：mvp_v4_random_r2（random masking, 50 problems, s=0.1~0.3）
- 截稿 EMNLP 2026 ARR = 2026-05-25，距今 11 天
- importance 指标修复 commit `20182ec`，v5_fixed 系列是修复后首批验证——结果未出前不能动 paper framing

### 2. 🖥️ 基础设施快照
- 服务器：westd-22162，4× RTX 6000 Pro 96GB
- 工作目录：`/root/autodl-tmp/pacs`
- Python：`/root/miniconda3/bin/python`（conda base 环境，非 venv）
- 环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：`/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B`
- 数据：`/root/autodl-tmp/pacs/data/math500.json`（500 题，之前跑 50 题子集，v5 跑全量 500）
- wandb：未配置（profiling 实验用本地 JSON 输出）
- 活跃进程（v5 修复验证，4 GPU 全占）：
  - mvp_v5_fixed_s020: cuda:0, PID 46568
  - mvp_v5_fixed_s030: cuda:1, PID 46935
  - mvp_v5_fixed_s015: cuda:2
  - mvp_v5_fixed_s025: cuda:3
- Cron：reconcile 返回 0 条活跃 cron（v5 实验可能是手动提交未挂 cron，需检查进程存活）
- 输出目录：`/root/autodl-tmp/pacs/profiling_output_v5_s0{15,20,25,30}/`
- GPU 预算：~250h，已用 ~2.9h

### 3. 📊 当前状态
**刚做完**：importance 指标三重 bug 修复（NaN skip + 位置归一化 + torch.where 消除 inf×0），commit `20182ec`。启动了 4 个 v5_fixed 验证实验（s=0.15/0.20/0.25/0.30），全量 500 题，4 GPU 并行。

**Registry 活跃实验**：
| exp_id | sparsity | GPU | 状态 |
|--------|----------|-----|------|
| mvp_v5_fixed_s020 | 0.20 | cuda:0 | RUNNING |
| mvp_v5_fixed_s030 | 0.30 | cuda:1 | RUNNING |
| mvp_v5_fixed_s015 | 0.15 | cuda:2 | RUNNING |
| mvp_v5_fixed_s025 | 0.25 | cuda:3 | RUNNING |

**等待中**：无活跃 cron 监控这 4 个实验。接手后第一件事：SSH 检查 4 个进程是否还活着，如果是手动启动的需要补挂 cron 或手动轮询。无 running Worker。无待处理 Director 决策。

### 4. 📋 待办（条件触发式）
- v5_fixed 4 个实验完成 → spawn worker 提取结果 JSON，计算 II，与 random baseline 对比：
  - importance II < 0 且 CI 上界 < 0（至少 2 个 sparsity level）→ **D010 pivot 假设成立**，汇报 Director，推进 M1'（cross-model validation on Qwen2.5-7B）
  - importance II ≥ 0 或 CI 跨零 → **假设不成立**，产出 red-section Framing 调整提案，汇报 Director 决策（可能需要再次 pivot 或终止项目）
- v5_fixed 任一实验 failed → 检查是否又是 OOM/NaN，诊断后决定是否 retry
- Director 批准 Framing 调整 → Read framing-reaudit skill，执行全文 re-audit
- 假设成立且 Director 批准推进 → 立即铺 Qwen2.5-7B 下载（ModelScope CDN）+ M2 per-phase grid search 代码准备

### 5. 🎯 战略上下文
**项目核心问题**：compound sparsity（attention head pruning + KV cache eviction）的交互是否依赖 masking strategy（importance vs random）出现方向反转（sub- vs super-additive）？

**决策链**：D007(v1 bug) → D008(v2 negative) → D009(random 混淆) → D010(**pivot**: phase-dependent → strategy-dependent reversal) → D011(float16 NaN) → D012(暂停 importance 实验) → D013(位置偏差根因确认，修复重跑)

**关键判断**：
- Random baseline 已确认全正（super-additive），这是稳定的。核心悬念只有：修复后 importance masking 的 II 是否显著为负。
- v5 跑的是全量 500 题（之前都是 50 题），统计效力会好很多，但耗时也更长（v3 跑 50 题约 55 分钟，500 题预估 ~9h per GPU）。
- 已经 pivot 一次（D010），如果 v5 再 negative，项目可能需要第二次 pivot 或终止。距截稿 11 天，时间极紧。

**易踩的坑**：
- 不要引用 v4 legacy 的任何 II 数值——全部无效
- v5 实验没有挂 cron 监控，需要手动检查进程状态
- `submit_training_job` 的 command 必须自带环境激活（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`），不能假设 .venv 存在
- II 统计要看 median 和 winsorized mean（不只是 mean），v5 代码已加入 robust statistics
- GRASPrune (ACL'26) 是最近的 competitor，写 related work 时必须区分


---
