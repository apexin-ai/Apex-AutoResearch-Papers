# agent / loop_24.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_24.md`
- **Structured JSON:** [`9dd54184cac2c97a305e.json`](../../sessions/9d/9dd54184cac2c97a305e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 24
reason: idle_timeout
updated: '2026-05-21T17:49:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-39279:cuda:0（gpu_ids 白名单仅此一张）
- DDL 2026-05-25 最终提交，论文已 Reviewer PASS
- 训练命令用 `--no_wandb`（服务器无 wandb API key），指标从 log 提取
- d154-8b-exec-s42-r3（K=2 版本）已 killed，不要重试
- 论文定位已收敛为 Findings track，不要在汇报中暗示冲 Main

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279，工作目录 ~/runs/solver-trace-ablation/
- Python：/root/miniconda3/bin/python（aml-train 镜像，conda base 环境）
- 模型路径：/root/autodl-tmp/models/Qwen3-8B（8B）；4B 模型同目录结构
- 数据：data/train_500_seed42.jsonl（500 条 FOLIO）
- 磁盘：根分区 ~400G 可用，/autodl-tmp ~5.3T 可用——充裕
- 活跃进程：无（GPU 空闲，0 active crons，0 running workers）

### 3. 📊 当前状态
全部实验完成，项目处于提交准备最终阶段。

- **Registry**: 176 total（70 success / 44 negative / 48 failed / 14 killed），0 RUNNING / 0 ANALYZING
- **D157 shuffled-ISR**: 3/3 seeds success，已写入 §4.3 + Limitations + Conclusion
- **D154 8B cross-model**: d154-8b-exec-s42-k4v2 conclusion=negative（8B 未复现 Goodhart collapse）
- **D158 LLaMA SFT**: killed（PR=0% gate 未通过）
- **论文**: v10+，Reviewer PASS，主文 ~7.4 页
- **等待中**: ISR 命名决策（待用户回复）；无 Worker/Cron 回调待处理

已向 Director 发送 Session #24 状态汇报，等待指令。

### 4. 📋 待办
- Director 回复 ISR 命名决策 → spawn Worker 全文替换术语 → 重新编译
- Director 指示最终提交 → 编译 PDF → 提交 ARR OpenReview
- 如 Director 要求补跑 d154-8b-exec-s43/s44 或 ISR 系列 → 按 D154 方案提交（命令模板同 k4v2）
- 如收到 R16+ 审稿反馈 → 按 action matrix 处理修改

### 5. 🎯 战略上下文
- **核心论点**: STA 作为 LOO 诊断工具揭示 GRPO 训练中 Goodhart effect。exec-only → TS 主导；ISR 本应缓解但引入不同 collapse pattern。D157 shuffled-ISR 提供因果证据排除 distributional confound。
- **决策链**: D147→D148→D149→D153→D154→D155→D156→D157→D158→D159。D159 确认 C2 不升级 "mechanistic"，§4.3 加 shuffled-ISR deconfounding。
- **d154-8b-exec-s42-k4v2 negative 的含义**: 8B 模型在 500 步内未复现 4B 的 Goodhart collapse，已在 limitations 标注 model-specificity。不代表 8B 免疫——可能需更长训练。但 DDL 内不再追加 8B 实验。
- **易错点**: 31 个 PREPARING 实验是历史占位，不是全部都要跑——以 Director 指令为准。report.md 告警区大量 failed/killed 是早期探索阶段的残留，不影响当前论文。


---
