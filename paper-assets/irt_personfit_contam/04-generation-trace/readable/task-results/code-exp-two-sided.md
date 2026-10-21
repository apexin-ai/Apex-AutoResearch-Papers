# code exp two sided

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_two_sided_20260520T083522_result.json`
- **Structured JSON:** [`de00d45331b7fc971240.json`](../../sessions/de/de00d45331b7fc971240.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 4 个输出文件已生成，热力图清晰展示了正负方向的 lz* 分布。

关键结果：
- **56/60** 个 (model, benchmark) 对被 flagged（|lz*| > 1.96）
- **50 个正向**（over-consistent），**6 个负向**（aberrant）
- 仅 4 个 normal：DeepSeek-V3/ARC-C、Vicuna-7B/ARC-C、Yi-Lightning/ARC-C、Doubao-pro/HumanEval
- 负向 flagged 的 6 个案例集中在 Gemini-1.5（HellaSwag/GSM8K/HumanEval）、Qwen-Plus（HellaSwag）、Doubao-pro（MMLU）、Hunyuan-Turbo（GSM8K）
- Gemini-1.5 在 MMLU 上 lz*=+34.7（100% accuracy，θ=0.78），在 HumanEval 上 lz*=-12.4——两极分化最极端

---
