# code exp 008 instruct rl proxy

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_008_instruct_rl_proxy_20260516T044959_result.json`
- **Structured JSON:** [`fda528dc68222a1a4bcc.json`](../../sessions/fd/fda528dc68222a1a4bcc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务进展总结：

## 完成情况

**Instruct 模型信号** — 已完成 ✓
- Qwen2.5-0.5B-Instruct 已下载到 `/root/autodl-tmp/models/Qwen/Qwen2.5-0.5B-Instruct-hf`
- 3 个 benchmark × 3 个信号 = 9 个信号文件完整（5月15日计算）
- 路径：`/root/autodl-tmp/exp008/signals/rl_aligned/`

**d000 SFT 信号** — 已完成 ✓
- 路径：`/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/`

**Base Pretrained 信号** — 运行中 (PID 701898, GPU 5, 已 18 分钟)
- MMLU S1 + S2 完成，S4 selfcritique 处理中
- GSM8K, ARC 待处理
- 预计总时间 30-45 分钟

## 关键发现

| Benchmark | Instruct S4 | d000 SFT S4 | Δ (Instruct-SFT) |
|-----------|-------------|-------------|-------------------|
| MMLU | -0.878 | -0.956 | **+0.078** |
| ARC | -0.923 | -0.954 | **+0.031** |
| GSM8K | -0.963 | -0.941 | -0.022 |

- **S4 (Self-Critique)** 区分训练 regime：RL 对齐在知识型任务（MMLU/ARC）上增加了自我评估不确定性
- **S2 (Min-K++)** 对 regime 不敏感（差异 <0.01）
- Artifact 已注册：`exp008_3regime_signal_comparison`
- Registry 状态：RUNNING（等待 base pretrained 完成）

---
