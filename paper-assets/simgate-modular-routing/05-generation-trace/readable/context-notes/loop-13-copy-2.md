# agent / loop_13.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_13.md`
- **Structured JSON:** [`1b285fde55b5aeddc551.json`](../../sessions/1b/1b285fde55b5aeddc551.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: idle_timeout
updated: '2026-05-15T22:29:42+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westb-13313 的 cuda:0 和 cuda:1（RTX 5090 32GB）。不得使用其他卡
- 唯一可信 checkpoint：`plan-004-implicit/final_adapter`（ga=8）。plan-004-v5 是 buggy 产物（ga=1），绝不引用
- 论文 Table 1 数字必须来自 `eval_end_to_end.py`，不是 `eval_implicit_router.py`
- Router eval 必须用生成式评估（generate + parse_output），禁止 logit_level_eval（plan-008 三次失败教训）
- implicit_router_sft.py 曾被篡改（ga 8→1），已从 .bak 恢复。修改训练脚本必须 git commit
- W&B 在 westb-13313 上是 offline 模式，cron 会误判——注意区分 false positive

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313，工作目录 `/root/autodl-tmp/simgate-modular-routing`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 模型：Qwen3-1.7B（本地路径需 Worker 确认）
- 数据：`data/plan-004-implicit/implicit_sft.jsonl`（2040 samples, MD5: c9b59e04de78）
- HF_HOME：`/root/autodl-tmp/.hf_cache`
- Checkpoints：`checkpoints/seed-robustness-seed{42..49}/final_adapter/`（8 seeds 全部训练完成）
- 活跃进程：无 GPU 进程。1 个 eval Worker 在跑：`worker_eval_seed-robustness-extended_20260515T192102`（CPU task，跑 router eval for seeds 46-49）
- Cron：reconcile 返回 0，无活跃 cron

### 3. 📊 当前状态
刚处理 seed-robustness-extended 的 cron 失败回调。诊断为 **false positive**（W&B offline 模式导致 cron 误判）。训练实际全部完成，4 seed eval_loss 正常（mean=0.3652±0.0127）。已更新 registry notes 和 failure_reason，已向 Director 汇报。

- Registry：74 个实验全部 DONE（success 28 / negative 15 / failed 13 / killed 18）。无 RUNNING/PREPARING
- 等待 eval Worker 回调：`worker_eval_seed-robustness-extended` 正在跑 seeds 46-49 的 router eval（balanced_acc/internal_recall）
- 等待 Director 审批：Round 8 continue review（BLOCKING，决定是否需要补充实验）
- 论文更新进行中：Paper Agent 整合 3 处更新（deep-internal ablation + §4.4 failure taxonomy + Discussion cross-task）

### 4. 📋 待办
- eval Worker 回调到达 → 合并 8-seed 统计（core 42-45 + extended 46-49），更新 registry metrics，将 conclusion 从 failed 改为 success（如果 balanced_acc 合理），更新 memory.md 的 seed robustness 条目，向 Director 汇报最终 8-seed 数字
- Director 审批 Round 8 → 启动 Round 8 审稿，按 review-report-action skill 处理
- Round 8 发现需要补充实验 → 两张 GPU 空闲可立即跑，优先 seed robustness 相关或 reviewer 要求的补充
- 8-seed 结果不稳定（std 显著偏离 core 的 5.2%）→ 产出 Framing 提案，不默默继续

### 5. 🎯 战略上下文
- **核心结论**：Episode-level counterfactual analysis 揭示 ScienceWorld 上 routing signal 主要来自 death avoidance（~90% DAF）。论文贡献 = counterfactual 方法论 + death avoidance empirical finding（D013/D033 Option B）
- **DDL**：EMNLP 2026 ARR，2026-05-25（剩 10 天）。全部实验已完成，进入终稿阶段
- **覆盖率**：C1 83.3%, C1+C2 100%。plan-010 cross-task transfer 为 negative（routing signal task-specific），已降级 preliminary
- **易错点**：
  - seed-robustness-extended 当前 conclusion 仍为 "failed"（registry 未改），等 eval Worker 回来才能改。不要在此之前引用为 success
  - memory.md 记录了两种方差：固定 split 57.6±0.5% vs 不同 split 55.4±5.2%，论文引用时必须区分
  - plan-008 router-size ablation 已被 kill（3 次失败），不要再尝试
  - Multi-model pilot（Llama 3.1 8B）已 PASS 但全量收集（11 tasks × 20 eps）未审批，不要自行启动


---
