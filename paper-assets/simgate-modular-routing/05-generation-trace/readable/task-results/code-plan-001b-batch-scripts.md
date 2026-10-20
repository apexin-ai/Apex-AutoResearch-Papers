# code plan 001b batch scripts

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-001b-batch-scripts_20260513T184222_result.json`
- **Structured JSON:** [`2ebf4950a57274a7d4f8.json`](../../sessions/2e/2ebf4950a57274a7d4f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

参数全部匹配，脚本已就绪。

**总结：**

| 脚本 | GPU | Tasks | 预估负载 |
|------|-----|-------|---------|
| `run_plan001b_gpu0.sh` | cuda:0 | chemistry-mix, find-animal, find-living-thing | 3 tasks × 20ep |
| `run_plan001b_gpu1.sh` | cuda:1 | find-plant, chemistry-mix-paint-tertiary-color | 2 tasks × 20ep |

GPU0 分 3 个（chemistry-mix 较轻），GPU1 分 2 个（tertiary-color 较重），时间大致平衡。两个脚本均设置 `CUDA_VISIBLE_DEVICES` + `--gpu_id 0`，输出到 `results/plan001b/`。脚本头部有预筛信号注释，尾部预留了扩展位置。准备好后 `nohup bash run_plan001b_gpu0.sh > /tmp/plan001b_gpu0.log 2>&1 &` 启动即可。

---
