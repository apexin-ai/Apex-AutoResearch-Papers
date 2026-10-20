# code gradient flow analysis

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gradient_flow_analysis_20260519T142343_result.json`
- **Structured JSON:** [`24795f12ff6c51853660.json`](../../sessions/24/24795f12ff6c51853660.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写好，语法和参数解析均通过验证。

**文件**: `src/gradient_flow_analysis.py`

**核心流程**:
1. 加载 GSM8K train 子集作为 calibration data
2. 对每个模型，在 `self_attn` 和 `mlp` 上注册 `register_full_backward_hook`，捕获 `grad_output[0]` 的 L2 norm
3. 逐样本 forward+backward，累积 per-layer 梯度范数
4. 计算统计量 (mean/std/min/max)，输出 JSON
5. 用 matplotlib 画 attention/MLP 双子图，log scale，Okabe-Ito 色盲友好 palette，error bar 表示 std

**用法示例**:
```bash
python src/gradient_flow_analysis.py \
  --model_paths /path/to/cka_only /path/to/standard /path/to/rasp \
  --model_names "CKA-only" "Standard" "RASP" \
  --n_samples 128 \
  --output_dir /root/autodl-tmp/recovery_aware_struct_prune/gradient_flow/
```

---
