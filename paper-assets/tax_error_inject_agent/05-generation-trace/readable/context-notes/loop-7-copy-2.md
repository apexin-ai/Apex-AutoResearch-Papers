# reviewer / loop_7.md

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_7.md`
- **Structured JSON:** [`ea293673ffecbfe697eb.json`](../../sessions/ea/ea293673ffecbfe697eb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_wall_time
updated: '2026-05-16T10:22:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0/1/2/3 on autodl-5090，无越界历史
- LLaMA 模型是 3.1-8B（非 3.3），D042 明确指定，之前有 Worker 搞混被纠正
- Detection_rate 指标已证实为假阳性（关键词 "back" 匹配导航语言），**不可作为 paper contribution**——已向 Director 发 critical
- Scale-up 收集进程被误杀过一次（我的误判），恢复后正常。再次质疑前先确认排除 exclusion stubs
- TaxEI s0 训练需用 `TMPDIR=/root/autodl-tmp/tmp`，否则 /tmp 爆盘

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090 (root)，工作目录 `/root/autodl-tmp/tax_error_inject_agent`
- Python：`/root/miniconda3/bin/python`，conda base env
- 模型：`/root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct/` (LLaMA) + Qwen3-8B (已在 HF cache)
- 数据：`/root/autodl-tmp/tax_error_inject_agent/data/` (trajectories, SFT datasets)
- Eval 结果：`/root/autodl-tmp/tax_error_inject_agent/eval_results/`
- Checkpoints：`/root/autodl-tmp/tax_error_inject_agent/output/` + `checkpoints/`
- Scale-up 数据：`/root/autodl-tmp/tax_error_inject_agent/data/trajectories_scaleup_p1/`（239/1000 successes, 8 workers 收集中）
- 无 W&B（report_to=tensorboard）
- 活跃进程（截止 handoff）：
  - GPU 0: llama31-vanilla-s0 训练 (tmux, 92% done, ~5min)
  - GPU 1: llama31-taxei-s0 训练 (tmux, v1 重启, 1%, ~2h)
  - GPU 2: llama31-random-s0 训练 (tmux, 48%, ~65min)
  - GPU 3: eval-rp-s7 (tmux, 9/47 episodes)
  - CPU: scale-up collection PID ~249190 (8 workers)

### 3. 📊 当前状态
刚完成：
- LLaMA s42 三条件 eval 全部出结果：Vanilla=74.5%, TaxEI=74.5%, Random=76.6%（跨模型 negative result 不成立——TaxEI 在 LLaMA 上中性）
- Detection_rate 机制分析完成：100% 假阳性，已 critical 报告 Director
- v4-taxei-rp-s7 训练完成，eval 启动 (9/47)
- Recovery-TaxEI-s1 eval 完成：61.7%, detection=0%
- Recovery eval 进度：10/15（Vanilla 5/5, TaxEI 4/5, Random 1/5）

等待中：
- RP-s7 eval 完成 → 5-seed 完整数据（当前 4-seed: 47.9±7.8%）
- LLaMA Vanilla s0 训练即将完成 → 启动 eval
- Director 对 detection_rate critical 和跨模型叙事 warning 的决策

### 4. 📋 待办（条件触发式）
- RP-s7 eval 出结果 → 计算 5-seed TaxEI-RP 均值±SD，确认 Claim 7 最终结论
- LLaMA Vanilla s0 训练完成 → 确认 eval 是否立即启动（GPU 0 释放）
- LLaMA TaxEI/Random s0 训练完成 → eval 启动，看 s0 是否重现 s42 的"中性"结论
- LLaMA 3-seed 全部 eval 完成 → 审查跨模型统计是否足够支撑 paper claim
- Scale-up 收集达 1000 → 验证数据完整性，确认下一步（注入 pipeline）
- Director 回复 detection_rate 决策 → 确认 paper framing 调整方向

### 5. 🎯 战略上下文
- **核心结论**：TaxEI 在 Qwen3-8B 有害 (-9pp, 5-seed)，但在 LLaMA-3.1-8B 中性 (0pp, 1-seed)。跨模型"universal negative result"叙事不成立。
- **D043**：TaxEI-RP (recovery pairing) 有害，47.9±7.8%，Claim 7 答案 = No
- **D041**：Recovery ≈ Resilience（模型被动忽略错误，非主动恢复）
- **Detection_rate 是废指标**：LLaMA 的 21-30% 全是 "go back" 导航词假阳性；Qwen 的 0% 是 `enable_thinking=False` 导致无 think text。两边都不反映真实能力。
- **最易判断错的事**：看到 LLaMA detection_rate=21-30% 不要以为是真实发现——这是我之前犯的错误并已撤回。
- **Scale-up 成功率**：真实 ~78%（排除 exclusion stubs 后），不是表面的 22%——之前因统计口径错误导致误杀进程。
- **Paper target**：EMNLP 2026 Findings 8-page long paper，negative result framing


---
