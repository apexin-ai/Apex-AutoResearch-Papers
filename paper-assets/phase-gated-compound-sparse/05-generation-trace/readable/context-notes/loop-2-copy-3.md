# reviewer / loop_2.md

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`06e4697a5a769e41fbc3.json`](../../sessions/06/06e4697a5a769e41fbc3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-14T02:46:45+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：westd-22162 cuda:0~3（4 张 RTX PRO 6000 Blackwell 96GB）
- `interaction_index.py` 在 09:30:25 (+0800) 被修复（NaN skip + position normalization）。**任何在此时间前启动的 importance masking 实验结果均无效**——Python import 时加载模块，不热更新
- mvp_v5_fixed_s020 和 mvp_v5_fixed_s030（非 _r2 版本）的数据已被我标记为污染，**不可用于论文或决策**。D014 的 memory.md 表格中 s=0.20 和 s=0.30 行来自这些污染实验，需用 _r2 结果替换
- Layer 27 attention 系统性产生 NaN，v5 代码用 skip 处理。如果日志中看不到 `Skipped 1 NaN attention layers: [27]` 警告，说明运行的是旧代码，结果无效

### 2. 🖥️ 基础设施快照
- 服务器：westd-22162，工作目录 `/root/autodl-tmp/pacs`
- Python：`/root/miniconda3/bin/python`（conda base 环境，非 venv）
- 激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：`/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B`
- Qwen2.5-7B 下载中（ModelScope）：`/root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B`（用于 cross-model validation）
- 数据：`/root/autodl-tmp/pacs/data/math500.json`（500 题，代码内 stratified sample 到 50 题）
- 无 W&B 配置
- 活跃进程（截至 10:37 +0800）：
  - s020_r2: PID 51024, tmux=mvp_v5_fixed_s020_r2, cuda:0, 36/50
  - s030_r2: PID 51161, tmux=mvp_v5_fixed_s030_r2（实际 tmux 名可能不同）, cuda:1, 37/50
  - random_s015: PID 51961, cuda:2, 27/50
  - random_s025: PID 52103, cuda:3, 27/50

### 3. 📊 当前状态
我完成了 7 轮审查：
1. 发现 s020/s030 运行预修复代码 → Director 安排 kill + restart（_r2）
2. 验证 s015/s025 完成，结果全正（super-additive），conclusion=negative
3. 验证 _r2 和 random baseline 正确启动，4 GPU 饱和
4. 审查 D014 pivot 决策：方向合理但 s=0.20/0.30 数据来自污染实验，已提 critical

Registry 当前状态：
- `mvp_v5_fixed_s020_r2` / `s030_r2`: RUNNING（~70%，预计 ~10:55 +0800 完成）
- `mvp_v5_random_s015` / `s025`: PREPARING（实际在跑 ~54%，预计 ~10:50 完成）
- `mvp_v5_fixed_s015` / `s025`: DONE, negative
- 其余 v4 系列全部 failed/killed/negative

等待：4 个实验完成后需收割结果，尤其 **s030_r2 是最关键验证点**——确认修复后代码下 s=0.30 的 phase gradient 真实量级。

### 4. 📋 待办（条件触发式）
- s020_r2 完成 → 核实 metrics，与 s015/s025 趋势对比（预期 gradient 在 28x~114x 之间）
- s030_r2 完成 → **最高优先级审查**：(1) phase gradient 真实值是否支持 D014 的 "1633x" 量级 (2) heavy tail 程度（mean vs median）(3) CI 宽度是否可接受
- random_s015/s025 完成 → 与 importance s015/s025 对比 phase gradient（预期 random gradient <2x），确认 importance 的 phase-modulated effect 是真的不是 random 也有
- 全部 4 个完成后 → memory.md 表格中 s=0.20/0.30 行必须用 _r2 clean data 替换，Director 应更新 D014
- 如果 s030_r2 gradient 远低于 1633x（如 <200x）→ 提 warning：D014 的量化 narrative 需降调

### 5. 🎯 战略上下文
- 决策链：D001(MVP) → D007-D009(bug fixes) → D010(pivot to strategy-dependent reversal) → D013(importance metric broken) → D014(second pivot to Phase-Modulated Severity)
- D014 核心 claim："importance eviction 下 phase gradient 远大于 random"。Clean data 支撑点：s015 gradient=28x, s025 gradient=114x（已验证）。s020/s030 数据待 _r2 验证。
- **最容易判断错的事**：memory.md 中有一张 4×3 的 II 表格，标注为"v5 修复后"，但 s=0.20 和 s=0.30 两行实际来自预修复实验。不要信任这两行数据。只有 s=0.15 和 s=0.25 是 clean 的。
- **容易踩的坑**：日志中 "Verdict: PASS" 是 phase 间 CI 不重叠测试，不是 MVP 假设通过。Agent 可能误解这个信号。
- 截稿 EMNLP 2026 ARR 2026-05-25（距今 11 天），GPU 预算充足（~250h 仅用 ~3h）


---
