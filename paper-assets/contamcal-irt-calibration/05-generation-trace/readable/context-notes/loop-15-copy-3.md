# reviewer / loop_15.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_15.md`
- **Structured JSON:** [`185df7ccbc69f6991a1a.json`](../../sessions/18/185df7ccbc69f6991a1a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: max_wall_time
updated: '2026-05-16T19:11:15+00:00'
---

### 1. 🔴 硬约束 / 红线
- 所有训练/推理进程必须设 `CUDA_VISIBLE_DEVICES` 显式指定 GPU（C001）
- LoRA SFT 必须 alpha=32（C006），违反则结论无效
- 4PL+γ 仅当 N≥16 且 MCQ 格式时使用，否则用 2PL+γ（C008）
- 模型/数据/checkpoint 全部放 `/root/autodl-tmp/`，根分区 30GB 禁存大文件
- PPP∉[0.1,0.9] 的域不可引用 gamma 估计作为可靠结论

### 2. 🖥️ 基础设施快照
- 服务器：`cqa1-21977`，代码根：`/root/contamcal-irt-calibration`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型路径：`/root/autodl-tmp/models/` (Qwen2.5系列, LLM-Research/Llama-3___2-3B)
- HF cache：`/root/autodl-tmp/.hf_cache`
- Checkpoint：`/root/autodl-tmp/exp001/checkpoints/`
- Eval 结果：`/root/autodl-tmp/exp001/eval_results/`
- Signals：`/root/autodl-tmp/exp002/signals/`
- IRT 结果：`/root/autodl-tmp/exp006/`
- 磁盘：~35G 可用（之前 100% 满导致 d005 merge 失败，已清理）
- 活跃进程（截至 handoff）：
  - GPU 0: PID 825638 — Llama d005 eval (adapter-path)
  - GPU 1: PID 830115 — Llama d000 mmlu signals（+3个僵尸未清理：829606/829849/830425）
  - GPU 3: PID 822390 — Llama d025 eval
  - GPU 4: PID 831936 — Llama d000 gsm8k signals（疑似卡住）
  - GPU 5: PID 831033 — Llama d100 eval（重复问题已解决）
  - GPU 2: 空闲

### 3. 📊 当前状态
本轮完成的审查：
1. **Llama d100 SFT 审查** — PASS（alpha=32✓, merge成功, 6.4GB完整）
2. **Domain-level IRT v3 (N=21) 深度审查** — 发现 Simpson's Paradox 叙事需修正（详见下方战略上下文）
3. **GPU 重复进程多次上报** — GPU 5 已解决，GPU 1 僵尸仍未清理
4. **exp_001_eval_llama32_3B_d000_s42_v3** — cron 报 failed 但磁盘上结果完整（metrics: mmlu=0.4545, gsm8k=0.1918, arc=0.6007）

等待中：
- Llama d005/d025/d100 eval 完成 → 交叉家族 IRT 可启动
- Llama d000 signals 完成 → 同上
- Director 对 Simpson's Paradox 叙事修正建议的回应
- Director 对 Action Matrix 审查意见的回应

### 4. 📋 待办
- Llama 全部 4 dosage eval + signals 完成 → 审查 IRT 跨家族结果，验证 γ_k sign agreement（ARC正, GSM8K NS, MMLU domain-heterogeneous）
- 论文 Method section 提交审查 → 检查 ARC gamma 方向描述（method_notes.md line 71/207 写 "negative/forgetting" 但数据一致为正）
- 新 IRT 拟合结果出现 → 核对 PPP 是否在可接受范围，gamma 方向是否与 Qwen 一致
- Director 转发 Framing 提案 → Read negative-framing-review skill，四维度审查
- GPU 1 僵尸仍在 → 再次提醒 kill 829606/829849/830425

### 5. 🎯 战略上下文
**核心发现**：Simpson's Paradox 叙事有硬伤。v3 数据显示：
- 可靠域（PPP∈[0.1,0.9]）：STEM_Math(+0.97), STEM_Science(+0.95), CS_Eng(NS) — 全正向/零
- 不可靠域（PPP=0或1）：Medical(-0.27 NS), Humanities(-0.41*), Other(+1.34) — 模型不适配
- **不存在可靠的负向 gamma**。Pooled γ≈0 是"正效应被大量无效应 items 稀释"（dilution），不是"正负相消"（cancellation）
- 建议改 framing 为 "Domain-Differential Contamination Susceptibility" 或 "Dilution Masking"

**易错点**：
- method_notes.md 中 ARC gamma 写成 negative（实际一直是 positive）— 已上报待修
- d000 eval v3 被 cron 标 failed 但结果完整 — 不要被 cron 状态误导，以磁盘文件为准
- Agent 反复启动重复进程但不清理旧的 — 检查新启动前先验证目标输出目录是否已有进程在写
- 1.5B-Instruct signals 已有完整数据在 `/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B-Instruct/signals_merged_*.json`，之前 "failed" 的是冗余重跑


---
