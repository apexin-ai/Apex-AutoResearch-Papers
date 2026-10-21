# diagnose smart compress eval bypass check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_smart_compress_eval_bypass_check_20260518T012442_result.json`
- **Structured JSON:** [`3e71eb8063aa1c054a25.json`](../../sessions/3e/3e71eb8063aa1c054a25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Diagnosis complete. Here's the full report:

---

## 诊断结果：Smart Compression eval 确实走了压缩路径

### 1. Eval 脚本确认
运行的是 `eval_smart_compress_libero.py`，两个进程：
- GPU 0: `--n_queries 32 --checkpoint_path checkpoints/smart_compress_m32/checkpoint.pt`
- GPU 1: `--n_queries 64 --checkpoint_path checkpoints/smart_compress_m64/checkpoint.pt`

### 2. 压缩路径验证 — **正确**

完整调用链：
```
predict_actions_compressed(wrapper, batch)
  → wrapper.forward_inference(batch)
    → vis_tokens = self._get_visual_tokens(images)          # (B, 128, 960)
    → compressed_vis = self.compressor(vis_tokens.float())   # (B, M, 960)  ← 真正压缩
    → _build_prefix_compressed(compressed_vis, ...)          # 只用 M tokens 构建 prefix
    → KV cache filled with compressed prefix → iterative denoising
```

`_build_prefix_compressed` 方法只使用 `compressed_vis`（M tokens），不会回退到原始 128 tokens。没有 bypass 路径。

### 3. Checkpoint 加载
- 使用 `strict=False`，但日志确认 **no missing/unexpected keys**，等效 strict
- M=32 compressor params: **22,179,840** (~22.2M) ✓
- M=64 compressor params: **22,210,560** (~22.2M) ✓
- 两者差值 30,720 = 32×960，正好是 learnable queries 的尺寸差异，正确

### 4. Vision tokens shape 变化
`VisionTokenCompressor.forward()` 通过 cross-attention pooling 将 `(B, N=128, D=960)` → `(B, M, D=960)`，M=32 或 64。代码中无条件执行，没有 skip/bypass 逻辑。

### 5. 结论

**代码层面没有 bug — eval 确实在做 128 → M 压缩。**

SR 高于 baseline（44.8%）的可能原因不是 bypass，而是：SmartCompressWrapper 训练时同时训了 compressor + action expert head，而 baseline 44.8% 可能是 pretrained SmolVLA 的 zero-shot 性能（没有在 LIBERO 数据上 finetune expert head）。如果 baseline 对比的是未 finetune 的模型，则 SR 差异来自 finetuning 而非压缩本身，这意味着需要一个 **finetuned but uncompressed baseline**（即 M=128 或 full tokens + finetuned expert）来做公平对比。

---
