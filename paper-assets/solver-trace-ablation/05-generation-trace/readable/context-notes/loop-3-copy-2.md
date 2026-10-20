# agent / loop_3.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`d88953fe5a48bfc5d260.json`](../../sessions/d8/d88953fe5a48bfc5d260.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: idle_timeout
updated: '2026-05-14T05:04:12+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单只有 `westd-39279:cuda:0` 和 `westd-39279:cuda:1`，绝无第三张卡
- 所有命令必须 `bash -c "export CUDA_VISIBLE_DEVICES=N && ..."`，inline 赋值子进程看不到（已有 3 次事故）
- 训练日志中的 ISR 是 binary approximation（_fast_fn），**禁止用于论文或跨实验对比**——所有 checkpoint 必须用 `eval_sta.py` (full STA) 重新评估才可引用
- checkpoint 路径：save_total_limit=1 时模型在 output_dir 根目录，不在 checkpoint-N 子目录
- TRL 必须 `log_completions=False` + `save_total_limit=1`，output 放 `/root/autodl-tmp/outputs/`（磁盘空间教训 C003）
- plan014 downstream NLI 已确认 negative (D021/D022)，不再重跑——ISR-accuracy 验证降级为 limitation/future work

### 2. 🖥️ 基础设施快照
- **服务器**: westd-39279，2× RTX PRO 6000 Blackwell 94GB
- **工作目录**: `/root/solver-trace-ablation/`
- **Python**: `/root/miniconda3/bin/python`（conda base，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- **模型**: `/root/autodl-tmp/models/Qwen3-4B`
- **数据**: `/root/solver-trace-ablation/data/train_500_seed42.jsonl`（500条，所有实验统一用此 C001）
- **Eval 数据**: `/root/solver-trace-ablation/data/proofwriter_fol_100.jsonl`
- **输出**: `/root/autodl-tmp/outputs/plan{NNN}_*`
- **活跃进程**:
  - plan001-exec-only-s44: PID 226200, tmux session, cuda:0
  - plan017-additive-random-s42: PID 207116, tmux session, cuda:1
- **Cron**: 两个活跃 cron 分别监控上述两实验

### 3. 📊 当前状态
**刚完成**: plan014 downstream NLI (negative)、plan002 additive β=0.3 eval (negative)、plan001-s43-r4 eval (negative: 13% eval PR，seed instability confirmed)。三个连续 negative 触发了论文 framing 大调整。

**RUNNING**:
- `plan001-exec-only-s44` (cuda:0): 第 3 seed，解决 s42(93%) vs s43(13%) 跨 seed 不稳定，3-seed mean±std 是论文必需
- `plan017-additive-random-s42` (cuda:1): additive random control (r=r_exec·(1+0.3·random))，隔离 ISR signal vs variance regularization

**等待中**: 两个 cron 回调（完成时自动触发 on-experiment-done）

### 4. 📋 待办（条件触发式）
- plan001-s44 完成 → `eval_sta.py` 评估 checkpoint → 得到 3-seed 统计 (s42=93%, s43=13%, s44=?)
- plan017 完成 → `eval_sta.py` 评估 → 与 plan001-s42 (ISR=0.123) 和 plan013 (ISR=0.535/tautological) 对比
- 两者 eval 出齐 → 完整 ISR 对比表：exec-only (3-seed) vs random-reward vs additive-random → 判断 ISR 是否有结构信号
- 若 plan017 ISR ≈ plan013 ISR (0.5 区间) → 确认 ISR 训练信号路线全死，论文 narrative 锁定 "ISR 作为诊断指标"
- 若 s44 eval PR >> s43 (接近 s42) → 3-seed 中位数为高 PR，s43 是异常值，仍可 claim exec-only convergence
- 若 s44 eval PR ≈ s43 → exec-only 高方差是系统性问题，需在论文中正面讨论
- 所有 eval 完成后 → 向 Director 汇报完整对比 + 论文 narrative 建议

### 5. 🎯 战略上下文
**核心结论链**: ISR 作为训练信号所有路线均失败（convex D005/penalty, additive D020/低泛化, random D018/tautological hacking）。论文方向已从 "STA improves training" pivot 到 "STA as diagnostic metric that detects structural quality/hacking"。

**决策链关键节点**:
- D010/D011: framing 从 "STA detects hacking" → "STA as diagnostic + additive bonus"
- D018: random reward ISR=0.535 是 tautological (2-component proof)，不是真的结构好
- D019: ISR 衡量 syntactic component necessity，不是 semantic faithfulness
- D021/D022: downstream NLI 验证降级为 limitation

**最易判断错的事**:
1. plan013 的 ISR=0.535 看起来很高——但它是 tautological hacking（2-component trivial proof），不要引用为 "random reward produces better structure"
2. 训练日志里的 ISR 数字（如 plan001 训练 ISR=0.86）全是 binary approximation，与 eval_sta.py 结果天差地别——只信 eval 结果
3. DDL 还有 11 天，GPU 时间充裕（528 GPU·h 可用），不要 fallback 思维
4. Dream review 给出 4/6 borderline reject——论文需要强化 narrative 而非堆更多实验


---
