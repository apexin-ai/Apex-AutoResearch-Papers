# diag exp012 r2 status

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp012_r2_status_20260515T145431_result.json`
- **Structured JSON:** [`3a589c15b9e5169f1882.json`](../../sessions/3a/3a589c15b9e5169f1882.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**进程已死。** PID 275856 不存在，无任何 python/vllm 进程在运行。GPU 空闲（0% 利用率，0 MiB 占用）。

### 崩溃原因

**flashinfer JIT 编译失败** — 不支持当前 GPU 的 CUDA 架构。

关键错误栈：
```
flashinfer/gemm/gemm_base.py → get_gemm_sm120_module() → gen_gemm_sm120_module()
→ get_nvcc_flags_list()
RuntimeError: No supported CUDA architectures found for major versions [12].
```

flashinfer 尝试为 SM120（Blackwell 架构）编译 FP8 GEMM kernel，但安装的 flashinfer 版本不支持该架构。GPU 有 ~98GB 显存，应为 B 系列卡。

另外日志显示：
```
WARNING: Unknown vLLM environment variable detected: VLLM_ATTENTION_BACKEND
```
vLLM v0.20.2 已不再识别 `VLLM_ATTENTION_BACKEND` 环境变量，脚本中的设置无效。

### 修复方向

1. **升级 flashinfer** 到支持 SM120 的版本
2. **或**通过 vLLM v0.20.2 的新方式禁用 flashinfer，改用 flash-attn backend（v0.20.2 用引擎参数而非环境变量控制）
3. **或**降级 vLLM 到仍支持 `VLLM_ATTENTION_BACKEND` 的版本

需要我执行哪个修复方案？

---
