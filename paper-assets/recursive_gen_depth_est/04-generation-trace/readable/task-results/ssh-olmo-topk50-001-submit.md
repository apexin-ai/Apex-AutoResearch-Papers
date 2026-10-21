# ssh olmo topk50 001 submit

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_olmo_topk50_001_submit_20260514T225926_result.json`
- **Structured JSON:** [`b31978689247046aafc5.json`](../../sessions/b3/b31978689247046aafc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:1 未空闲。PID 213402 正在运行 olmo_temp09 的 depth-2 生成（已运行 3 分钟）：

```
python scripts/generate_next_depth.py --adapter_dir checkpoints/olmo_temp09/lora_depth_1 \
  --output_path data/olmo_temp09/depth_2.jsonl --target_depth 2 \
  --model_name /root/autodl-tmp/models/olmo-1b-hf \
  --decoding_strategy temp_only --temperature 0.9 --gpu 0
```

olmo_temp09 pipeline 仍在 cuda:1 上活跃，尚未退出。需要等它完成或手动终止后才能提交 olmo_topk50_001。

是否要等待，还是终止该进程后立即提交？

---
