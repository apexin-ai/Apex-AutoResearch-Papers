# ops cuda4 eval submit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda4-eval-submit_20260516T005431_result.json`
- **Structured JSON:** [`70045298dad7359a9e2f.json`](../../sessions/70/70045298dad7359a9e2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部诊断完成。汇总结果：

---

### 1. v8_recovery 死因
- **SIGTERM killed**（不是 OOM）。日志末尾显示 `Terminated` + `FAILED: arc_challenge`
- 完成了 d100_a32_s123 的 s1_embedding_mmlu、s2_minkpp_mmlu、s4_selfcritique_mmlu
- 在 arc_challenge 的 s1_embedding 阶段被 SIGTERM 杀掉
- 日志路径：`exp_002_signals_3B_v8.log`（不是 v8_recovery）

### 2. d000_s42_a32 checkpoint
- **`Qwen2.5-3B_d000_a32_s42/lora_adapter/` 是空目录**（0 文件）—— 不可用
- **`Qwen2.5-3B_d000_s42/lora_adapter/` 有完整权重**（adapter_model.safetensors 114MB）
  - `adapter_config.json` 确认 **lora_alpha=32** ✓
  - 训练日志 `exp_001_sft_3B_d000_s42_a32.log` 显示 r=16, alpha=32, EXIT_CODE=0
  - 尽管目录名在 C006 黑名单中，但实际 alpha 值是 32（D088 说的命名不一致就是这个情况）
- **正确的 adapter 路径**：`/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter`

### 3. cuda:4 不空闲 —— 阻断提交
| GPU | PID | 进程 | VRAM | 启动时间 |
|-----|-----|------|------|---------|
| cuda:4 | 668217 | compute_signals d025_s123 (s4_selfcritique) | 6876MiB | 08:51 |

PID 668217 是 **v8_recovery 死后新起的 signals 进程**（d025_s123，alpha=32 已验证）。cuda:4 被占用，**不能提交 eval batch**。

### 4. cuda:3 d025_v3_s42_batch
- PID 655989 **存活**，07:22 启动，正在跑 aligned eval（mmlu gsm8k arc_challenge）
- 输出目录 `Qwen2.5-3B_d025_v3_s42_aligned/` 已创建但尚无结果文件（仍在推理中）
- GPU 3 占用 8985MiB，util 68%

---

**需要决策**：
1. cuda:4 上 PID 668217（d025_s123 signals）要 kill 给 eval 让路，还是等它跑完？
2. d000_s42 虽在 C006 黑名单但实际 alpha=32 —— 是否确认可用并更新黑名单？

---
