# ssh write internlm2 custom profiling

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_write_internlm2_custom_profiling_20260515T231058_result.json`
- **Structured JSON:** [`8d80eae14a9af1e2c1fc.json`](../../sessions/8d/8d80eae14a9af1e2c1fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有验证通过。

**产出总结：**

1. **InternLM2 attention 结构分析：**
   - 使用 fused `self.wqkv` 而非 `q_proj/k_proj/v_proj`
   - 输出投影 `self.wo` 而非 `o_proj`
   - 层路径 `model.model.layers[i].attention` 而非 `self_attn`
   - QKV 拆分通过 `einops.rearrange` 实现：`"b q (h gs d) -> b q h gs d"`, `gs=2+num_kv_groups`
   - 架构：32L × 8KV heads, GQA 4:1, head_dim=128, 共 256 个 KV heads

2. **eval_ppl.py 兼容性：不兼容。** 三处硬编码不匹配（`q_proj/k_proj/v_proj`, `self_attn`, `position_embeddings`）

3. **脚本 `/root/ratekv/run_internlm2_hires_profiling.py`** 已完成，包含自定义 `patch_attention_internlm2`：
   - 正确处理 fused wqkv → einops rearrange → Q/K/V split
   - 使用模型自带的 `rotary_emb` 做 RoPE
   - 在 RoPE 后对目标 head 的 K/V 做 round-trip quantization
   - forward 签名与 InternLM2Attention 完全匹配（`position_ids` 而非 `position_embeddings`）
   - 默认 `--gpu cuda:1`

4. **验证：** 语法 OK，所有 imports 正常，config 确认 32L×8KV。模型权重仍在下载中，无法 dry-run。

---
