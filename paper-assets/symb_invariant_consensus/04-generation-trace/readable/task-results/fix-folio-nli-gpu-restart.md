# fix folio nli gpu restart

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_folio-nli-gpu-restart_20260523T165556_result.json`
- **Structured JSON:** [`d58f8877cd5a214c0d71.json`](../../sessions/d5/d58f8877cd5a214c0d71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**执行结果**：
- Kill 了 3 个 CPU 进程（PID 35767/35904/36041），清理了旧 tmux sessions
- 修复了 `libnvrtc-builtins.so.13.0` 路径问题（加 LD_LIBRARY_PATH）
- 3 个 verifier 在 cuda:0 上串行完成，每个 ~2-4 秒/generator（vs CPU 上数小时）
- cuda:2 上的 LLaMA seed456-v2 实验未受影响

**关键发现**：
- NLI standalone ~47-50%，接近随机——NLI 模型无法处理 FOLIO 的一阶逻辑推理
- 弱 generator（Mistral-7B）受益最多（+3.4~+4.4pp at w=5），但均不显著（best p=0.0636）
- 强 generator（Qwen2.5-14B）反而下降 -0.5~-1.0pp
- **全部 36 个 verifier×generator×weight 组合均无统计显著提升**（p > 0.05）
- 3 个 NLI 架构表现高度一致，结论稳健

Artifact 已注册：`art_20260523_4140cb`

---
