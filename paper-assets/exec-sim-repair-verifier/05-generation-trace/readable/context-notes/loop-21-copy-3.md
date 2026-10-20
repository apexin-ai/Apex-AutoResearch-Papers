# reviewer / loop_21.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_21.md`
- **Structured JSON:** [`66e24f94b687aed90e6f.json`](../../sessions/66/66e24f94b687aed90e6f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 21
reason: max_wall_time
updated: '2026-05-19T08:47:52+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：seetacloud-westd-4x5090 上 cuda:0-3。越界立即 CRITICAL。
- Reviewer 只读：不执行实验、不修改文件。唯一输出渠道 `reviewer_post_to_director`。
- 论文 TOST 数据溯源已验证：§Equivalence 的 gap=-0.45pp / p=0.007 来自 5-seed variant-level clustered bootstrap（registry line 1460-1491），**不是** `tost_sensitivity_cls_traj.json`（那个是 per-test 3-seed，且 CLS seed42 值有误=87.51 实为 CWM 值）。下一个"你"不要混淆这两个数据源。
- Appendix 的 TOST sensitivity table 已在 D152 中整个删除（因 CLS-CWM SE 是反推的，circular）。不要试图恢复它。

### 2. 🖥️ 基础设施快照
- 服务器：seetacloud-westd-4x5090，工作目录 /home/sonny/exec-sim-repair-verifier
- Python：/root/miniconda3/bin/python
- 模型路径：/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/, /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct
- Checkpoints：/root/autodl-tmp/checkpoints_*
- 数据：func-level data/, repo-level data/swebench_full/
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/
- 论文：docs/paper/*.tex
- 活跃进程：qwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval (PID 778328, cuda:0, tmux)
- GPU 1/2/3 空闲（GPU 2 nvidia-smi 显示 100% 是驱动虚报，无真实进程）

### 3. 📊 当前状态
**刚完成**：Round 4 审稿 Action Matrix 独立评估，已 post 给 Director。评估结论：全部可行，6 天内完成，预期 3.0→3.5。

**RUNNING**：
- `qwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval`：41.5% (4064/9784), running_acc=63.6%, ETA ~2026-05-20 04:00 UTC。解决 D146 seq_length 混淆变量。

**PREPARING** (14项，多数是历史残留)：
- `exp-downsample-cls-func-v3-eval-v2`：downsample eval 重跑（v1/v2 均 FileNotFoundError，但 metrics 已从 log 提取到 registry: 80.74%）

**等待中**：
- Director 对 Action Matrix 评估的回复/决策
- CWM eval 完成 → 需审查最终 accuracy 并决定是否更新 Table 4

### 4. 📋 待办
- CWM eval 完成回调 → 审查最终 per-test accuracy + variant-level accuracy；与 seq8192 结果 (65.17%) 对比；如差距 <3pp 建议更新 Table 4 消除 footnote "not directly comparable"
- Director 下发 Action Matrix 执行 → 审查 C1 TOST margin sweep 数据正确性（必须用 variant-level bootstrap，不是 per-test）；审查 C3 bootstrap CI 计算
- Paper Agent 提交修订稿 → 做 Round 5 写作审查（用 §5.3 评分模板）
- Worker 新实验提交 → 常规审查（GPU 白名单 + 指标一致性）

### 5. 🎯 战略上下文
- **项目核心**：三种 execution-free verification formulation (CLS/CWM/TRAJ) 的系统比较，目标 EMNLP 2026 ARR (DDL May 25)
- **D116 pivot**：从 "CLS advocacy" 转为 "formulation design space empirical characterization"
- **D148→D152 决策链**：TOST 交叉污染发现→修正→过度修正→恢复。最终状态：§Equivalence 保留 variant-level gap=-0.45pp, p=0.007；删除了 CLS-CWM 反推数据
- **Round 4 评分 3.0 (Findings)**：两位审稿人共识。C1(TOST margin)/C2(controlled overclaim)/C3(n=48 power) 是三个 critical
- **最易判断错的事**：
  1. 论文中有两套 TOST 数据——variant-level (gap=-0.45pp, 正确) 和 per-test (gap=+1.89pp, Worker 分析有数据错误)。不要用后者替代前者
  2. experiments.tex line 139 写 "~8K instances" 而 appendix 写 "386 variant-level instances"——这是跨文件不一致，已报告 Director 但未修
  3. CWM 的 NaN validation loss 不是 bug 而是 truncate preprocessing 的已知行为(D144)，不可能 6 天修复，应作为 limitation 讨论


---
