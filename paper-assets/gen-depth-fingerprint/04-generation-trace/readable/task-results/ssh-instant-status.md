# ssh instant status

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_instant-status_20260515T023717_result.json`
- **Structured JSON:** [`4ee8bb8309dad22d3c2c.json`](../../sessions/4e/4ee8bb8309dad22d3c2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== GPU ===
0, 80 %, 16473 MiB
1, 0 %, 0 MiB
2, 98 %, 21342 MiB
3, 0 %, 0 MiB

=== plan-014 ===
134817    02:18:27
ALIVE

lines:
416 /root/gen-depth-fingerprint/data/qwen3-8b/generations_shard0.jsonl

=== plan-004-v2 ===
all_results.json
all_seed123
all_seed42
all_seed456
binary_filtered_seed123
binary_filtered_seed42
binary_filtered_seed456
depth01_seed123
depth01_seed42
depth01_seed456
depth0_only_seed123
depth0_only_seed42
depth0_only_seed456
size_matched_seed123
size_matched_seed42
size_matched_seed456

=== results ===
/root/autodl-tmp/gen-depth-fingerprint/experiments/downstream/size_matched_seed123/results.json
/root/autodl-tmp/gen-depth-fingerprint/experiments/downstream/size_matched_seed42/results.json
/root/autodl-tmp/gen-depth-fingerprint/experiments/downstream/depth01_seed456/results.json
/root/autodl-tmp/gen-depth-fingerprint/experiments/downstream/size_matched_seed456/results.json
/root/autodl-tmp/gen-depth-fingerprint/experiments/downstream/all_seed42/results.json
/root/autodl-tmp/gen-depth-fingerprint/experiments/downstream/binary_filtered_seed42/results.json
/root/autodl-tmp/gen-depth-fingerprint/experiments/downstream/binary_filtered_seed123/results.json
/root/autodl-tmp/gen-depth-fingerprint/experiments/downstream/binary_filtered_seed456/results.json
/root/autodl-tmp/gen-depth-fingerprint/experiments/downstream/all_seed123/results.json
count: 9
/15 total

=== disk ===
overlay          30G  7.5G   23G  25% /
```

**plan-014**: ALIVE（416 行，运行 2h18m，未完成）
**plan-004-v2**: 9/15 results.json，未完成。缺少：all_seed456, depth01_seed123, depth01_seed42, depth0_only_seed123, depth0_only_seed42, depth0_only_seed456

两个实验均未完成，无需执行额外命令。

---
