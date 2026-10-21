# infra gpu check

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-check_20260522T003330_result.json`
- **Structured JSON:** [`4b36313178268af43b2d.json`](../../sessions/4b/4b36313178268af43b2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态汇总：

- **4 张 RTX PRO 6000 Blackwell (98GB each) 全部被 vLLM 占满**，GPU 利用率均为 0%
- **vLLM 实例 1**: Qwen3-32B → GPU 0,1 / port 8000 / PID 121781（May 21 启动）
- **vLLM 实例 2**: Llama-3.3-70B-Instruct → GPU 2,3 / port 8003 / PID 168588（May 21 启动）
- **无其他训练进程**

两个 vLLM 都在空转（0% 利用率），可以安全关闭。执行 `kill 121781 168588` 即可释放全部 4×98GB 显存。报告已写入 `artifacts/gpu_status_check.md`。

---
