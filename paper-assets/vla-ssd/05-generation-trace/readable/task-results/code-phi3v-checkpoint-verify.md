# code phi3v checkpoint verify

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phi3v_checkpoint_verify_20260519T164210_result.json`
- **Structured JSON:** [`586bd65893b3fd53824a.json`](../../sessions/58/586bd65893b3fd53824a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果汇总

**TracVLA-Phi3V checkpoint 全部 5 步验证通过。**

### Step 1: 下载 ✅
两个 shards 完整下载到 `/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/` (7.9GB)

### Step 2: 架构参数 ✅
- 32 layers, 32 heads, hidden=3072, vocab=32064
- 与 OpenVLA-7B 同为 full MHA (非 GQA), 同 vocab_size
- 关键差异: 融合 `qkv_proj` 而非分离 q/k/v proj; 用 CLIP 而非 DINOSigLIP

### Step 3: 推理验证 ✅
- 模型加载到 cuda:1, bf16, ~7.8GB 显存
- 生成 7 个 action token → 256-bin 离散化解码正确
- token ids `[31835, 31918, ...]` → discretized `[228, 145, 145, 254, 233, 159, 191]`

### Step 4: Attention 提取 ✅
- `output_attentions=True` + `eager` attention → 32 层 attention 矩阵 `(1, 32, seq, seq)`
- Attention row sum = 1.0000
- `generate()` 也能返回逐步 attention (用于 routing 分析)

### Step 5: Blockers
- 使用 `tracevla-phi3v` (非 gated) 替代 `openvla_phi3v` (gated), 架构完全一致
- 环境依赖: **transformers 4.48.3** (不能用 5.x), tokenizers ≥0.21
- 注意融合 QKV: 做 routing 分析提取单独的 Q/K/V 时需要 split `qkv_proj` 输出 (dim 按 `3 * hidden_size` 切分)

---
