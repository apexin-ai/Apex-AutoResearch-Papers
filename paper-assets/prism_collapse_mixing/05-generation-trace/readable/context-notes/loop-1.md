# director / loop_1.md

**prism collapse mixing** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`47fb7b3c854add57d2a6.json`](../../sessions/47/47fb7b3c854add57d2a6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-15T22:17:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 仅限 cuda:0 和 cuda:1 @ rtx6000-diagprobe（C001 已注册）
- 服务器账号: root，远程路径: `/root/prism_collapse_mixing`
- MVP pass/fail 阈值已预注册（D002），**禁止修改**: entropy |ρ|>0.7@Gen0-1 → |ρ|<0.5@Gen3 + 信号退化≥15% + 2 seed 一致
- spectral_rank per-example ρ 基线低（0.21）是结构性的不是 bug，不要试图"修复"或调整阈值（D003）
- W&B 未配置，启动训练必须带 `WANDB_MODE=disabled`

### 2. 🖥️ 基础设施快照
- 服务器: rtx6000-diagprobe (connect.westd.seetacloud.com)，2× RTX PRO 6000 Blackwell (98GB each)
- 工作目录: `/root/prism_collapse_mixing`（6 个 Python 文件 ~800 行）
- Python: `/root/miniconda3/bin/python`（conda base, Python 3.12.3, PyTorch 2.10.0+cu128）
- HF cache: 模型 `EleutherAI/pythia-410m-deduped` 已缓存，启动带 `HF_HUB_OFFLINE=1`
- 数据: probe_set.jsonl (5000行), val_set.jsonl (14881行), real_pool.jsonl (579K行/1.8GB), Gen 1 合成数据已生成 (seed42 335MB + seed137 336MB), Gen 1 混合数据已生成
- 活跃进程: **需要确认** — 刚发了紧急消息让 Agent 检查 PID 197985/198116/198117 是否存活，GPU 显示 0% compute 疑似训练又崩了
- tmux session: `mvp_collapse_decoupling`
- 日志: `~/runs/prism_collapse_mixing/mvp_collapse_decoupling.log`

### 3. 📊 当前状态
训练已经崩溃两次: 第一次 W&B API key 未配置，第二次疑似又崩（GPU 0% compute）。我刚发了 urgent_agent_message 让 Agent 检查进程状态和日志，**Agent 尚未回复**。

registry: `mvp_collapse_decoupling` RUNNING（但实际可能已崩）
Gen 0 baseline 信号已完成: entropy↔loss ρ=0.929, spectral_rank↔loss ρ=-0.211
Gen 1 合成数据 + 混合数据已生成（~135min），不需要重跑
Gen 1 训练: checkpoints 为空，尚未成功完成过

RESET_BOTH 已批准，Reviewer 即将重置。

### 4. 📋 待办
- Agent 回复训练状态 → 如果崩了，诊断根因并修复重启（这是最高优先级，不做其他任何事）
- Gen 1 训练完成 → 收 per-example ρ(loss, entropy) 值，对比 Gen 0 的 0.929
- Gen 1/2/3 全部完成 → 用预注册标准判 pass/fail（entropy |ρ| 衰减 + 均值退化 ≥15% + 2 seed 一致）
- MVP pass → `complete_mvp()` 进入 research 阶段，写 paper_framing.md + experiment_plan.yaml
- MVP fail/weak pass → 按 memory.md 备选叙事: (a) 扩到 5 代 (b) 增加 tokens/gen (c) 换 1B 模型

### 5. 🎯 战略上下文
- 项目核心: PRISM 用 collapse 信号增强 online data mixing。MVP 验证 collapse 信号是否与 loss 脱钩。
- 决策链: D001(MVP方案) → D002(量化阈值+2seed) → D003(entropy为主信号，spectral_rank降为辅助)
- 目标: EMNLP 2026 ARR (5/25, 仅剩10天，极紧) → ICLR 2027 (~9月)
- 立项评审出口共识仅 33%，主要风险是 novelty ceiling（"显而易见的工程组合"）
- **最容易判断错的事**: 训练不稳定不要反复尝试同一个修复方案——已经崩了两次，第三次启动前必须彻底排查 train.py 的所有外部依赖（W&B 已修，可能还有别的）。同时注意 `run_pipeline.py` 的数据复用逻辑——已有合成/混合数据应被跳过，检查 `--start_gen 1` 是否真的跳过了生成步骤
- plot_results.py 可视化脚本已写好（3 个 PDF），备选叙事和 figure layout 已写入 memory.md


---
