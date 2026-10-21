# analysis check re lp server status

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_check_re_lp_server_status_20260515T154816_result.json`
- **Structured JSON:** [`a45421a2c5bdc6ab860b.json`](../../sessions/a4/a45421a2c5bdc6ab860b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### GPU 状态
4× RTX 5090 全部空闲（2 MiB / 0%），无实验在运行。

### tmux sessions
3 个活跃 session，但都是**其他实验**（exp_011_ood、exp_017_llama），与目标实验无关。

---

### 实验 1: exp_re_scierc_seed123 — SciERC RE joint N=8 T=1.0 seed=123
- **状态**: ✅ 已完成
- **产出路径**: `/root/autodl-tmp/struct_self_consist_ie/output/exp_re_scierc_seed123/`
- **文件**: `report.json` (3.3KB) + `samples.jsonl` (3.8MB)，时间 May 15 23:45
- **关键指标**:
  - NER: greedy F1=0.663, oracle F1=0.786, headroom=12.3pp, ρ_sj=0.404 (cond), ρ_fk=0.182 (cond)
  - RE: greedy F1=0.420, oracle F1=0.593, headroom=17.3pp, ρ_sj=0.277 (cond), ρ_fk=0.063 (cond)
  - **Verdict: FAIL** — RE ρ_sj(cond)=0.277 < 0.40 阈值
  - ⚠️ RE 43.6% samples F1=0

### 实验 2: exp_re_scierc_seed456 — SciERC RE joint N=8 T=1.0 seed=456
- **状态**: ✅ 已完成
- **产出路径**: `/root/autodl-tmp/struct_self_consist_ie/output/exp_re_scierc_seed456/`
- **文件**: `report.json` (3.4KB) + `samples.jsonl` (3.8MB)，时间 May 15 23:45
- **关键指标**:
  - NER: greedy F1=0.664, oracle F1=0.775, headroom=11.1pp, ρ_sj=0.283 (cond), ρ_fk=0.145 (cond)
  - RE: greedy F1=0.417, oracle F1=0.581, headroom=16.3pp, ρ_sj=0.315 (cond), ρ_fk=0.123 (cond)
  - **Verdict: FAIL** — RE ρ_sj(cond)=0.315 < 0.40 阈值
  - ⚠️ RE 45.3% samples F1=0

### 实验 3: exp_lp_scierc_t07 — Qwen SciERC N=8 T=0.7 LP 推理
- **状态**: ✅ 已完成
- **产出路径**: `/root/autodl-tmp/struct_self_consist_ie/output/exp_lp_scierc_t07/`
- **文件**: `report.json` (1.7KB) + `samples.jsonl` (3.9MB)，时间 May 15 23:40
- **关键指标** (NER only, subtask=ner):
  - greedy F1=0.662, oracle F1=0.764, headroom=10.2pp
  - ρ_sj=0.363 (cond), ρ_fk=0.255 (cond), rho_advantage=0.076
  - logprob baseline: ρ=0.185 (cond) — structural signal (0.363) 大幅优于 logprob (0.185)
  - **Verdict: MARGINAL**
  - T=0.7 下 zero-F1 比例降至 11.0%（vs T=1.0 的 ~12.6%）

---

### 小结
三个实验均已完成并有完整产出。RE joint 两个 seed 都 FAIL（conditional ρ_sj 不达标），LP T=0.7 NER-only 为 MARGINAL。`analysis_round8/` 目录下有额外分析文件（seed456_lp_range.json、epsilon_sweep 等），时间戳也是今天。

---
