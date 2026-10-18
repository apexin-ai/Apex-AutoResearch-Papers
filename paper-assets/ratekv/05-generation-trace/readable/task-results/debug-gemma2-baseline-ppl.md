# debug gemma2 baseline ppl

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_gemma2_baseline_ppl_20260514T152217_result.json`
- **Structured JSON:** [`0159fdf1c8bed832c9ed.json`](../../sessions/01/0159fdf1c8bed832c9ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**修复验证成功。**

| 指标 | 修复前 | 修复后 |
|------|--------|--------|
| Baseline PPL | 711.38 | **8.90** |

PPL 从 711 降到 8.90，符合 Gemma-2-9B 预期（~8-12）。

## 根因

**Gemma-2 对 BOS token 极度依赖。** `evaluate_perplexity` 将全文编码后切成 512-token 的非重叠 chunk，只有第 0 个 chunk 起始有 BOS（tokenizer 自动添加），其余 563 个 chunk 位置 0 是普通 token。没有 BOS 时 Gemma-2 的预测质量崩溃（单 chunk PPL 从 ~10 暴涨到 700-1300）。

同理 `_load_calibration_data` 用了 `add_special_tokens=False` 导致 calibration 也没有 BOS，baseline calibration PPL=1077 同样异常。

## 修复内容（两处）

1. **`evaluate_perplexity`**：对每个 chunk，检测首 token 是否为 BOS，若不是则 prepend BOS，loss 计算时跳过 BOS 位置
2. **`_load_calibration_data`**：手动 prepend BOS id 到每条序列开头（截断到 `seq_len` 保持长度不变）

本地文件 `run_gemma2_full_pipeline.py` 已修改。需要同步到服务器后重跑完整 pipeline 来获取正确的实验结果。要现在同步并重跑吗？

---
