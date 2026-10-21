# agent / loop_2.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`720a4eaaaca06f989980.json`](../../sessions/72/720a4eaaaca06f989980.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: idle_timeout
updated: '2026-05-13T21:45:06+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 `cuda:0`, `cuda:1`（westb-13313）。config `gpu_ids` 就这两张，Director 指定其他卡也必须 push back
- 模型路径有三下划线：`/root/autodl-tmp/models/Qwen/Qwen2___5-7B-Instruct/`（HF cache 路径转义），写错就 FileNotFoundError
- vLLM 兼容 patch：torch 2.10.0 + vLLM 0.18.1 需注释 `select_algorithm.py` 第 1695/2164 行，否则启动崩溃
- Tie-break 必须 `>`（strict），不能 `>=`。`>=` 在 95%+ delta=0 步骤下 oracle 退化为 always-internal（D003 教训）
- Death filter 仅用于 det/oracle 模式，always-internal 是纯 LLM baseline 不能加 fork/is_lethal
- `phase1_signal.py` 不支持 `--seed` 参数——不要传，会报错
- research-cf-pilot-gpu1 已 killed（D010 取消 episode-terminal K=10 方案，成本 78h 不可接受）——不要复活

### 2. 🖥️ 基础设施快照
- **服务器**：westb-13313，2× RTX 5090 32GB（cuda:0, cuda:1）
- **工作目录**：`/root/autodl-tmp/simgate-modular-routing`
- **Python**：aml-train 镜像，`/root/miniconda3/bin/python`（conda base 环境，无 venv）
- **激活命令**：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型**：`/root/autodl-tmp/models/Qwen/Qwen2___5-7B-Instruct/`（Qwen2.5-7B-Instruct）
- **数据**：ScienceWorld API（JVM 后端，无本地数据集文件）
- **W&B**：未配置（本项目目前用 registry + JSON 结果文件追踪）
- **活跃进程**：
  - research-prescreening-gpu0: PID 649681, cuda:0, tmux 监控中
  - research-prescreening-gpu1: PID 265929, cuda:1, tmux 监控中
- **Cron**：2 个 active（上述两个 prescreening 的 reconcile 均确认 still running）
- **Workers**：`worker_analysis_plan-001b-revised-proposal`（running）、`worker_code_pipeline-format-fix`（running）

### 3. 📊 当前状态
**刚完成**：research-boil-v3-gpu1 分析（success，boil v3 数据与其他 4 task 代码版本一致）。D013 framing pivot 落地（death avoidance = ~99% routing signal）。D014 keywords v2 分析完成（keyword heuristic 在 episode-level 完全失效）。

**RUNNING 实验**：
- `research-prescreening-gpu0`：25 task types 预筛（5 ep/task），已跑 14/25，剩余 ~2h。已发现 9 death-dominated, 3 genuine-det (2 个统计不显著), 1 internal-preferred, 1 mixed
- `research-prescreening-gpu1`：剩余 8 task types 预筛（measure-melting-point, mendelian-genetics ×2, power-component ×2, test-conductivity ×2, use-thermometer），剩余 ~40min

**等待中**：
- 2 个 Worker 回调（plan-001b revised proposal 分析 + pipeline format fix）
- 预筛完成后需汇总全 25 task 结果 → 提交 revised plan-001b 给 Director
- mvp-p1-signal 仍在 PREPARING，已被实际实验流程超越，可 kill

### 4. 📋 待办（条件触发式）
- research-prescreening-gpu1 cron 回调 → spawn worker 汇总 GPU1 的 8 task 结果，合并到预筛总表
- research-prescreening-gpu0 cron 回调 → spawn worker 汇总全部 25 task 结果 → 分类（death-dominated / genuine-det / internal-preferred / no-effect / mixed）→ 选 plan-001b 的 task 组合
- 两个预筛都完成 → 向 Director 提交 revised plan-001b 方案（含 task 选择 + 预计 GPU 时长 + class balance 策略）
- Director 批准 plan-001b → 双卡并行数据收集（episode-level 2-way，预计 ~3.7h 双卡 = ~20h 单卡等效）
- plan-001b 数据收集完成 → plan-012 death decomposition（CORE，已有代码）+ plan-011 rule-based baseline + plan-002 router SFT diagnostic probe
- Worker plan-001b-revised-proposal 回调 → 整合分析结果，准备汇报 Director
- Worker pipeline-format-fix 回调 → 验证修复，确认 pipeline 可用

### 5. 🎯 战略上下文
**核心结论链**：D001(MVP设计) → D005(MVP PASS, 4/5显著) → D011(det优势=纯death avoidance) → D013(**framing pivot**: C1=empirical finding death avoidance ~99%, C2=episode-level counterfactual methodology + diagnostic probe)

**DDL**：EMNLP 2026 ARR May 25，剩 12 天。关键路径：预筛(~2h) → plan-001b数据(~3.7h双卡) → plan-002/012分析(~8h) → 写作(~3天) ≈ 总共 ~5天，余量约 1 周。

**最容易判断错的事**：
1. **不要试图复活 per-step labeling**。1-step tie rate 98.2%（D008），episode-terminal K=10 成本 78h（D009/D010 取消）。当前方案是 Plan C episode-level 2-way，这是唯一可行路径
2. **genuine-det tasks 极其珍贵**。预筛 14 task 中仅 3 个 genuine-det 且 2 个统计不显著。如果 25 task 全筛完 genuine-det 仍很少，C1 的 story 更加聚焦 death avoidance（这是特性不是缺陷，D013 已调整 framing）
3. **不要把 melt 和 change-state 当独立数据点**。它们共享 environment variations，论文中合并报告（D006）
4. **Router ≈ always-det 是预期结果**，不是失败。D013 framing 下 router 是 diagnostic probe，不需要证明 router > always-det。plan-011 keywords v2 已证明 keyword heuristic 在 episode-level 失效，这支撑了 learned routing 的价值
5. **mvp-p1-signal (PREPARING) 是历史遗留**，从未启动，已被实际 mvp-p1-gpu0/gpu1 系列取代


---
