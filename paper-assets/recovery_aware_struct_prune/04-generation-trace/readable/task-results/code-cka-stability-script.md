# code cka stability script

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cka_stability_script_20260519T212201_result.json`
- **Structured JSON:** [`a956a311708cf4e549ea.json`](../../sessions/a9/a956a311708cf4e549ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 3 有 97GB 可用，完全够用。以下是脚本和运行方案总结：

---

**脚本路径**: `src/cka_stability_analysis.py`

**运行命令** (westd-29022, cuda:3):
```bash
cd /root/recovery_aware_struct_prune && python src/cka_stability_analysis.py \
  --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B \
  --output_path /root/autodl-tmp/recovery_aware_struct_prune/cka_stability_results.json \
  --device cuda:3
```

**脚本逻辑**:
1. 加载 7B dense 模型到 cuda:3
2. 加载 1024 个 GSM8K train 校准样本（seed=42，与 pruning 一致）
3. 收集全部 1024 样本的 q_proj（attn heads）和 gate_proj（MLP groups）激活
4. 释放模型，对 256/512/1024 三种 size 分别计算 F(h)（通过 subsample indices，256 ⊂ 512 ⊂ 1024）
5. 计算 3 对 Spearman rank correlation（attn / mlp / combined）
6. 输出 top-10 / bottom-10 结构 + 完整 JSON

**复用函数**: `load_calibration_data`, `set_seed` from `cka_overlap.py`; `collect_qproj_activations`, `collect_mlp_activations`, `compute_fh_scores` from `run_cka_reliability.py`

**预估运行时间**: ~25-35 分钟
- 模型加载: ~1 min
- 前向收集激活 (2×1024 samples): ~10 min
- F(h) 计算 (3 sizes × 2 types × 28 layers × 378 pairs): ~15-20 min

需要先把脚本 sync 到 westd-29022，是否批准运行？

---
