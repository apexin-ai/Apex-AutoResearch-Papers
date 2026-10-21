# ssh 5epoch merge inference

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_5epoch_merge_inference_20260521T175333_result.json`
- **Structured JSON:** [`ff203b0ab71c90012ec9.json`](../../sessions/ff/ff203b0ab71c90012ec9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个推理任务都在正常运行：
- **Seed 42** (GPU 1): 正在渲染 prompts，~5% 完成
- **Seed 123** (GPU 2): 同上，~4% 完成
- 4 张 GPU 全部在用（GPU 0/3 有其他任务）

总结：
1. **Merge 完成** — `checkpoints/qwen3-8b-fewnerd-5epoch-merged/` (16GB, 4 shards)
2. **推理已启动** — `exp_fewnerd_5epoch_s42` (GPU 1) 和 `exp_fewnerd_5epoch_s123` (GPU 2) 在 tmux sessions 中运行
3. **Seed 456** — 等这两个完成或有空闲 GPU 后再跑（当前 4 卡全满）

监控命令：
```bash
tail -5 /tmp/fewnerd_5epoch_s42.log
tail -5 /tmp/fewnerd_5epoch_s123.log
tmux ls
```

---
