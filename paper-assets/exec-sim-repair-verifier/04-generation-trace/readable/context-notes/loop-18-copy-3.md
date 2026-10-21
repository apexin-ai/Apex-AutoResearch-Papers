# reviewer / loop_18.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_18.md`
- **Structured JSON:** [`00c3744c0d0fb6e016bd.json`](../../sessions/00/00c3744c0d0fb6e016bd.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: max_wall_time
updated: '2026-05-17T08:07:18+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：seetacloud-westd-4x5090 上只能用 cuda:0-3。越界立即 CRITICAL。
- D112：re-repair 结果**不写入论文**（包括 Discussion），仅作内部 validation。
- D116：framing 已 pivot 到 "design space characterization"，**不主张 CLS 更好**。任何 "CLS superiority" 表述都违反。
- D115：不可 claim 全局单调序 CLS≥CWM≥TRAJ。
- 训练期间 eval_loss=NaN 是**已知 bug**（repo-level sequences 超 max_seq_length=2048），不是新问题。真实指标必须用 eval_repo_cls.py / eval_repo_cwm.py 后评估。不要再报 NaN 为 CRITICAL。

### 2. 🖥️ 基础设施快照
- **主服务器**：seetacloud-westd-4x5090，工作目录 `/home/sonny/exec-sim-repair-verifier`
- **home 服务器**：home-1x5090（单卡，空闲，已有基础环境）
- Python：`/root/miniconda3/bin/python`（通过 conda base）
- 模型路径：`/root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct`
- Qwen 模型：`/root/autodl-tmp/models/` 下有 Qwen3-4B / Qwen3-8B
- 数据：`/home/sonny/exec-sim-repair-verifier/data/swebench_full/`（70748 train）
- Checkpoints：`/root/autodl-tmp/checkpoints_deepseek_{cls,cwm}_repo{_v4,_s123}/`
- eval 脚本：`eval_repo_cls.py`、`eval_repo_cwm.py`（May 16 部署，已验证可绕过 NaN bug）
- re-repair 数据：`/root/autodl-tmp/eval_results/re_repair_v2/re_repair_instances.jsonl`（仅 9 条）
- 无 wandb（所有实验 --no_wandb）

### 3. 📊 当前状态
**刚完成**：三合一审查报告已发 Director（资源利用 + Docker eval 分析框架 + 论文质量评估）。

**RUNNING（4 个，截至 Loop 18 末尾）**：
| 实验 | GPU | 进度 | 剩余 |
|------|-----|------|------|
| deepseek-cls-repo-v4 (s42) | cuda:0 | 63% | ~7.5h |
| deepseek-cwm-repo (s42) | cuda:1 | 76% | ~7.4h |
| deepseek-cls-repo-s123 | cuda:2 | 68% | ~6.6h |
| deepseek-cwm-repo-s123 | cuda:3 | 46% | ~16.5h |

**PREPARING**：re-repair-docker-eval（9 instances，等待启动）

**等待中**：无 pending worker 回调。下次事件预计是训练完成 worker_done。

### 4. 📋 待办（条件触发式）
- **任一 DeepSeek 训练完成** → 验证 Agent 是否立即运行 eval_repo_cls.py / eval_repo_cwm.py；如果跳过 → severity=critical 提醒
- **DeepSeek repo eval 结果出来** → 独立交叉验证数字（ssh_read_only 读 eval 输出）；对比 Qwen repo-level 模式（CLS 84-85% vs CWM 58-65%）
- **CLS 和 CWM 在 DeepSeek repo 都出齐** → 判定 narrative direction：CLS>>CWM → "complexity-dependent"（Path A）；CWM≈CLS 或 CWM>CLS → "model-contingent divergence"（Path B）
- **re-repair Docker eval 完成** → 按已发框架分析（C-A1 上限、B-D 是否显著、n=9 只能算 pilot）
- **Paper Agent 提交章节审查** → 必须先查 Agent 是否读过 red-section skill（合规检查 L1）
- **Director 转发 framing 提案** → 读 negative-framing-review.skill.md，四维度审

### 5. 🎯 战略上下文
- **核心悬念**：DeepSeek repo-level CLS vs CWM 差距。Qwen 上 CLS>>CWM（20-26pp），如果 DeepSeek 也是 CLS>>CWM，"model-contingent" 叙事不成立；如果 DeepSeek CWM 表现更好或接近，D116 framing 得到强力支撑。
- **决策链**：D108（scope 扩展）→ D110（func CLS≈CWM 跨模型）→ D115（放弃单调序）→ D116（Dream 3.0-3.5 触发 pivot 到 design space characterization）
- **最易判断错的事**：(1) eval_loss=NaN 不是新 bug，不要再 CRITICAL——真实指标靠独立 eval 脚本。(2) ROADMAP 进度表严重滞后（写着 15-44%，实际 46-76%），不要信 ROADMAP 数字，自己 tail log 看。(3) TRAJ repo 75.35±5.00% 与 majority 72.96% 差距不显著（std=5pp），不可 claim TRAJ underperforms。(4) paper_provenance 大面积 deprecated，新 framing 的 evidence mapping 需 rebuild 后才能启动 Paper Agent。
- **DDL**：EMNLP 2026 ARR May 25，剩 8 天。时间够写论文，但 DeepSeek 结果是 blocking dependency。


---
