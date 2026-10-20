# research dream action prep

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_dream-action-prep_20260515T031103_result.json`
- **Structured JSON:** [`391930fcae9a8f06e0f7.json`](../../sessions/39/391930fcae9a8f06e0f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部语法检查通过。

---

## 创建状态汇总

| # | 脚本 | 路径 | 运行命令 | 预估 GPU 时间 |
|---|------|------|----------|--------------|
| **plan_015** | `run_alpha_ablation.sh` | `src/run_alpha_ablation.sh` | `CUDA_VISIBLE_DEVICES=0,1 bash src/run_alpha_ablation.sh` | ~3h（5次剪枝 ~15min/次 + 5次全量 GSM8K eval ~25min/次，双 GPU 并行） |
| **plan_016** | `measure_inference_speed.py` | `src/measure_inference_speed.py` | `CUDA_VISIBLE_DEVICES=0 python src/measure_inference_speed.py` | ~20min（3 模型 × 50 prompts × 256 tokens） |
| **plan_017** | `run_unstructured_baseline.py` | `src/run_unstructured_baseline.py` | `CUDA_VISIBLE_DEVICES=0 python src/run_unstructured_baseline.py` | ~40min（剪枝 5min + 全量 GSM8K eval 35min） |

### 关键设计决策

- **plan_015**: `--alpha` 已在 `prune.py:166` 支持，无需改代码。α=0.0 时 `(1-F(h))^0=1`，退化为纯 importance 排序。脚本按奇偶分配到 GPU0/GPU1 并行。剪枝后模型写 `/root/autodl-tmp/recovery_aware_struct_prune/alpha_ablation/`（遵守 C002 磁盘约束）。
- **plan_016**: `max_new_tokens=256`（速度测试不需完整推理链）。支持 `--models name:path` 自定义模型列表。自动计算相对 original 的 speedup。
- **plan_017**: 全局 magnitude pruning，跳过 embedding/lm_head/norm 层。直接在内存中 zero-out 不保存模型（省磁盘），就地 eval。

---
