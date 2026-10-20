# reviewer / loop_16.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_16.md`
- **Structured JSON:** [`d7483c294adf81ce5c95.json`](../../sessions/d7/d7483c294adf81ce5c95.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: max_wall_time
updated: '2026-05-19T08:46:51+00:00'
---

### 1. 🔴 硬约束 / 红线
- westb-13313 只能用 cuda:0, cuda:1（2× RTX 5090 32GB）。westd-18266 的 gpu_ids 需查 project config 确认。
- llama-cross-model-full 的 registry status 被 Worker 错误改为 DONE（实际仍在运行），我已 warning 过但未确认是否恢复。读 registry 时不要信这个 status，要 SSH 看实际进程。
- Llama pilot 数据（llama-cross-model-v2）registry metrics 曾有严重错误（internal_death_rate=0.343 应为 0.586，det_death_rate=0 应为 0.243），M008 已修正论文但 registry metrics 未必更新。
- δ 值全文不一致：intro 写 0.266，experiments 写 0.265，discussion 写 26.6pp。精确值 = 65/245 = 0.26530...，需统一。
- Discussion 中 0.5B inverted-U 引用 `Appendix~\ref{app:cross-model}` 指向 Llama 附录，实际无 0.5B 数据。已 warning，待修。

### 2. 🖥️ 基础设施快照
- **westb-13313** (root): /root/autodl-tmp/simgate-modular-routing, 2× RTX 5090 32GB
  - D118 数据收集: tmux sessions `llama-full-gpu0` (PID 276421) + `llama-full-gpu1` (PID 276639)
  - 输出: results/llama_cross_model_full/{task_name}/episode_summary.jsonl
  - 模型: /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct
  - Cron 监控有 bug：脚本每 task 重启 vLLM 导致原始 PID 失效，反复 false alarm
- **westd-18266** (root): 4× RTX PRO 6000 96GB, 本轮未用
- 论文本地路径: projects/simgate-modular-routing/docs/paper/

### 3. 📊 当前状态
**刚完成**: D118 中期数据深度审查（5 维分析），尚未 post 报告。

**D118 进度** (截至 ~08:30 UTC):
- 完成 8/11 tasks (160 eps): chemistry-mix, find-animal, find-non-living-thing, freeze, identify-life-stages-2, inclined-plane, lifespan-longest, lifespan-l-then-s
- 进行中: grow-fruit (13/20), measure-melting-point (15/20)
- 未开始: 1 task（第 11 个，查 GPU0/GPU1 脚本确认是哪个）
- ETA: ~2-3h 完成全部

**待 post 的审查报告** (Director 触发的 5 问分析，已计算完毕):
1. N=20 足够做方向性判断，单 task Wilson CI ~±15-20pp
2. find-non-living-thing 零死亡是 systematic（Qwen 也零死亡，answer distribution 导致）
3. Per-task Llama vs Qwen Δ DR correlation: r=0.73 (p≈0.04) 但去掉 (0,0) 后 r=0.25 (p>0.5)——correlation 被 find-non-living-thing outlier 严重膨胀
4. C3 claim 可升级到 "cross-model replication" 但不能说 "model-independent"（仅 2 个同尺寸模型）
5. Llama Δ DR ~27pp ≈ Qwen ~27pp，pilot 的 +34.3pp 是小样本过高估计，全量数据反而 STRENGTHENS cross-model convergence 叙事

**其他 pending**:
- D114 decisions.yaml 仍含错误 "N=3 40.9%"（正确: 43.5%），已 flag 两次未修
- 叙事打磨验证已 post（δ 不一致 + 0.5B 断裂引用两个 warning）

### 4. 📋 待办
- **D118 全部完成** → 独立验证全部 11 tasks 数据，计算 aggregate metrics (DAF, label fraction)，与 Qwen 做 full comparison，post 最终审查报告
- **D118 数据整合到论文** → 审查 Paper Agent 更新的 app:cross-model 附录，核对数字，检查 pilot→full 的叙事过渡是否平滑
- **Pilot Δ DR 下调** → 论文 intro 和 app:cross-model 会从 "+34.3%" 改为实际全量值 (~+27pp)，需审查新措辞是否准确、是否与 "cross-model convergence" 叙事一致
- **0.5B + δ 修复** → 确认 Paper Agent 是否修了这两个 warning
- **find-animal 有 2 个 internal-preferred (det_died_int_alive)** → 这在 Llama 全量中是新发现（pilot 是 0 个 int-preferred），审查论文是否需要调整 "0 internal-preferred" 的措辞

### 5. 🎯 战略上下文
**核心结论**: Death dominance (DAF ~90%, 78.9% penalty-independent) 是 ScienceWorld 中 routing signal 的唯一来源。四种干预（retry/scaling/reflexion/filter）都无法消除。MATH 是 negative control (p=0.81)。

**最关键判断**:
- Per-task Llama-Qwen correlation (r=0.73) 看起来不错但被 (0,0) outlier 膨胀。去掉后 r=0.25。**不要在论文中 claim per-task magnitude correlation across models**——只能 claim direction consistency (8/8) 和 aggregate convergence (~27pp both)。
- Pilot 的 "+34.3% > Qwen +26.5%" 叙事需要反转：全量数据显示两者几乎相同 (~27pp)。这其实是更强的 finding（convergence > divergence for cross-model claim），但 Paper Agent 可能会保留旧叙事。
- Llama 全量出现 3 个 int-preferred labels（pilot 是 0），int-preferred rate 1.9%。论文 app:cross-model 当前写 "0 internal-preferred"——必须更新。
- Cron 监控持续误报，不要被 "failed" 吓到。SSH 看进程再判断。


---
