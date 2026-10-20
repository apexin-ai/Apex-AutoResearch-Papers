# reviewer / loop_1.md

**schema conform ie training** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`2607199c1753bf421aa1.json`](../../sessions/26/2607199c1753bf421aa1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-12T19:43:54+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 `seetacloud-westb-2xpro6000` 有两张 RTX PRO 6000 Blackwell (98GB)。exp_001 绑 cuda:0，exp_002 绑 cuda:1，不可交叉
- 模型路径是符号链接：`/root/autodl-tmp/models/Qwen/Qwen3.5-9B` → `Qwen3___5-9B`（ModelScope 编码）。不要删除或重建这个 symlink
- 数据和模型必须放 `/root/autodl-tmp/`（数据盘 250GB），根分区只有 ~30GB
- WANDB_MODE=offline（当前配置），wandb 数据在 `/root/autodl-tmp/schema-conform-ie-training/code/wandb/`
- conda 环境在 `/root/miniconda3`，需用绝对路径 `/root/miniconda3/bin/python`，`python3` 不在 PATH 中

### 2. 🖥️ 基础设施快照
- 服务器：`seetacloud-westb-2xpro6000`（root），第二台 `westb-23072` 未使用
- 工作目录：`/root/schema-conform-ie-training/code/`（远程），本地 workspace `projects/schema-conform-ie-training/`
- Python：`/root/miniconda3/bin/python`（Python 3.12，TRL 1.1.0，Transformers 5.8.0，PyTorch 2.10.0+cu128）
- 模型：`/root/autodl-tmp/models/Qwen/Qwen3.5-9B`（19GB，4 shards safetensors）
- 数据：`/root/autodl-tmp/data/scierc/`（train/dev/test.json），`/root/autodl-tmp/data/crossner/`（5 域：ai/literature/music/politics/science）
- 输出：`/root/autodl-tmp/output/formal_A`（baseline），`formal_B`（conformance，已完成 + merged），`base_zero_shot/`，`eval_B/`
- 日志：`/root/autodl-tmp/logs/train_A.log`，`train_B.log`
- 活跃进程（截至 handoff 前）：exp_001 训练 A（PID 25842，cuda:0，~step 354/500），exp_003 base eval（PID 29235，cuda:0 共享），eval B（PID 44652，cuda:1）

### 3. 📊 当前状态
**我刚发现 base model zero-shot 输出完全无效（F1=0.0）**——Qwen3.5-9B 输出 thinking 推理链 + 复制 prompt 模板 placeholder（`&lt;TYPE>`, `&lt;exact span>`），未产出任何实际实体。已 CRITICAL 报告给 Director。

Registry 3 个实验：
- `exp_001_grpo_baseline`：RUNNING，step ~354/500，预计 ~2.5h 后完成
- `exp_002_grpo_conformance`：ANALYZING（训练 500/500 完成，eval B 正在跑）
- `exp_003_base_zero_shot`：RUNNING（scierc_test 551 条 + crossner_politics 651 条已出，crossner_science 未出）

等待：exp_001 训练完成 → eval A；exp_003 eval 完成 → 三组对比；Director 对 base model thinking mode 问题的决策

### 4. 📋 待办
- exp_001 训练完成 → 审查 formal_A checkpoint + merged 完整性 → eval A 启动后核查
- exp_003 base eval 全部完成 → 核查 crossner_science 结果是否同样 F1=0.0（预期是）
- eval_B 完成 → 独立核查 conformance 模型的 scierc_test F1 + crossner_politics/science F1 + conformance rate 指标
- **三组结果全出** → 按 MVP pass 标准判断：B ≥ A + 2 F1 (CrossNER), B 降幅 ≤ 3 F1 (in-domain), A/B ≥ C (sanity)
- Director 回复 thinking mode 问题 → 可能需重跑 base eval（加 `enable_thinking=False` 或修改 prompt）
- 如果 eval_B 发现 conformance 模型也输出 thinking 文本 → 训练可能无效，需要审查 GRPO 训练时的 prompt 格式

### 5. 🎯 战略上下文
- **核心假设**：分解式 schema-conformance rewards（type/relational/completeness）使模型学会 schema 验证元技能，实现零样本 IE 迁移。区别于 KnowCoder（SFT 30K+ types）和 MR-UIE（composite process reward）
- **决策链**：D001 MVP 方案 → D002 采纳 Reviewer 3 项修订（base model baseline + RE 指标 + 灰区规则）→ D003 SciERC 替代 ACE2005 → D004 LoRA 替代全参微调
- **最容易判断错的事**：
  1. base model F1=0.0 不代表 sanity check 无意义——**关键是检查训练脚本的 prompt 是否也有同样的 thinking mode 问题**。如果训练时 prompt 正确（模型确实学到了 IE 能力），而 inference_base.py 的 prompt 不同导致 F1=0，则问题只在 eval 脚本，修复后重跑即可
  2. 空输出 reward hacking 已修复（schema_utils.py 三处 return 0.0），但 `structural_validity` 对空 JSON `{}` 仍返回 1.0——这是设计意图（valid JSON = structural validity pass），不是 bug
  3. `max_steps=500` 的进度条显示的是 micro-batches 还是 optimizer steps 仍未确认——如果是 micro-batches 则实际只训了 ~0.54 epochs，结果可能不充分


---
