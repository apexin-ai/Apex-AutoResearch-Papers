# code narrow dual critic implementation

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_narrow_dual_critic_implementation_20260521T074733_result.json`
- **Structured JSON:** [`1b19cdd5715f3b69a1dd.json`](../../sessions/1b/1b19cdd5715f3b69a1dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
NARROW_DUAL_CRITIC: hidden=256, 2× critics, each ~0.525M params, total ~1.050M params
BASELINE_CRITIC: hidden=512, 1× critic, ~1.181M params
RATIO: narrow_dual / baseline = 0.89×
DRYRUN: pass (value1/value2 独立训练，min操作生效，metrics正常)
SYNC_45299: done (md5 一致: f5ad0d44...models.py, 4c009d15...configs.yaml)
STATUS: ready_for_035
```

实现细节：
- `configs.yaml` L65: `narrow_dual_critic: false`
- `models.py`: `self._use_dual_critic` 统一控制 `dual_critic` 和 `narrow_dual_critic` 两条路径
- `narrow_dual_critic=True` 时 `critic_units = config.units // 2 = 256`，两个 critic 均用 256 hidden
- 三组互斥断言：narrow_dual_critic vs wide_critic vs dual_critic
- CLI 用法：`--narrow_dual_critic True`

---
