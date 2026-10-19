# code flashinfer benchmark script

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_flashinfer_benchmark_script_20260519T162354_result.json`
- **Structured JSON:** [`d55c0924ece8f700f2d7.json`](../../sessions/d5/d55c0924ece8f700f2d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks pass. Here's the summary:

**脚本路径**: `/root/distill_sparse_swiglu/src/benchmark_flashinfer.py`

**结构**:
- **5 种 benchmark 模式**: `dense`, `mask_multiply_{30,50}` (现有方法，无 FLOP 节省), `sparse_{30,50}` (gather-matmul，真正跳过零神经元)
- **Sparse 实现**: `torch.index_select` 提取 active neurons → 预切片 `down_proj.weight[:, active_idx]` → `F.linear` 做小 matmul。`down_proj` 从 `[H, I]=[4096, 14336]` 降到 `[H, K]`，30% sparsity 时 K≈10035，50% 时 K≈7168
- **Timing**: `torch.cuda.Event` 精确 GPU timing，取 median
- **输出**: JSON 到 `results/benchmark_flashinfer.json` + Markdown 汇总表
- **两层测量**: 全模型 end-to-end latency + FFN-only isolated latency + predictor-only overhead

**验证结果**:
- Syntax check: PASSED
- Import check: PASSED
- `--help`: PASSED
- 两个 checkpoint 都存在
- flashinfer 实际已安装（`HAS_FLASHINFER=True`），脚本检测到了（但当前未实现 flashinfer 特定 kernel 路径，仅 detect；gather-matmul 是主要 sparse 路径）

**潜在问题**:
1. **GPU 占用**: 34887:0 和 :1 当前都在跑实验，不能做 dry_run with GPU。等实验完成后再跑
2. **flashinfer kernel 路径**: 脚本 detect 到 flashinfer 可用但 `flashinfer_{30,50}` 模式尚未实现具体 kernel 调用——如果需要 flashinfer sparse matmul API 对比，需要补充实现
3. **mask 计算用简单 calibration text**: 生产 benchmark 可能需要用 C4 calibration data 替代重复文本

---
