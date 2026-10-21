# agent / loop_19.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_19.md`
- **Structured JSON:** [`42845dca87b7bea4afee.json`](../../sessions/42/42845dca87b7bea4afee.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: idle_timeout
updated: '2026-05-16T19:27:20+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单只有 westd-39279:cuda:0 和 cuda:1，不可用其他卡
- Round 2 实验全部用 `--no_wandb`（服务器无 wandb key），metrics 从 reward_log.csv / eval 输出提取
- submit_training_job command 必须 `bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && ..."`——裸 source 在 tmux sh 下会 127
- 训练脚本路径：`python3 scripts/train_grpo.py --config configs/...`（不是根目录下的 train_grpo.py）
- conclusion=success 判断标准：高 hacking + ISR collapse = 验证 Goodhart 假设 = success（不是 negative）
- 不要说 "H7 is ISR-specific"——只有 H7b 是，H7a 是 GRPO 通用的
- gated-ISR-curriculum 两个实验已 **FAILED**（report.md 外部更新确认），双卡现在空闲

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279，工作目录 `/root/solver-trace-ablation`
- Python：`/root/miniconda3/bin/python3`（conda base env）
- 4B 模型：`/root/autodl-tmp/models/Qwen3-4B`
- 1.7B 模型：`/root/autodl-tmp/models/Qwen3-1.7B`（已下载确认）
- 数据：`data/train_500_seed42.jsonl`（训练），`data/proofwriter_fol_100.jsonl`（eval）
- 输出目录：`/root/autodl-tmp/outputs/`
- 活跃进程：**无**（双卡空闲）
- 无 wandb，无 HF 下载需求

### 3. 📊 当前状态
**刚做完**：Session-start 初始化。发现 report.md 被外部系统更新——gated-isr-curriculum-t02 s42/s43 r2 已 FAILED，新实验出现：
- `gated-isr-warmstart-t015-s43` (success)
- `exec-retrain-for-warmstart-s42` (success)
- `gated-isr-warmstart-t02-s43-r2` (failed)
- 新 QUEUED：`w2-qwen3-1.7b-isr-b03`（1.7B ISR β=0.3 dose-response 验证）

**Registry 关键**：
- RUNNING: 0（双卡空闲）
- QUEUED: `w2-qwen3-1.7b-isr-b03` 等待 GPU
- 成功 33 / 负向 31 / 失败 41 / 共 116

**已向 Director 汇报**（本轮初始化时），但汇报基于旧状态（gated-ISR 还在跑时的）。需要根据新状态再次汇报。

**Worker 池**：2 个 Worker 已派出但可能已完成（`ssh:check-gated-isr-progress` + `research:gated-isr-paper-narrative`），需要检查回调。

### 4. 📋 待办
- 检查 Worker 回调结果 → 整合发现
- `w2-qwen3-1.7b-isr-b03` 在 QUEUED → 双卡空闲 → 应立即提交（cuda:0 或 cuda:1）
- `gated-isr-warmstart-t015-s43` success → 需要分析其 metrics，理解 warmstart 策略为什么 work
- 向 Director 更新汇报：gated-ISR 方向已有 success（warmstart t015），1.7B β=0.3 待提交
- GPU 空闲 = 失职 → 立即填满双卡（1.7B β=0.3 + 其他 QUEUED 实验）

### 5. 🎯 战略上下文
- **核心方向**：ISR 作为 Goodhart's Law 案例研究，DDL 2026-05-25（剩 9 天）
- **D110**：H9 (ex falso quodlibet) 确认为第 9 种 hacking mode，1.7B 独有，纯加性证据
- **Gated-ISR warmstart 方向**：tau=0.15 的 warmstart 版本已 success，可能是 mitigation 方案。但 tau=0.2 版本 failed，tau=0.2 curriculum（非 warmstart）也 failed。说明门控阈值和初始化策略都很敏感。
- **下一个关键实验**：1.7B ISR β=0.3（验证更高 β 是否加剧 H9 hacking = dose-response at 1.7B scale）
- **易错点**：
  - gated-isr-warmstart 和 gated-isr-curriculum 是不同方案（warmstart = 从 exec-only checkpoint 继续训练 + 门控；curriculum = 从头训练 + 前 100 步 exec-only warmup）
  - `exec-retrain-for-warmstart-s42` 是 warmstart 的前置步骤（先训练 exec-only checkpoint），不是独立实验
  - report.md 被外部更新说明有其他 Loop 在并行处理，注意不要重复提交已完成的工作


---
