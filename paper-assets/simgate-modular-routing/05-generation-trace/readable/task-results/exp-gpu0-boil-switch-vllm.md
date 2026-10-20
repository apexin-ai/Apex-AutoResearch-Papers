# exp gpu0 boil switch vllm

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_gpu0-boil-switch-vllm_20260513T091835_result.json`
- **Structured JSON:** [`7a954cca2a365134acba.json`](../../sessions/7a/7a954cca2a365134acba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

vLLM 后端正常推理中，速度约 1000-1300 toks/s input。

**汇总：**

1. **Boil 数据完整**：20 episodes, summary.json 存在。均分：internal=-49.8, deterministic=-19.7, oracle=-29.7
2. **GPU0 清理完成**：PID 20296 + 残留 PID 20301 均已 kill，tmux session `mvp-p1-gpu0` 已销毁，GPU0 显存完全释放
3. **vLLM 加载验证**：内联测试超时（30s 限制），但实际任务已成功加载 vLLM 并开始推理
4. **新实验**：PID 572089, tmux session `mvp-p1-gpu0-vllm`, registry 已更新为 RUNNING
5. **GPU1 未受影响**：PID 325695 正常运行，28004 MiB 占用

---
