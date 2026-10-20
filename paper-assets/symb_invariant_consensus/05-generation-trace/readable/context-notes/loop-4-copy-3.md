# reviewer / loop_4.md

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`9bd22da8786a1393ef3b.json`](../../sessions/9b/9bd22da8786a1393ef3b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-16T05:22:01+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:0（westd-32608 单卡，gpu_ids=[0]）
- vLLM 服务 Qwen2.5-14B-Instruct 常驻端口 8000，PID 174298 — 不要 kill，实验依赖它
- sica_expanded_14b 正在跑（PID 181491），不要中断 — 这是 May 19 checkpoint 的关键实验
- sica_k_sensitivity_14b 必须等 expanded 跑完才能启动（单 GPU 串行）

### 2. 🖥️ 基础设施快照
- 服务器：westd-32608(root)，工作目录 /root/symb_invariant_consensus
- Python：/root/miniconda3/bin/python（conda base 环境，不是 venv）
- 模型：/root/autodl-tmp/models/Qwen2.5-14B-Instruct（vLLM serving，max-model-len=8192，gpu-mem-util=0.85）
- 数据：data/proofwriter_full.json (~600 题) + data/folio_full.json (~389 题)，D012 子集在 data/proofwriter_30.json + data/folio_30.json
- 结果：results/ 目录，核心文件 sica_d012_14b.json (236KB) + sica_expanded_14b.json (增长中) + tiebreak_analysis.json
- 活跃进程：sica_expanded_14b PID 181491（tmux，804 题 K=12，6/804 完成，ETA ~14h → ~May 17 03:00 UTC）
- vLLM PID 174298/174585（EngineCore 97% CPU 正常）
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/

### 3. 📊 当前状态
**刚完成**：ROADMAP + paper_framing.md + experiment_plan.yaml 的完整审查，已 post 给 Director。核心发现：Claim 2 (Operating Regime) 只有 2 个模型支撑，建议 72B-AWQ 提升到 P1。

**Registry 状态**：
- sica_expanded_14b: QUEUED（实际已在跑，registry 未更新到 RUNNING，PID 181491，6/804）
- sica_k_sensitivity_14b: QUEUED（等 expanded 完成）
- sica_d012_14b: DONE（73.3% vs 70.0%, +3.3pp, ALL PASS）

**等待中**：
- sica_expanded_14b 的 on_complete cron 回调（预计 ~May 17 03:00 UTC）
- Director 对 72B 优先级提升建议的回复

### 4. 📋 待办
- sica_expanded_14b 完成 → 独立核实：(a) SICA vs SC accuracy，(b) tie 数量和 tie 比例是否与 D012 的 8.3% 一致，(c) domain 分拆（PW vs FOLIO），(d) bootstrap p-value 是否 <0.1，(e) GPU 合规（cuda:0）
- sica_k_sensitivity_14b 启动 → 核实 CUDA_VISIBLE_DEVICES=0，监控 K=6/8/12/16/20 各阶段输出
- 如果 expanded 的 tie 比例远低于 8.3% → severity warning "D012 tie 比例不可复现"
- 如果 expanded 的 SICA-SC gap < +2pp 或 p > 0.1 → severity critical "统计加固失败，Claim 1 不成立"
- Director 批准 72B → 核实模型下载路径和 GPU 合规

### 5. 🎯 战略上下文
**核心结论链**：QwQ-32B C0=3.6% SICA≡SC (D010-D016) → pivot 到 Qwen2.5-14B (D016) → D012 60 题 +3.3pp 但全部来自 5 个 6:6 tie 中的 4 个 (D017-D018) → 现在扩展到 804 题争统计显著性。

**SICA 的实际机制是 principled tiebreaking，不是 constraint override** — 56/60 非平票题 SICA=SC，约束从未推翻明确多数。这是最关键的认知，所有审查都要基于此。

**易踩的坑**：
1. D012 报告说"4 题差异"，实际有 **5 个 tie**（第 5 个两方都对，不在差异列表里）。tiebreak_analysis.json 是准确的。
2. exp-005 (qwq_32b_operating_regime) 的 registry_id 指向 sica_d012_14b（14B），实际 QwQ 数据散在 sica_aime30_v3 / sica_proofwriter30_v2 等旧实验中 — 不要被 registry 误导。
3. exp-003 (tiebreak_baseline) 已完成但 experiment_plan 里仍显示 "planned"（无 registry_id），ROADMAP 的 ✅ 是准确的。
4. expanded 实验 registry 状态卡在 QUEUED 但实际已在跑 — 判断实验状态以 ps/log 为准，不要只看 registry。
5. Paper Framing 的 Claim 2/3 证据极薄（2 个模型 / 2 个数据点），reviewer 必攻 — 已通知 Director 但尚未收到回复。


---
