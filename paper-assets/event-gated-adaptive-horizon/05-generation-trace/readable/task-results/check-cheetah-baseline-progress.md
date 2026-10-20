# check cheetah baseline progress

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cheetah-baseline-progress_20260517T170416_result.json`
- **Structured JSON:** [`4ad76cbc675632a3166a.json`](../../sessions/4a/4ad76cbc675632a3166a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
023a: step 85K/200K (42.5%), eval@85k = 330.6 (peak 404.2@75k), ETA ~3h
023b: step 125K/200K (62.5%), eval@125k = 537.7 (稳步上升), ETA ~2h
```

两个进程均正常运行，无 error。023b 领先 023a 约 40K steps。

eval_return 趋势：
- **023a**: 338→386→404→331 (85K 有回落)
- **023b**: 457→436→506→538 (稳步提升，表现良好)

---
