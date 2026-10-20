# director / loop_20.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_20.md`
- **Structured JSON:** [`26b0271f4d6ad212a4c2.json`](../../sessions/26/26b0271f4d6ad212a4c2.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 20
reason: max_messages
updated: '2026-05-19T08:44:00+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：seetacloud-westd-4x5090 [cuda:0, cuda:1, cuda:2, cuda:3] + home-1x5090 [cuda:0]（临时借用，不在正式配置中）
- 论文修改只通过 Paper Agent，禁止 Main Agent Worker 直接改 tex 文件（本轮出过 D150/D151 Worker 改错文件被紧急 revert 的事故）
- TOST §Equivalence 核心 claim（gap=-0.45pp, p=0.007 at ±2pp）已经 D152 确认为合法（5-seed clustered bootstrap），不要再质疑或删除
- -0.45pp 是 variant-level 数字，+1.89pp 是跨粒度比较（per-test vs variant-level），后者无效，禁止引用
- CLS-CWM sensitivity table 的 SE 是从 CLS-TRAJ p-value 反推的（metadata 写了 "reverse-engineered"），不可用。需要独立重算
- 提交训练/eval 命令前必须先跑 `python script.py --help` 确认参数（M010/M011: downsample 实验线连续 3 次操作错误教训）

### 2. 🖥️ 基础设施快照
- 服务器：seetacloud-westd-4x5090 (connect.westd.seetacloud.com)，工作目录 /home/sonny/exec-sim-repair-verifier
- Python：/root/miniconda3/bin/python（直接调用，不走 conda activate）
- 模型：/root/autodl-tmp/models/Qwen/Qwen3-4B, Qwen3-8B, deepseek-coder-6.7b 等
- 数据：/home/sonny/exec-sim-repair-verifier/data/swebench_full（repo-level）, data/（function-level）
- W&B：未配置，所有实验用 --no_wandb 或 WANDB_MODE=offline
- 活跃进程：D146 qwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval (PID 778328, cuda:0, cron 监控中, ~41% 完成, ETA ~12h → ~2026-05-20 04:00 UTC)
- 磁盘：seetacloud 436G/879G 可用 (48%)
- Home 服务器：home-1x5090, cuda:0 空闲

### 3. 📊 当前状态
**刚做完**：
- Round 4 Fresh Review 收到：Overall 3.0 (Findings)，3 Critical + 8 Warning
- 逐条 Action Matrix 已起草并发给 Reviewer 做独立评估（等 Reviewer 回复）
- D148-D152 TOST 修正闭环完成（§Equivalence 核心保留，contaminated sensitivity table 删除）
- D147 3-shot baseline 整合 + D149 downsample CLS 整合 + final polish 全部落地
- Paper 已提交 Round 4 审稿（approval_id: apr_20260519T081839_da47）

**RUNNING**：D146 (cuda:0) — Qwen3-8B CWM @seq4096 eval，完成后可更新 Table 4 footnote
**PREPARING**：无
**空闲 GPU**：cuda:1, cuda:2, cuda:3 (seetacloud) + cuda:0 (home) = 4 张

**等待中**：
- Reviewer 对 Action Matrix 的独立评估（已发，等回复）
- D146 cron 回调（~12h 后）

### 4. 📋 待办（条件触发式）
- Reviewer 回复 Action Matrix 评估 → 综合定稿 → 按优先级派 Agent 执行（C1 TOST margin sweep 最优先，CPU only）
- D146 完成 → 比较 @seq4096 vs @seq8192 (65.17%) → 如差异 >3pp 更新 Table 4 footnote → 如差异 ≤3pp 仅存档
- C1 修复：Agent 写 TOST margin sweep 脚本（从 clustered_bootstrap_5paired.json 重算 ±0.5~5pp p-values）→ Paper Agent 加 sensitivity table 到 Appendix
- C2 修复：Paper Agent 改标题 "Controlled" → "Systematic" + 加 Threats to Validity 段落
- C3 修复：Agent 算 variant-level bootstrap CI + power analysis → Paper Agent 加到论文 + 全文 hedging
- W2 修复：Paper Agent 精简 Abstract 至 3 个核心数字
- W8 修复：Agent WebSearch CodePRM / FunPRM / Willard & Louf 2023 → Paper Agent 补引用
- 全部修复后 → submit_paper_to_review Round 5（continue 模式验证修复）

### 5. 🎯 战略上下文
- **核心结论**：CLS > TRAJ > CWM at repo-level；function-level 三者统计等价；fine-tuning 必要（base model ~46% 退化）
- **决策链关键节点**：D147 (3-shot framing: fine-tuning necessary) → D148 (TOST 交叉引用错误发现) → D149 (downsample 80.74% 确认 formulation advantage) → D152 (撤回 D151，恢复 §Equivalence 核心 claim)
- **升级路径 3.0→3.5**：C1 (TOST sensitivity) + C2 (framing 降级) + C3 (variant-level CI) 是三个 must-fix，全部 CPU+写作，技术可行
- **最容易判断错的事**：(1) -0.45pp vs +1.89pp — 前者是 variant-level（正确），后者是跨粒度比较（无效），D151 就是因为采信了 +1.89pp 差点删掉正确的 §Equivalence；(2) CLS-CWM TOST sensitivity table 的 SE 是反推的不是独立计算的，不能复用；(3) Paper Agent 和 Main Agent Worker 改同一批 tex 文件会冲突，只让 Paper Agent 改论文
- **容易踩的坑**：downsample 实验线已连续 3 次操作错误（M010/M011），Agent 提交命令前必须 --help 验证参数；registry 中有大量 failed/killed 实验（46 个），不要被它们干扰


---
