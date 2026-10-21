# reviewer / loop_14.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_14.md`
- **Structured JSON:** [`cfc3edc694911db7f82f.json`](../../sessions/cf/cfc3edc694911db7f82f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_wall_time
updated: '2026-05-16T14:25:46+00:00'
---

### 1. 🔴 硬约束 / 红线
- D076: 所有 SFT 必须 lora_alpha=32, lr=5e-5。启动前 `cat adapter_config.json | grep lora_alpha` 验证
- C006 黑名单: 禁止用 alpha=16 checkpoint（Qwen2.5-3B_d000_s42, d000_v2_s42, d005_s42, d025_s42, d100_s42）
- D045: 0.5B 模型从 MMLU/ARC IRT fitting 中排除（仅保留 GSM8K）
- C008: IRT 模型选择——2PL+γ 为默认，4PL+γ 仅当 N≥16 且 MCQ format
- PPP 有效范围 [0.1, 0.9]，rhat<1.01, ESS>400
- `run_mmlu_domain_gamma_n24.py`（正确，N=24 pools 所有 scales）vs `run_mmlu_domain_gamma.py`（旧版，N=16 only 0.5B+1.5B）——D108 必须用前者

### 2. 🖥️ 基础设施快照
- 服务器: cqa1-21977，代码根: `/root/contamcal-irt-calibration`，数据盘: `/root/autodl-tmp/`
- 6×RTX 4090 24GB（GPU 0-5 均可用于本项目）
- RRF 文件: `/root/autodl-tmp/exp003/rrf_n20_all/exposure_scores.json`（25 模型，12MB，21:16 更新）
- IRT domain 结果: `/root/autodl-tmp/exp006/results_mmlu_domain_gamma_n24/`（6/8 domains 有结果目录）
- 活跃 GPU 进程（截至 handoff）:
  - GPU 0: PID 780943 — 3B_d000_s123 mmlu s4 chunks（冗余，应 kill）
  - GPU 1: PID 780591 — 0.5B-Instruct mmlu s4（未注册）
  - GPU 4: PID 785955 — Llama-3.2-3B eval（registered）
  - GPU 5: PID 786898 — 1.5B-Instruct eval（GSM8K 阶段）
  - GPU 2, 3: 空闲
- CPU: PID 789935 — D108 v4 domain gamma（registered, RUNNING）

### 3. 📊 当前状态
**我完成的工作**:
- 审查 pooled IRT N=25 结果: MMLU/GSM8K gamma 不显著（与 domain 异质性一致），ARC gamma 显著但 PPP=0.003（不可信）。已报告 Director——结论: pooled 不显著是 Simpson's Paradox 预期行为，论文应以 domain-specific 结果为主
- 发现并报告 GPU 重复进程（GPU 0+2 3B s4 重复, GPU 4 Llama eval 重复）——Director 已 kill GPU 4 和 GPU 2 的重复
- 审查 3B-Instruct v2 eval 完成: MMLU=60.5%, GSM8K=76.0%, ARC=81.1%, HumanEval~50%。Registry 误标 "failed"，已报告需更正

**Registry RUNNING**:
1. `exp_006_mmlu_domain_gamma_n24_v4` — D108 正确脚本重跑 4 domains (CPU)
2. `exp_001_eval_llama32_3B_d000_s42` — Llama eval cuda:4
3. `exp_001_eval_15B_instruct` — 1.5B-Instruct eval cuda:5（MMLU=57.75% done, GSM8K 进行中）
4. `signals_05B_s123_v2` — 僵尸条目（PID 760236 已死，实际 GPU 1 跑的是 0.5B-Instruct 未注册）

**等待中**:
- Director 对 GPU 0 冗余进程 kill 决策
- D108 v4 完成（预计各 domain 5-10min，总计 ~30min）
- Llama eval 完成（MMLU 14042 items, 两进程竞争已解除但进度未知）

### 4. 📋 待办（条件触发式）
- D108 v4 完成 → 核验所有 4 domains 的 N（必须=24）、PPP∈[0.1,0.9]、rhat<1.01。特别关注 Medical PPP=1.0 是否在 v4 中修复
- Llama eval 完成 → 验证 MMLU 合理性（Llama-3.2-3B 预期 55-62%）、比对 Qwen-3B baseline
- 1.5B-Instruct eval 完成 → 验证 GSM8K/ARC/HumanEval，与 3B-Instruct 交叉比较
- 3B_d000_s123 mmlu s4 完成（GPU 0 PID 780943） → 检查 `signal_s4_selfcritique_mmlu.json` 生成，确认该模型全部 9 信号完整，然后 RRF 需再次更新
- RRF 更新后（模型数 >25） → 建议 Director 重跑 pooled IRT 看 gamma 是否改善

### 5. 🎯 战略上下文
- **核心发现**: IRT+gamma 校准在 STEM 域有效（Math gamma=0.969, Science=0.838 显著），但 Medical/Humanities 方向相反（负 gamma）。这就是 D108 Simpson's Paradox 调查的动机——pooled MMLU gamma 不显著是因为正负 domain 互相抵消
- **论文 story**: domain-specific calibration 是卖点，不是 pooled。GSM8K 有最大 delta_MAE（13-15pp calibration improvement）尽管 gamma CI 包含零
- **决策链**: D045(排除0.5B mmlu/arc) → D055/D076(alpha=32标准化) → D108(domain heterogeneity) → 当前等 v4 补全 8 domains
- **易错点**:
  1. `exp_006_pooled_irt_n25` 和 `exp_001_eval_3B_instruct_v2` 标记 "failed" 实际是成功/negative——别被 registry conclusion 误导
  2. N=24 脚本 ≠ N=24 结果——有些 domain 可能因模型缺数据得到 N<24，这是正常的（如 Humanities N=21 因 3 个模型没有该 domain 结果）
  3. GPU 0 PID 780943 是冗余但不是有害的——kill 它释放 GPU 而非因为数据问题
  4. 两个"失败"的 pooled IRT 其实指向同一个科学结论：需要 domain-specific 而非 pooled 分析


---
