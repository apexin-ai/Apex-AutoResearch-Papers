# code uniform perlayer allocation

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_uniform_perlayer_allocation_20260516T030803_result.json`
- **Structured JSON:** [`5260ceac71d6ff04c2fc.json`](../../sessions/52/5260ceac71d6ff04c2fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两块 GPU 均有活跃进程（cuda:0: 1 进程 ~20GB, cuda:1: 2 进程 ~62GB），不启动分析。

---

**产出汇总：**

1. **`src/analyze_perlayer_sparsity.py`** — 分析脚本
   - 加载 predictor + base model，对 calibration data 运行推理
   - 计算 global top-k masks，统计每层实际 sparsity
   - 输出：每层 sparsity + 统计摘要（mean/std/min/max/前半后半对比），保存 JSON
   - 参数：`--model_path`, `--predictor_path`, `--sparsity_target`, `--output_path`, `--device`

2. **`src/lm_eval_sparse_uniform.py`** — 带 uniform allocation 的 eval 脚本
   - 基于 `lm_eval_sparse.py`，新增 `--allocation` 参数（`global` | `uniform`，默认 `uniform`）
   - `_uniform_topk_masks()`: 每层独立做 top-k，确保每层 sparsity 严格等于 `sparsity_target`
   - `_global_topk_masks()`: 保留原始行为供对比
   - 新增 `--device` 参数（原版硬编码 cuda:0）

3. **Dry-run 验证**：两个脚本 `--help` 均正常通过

4. **50% 分析未运行**：两块 GPU 均有活跃进程，跳过。空闲时运行命令：
   ```bash
   CUDA_VISIBLE_DEVICES=0 python src/analyze_perlayer_sparsity.py \
       --model_path /root/autodl-tmp/models/llama-3.1-8b \
       --predictor_path checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt \
       --sparsity_target 0.5
   ```

---
