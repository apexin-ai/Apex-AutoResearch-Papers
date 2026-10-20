# ops westd comprehensive fill

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_comprehensive_fill_20260516T184707_result.json`
- **Structured JSON:** [`cf2e3934fbcd4ffcb573.json`](../../sessions/cf/cf2e3934fbcd4ffcb573.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Phase 4: 最终状态表

| GPU | VRAM | PID | 实验名 | 状态 |
|-----|------|-----|--------|------|
| cuda:0 | 58725/97887 MiB (60%) | 32087 | grpo_rasp_rlvr_20_qwen_math | 运行中 (24min+), GRPO v5 训练 |
| cuda:1 | 55833/97887 MiB (57%) | 32427 | grpo_standard_25 | 运行中 (20min+), GRPO v5 训练 |
| cuda:2 | 加载中 → ~15GB | 34032 | **eval_pass_k8_standard_20_grpo_qwen_math** | **刚启动**, 模型加载中 |
| cuda:3 | 0/97887 MiB | — | — | **空闲** (PID 32087 仍在运行，按指令不动) |

### 汇总

**Phase 2**: `eval_pass_k8_rasp_20_sft_qwen_math` → **pass@8=0.935** (N=200, T=0.7, stderr=0.017, eos_rate=99.6%)。Registry metrics+conclusion 已更新。

**Phase 3 调度**:
- **cuda:0**: 忙，跳过原定 eval
- **cuda:2**: alpha ablation Phase A 从未在 westd 本地执行（`/root/autodl-tmp/recovery_aware_struct_prune/alpha_ablation/` 为空）。Phase B 无法启动。**改为运行** cuda:0 原定的 `eval_pass_k8_standard_20_grpo_qwen_math` (PID 34032)
- **cuda:3**: PID 32087 (grpo_rasp_rlvr_20_qwen_math) 仍在 cuda:0 运行中 (24min elapsed, max_steps=100, ~400s/step → 预计还需 ~8h)。按指令保持空闲

---
