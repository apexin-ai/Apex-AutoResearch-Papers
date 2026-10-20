# check split softmax result

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_split_softmax_result_20260523T074816_result.json`
- **Structured JSON:** [`80cd51ea29023c8099a0.json`](../../sessions/80/80cd51ea29023c8099a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：**FAILED** — 有 critical bug

### 文件状态

| 文件 | 状态 | 备注 |
|------|------|------|
| `base_tf_n50.json` | 已完成 | 但有 bug |
| `tg_s42_v7_tf_n50.json` | 已完成 | 但有 bug |
| `base_gen_n50.json` | 已完成 | 4/5 k 值全 NaN |
| `tg_s42_v7_gen_n50.json` | **运行中** | PID 84029, 已跑 6 min |

### 两个 Critical Bug

**Bug 1: `system_prompt_len=0`（line 373）**
```python
ss.activate(system_prompt_len=0)
```
Split-softmax 标记 0 个 token 为 system prompt → 无 token 被放大 → k 值变化完全无效果。证据：base_tf 和 tg_tf 所有 7 个 k 值的 mid_gar 完全一样：
- base_tf: 全部 = 0.0103
- tg_tf: 全部 = 0.4602

**Bug 2: gen mode 多数 k 值产生 NaN**
base_gen 的 k=0.0/0.3/0.5/0.7 全部 NaN（mid_gar 和 avg_ppl），只有 k=1.0（identity）有效值 0.0186。推测 split-softmax 在 gen 时某处产生 NaN 注意力权重污染了生成。

### TF 数据的残余价值

虽然 split-softmax 没生效，TF 结果相当于 base vs TG 裸对比：
- **Base**: mid_gar=0.0103, PPL=4.34
- **TG (s42_v7)**: mid_gar=0.4602, PPL=2.78
- GAR 提升 ~45x，PPL 降 36%。但这**不是** split-softmax baseline 对比。

### GPU / 磁盘
- GPU **忙**：PID 84029 占用 26.8GB / 97.9GB，59% util
- tg_gen 正在跑但大概率同样有 bug
- 磁盘：17GB / 30GB（55%）

### 建议
1. Kill PID 84029（tg_gen 结果也会有同样问题）
2. 修 `eval_split_softmax.py` line 373：应动态计算每个 conversation 的 system_prompt_len（`get_system_prompt_token_len` 已 import 但未使用）
3. 排查 gen mode NaN 的根因（可能与 k=0 时注意力归一化有关）
4. 重跑全部 4 组

---
