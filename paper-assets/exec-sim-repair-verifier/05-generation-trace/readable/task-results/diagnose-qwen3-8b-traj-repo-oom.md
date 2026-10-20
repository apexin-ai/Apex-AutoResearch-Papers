# diagnose qwen3 8b traj repo oom

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_qwen3-8b-traj-repo-oom_20260518T224312_result.json`
- **Structured JSON:** [`6b8eeb7e320d7654049d.json`](../../sessions/6b/6b8eeb7e320d7654049d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 根因

**gradient_checkpointing 已开启**（代码第 ~170 行 `"gradient_checkpointing": True`），不是缺少 GC 的问题。

实际原因：**8B bf16 模型权重 (~16GB) + 8192 seq_length 的 activation memory 超过 RTX 5090 的 31.36GB 显存上限**。

关键细节：
- OOM 发生在 **backward pass**（step 2），step 1 成功通过 — 说明不同样本序列长度不同，长样本触发 OOM
- **flash_attn 未安装**，回退到 SDPA（日志：`Attention: sdpa`）。SDPA 在长序列时内存效率低于 FlashAttention-2
- OOM 时 PyTorch 已分配 27.10 GiB，尝试再分配 4.64 GiB，总计需要 ~31.7 GiB > 31.36 GiB
- 差距仅 ~2 GB，属于边际 OOM

### 对比分析
| 配置 | 模型权重 | seq_len | 结果 |
|------|---------|---------|------|
| Qwen3-4B + 8192 | ~8GB | 8192 | 成功 |
| Qwen3-8B + 2048 | ~16GB | 2048 | 成功 |
| Qwen3-8B + 8192 | ~16GB | 8192 | OOM |

符合预期：权重翻倍+序列翻4x，activation memory 爆掉。

### 推荐修复方案

**方案 A（首选）：安装 flash-attn，不改任何超参数**

差距仅 ~2GB，FlashAttention-2 对 8192 长序列可节省 2-4GB activation memory（O(1) vs O(S²) attention memory）。预估修复后显存：25-27 GB / 31.36 GB，有余量。

```bash
pip install flash-attn --no-build-isolation
```

无需改训练命令，脚本已有自动检测逻辑（`import flash_attn` → `attn_impl = "flash_attention_2"`）。

**方案 B（备选）：降 seq_length 到 4096**

一定能解决，但需评估 truncation rate。当前 8192 时只有 1% truncated（4/386），降到 4096 后 repo-level 数据 truncation 会显著增加，可能影响训练质量。需要 Director 批准参数变更。

**方案 C（辅助）：`PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`**

日志显示仅 819MB reserved-but-unallocated，碎片化不严重。单独使用不足以弥补 ~2GB 缺口，但可与方案 A 配合减少碎片。

### 建议

先尝试方案 A（安装 flash-attn），保持所有训练参数不变。如果 5090 上 flash-attn 编译有问题，再考虑方案 B。是否执行？

---
