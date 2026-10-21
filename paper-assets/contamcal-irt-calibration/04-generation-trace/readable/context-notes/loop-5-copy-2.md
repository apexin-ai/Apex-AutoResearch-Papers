# agent / loop_5.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_5.md`
- **Structured JSON:** [`01d35829459796878b90.json`](../../sessions/01/01d35829459796878b90.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: idle_timeout
updated: '2026-05-14T13:09:46+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 cuda:0-5（cqa1-21977 全 6 卡），不可用其他服务器卡
- 所有 MC eval 必须 `--mc-format aligned`（D017），legacy 结果仅供诊断
- 3B GSM8K 排除出 dose-response 分析（D018 决策），eval 照跑但不入正式结果
- exp-002 进度必须 `ps aux | grep compute_signals` 核实，不能从文件时间戳推断（被 Reviewer CRITICAL 过）
- `server: local` 实验（exp-004/005）用 `ps -p PID`，**禁止 SSH 查**
- SFT EXIT_CODE=129 是 wrapper SIGHUP false positive，覆盖 conclusion=success，不重训
- 论文结果必须用 CmdStanPy MCMC（D011），不能用 PyTorch MLE
- 提交实验前必须 nvidia-smi 查目标 GPU 有无同类进程（C001）
- `train_sft.py` 和信号脚本中已删除 `os.environ["CUDA_VISIBLE_DEVICES"]` 覆写，GPU 绑定由 wrapper 控制，脚本只用 `cuda:0`

### 2. 🖥️ 基础设施快照
- **服务器**: cqa1-21977, 6× RTX 4090D (24GB), 全部分配本项目
- **环境激活**: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`（conda 环境，不是 venv）
- **项目代码**: `/root/contamcal-irt-calibration/`（exp001/ exp002/ exp008/ 子目录）
- **数据盘**: `/root/autodl-tmp/`
  - HF cache: `/root/autodl-tmp/.hf_cache/`
  - SFT data: `/root/autodl-tmp/exp001/sft_data/sft_dosage_{000,005,025,100}.jsonl`
  - Checkpoints: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-{0.5B,1.5B,3B}_{dosage}_{seed}/lora_adapter/`
  - Eval results: `/root/autodl-tmp/exp001/eval_results/`
  - Signal outputs: `/root/autodl-tmp/exp002/signals/`
- **Stan**: CmdStanPy v1.3.0, CmdStan 2.38.0, 4 模型已编译 (contam_irt_4pl_simple.stan 等)
- **活跃 cron**: exp_001_sft_d005_3B, exp_001_eval_3B_d000_aligned (均刚进入 ANALYZING), exp_002_signals_05B (PID 370957), exp_001_eval_3B_d100_aligned (PID 362942)
- **本地 CPU 实验**: exp-004 sim sweep v2 (PID 411032, 3/12 conditions), exp-005 noise prop v3 (PID 426335, 44%)
- **AutoDL 特殊**: 安装前 `source /etc/network_turbo`, HF 下 `HF_HUB_DISABLE_XET=1`, SSL certs 需 export

### 3. 📊 当前状态
**刚完成 / ANALYZING（需要你接手处理的回调）**:
- `exp_001_sft_d005_3B` → ANALYZING：3B d005 SFT 完成（cuda:4 释放），需确认 checkpoint 存在，然后提交 3B d005 aligned eval
- `exp_001_eval_3B_d000_aligned` → ANALYZING：3B d000 aligned eval 完成（cuda:5 释放），需提取 metrics 写入 registry

**RUNNING 实验**:
| GPU | 实验 | 摘要 |
|-----|------|------|
| 0 | exp_002_signals_05B (PID 370957) | 0.5B 3 signals × 3 dosages × 3 benchmarks, task ~3/9 进行中, selfcritique 已修复 |
| 1 | exp_001_eval_15B_aligned_batch (PID 336750) | 1.5B aligned eval batch, d000 aligned 完成, 正在跑 para_aligned |
| 2 | exp_001_eval_05B_aligned_batch (PID 332207) | 0.5B aligned eval batch, d000 + d000_para 完成, 正在跑 d005 aligned |
| 3 | exp_001_eval_3B_d100_aligned (PID 362942) | 3B d100 aligned eval, MMLU=64.17% 完成, GSM8K 进行中 |
| 4 | **空闲** — d005_3B 刚完成 | → 应提交 3B d005 aligned eval |
| 5 | **空闲** — 3B d000 aligned eval 刚完成 | → 应提交下一个 eval |
| local | exp-004 sim sweep (PID 411032) | 3/12 conditions, ETA May 16-17 |
| local | exp-005 noise prop v3 (PID 426335) | 44%, ETA ~20:30 UTC today |

**Registry 统计**: 57 实验总计 — RUNNING 6, ANALYZING 2, DONE 39 (26 success, 12 failed, 1 killed), PREPARING 10

**Worker 池 = 0**（上轮所有 Worker 已完成）。两个 ANALYZING 回调尚未处理。

### 4. 📋 待办（条件触发式）
- **立即**: 处理 exp_001_sft_d005_3B ANALYZING → 确认 checkpoint → 在 cuda:4 提交 3B d005 aligned eval
- **立即**: 处理 exp_001_eval_3B_d000_aligned ANALYZING → 提取 metrics → update_registry DONE
- cuda:5 空闲 → 按优先级填充（1.5B d025 SFT 或 0.5B d025 aligned eval）
- exp_002_signals_05B 全 9 tasks 完成 → 立即跑 exp-003 RRF: `python aggregate_rrf.py --generate-exposure --signal-dir /root/autodl-tmp/exp002/signals --output-dir /root/autodl-tmp/exp003 --benchmarks mmlu gsm8k arc_challenge --k 60 --normalize`
- exp-003 完成 → 立即跑 exp-006 IRT calibration + 7 baselines（代码、Stan 全部 ready）
- 3B d100 aligned eval 完成 (cuda:3) → 汇总 metrics，cuda:3 接续 3B d005 para_aligned eval 或 d100 para_aligned
- GPU 1/2 当前 eval batch 完成 → 接续 d005/d100 的 aligned + para_aligned（脚本自动串行）
- exp-005 完成 (~20:30 UTC) → 分析 noise propagation 结果
- exp-004 每完成新 condition → 增量分析

### 5. 🎯 战略上下文
- **EMNLP 2026 ARR May 25 投稿，距今 11 天**
- **Critical path**: exp-002 signals (0.5B, ~30min 估计) → exp-003 RRF (CPU, fast) → exp-006 IRT calibration = **核心 Table 1**。这是整个项目最紧要的管线，优先于一切。
- **决策链**: D017 aligned 格式统一 → D018 3B GSM8K 排除 → D016 Min-K++ ref model 用 d000 fine-tuned → D013 Simple IRT model → D011 CmdStanPy Bayesian → D014 C1 claim 加条件限定 → D015 C2 cliff claim 需 exp-008 验证
- **已有关键结果**: ARC aligned +9.1pp（D017 有效），3B GSM8K 崩塌确认为 LoRA CoT 遗忘（不是格式问题），exp-004 γ 在 AUC=0.55 就可辨识
- **易错点**:
  1. exp-002 文件时间戳 ≠ 当前 run 产出（v3/v4 残留文件会误导，必须 `ls -la` 核实时间）
  2. cron EXIT_CODE=129 是 SIGHUP false positive，不要重训
  3. 0.5B para_aligned MMLU 是 6596 项子集，不能和 14042 项 original 直接比绝对值
  4. ConStat (S3) 需要 paraphrase eval 结果才能跑——目前 paraphrase eval 正在 GPU 1/2 进行中
- **Table 2 风险**: Related Work 表中 ContamCal "RL-robust partial✓" claim 唯一证据是 exp-008（尚未启动，依赖 exp-002 完成）
- **SFT 完成表**: 0.5B 全部 ✅, 1.5B d000/d005/d100 ✅, 3B d000/d100 ✅ d005 刚完成。d025 仅 0.5B 完成。d050 全部 deprioritized


---
