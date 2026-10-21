# code profiling script

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_profiling_script_20260525T114510_result.json`
- **Structured JSON:** [`d66fb15a8b159e66e46b.json`](../../sessions/d6/d66fb15a8b159e66e46b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写入 `/artifacts/profile_inference_efficiency.py` 并注册到 manifest。

支持的功能：
- **三个模型**: OpenVLA（projector hook pruning）、Pi0.5（embed_prefix monkey-patch）、X-VLA（_encode_image 包装）
- **四种方法**: baseline / random / l2norm / attention（attention 仅 OpenVLA）
- **批量扫描 k_ratio**: 一次加载模型，切换 k_ratio（OpenVLA/X-VLA 不需重载；Pi0.5 因 patch 不可逆每次重载）
- **精确计时**: 每个 inference step 前后 `torch.cuda.synchronize()`，跳过前 N 个 warmup step
- **Memory**: `torch.cuda.reset_peak_memory_stats()` + `max_memory_allocated()`
- **CSV 追加模式**: 多次运行结果可拼接

---
