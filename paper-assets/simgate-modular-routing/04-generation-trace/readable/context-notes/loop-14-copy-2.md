# agent / loop_14.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_14.md`
- **Structured JSON:** [`f91e71b994e95954b524.json`](../../sessions/f9/f91e71b994e95954b524.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: idle_timeout
updated: '2026-05-16T01:35:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 `cuda:0` 和 `cuda:1`（服务器 westb-13313）。历史上有 cuda:0/1 以外的违规记录
- 论文最新版在 `docs/paper/`，**不是** `artifacts/_project/paper/latex/`（后者是 5/14 旧版，Reviewer 验证以前者为准）
- Seed 42 adapter 使用了 episode-level split，与 seeds 43-49 的 step-level split 不同——任何涉及 seed 42 的 8-seed 汇总数据不可信，不能直接引用
- 55.7±5.0% step-level balanced_acc 已被 D082 判定为 data leakage artifact，**禁止在论文中作为 router 性能引用**。episode-level 独立 eval = 47.1±2.2%（随机水平）
- C2 reframe 提案（Narrative A：router cross-split failure confirms task-type-level signal）已提交 Director 但**尚未收到 [FRAMING APPROVED]**，论文 C2 相关章节**不能动**直到批准

### 2. 🖥️ 基础设施快照
- 服务器：**westb-13313**，2× RTX 5090
- 工作目录：`/root/autodl-tmp/simgate-modular-routing`
- Python：`/root/miniconda3/bin/python`（conda base 环境，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 模型路径：`/root/autodl-tmp/models/Qwen/Qwen3-1.7B`
- 数据路径：`data/plan-004-implicit/implicit_sft.jsonl`（implicit SFT 训练数据，81 episodes / 2040 steps）
- Checkpoints：`checkpoints/plan-008-qwen3-1.7b/final_adapter/`（seed 42，注意 split 不一致问题）；seeds 43-49 在各自 seed 子目录
- W&B：wandb 项目已配（训练时传 `--wandb`）
- 活跃进程：**无 cron 注册**。r7n2-data-size-ablation PID 921548 提交于 01:17 UTC，状态 ANALYZING，但无 cron 监控
- 活跃 Worker：`worker_exp_cross-split-multi-seed-eval_20260516T012511`（running，01:25 UTC 启动）

### 3. 📊 当前状态
- **78 DONE / 1 ANALYZING**，无 RUNNING 实验。两张 GPU 均空闲
- **r7n2-data-size-ablation**（ANALYZING）：data size ablation（81→200/400/800 synthetic episodes），验证 router balanced_acc 是否因数据不足饱和。PID 921548 on cuda:0，但**无 cron 监控**——需要手动 poll 或 SSH 检查进程是否还活着。如果已完成需要 spawn worker 分析结果
- **cross-split-robustness-8seed**（DONE, negative）：episode-level held-out balanced_acc = 47.1±2.2%，确认 router 不能跨 episode 泛化。已写入 D081-D086，Framing 调整提案（Narrative A）已提交 Director
- **Worker `cross-split-multi-seed-eval`** 仍在运行（01:25 UTC 启动），可能在做 cross-split 的详细分析
- **Round 8 审稿 + 用户审批 = BLOCKING**，Reviewer 最终验证进行中
- Director 尚未回复 C2 reframe 提案

### 4. 📋 待办（条件触发式）
- r7n2-data-size-ablation 完成 → spawn worker 分析结果：若 balanced_acc 随数据量饱和则确认 thin signal 是信号本身性质（支撑 Narrative A），若持续上升则 C2 有救需汇报 Director
- Worker `cross-split-multi-seed-eval` 回调到达 → 整合分析结果到 registry + report.md
- Director 回复 C2 reframe → 若 [FRAMING APPROVED] → Read `framing-reaudit` skill → 全文 re-audit（逐章节 diff 清单）
- 用户审批 Round 8 → 根据 Reviewer 反馈迭代论文
- GPU 空闲 + Director 有新指令 → 按指令提交（当前两张卡都空着，应尽快利用）

### 5. 🎯 战略上下文
- **核心结论链**：C1（death avoidance dominates routing signal，DAF=90.4%）稳固不受影响。C2 遭受重大打击——router step-level 55.7% 是 data leakage，episode-level = 随机。D086 采用 Narrative A：router 失败本身是 C1 的补充证据（信号在 task-type level，非 episode level，lightweight router 无法捕捉）
- **最容易判断错的事**：不要把 step-level eval 数字（55.7%、Table 7 的 56.2%）当作有效结果引用——这些全部被 D082 作废。只有 episode-level 47.1±2.2% 是可信数字，但它说明 router 不 work
- **容易踩的坑**：r7n2-data-size-ablation 没有 cron 监控，不会自动回调。第一件事应该 SSH 检查 PID 921548 是否存活，手动推进状态
- **DDL 压力**：EMNLP ARR 5/25，剩 9 天。实验基本完成，瓶颈在论文 reframing + Reviewer 验证 + 用户审批。C2 reframe 如果 Director 批准，需要全文 re-audit（非小改），预留 2-3 天
- **论文数据描述已修正**（D077）：step-level split、corrected gen eval、Table 7 统一。但 C2 reframe 后这些可能需要再改


---
