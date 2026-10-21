# reviewer / loop_6.md

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_6.md`
- **Structured JSON:** [`b9b767ee072dc9785e90.json`](../../sessions/b9/b9b767ee072dc9785e90.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_wall_time
updated: '2026-05-17T08:00:04+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **cuda:0**（westd-32608 单卡机，RTX PRO 6000 Blackwell 98GB）
- submit_training_job 的 command 不能包含 `pkill` 和实验脚本在同一个 compound command 中（v2 教训：pkill 匹配 parent shell cmdline 导致 SIGTERM 自杀）。pkill 必须在脚本内部执行。
- vLLM 独占 GPU：同一时间只能有一个 vLLM 实例运行。exp-010-mistral 脚本内的 `pkill -9 -f "vllm.entrypoints"` 会杀死任何现有 vLLM，不能与其他实验并行。

### 2. 🖥️ 基础设施快照
- 服务器：**westd-32608(root)**，工作目录 `/root/symb_invariant_consensus`
- Python：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`（`python` 或 `python3` 均可，但裸 `python` 在非 conda 环境下 not found）
- 模型路径：
  - Qwen2.5-14B: `/root/autodl-tmp/models/Qwen2___5-14B-Instruct`
  - LLaMA-3.1-8B: `/root/autodl-tmp/models/Llama-3.1-8B-Instruct/LLM-Research/Meta-Llama-3___1-8B-Instruct`（shard 2 已修复 May 17）
  - Mistral-7B: `/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3`（4 shards 完整 ~14.5GB）
- 数据：`/root/symb_invariant_consensus/data/`（proofwriter_30.json, folio_30.json, arc_challenge_60.json）
- 活跃进程：exp-010-mistral-v3 (PID 298717/vLLM PID 298742, port 8000, tmux)

### 3. 📊 当前状态
**刚完成审查**：
- exp-018-arc-v2 DONE (success): SICA 95% vs SC 96.67% = -1.67pp，ARC 域 capability trap confirmed
- exp-011-llama8b-v3 DONE/ANALYZING: **SICA 66.7% vs SC 60.0% = +6.7pp** — 最重要数据点，MaxSAT 首次大规模激活（43/60 contradictions），但统计显著性未确认（net 4 discordant pairs）

**正在运行**：
- exp-010-mistral-v3 RUNNING: Mistral-7B 跨模型家族验证，问题 3/60 进行中，ETA ~18min（~08:16 UTC 完成）

**等待**：
- exp-011-llama8b-v3 registry 更新为 DONE（analysis worker 完成但 status 仍 ANALYZING）
- pilot-contrastive-prompt-v2 修复后重提交（环境问题：需 conda activation）
- Director 对 D030 vs D025 方向的最终决策

### 4. 📋 待办
- exp-010-mistral-v3 cron on_complete → 审查结果（关注：是否像 Qwen-14B 高一致性还是像 LLaMA-8B 有多样性）
- exp-011-llama8b-v3 metrics 入 registry → 核对 McNemar p 值（如 Agent 未报 p 值 → warning 要求补充）
- pilot-contrastive-prompt-v2 重提交 → 审查 discriminative ratio（baseline=11.5%，目标>70%）
- 如果 Mistral-7B 结果也显示 SICA>SC → D025 paper story 需从"everywhere vacuous"调整为"capability-dependent operating regime"

### 5. 🎯 战略上下文
**项目核心**：D025 Analysis Paper — "Capability Trap: why symbolic consensus ≈ voting"。ARR May 25 deadline。

**决策链关键**：D025（Analysis Paper pivot）→ D030（Methods Paper pivot, 用户指示）→ pilot 负面结果（filtering vacuous）→ 方向未定。paper_framing.md 仍停在 D025。

**最容易判断错的事**：
1. **exp-011-llama8b-v3 的 +6.7pp 不等于"SICA works"**。与 D012 的 +3.33pp（后在 n=804 消失）相同风险。n=60 的 ±6pp 在 SE≈6pp 范围内。必须看 McNemar p 值，不能被绝对值迷惑。
2. **D030 contrastive pilot 的 V1/V2 scoring 本质是 weighted majority vote**（绕过了 MaxSAT），可能测出的"improvement"只是信息量等价于 SC 的重新包装。审查时要问：去掉 polarity 标签后是否退化为 trace 计数。
3. **优先级**：D025 跨域/跨模型实验（exp-010/011/017/018）是论文主线数据。D030 探索性 pilot 不应抢占 GPU 时间。


---
