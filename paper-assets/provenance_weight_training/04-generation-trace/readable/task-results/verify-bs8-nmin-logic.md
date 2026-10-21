# verify bs8 nmin logic

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_bs8-nmin-logic_20260516T155618_result.json`
- **Structured JSON:** [`5e4a3e8a5df843b2f9a1.json`](../../sessions/5e/5e4a3e8a5df843b2f9a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认完毕。结论如下：

---

## 结果

### 1. n_min auto-compute 逻辑

```python
# Line 280: argparse 定义
parser.add_argument("--n_min", type=int, default=None, ...)

# Lines 331-332: auto-compute
if args.n_min is None:
    args.n_min = max(2, args.batch_size // 2)
```

### 2. 当 batch_size=8 时的计算值

`max(2, 8 // 2) = max(2, 4) = 4` ✓

### 3. bs8_auto_nmin 脚本配置确认

`scripts/run_bs8_auto_nmin_seed42.sh`:
- `--batch_size 8` ✓
- **未传 `--n_min`** ✓（auto-compute 生效）
- `--gradient_accumulation_steps 2`
- 脚本末尾注释也自证：`echo "DONE: bs8_auto_nmin seed42 (n_min auto = max(2, 8//2) = 4)"`

### 4. 潜在风险

无。逻辑清晰，`default=None` + 显式 auto-compute guard 是标准模式。唯一值得注意的是 effective batch size = 8 × 2 = 16（含 gradient accumulation），但 n_min 是基于 per-step batch_size=8 计算的，这是正确行为——n_min 约束的是单步内的有效样本下限。

---
