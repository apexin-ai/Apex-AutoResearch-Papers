# submit v5 s015 s025

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_v5-s015-s025_20260514T013032_result.json`
- **Structured JSON:** [`676f7d29f7ca8fa7500c.json`](../../sessions/67/676f7d29f7ca8fa7500c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出

### GPU 状态（提交前）
```
0, 27719 MiB, 78 %   ← cuda:0 在跑 v5_s020
1, 27719 MiB, 74 %   ← cuda:1 在跑 v5_s030
2, 0 MiB, 0 %        ← 空闲 ✓
3, 0 MiB, 0 %        ← 空闲 ✓
```

### 修复代码确认
- Commit: `20182ec fix: NaN layer skip + position normalization + robust II statistics`
- `torch.isnan` → line 339
- `position_counts` normalization → lines 282-283

### 提交结果
| 实验 | tmux session | GPU | 显存占用 | 状态 |
|------|-------------|-----|---------|------|
| mvp_v5_fixed_s015 (s=0.15) | `mvp_v5_s015` | cuda:2 | 15295 MiB | 正在处理 [1/50] |
| mvp_v5_fixed_s025 (s=0.25) | `mvp_v5_s025` | cuda:3 | 15275 MiB | 正在处理 [1/50] |

4 张 GPU 全部在跑，各跑一个进程，无冲突。Registry 状态已推进至 RUNNING。

---
