# verify pi05 r2 normfix

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_pi05-r2-normfix_20260521T033549_result.json`
- **Structured JSON:** [`bad2c013893f0eefc29d.json`](../../sessions/ba/bad2c013893f0eefc29d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

### 1. PID 802639
- **已死亡**（`ps -p` 返回空）。启动于 09:49，使用**旧版代码**（fix 在 11:29 才部署），但已不再运行。不是问题。

### 2. Wrapper 当前 normalization
- **MEAN_STD** ✅ — 代码使用 `self.state_mean` / `self.state_std`，无 `q01`/`q99`/`QUANTILES` 的任何痕迹。修改时间 11:29:58。

### 3. PID 811001 (r2) 当前进度
- 正在跑修复版代码，**但全部 OOM 失败**
- 已过 6/10 tasks，258 个 rollout 记录，**success rate 全部为 0%**
- 每个 rollout 在 step 0 就 CUDA OOM（`resize_with_pad_torch` → `clamp` 报错）
- GPU 当前占用 10.5GB/24.5GB — 看起来不满，但推理峰值内存超限

### 4. 结论：需要 kill 811001 并排查 OOM
r2 结果不可用（全 0 是 OOM 导致的，不是模型真实表现）。可能原因：
- 之前 802639 死亡时没有完全释放 GPU 显存（需 `torch.cuda.empty_cache()` 或清理残留进程）
- π0.5 模型本身在 4090 24GB 上推理时峰值内存紧张

建议：kill 811001，确认 GPU 完全释放后重新启动 eval。

---
