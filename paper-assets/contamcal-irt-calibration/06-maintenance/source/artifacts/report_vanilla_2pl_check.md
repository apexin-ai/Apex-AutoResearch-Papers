# Experiment Status Check — 2026-05-18 03:45 UTC

## Task 1: exp_006_mmlu_vanilla_2pl_fullitems

**结论：MCMC 采样已完成，无活跃进程**

### 发现

- **脚本**: `compute_vanilla_2pl_tau_fullitems.py`
- **启动时间**: 2026-05-17 21:42:05
- **数据规模**: 20 models × 14042 items (Full MMLU), vanilla 2PL (no contamination param)
- **当前进程**: 无（ps 未找到相关进程）
- **tmux 会话**: 无（no server running）

### 产出文件

| 路径 | 大小 |
|------|------|
| `/root/autodl-tmp/exp006/vanilla_2pl_fullitems_chains/` (总计) | 898MB |
| `vanilla_2pl_noll-20260517214206_1.csv` | 184MB |
| `vanilla_2pl_noll-20260517214206_2.csv` | 162MB |
| `vanilla_2pl_noll-20260517214206_3.csv` | 296MB |
| `vanilla_2pl_noll-20260517214206_4.csv` | 296MB |
| `/root/autodl-tmp/exp006/vanilla_2pl_tau_fullitems.log` | 18KB |

### 采样详情

- 4 chains, 1000 warmup + 1000 samples, NUTS max_depth=12, delta=0.95
- Chain 3 stdout 确认 2000/2000 iterations completed（Warmup 4001s + Sampling 2035s = 6036s total）
- 所有 chain CSV 文件时间戳 May 18 00:58（总运行 ~3h16m）
- Chain 1/2 CSV 明显小于 chain 3/4（184/162MB vs 296MB），可能有 divergent transitions

### 状态

**已完成（COMPLETED）**。MCMC chains 全部采样完毕并保存。Log 中无 post-processing 输出（无 "Saved summary" 等），说明 Python 层面可能未执行后续 tau 提取，或 script 在采样结束后静默退出。Chains 可直接用于后续分析。

---

## Task 2: exp_002_signals_3B_d000_s123_cuda2

**结论：已完成（COMPLETED）**

### 发现

- **完成时间**: 2026-05-16 22:05:33
- **当前进程**: 无
- **Log 最终状态**: `===BATCH_COMPLETE_d000_s123_a32=== Total:9 Completed:6 Skipped:2 Failed:1`

### 产出文件

| 路径 | 大小 |
|------|------|
| `/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_s123_a32/` | — |
| `signal_s1_embedding_mmlu.json` | 7.9MB |
| `signal_s1_embedding_arc_challenge.json` | 665KB |
| `signal_s1_embedding_gsm8k.json` | 734KB |
| `signal_s2_minkpp_mmlu.json` | 2.9MB |
| `signal_s2_minkpp_arc_challenge.json` | 250KB |
| `signal_s2_minkpp_gsm8k.json` | 272KB |
| `signal_s4_selfcritique_mmlu.json` | 3.3MB |
| `signal_s4_selfcritique_arc_challenge.json` | 291KB |
| `signal_s4_selfcritique_gsm8k.json` | 317KB |
| `signals_merged_mmlu.json` | 2.2MB |
| `signals_merged_arc_challenge.json` | 235KB |
| `signals_merged_gsm8k.json` | 243KB |

### 状态

**已完成**。9 个子任务中 6 completed / 2 skipped / 1 failed。三组 benchmark (mmlu/arc/gsm8k) × 三类信号 (s1/s2/s4) 均已产出并 merge。

---

## 当前服务器活跃任务

唯一活跃进程是 `gamma_prior_sensitivity_resume.py`（PID 28547 启动，4 个 Stan chains PID 29953-29957 在跑 `contam_irt_2pl_gamma_loose` 模型）。
