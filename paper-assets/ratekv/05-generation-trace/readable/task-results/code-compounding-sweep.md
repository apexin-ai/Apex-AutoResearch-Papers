# code compounding sweep

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_compounding_sweep_20260514T002939_result.json`
- **Structured JSON:** [`d8afde5c652ecd52197a.json`](../../sessions/d8/d8afde5c652ecd52197a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。完整结果：

```
max_2bit     PPL    n_2bit  n_4bit  n_8bit  n_16bit  mem_ratio
       0   15.45        0     112       0        0     0.2500
       4   11.77        4     106       2        0     0.2500
       8   11.23        8     100       4        0     0.2500  ← optimum
      16   11.81       16      92       2        2     0.2500
      24   13.14       24      84       0        4     0.2500
      48   22.88       48      56       0        8     0.2500
      75   35.35       75      25       0       12     0.2467
     112   35.35       75      25       0       12     0.2467
```

**分析：**

1. **Compounding threshold 在 max_2bit=8**。这是 PPL 最低点 (11.23)，与 exp_c 完美吻合。

2. **U 型曲线**：太少 2-bit head (0) 等价于 uniform 4-bit (15.45)；太多则 compounding effect 导致崩溃。

3. **拐点在 24→48**：PPL 从 13.14 跳到 22.88 (+74%)，这是最大恶化区间。

4. **max_2bit=112 饱和在 75**：即使允许全部 112 heads 用 2-bit，solver 只选了 75 个（剩余 head 的 2-bit distortion 太高不值得选），PPL=35.35 接近 exp_b 的 36.92。

5. **Sweet spot: 4-8 个 2-bit head**。Solver 用这些 head 省下的 memory budget 分配给其他 head 升到 8-bit，整体 PPL 显著优于 uniform 4-bit。

---
