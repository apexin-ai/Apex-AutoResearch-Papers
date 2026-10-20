# agent / loop_1.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`4ed3d1c688c7a3e91223.json`](../../sessions/4e/4ed3d1c688c7a3e91223.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: idle_timeout
updated: '2026-05-13T22:40:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0-5（全部 6 张 4090D），服务器 cqa1-21977，无其他服务器
- `train_sft.py --gpu N` = **物理 GPU N**，脚本内部覆盖 `CUDA_VISIBLE_DEVICES=N`，不走框架映射。`--gpu 0` ≠ "分配到的第一块卡"
- **Phase 3 contaminated SFT 启动前置条件**：必须验证 `paraphrases/mmlu_paraphrases.json` 存在且非空 → 重跑 `prepare_sft_data.py` → 确认 MMLU+GSM8K+ARC 三个 benchmark 齐全 → 才可启动。绝不可在 MMLU 缺失时启动 Phase 3
- exp_005/exp_004 运行在 local CPU（无 SSH 服务器），cron SSH 检查会 false positive（已发生两次 rollback），需用本地 `ps -p PID` 验证存活
- vLLM 多实例不可并发启动（duplicate template bug），需串行

### 2. 🖥️ 基础设施快照
- **服务器**：cqa1-21977，6× RTX 4090D，工作目录 `/root/contamcal-irt-calibration`
- **Python**：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）。激活方式：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型缓存**：`/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-{0.5B,1.5B,3B}`（已下载）；`HF_HOME=/root/autodl-tmp/.hf_cache`
- **数据**：`/root/autodl-tmp/exp001/sft_data/sft_dosage_*.jsonl`（0% 已生成，5-100% 仅含 ARC+GSM8K 缺 MMLU）
- **Checkpoints**：`/root/autodl-tmp/exp001/checkpoints/{model}_{dosage}_{seed}/`
- **Eval 代码**：`/root/contamcal-irt-calibration/exp001/evaluate.py`
- **Paraphrase 输出**：`/root/contamcal-irt-calibration/exp001/paraphrases/{arc,gsm8k}_paraphrases.json`（✅），`mmlu_paraphrases.json`（⏳ 生成中）
- **Stan 模型**：`artifacts/exp005_noise_propagation/` 下 `.stan` 文件（已修复 sigma_e/c/d/treedepth）
- **活跃 GPU 进程**：
  - cuda:0 — MMLU paraphrase vLLM (PID 204467, exp_001_sft_injection)
  - cuda:1 — 已释放（0.5B-s123 已完成）
  - cuda:2 — 已释放（1.5B-s123 已完成）
  - cuda:3 — 3B-s123 训练 (PID 216935, exp_001_sft_0pct_3B_s123)
  - cuda:4 — 1.5B-s42 eval (PID 221376, exp_001_eval_15B_d000_s42)
  - cuda:5 — 3B-s42 训练 (PID 210666/210671, exp_001_sft_0pct_3B)
- **活跃 CPU 进程**：
  - exp_004_sim_sweep (PID 219346, ~28h total, 120 Stan fits)
  - exp_005_noise_prop_v2 (PID 251971, 50 Stan fits)
- **活跃 Cron**：exp_001_sft_injection / exp_001_sft_0pct_3B / exp_001_sft_0pct_3B_s123 / exp_001_eval_15B_d000_s42

### 3. 📊 当前状态
**刚完成**：0.5B-s123 和 1.5B-s123 的 0% baseline SFT 训练（均 success），已更新 registry。1.5B-s42 eval 已提交。exp_005 Stan bug 修复并重启 v2。

**RUNNING (6)**：
| exp_id | 摘要 | 位置 | ETA |
|--------|------|------|-----|
| exp_001_sft_injection | MMLU paraphrase Attempt 2/3 (vLLM) | GPU 0 | ~2.5-3h (07:30-08:00 北京) |
| exp_001_sft_0pct_3B | 3B 0% baseline s42 | GPU 5 | ~3-4h |
| exp_001_sft_0pct_3B_s123 | 3B 0% baseline s123 | GPU 3 | ~3h |
| exp_001_eval_15B_d000_s42 | 1.5B eval (MMLU/GSM8K/ARC/HumanEval) | GPU 4 | 未知 |
| exp_004_sim_sweep | 120 条件 Stan sweep (CPU) | local | ~20h+ |
| exp_005_noise_prop_v2 | ME model noise propagation (CPU) | local | ~4-12h |

**PREPARING (2)**：exp_001_eval_15B_d000_s123, exp_001_eval_05B_d000_s123（等对应 SFT 完成）

**DONE 成功 (5)**：mvp_sim_4pl_gamma, mvp_sim_confounding, exp_001_sft_0pct_05B, exp_001_sft_0pct_15B, exp_001_sft_0pct_05B_s123, exp_001_sft_0pct_15B_s123

**等待中**：
- MMLU paraphrase 完成 → 触发 Phase 2 数据重建 → Phase 3
- 3B 两个 seed 训练完成 → 提交 3B eval
- cuda:1 和 cuda:2 **已空闲**，应立即安排 0.5B eval 任务

### 4. 📋 待办（条件触发式）
- **cuda:1/2 已空闲** → 立即提交 exp_001_eval_05B_d000_s42（0.5B-s42 eval）和 exp_001_eval_05B_d000_s123（0.5B-s123 eval），不要让 GPU 空着
- exp_001_sft_0pct_3B 完成 → 提交 exp_001_eval_3B_d000_s42（3B-s42 eval）
- exp_001_sft_0pct_3B_s123 完成 → 提交 exp_001_eval_3B_d000_s123（3B-s123 eval）
- exp_001_eval_15B_d000_s42 完成 → 记录 metrics 到 registry，与 train loss 交叉验证
- MMLU paraphrase 3-attempt 全部完成 → (1) 验证 `mmlu_paraphrases.json` 非空 (2) 重跑 `prepare_sft_data.py` (3) 确认 3 benchmark 齐全 (4) 启动 Phase 3 contaminated SFT（12 runs seed=0: {5%,25%,50%,100%} × {0.5B,1.5B,3B}）
- Phase 3 调度预案：GPU 0-3 各跑 1×3B+1×0.5B (~4.5h)，GPU 4-5 各跑 2×1.5B (~3.4h)
- exp_004_sim_sweep 完成 → 验证 identifiability 阈值 vs Fisher 理论，写入 paper
- exp_005_noise_prop_v2 完成 → 验证 ME model coverage improvement，更新 Table/Figure
- Phase 3+4 完成 → exp-002 contamination signals → exp-003 RRF → exp-006 IRT calibration → **exp-008 signal_survival_analysis**（C2 唯一证据，P0）

### 5. 🎯 战略上下文
- **投稿目标**：EMNLP 2026 ARR May 25，距今 12 天。**全速推进，不留 buffer**
- **核心方法**：ContamCal = post-hoc statistical calibration via contamination-augmented 4PL IRT。用 contamination exposure signal 作为 IRT 的额外参数 γ，分离真实能力 θ 和 contamination inflation
- **MVP 已通过 (D004)**：4PL+γ 在 N_items=300 下成功分离 γ 和 θ（PASS），confounding 场景也通过（corr=0.38 下 γ_rel_bias=7.7%，PASS）
- **Critical path 瓶颈**：MMLU paraphrase（GPU 0）。MMLU 完成前无法启动 Phase 3 contaminated SFT（核心实验）
- **易错点**：
  - exp_001_sft_0pct 是 parent entry（无直接进程），不要尝试 SSH 检查它
  - Cron 会对 server="local" 的实验 false positive（SSH 连接失败 → 误判 failed），已发生两次 rollback，看到这类回调先 `ps -p PID` 本地验证
  - 0% dosage 数据 = 纯 SlimOrca，不含 paraphrases，当前训练有效（D010 确认）
  - dosage >0% 文件目前仅含 ARC+GSM8K，**MMLU 完成后必须重跑 prepare_sft_data.py**
- **Table 2 风险**：Related Work 表中 ContamCal "RL-robust partial✓" claim 唯一证据来源是 exp-008（signal_survival_analysis），尚未启动。若结果不支持需删除该 claim
- **Fisher 推导**：已完成 appendix.tex（Theorem 1 + 2 Corollaries），用于理论支撑 identifiability
- **决策链**：D001(MVP 策略) → D003(Phase A PASS) → D004(MVP 通过) → D006(回归 EMNLP) → D009(HumanEval 降级) → D010(数据策略)


---
