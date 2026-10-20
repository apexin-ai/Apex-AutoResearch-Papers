# ops verify gpu after kill

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-gpu-after-kill_20260515T125858_result.json`
- **Structured JSON:** [`a9c0cc7f67f42bf998b1.json`](../../sessions/a9/a9c0cc7f67f42bf998b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**nvidia-smi 输出：**

| GPU | 进程 | 显存占用 | GPU利用率 |
|-----|------|---------|----------|
| 0 | PID 352142 (python3) | 63,852 MiB / 97,887 MiB | 93% |
| 1 | PID 353661 (python3) | 40,692 MiB / 97,887 MiB | 0% |

PID 352975 已从进程列表消失，cuda:1 显存从 ~93GB（53GB僵尸+40GB r3）降到 40,701 MiB，僵尸显存已释放。

**PID 353661 进程状态：**
- STAT: `Rl`（运行中）
- ELAPSED: `03:11`
- CMD: `python3 scripts/train_sft.py --model_path .../Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir .../plan009_sft_baseline_s44_1000 --num_steps 1000 --seed 44 --gpu 1`

**日志最后状态：**
- 进度：step 100/1000（10%），速度 ~1.2 it/s
- 无 error/OOM
- step 50 附近有短暂降速（17s/it → 恢复到 1.2 it/s），可能是 eval checkpoint 或僵尸进程被杀时的 GPU 资源重分配抖动

一切正常，r3 在健康运行。

---
