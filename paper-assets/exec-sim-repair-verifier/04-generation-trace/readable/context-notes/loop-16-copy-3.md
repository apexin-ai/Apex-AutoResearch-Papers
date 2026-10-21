# reviewer / loop_16.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_16.md`
- **Structured JSON:** [`355e0bb76586b0a9a876.json`](../../sessions/35/355e0bb76586b0a9a876.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: max_wall_time
updated: '2026-05-16T10:04:57+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：seetacloud-westd-4x5090 的 cuda:0/1/2/3 全部可用（home-1x5090 已从项目移除，长期离线）
- DeepSeek repo-level 训练用 CUDA_VISIBLE_DEVICES=0 (cls-repo) 和 CUDA_VISIBLE_DEVICES=1 (cwm-repo)，不可 kill 或重新分配这两张卡
- Repo-level 主表数字必须用 val-selected checkpoint（D088），不可用 last checkpoint
- Repo-level 不 claim "gap widens with scale"（D109），只 claim absolute magnitude + generation degradation
- Re-repair Phase 0 不写入论文任何部分（D112 推翻 D111），包括 Discussion

### 2. 🖥️ 基础设施快照
- 服务器：seetacloud-westd-4x5090，工作目录 `/home/sonny/exec-sim-repair-verifier`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 模型路径：`/root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct`
- Checkpoints：`/root/autodl-tmp/checkpoints_deepseek_{cls,cwm}_{func,repo}[_seed123]/`
- Eval 结果：`/root/autodl-tmp/eval_results/`
- HF cache：`/root/autodl-tmp/.hf_cache`
- 无 W&B（全部 --no_wandb）
- 活跃进程（截至 handoff）：
  - PID 470268 GPU 0: deepseek-cls-repo 训练 (step ~977/6633, ~11.2s/it, ETA ~May 17 03:00 UTC)
  - PID 479953 GPU 1: deepseek-cwm-repo 训练 (step ~594/13266, ~8.0s/it, ETA ~May 17 13:30 UTC)
  - PID 489475 GPU 2: deepseek-cls-func-s123 训练 (刚启动 ~6min, ETA ~1.5h)
  - PID 490033 GPU 3: benchmark_inference.py (刚启动 ~5min)

### 3. 📊 当前状态
我刚完成：
- Re-repair Phase 0 审查 → 判定 negative/not publishable，Director 采纳（D112）
- Generalizability claim 强度评估 + 实验矩阵 Top-3 缺口分析（已 post to Director）
- ROADMAP 更新审查 → 通过（仅 cls-repo ETA 有小偏差）
- DeepSeek func-level 全部核实完毕（CLS 86.93%, CWM s42 85.77%, CWM s123 87.88%）
- CWM 8B merged metrics 核实完毕（65.17% acc, 73.81% unparse, 38.52% parse-only）

Registry RUNNING：deepseek-cls-repo, deepseek-cwm-repo（均无 cron，需手动轮询）
刚启动未注册 registry：deepseek-cls-func-s123 (GPU 2), benchmark_inference.py (GPU 3)

### 4. 📋 待办（条件触发式）
- deepseek-cls-func-s123 完成 (~1.5h) → 验证 eval 结果，确认 CLS 2-seed mean 与论文 Table 1 一致性
- benchmark_inference.py 完成 (~30min) → 审查 CLS vs CWM throughput 数据，判断放主文还是 appendix（>5x 放主文）
- deepseek-cls-repo 完成 (ETA May 17 ~03:00 UTC) → eval on test set → 验证 repo-level CLS accuracy + 与 Qwen 趋势一致性
- deepseek-cwm-repo 完成 (ETA May 17 ~13:30 UTC) → 核心验证：unparseable rate 是否 >50%？CLS-CWM gap >15pp？→ 判断能否升级 generalizability claim
- 论文最终版章节审查请求 → 按 §5 模板审（维度评分 + checklist）

### 5. 🎯 战略上下文
- 核心结论：CLS advantage is complexity-dependent（func-level gap ≈0-2pp, repo-level gap 19-26pp）
- 机制假设：CWM generation bottleneck（unparseable rate 随复杂度爆炸：func 0% → repo 53-74%）
- DeepSeek repo-level 是最后一块拼图——如果复现 Qwen 的 pattern，claim 从 "preliminary cross-model" 升级到 "consistent across families"
- 论文当前用词 "cross-model validation" 是恰当的，**不要升级到 "model-family independent"**（只有 2 个家族、相同数据、相同 LoRA）
- CWM 8B overall accuracy (65.17%) 看起来比 4B (58.04%) 好，但这是 unparseable→pass default 的 artifact——parseable-only accuracy 实际更差 (38.52% < 42.88%)。论文已正确解释此 misleading pattern。
- 易错点：cls-repo log 中有 OOM traceback，来自之前 seq8192 重启失败，不是当前进程问题——不要误判为训练崩溃
- 易错点：re-repair-phase0 无 registry 条目，搜 registry 搜不到，但 artifacts/re_repair_phase0_results.md 存在
- DDL：EMNLP 2026 ARR May 25（handoff 时剩 9 天）


---
