# exp gemma scienceworld cross model

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_gemma-scienceworld-cross-model_20260520T055916_result.json`
- **Structured JSON:** [`89472fff8e07e6f4f09a.json`](../../sessions/89/89472fff8e07e6f4f09a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

- **westd-18266** 连接失败，切换到 **westb-13313**（2x RTX 5090 32GB）
- **Gemma-2-9B-it** 通过 ModelScope 下载完成（21GB，~25 分钟），HuggingFace 因 gated repo 403 被拒
- 模型路径：`/root/autodl-tmp/models/gemma-2-9b-it/AI-ModelScope/gemma-2-9b-it`
- **实验已启动**：
  - `gemma-gpu0` tmux session — 6 tasks (chemistry-mix, find-animal, find-non-living-thing, freeze, grow-fruit, identify-life-stages-1)
  - `gemma-gpu1` tmux session — 5 tasks (identify-life-stages-2, inclined-plane-determine-angle, lifespan-longest-lived, lifespan-longest-lived-then-shortest-lived, measure-melting-point-unknown-substance)
  - 11 tasks × 20 episodes × 2 strategies = 440 episode runs
- **Registry** 已更新为 RUNNING，exp_id: `gemma-scienceworld-cross-model`

---
