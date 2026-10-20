# exp vllm resubmit v2

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_vllm-resubmit-v2_20260513T071255_result.json`
- **Structured JSON:** [`4831ac69924fa84432bf.json`](../../sessions/48/4831ac69924fa84432bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

1. **GPU1 清理** — 成功。杀掉了旧 tmux 会话 `mvp-p1-gpu1` + 残留的 vLLM EngineCore 进程 (PID 145984, 占 27892 MiB)
2. **vLLM 验证** — 通过。根因：`llm_agent.py:195` 用 `os.environ["CUDA_VISIBLE_DEVICES"] = str(self.gpu_id)` 覆盖了 shell 设的值。修复为 `os.environ.setdefault()`，改用 `CUDA_VISIBLE_DEVICES=1 + --gpu_id 0` 方案。1 episode / 5 steps 全部完成无 crash
3. **提交后端** — **vLLM**（20 episodes × 2 tasks × 30 steps）
4. **新 PID**: 162572 (主进程), 163319 (EngineCore on GPU1, 15352 MiB)；**tmux 会话**: `mvp-p1-gpu1-vllm`

---
