# eval exp8 scrambled seed123 v2

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp8-scrambled-seed123-v2_20260518T173539_result.json`
- **Structured JSON:** [`151233ee14ba16f52dbd.json`](../../sessions/15/151233ee14ba16f52dbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已完整存在于 `exp8_macro_f1_corrected.json` 中，scrambled seed123 的结果已经算好了。无需重跑。

```
scrambled_seed123_toxicchat_macro_f1: 0.654
scrambled_seed123_toxicchat_binary_f1: 0.738
scrambled_seed123_verazuo_macro_f1: 0.880
scrambled_seed123_verazuo_binary_f1: 0.930

scrambled 3-seed ToxicChat macro F1: mean=0.616 std=0.056 (seeds: 42=0.537, 123=0.654, 456=0.657)
scrambled 3-seed verazuo macro F1: mean=0.822 std=0.046 (seeds: 42=0.818, 123=0.880, 456=0.768)
```

verazuo_test_only_benign（排除泄露后）:
```
scrambled_seed123_verazuo_test_only_macro_f1: 0.722
scrambled_seed123_verazuo_test_only_binary_f1: 0.930

scrambled 3-seed verazuo_test_only macro F1: mean=0.649 std=0.056 (seeds: 42=0.640, 123=0.722, 456=0.585)
```

---
