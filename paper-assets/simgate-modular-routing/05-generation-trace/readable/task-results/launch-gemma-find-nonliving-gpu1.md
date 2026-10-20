# launch gemma find nonliving gpu1

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_gemma-find-nonliving-gpu1_20260520T204328_result.json`
- **Structured JSON:** [`02f21008dc0772633935.json`](../../sessions/02/02f21008dc0772633935.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已启动，运行正常。

**报告：**

1. **cuda:1 状态**：旧 vLLM 进程 (PID 688633, 26374 MiB) 已 kill，显存完全释放后重新启动
2. **脚本**：`scripts/run_gemma_gpu1_findnonliving.sh` — 单 task `find-non-living-thing`，20 episodes，`CUDA_VISIBLE_DEVICES=1`，`enforce_eager=True`，模型路径 `/root/autodl-tmp/models/gemma-2-9b-it/AI-ModelScope/gemma-2-9b-it`，输出 `results/gemma_scienceworld_counterfactual/find-non-living-thing/`
3. **启动确认**：tmux session `gemma-gpu1-final` 运行中，vLLM EngineCore 已加载 (17.22 GiB)，正在处理 episode 0 的 steps（inference 速度 ~800-1300 toks/s input, ~40 toks/s output），cuda:1 占用 26383 MiB / 8% utilization

---
