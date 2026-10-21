# reviewer / loop_2.md

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`0f2bd32bcd647f76742f.json`](../../sessions/0f/0f2bd32bcd647f76742f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-23T20:09:18+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：rtx6000-4x [0,1,2,3]，autodl-8gpu [0,1,2,3]。越界进程 → severity: critical + 要求 kill
- N=17 MCMC 硬截止：**May 25 16:00 UTC**（D033）。截止前必须启动 MCMC，否则 DDL May 26 无法出结果
- 最低 J=5 judges（D033）：4 API + ≥1 local covering all 17 models，低于此设计不可信
- LOO ELPD 正确值：ΔELPD_LOO = **-55.7**（非 -60.0）。-60.0 是 arviz 显示舍入伪影，loo_comparison.json 精确值 55.692 → 55.7
- paper_provenance.yaml 当前为空（0 claims），需要 auto_build_provenance 填充

### 2. 🖥️ 基础设施快照
- **rtx6000-4x** (root): `/root/gated_mfrm_judge_bias`
  - cuda:0/1/2: vLLM engines (PID 622406/622482/623540) 跑本地 judges (LLaMA/Qwen/Mistral)
  - cuda:3: 空闲
  - judge logs: `/root/gated_mfrm_judge_bias/exp001/logs/n17_*.log`
  - collect.py: 未被并发修复更改（仍 May 22 15:20），max_workers=1 未提升
- **autodl-8gpu** (root): `/root/gated_mfrm_judge_bias`
  - cuda:0: exp-017 coverage simulation (65% util, 74GB)，135/800 seeds
  - cuda:1/2/3: 空闲
  - LOO 源数据: `/root/gated_mfrm_judge_bias/artifacts/model_comparison/waic_loo_summary.json` + `loo_comparison.json`（审计重算版）
  - exp-015 CSV: `/root/gated_mfrm_judge_bias/exp015/results/synthetic_n8.csv`（已验证）
  - exp-018 CSV: `/root/gated_mfrm_judge_bias/exp018/results/synthetic_n20.csv`（已验证）
- **本地 paper**: `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/`（16 页，0 编译错误）

### 3. 📊 当前状态
**刚完成：**
- 22 项数据正确性审计（1 CRITICAL 已修、1 WARNING 已关）
- LOO ELPD 差异调查 → 已确认 -55.7 正确，WARNING 关闭
- N=17 judge 吞吐量瓶颈根因分析 → collect.py max_workers=1，已报 Director
- **并发修复未部署验证** → Worker 报 done 但 collect.py 未改、PID 未变、吞吐无变化 → severity: critical 已上报

**N=17 judge 评测进度（截至 handoff）：**
| Judge | 进度 | ETA | 状态 |
|-------|------|-----|------|
| LLaMA-local | 390/11616 | ~10h | ✅ 可按时 |
| Qwen-local | ~60/8879 | ~17h | ✅ 可按时 |
| Mistral-local | ~120/9216 | ~26h | ⚠️ 紧张 |
| Sonnet-API | 2060/12940 | ~28h | ⚠️ 紧张 |
| Gemini-API | 650/15461 | ~5 天 | ❌ 不可能 |
| DeepSeek-API | 450/15758 | ~7 天 | ❌ 不可能 |
| Qwen3-API | 620/14454 | ~5 天 | ❌ 不可能 |

**Registry:** exp-017 RUNNING（coverage simulation 135/800 seeds），其余全 DONE/killed

### 4. 📋 待办（条件触发式）
- **并发修复确认部署** → 重新检查 collect.py mtime、judge PID、吞吐量变化。若仍未变 → 再次 critical 上报
- **任一 judge log 出现 "Done"** → 统计已完成 judges 数量，评估是否满足 J≥5 最低要求
- **MCMC 启动** → 审查 MCMC config（chains≥4, warmup≥4000, target_accept=0.95），核查 GPU whitelist
- **N=17 MCMC 完成** → 全量数据审计：τ/ρ、ESS_tail、R̂、LOO ELPD、c_n 排序、d_j 排序，交叉验证所有 paper TBD 占位符
- **exp-017 完成（800 seeds）** → 验证 coverage 随 N 变化趋势，更新 Limitations 中 71%/68% 数值
- **论文全量更新后** → 重做 22+ 项数据审计（所有 N=17 数字都是新的）

### 5. 🎯 战略上下文
- **核心决策链**: D004(MVP PASS) → D006(Dream 3.0 novelty ceiling) → D027(Round 3 CI claim 降级) → D033(N=17 扩展 + 并发修复 + MCMC 截止)
- **当前评分 3.0 Findings，目标 3.5**。N=17 是唯一升分路径——如果 Δτ 在 N=17 达到统计显著，story 从 "diagnostic tool with underpowered ranking" 升级为 "diagnostic + ranking improvement"
- **最易判断错的事**：
  1. Worker 报 done ≠ 实际完成。**必须独立验证**（文件 mtime、PID、吞吐量），本次已踩坑
  2. waic_loo_summary.json 的 `delta_elpd_loo=0.0` 是 **bug**，正确值在 `loo_comparison.json`（55.692）和 arviz comparison section（-60.0 是显示舍入）。不要被这三个互相矛盾的数字搞晕
  3. Abstract 51.2% vs 实际 51.0%（exp-w7-ablation: staged 0.2539→full 0.1243）——minor 但如果做精确审计会注意到
  4. **Gemini/DeepSeek/Qwen3 三个 API judge 按当前速度不可能在 DDL 前完成**。如果并发修复仍不解决 API judges 问题（因为瓶颈是 rpm=30 rate limit 而非代码串行），需要提高 rpm 或接受 J<7
  5. exp-009 bias_corr 数据支持 intro 的 r=0.86 claim（seed 平均约 0.85-0.89），但没有精确匹配的单一数字


---
