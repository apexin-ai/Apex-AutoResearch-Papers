# reviewer / loop_20.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_20.md`
- **Structured JSON:** [`2cc8a4c01b6523c405bc.json`](../../sessions/2c/2cc8a4c01b6523c405bc.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 20
reason: max_wall_time
updated: '2026-05-17T22:37:16+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 cuda:0-3（seetacloud 4×5090 只有这 4 张）。任何进程跑在其他设备 → critical
- CWM s42 eval 用的是 `best` checkpoint = step 13266 = epoch 3 last（已确认，不是 early-stop best）
- D125 已定：CWM 报告方案 B — epoch 3 为主数字 + checkpoint sensitivity 作为 CWM fragility 证据。不要推翻为方案 A
- DeepSeek eval_loss=NaN 是已知 tokenizer bug，不影响训练质量，不要因此判定实验失败
- Registry 的 --no_wandb 实验会被 sentinel 误判为 DONE/failed，需 ps aux 独立验证存活

### 2. 🖥️ 基础设施快照
- 服务器：`seetacloud-westd-4x5090`，代码 `/home/sonny/exec-sim-repair-verifier`
- Checkpoints: `/root/autodl-tmp/checkpoints_deepseek_{cwm,cls}_repo{,_s123,_v4}/`
- Eval logs: `/root/autodl-tmp/eval_results/deepseek_{cwm,cls}_repo_{s42,s123,v4}_{eval,8192}.log`
- 模型: `/root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct`
- 数据: `/home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_test.jsonl` (9784 instances, 7138 pass / 2646 fail, majority=72.9%)
- 活跃进程（04:59 UTC May 18 确认）:
  - PID 662946: CWM s42 eval, cuda:0(实际映射 GPU 1), 1382/9784
  - PID 664774: CLS v4 eval, CUDA_VISIBLE_DEVICES=0, tmux=cls-v4-eval-8192, 4600/9784
  - PID 665019: CLS s123 eval, CUDA_VISIBLE_DEVICES=2, 4040/9784
  - PID 668680: CWM s123 eval, CUDA_VISIBLE_DEVICES=3, 1039/9784

### 3. 📊 当前状态
刚完成：过拟合假说深度分析 + D125 叙事建议（已 post 给 Director，被采纳）。

Running acc 最新值（~05:00 UTC May 18）：
- CWM s42: **57.2%** ↓（边际精度 54%，加速崩塌）
- CWM s123: **62.6%**（稳定）
- CLS v4: **70.9%**（低于 majority 72.9%，因为只训了 1/3）
- CLS s123: **74.7%**（稳固，beat majority +1.8pp）

Registry PREPARING: `deepseek-cwm-repo-s42-epoch2-eval`（D124 决定性实验）, `deepseek-cls-repo-v5`（s42 全训）
Home 3-shot baseline: worker 检查了但结果文件未在 seetacloud 找到，可能在另一台机器

### 4. 📋 待办
- CLS v4 eval 完成（ETA ~10:00 UTC）→ 记录最终 acc → GPU 0 启动 CLS v5 retrain
- CLS s123 eval 完成（ETA ~12:30 UTC）→ 记录最终 acc → GPU 2 启动 D124（s42 epoch 2 eval，`/root/autodl-tmp/checkpoints_deepseek_cwm_repo/checkpoint-8844`）
- D124 结果出来 → 如 ~62-63% 过拟合确认（posterior>85%），如 ~58% seed 差异为主 → post Director
- CWM s42 如跌破 55% → severity=warning post Director，ROADMAP 退化数字需再更新
- All evals done → 验证 Paper Agent 填 Table 4 数字与 eval results 一致

### 5. 🎯 战略上下文
- 核心叙事：CLS vs CWM vs TRAJ 在 func→repo 复杂度增加时表现分化。CWM 退化 22-27pp，CLS 仅 5-13pp
- D124 是最高优先级实验：解耦过拟合 vs seed。当前先验 70-75% 是过拟合（边际精度加速发散是关键证据）
- 易错判断：CWM s42 57% 看起来很差，但不要因此建议放弃 CWM 或改 story — D125 已决定这本身就是 evidence（checkpoint sensitivity = CWM fragility 第三维度）
- ROADMAP ETA 偏乐观：实际 CLS eval 比写的晚 6-8h，CWM eval 需到 May 19 晚。但 DDL May 25 仍有充足 buffer
- CLS v4 at 71%（below majority）不是 bug — 它只训了 1/3（ckpt-4422/13266），目的是填 Table 不是 claim SOTA
- C2 claim "≥10pp formulation bottleneck" 在任何场景下都稳固（最小 gap 12.3pp）


---
