# debug disk cleanup

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_disk_cleanup_20260519T050407_result.json`
- **Structured JSON:** [`edeebd463cb009223eef.json`](../../sessions/ed/edeebd463cb009223eef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 清理结果

| | Before | After |
|---|---|---|
| `/root/autodl-tmp` | 236G / 250G (**95%**) | 220G / 250G (**88%**) |
| `/` (overlay) | 20G / 30G (66%) | 17G / 30G (55%) |

**已释放 ~19G**，明细：
- HF cache (Llama-2-7b-hf): 13G
- CLIP checkpoint 重复副本: 3.2G
- pip cache: 3.6G (overlay)
- LIBERO.zip, aria2 logs, smoketest files, sr_debug logs, 空目录: ~0.2G

**待决策**: `checkpoints/openvla-7b-untrained/` (15G) — 不在 registry checkpoint_path 中，features 已提取，可通过 `init_untrained.py` + openvla-7b 重建。删除后 autodl-tmp 降至 82%。是否清理？

---
