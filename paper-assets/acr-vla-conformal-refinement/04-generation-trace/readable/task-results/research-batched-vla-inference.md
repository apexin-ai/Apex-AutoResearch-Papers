# research batched vla inference

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_batched-vla-inference_20260519T040329_result.json`
- **Structured JSON:** [`23e96e101afe9c2af46a.json`](../../sessions/23/23e96e101afe9c2af46a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到 `artifacts/batched_inference_feasibility_report.md`。

核心结论：

1. **支持 batch > 1**: YES。`denoise_step` 和底层 `SmolVLMWithExpertModel.forward()` 全部以 batch 维度运算，无 B=1 硬编码。当前 K sample 的瓶颈是 `generate_k_samples()` 中的 `for _ in range(K)` 循环。

2. **Flow-matching batch 化**: YES。K 个 sample 只是不同初始噪声的确定性 ODE 积分。KV cache 在 denoising 中是只读的（self_attn 层的 `torch.cat` 创建新张量，cross_attn 层直接读 cached KV），可安全 `repeat_interleave` 到 B*K 后共享。

3. **VRAM**: K=5 额外 ~215 MB，K=10 额外 ~500 MB。当前总占用 ~13.5 GB，RTX 4090 24GB 完全无压力。

4. **改动量**: **~27 行，仅改 `src/smolvla_wrapper.py`**。核心操作：`repeat_interleave` KV cache 和 masks 从 B→B*K，生成 B*K 噪声，跑一次 10-step denoising loop，reshape 回 `(B, K, ...)`。不需要改 lerobot 源码。

5. **推荐实现**。K=5 时 denoising 从 50 次 forward → 10 次，预期 3-4x 加速，风险极低。

---
