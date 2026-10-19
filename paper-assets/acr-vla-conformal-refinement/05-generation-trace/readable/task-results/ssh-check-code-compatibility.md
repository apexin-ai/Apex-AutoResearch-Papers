# ssh check code compatibility

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-code-compatibility_20260520T060329_result.json`
- **Structured JSON:** [`1a41e7566b45ac4aea3e.json`](../../sessions/1a/1a41e7566b45ac4aea3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报结果：

---

### 1. Spatial Adaptive K: **支持**

- `adaptive_k` 是 `--mode` 的合法选项（line 74），无 benchmark 硬编码限制
- `load_libero_env` 通过 `benchmark_dict` 泛化支持 object/spatial/goal/long/90，adaptive_k 流程不检查 benchmark 类型
- `--adaptive_threshold` 正确传递：line 88 定义 → line 468/473 传入 `select_action_adaptive_k` → line 541 写入 summary
- 输出 JSON 包含 `avg_actual_k` 和 `fast_path_ratio`，但嵌套在 `summary["adaptive_stats"]` 下（非顶层字段）

`python evaluate.py --mode adaptive_k --benchmark spatial` 可以直接用。

---

### 2. Random Selection: **mode 存在，代码运行正常，之前的实验并未 crash**

- `random_selection` 是合法 mode（line 74），对应 `select_action_random` 函数（line 237），action_fn 绑定在 line 483-484
- 之前的运行日志显示实验**正常完成**（EXIT_CODE=0）：
  - seed43: 9.0% (9/100)
  - seed45: 10.0% (10/100)
- 你提到的 `/root/runs/.../eval-random-selection-object-seed46-r2.log` 不存在——该 run 从未被调度。实际存在的是 seed43 和 seed44 的日志
- **"failed" 不是代码错误，大概率是实验调度系统的状态标记问题**（比如 run 未提交或命名不匹配）

---

### 3. Latency Profiling 脚本: **两个文件都存在**

| 文件 | 大小 | 修改时间 |
|------|------|---------|
| `/root/acr-vla-conformal-refinement/src/profile_latency.py` | 14,486 B | May 20 13:52 |
| `/root/acr-vla-conformal-refinement/src/latency_profile.py` | 7,304 B | May 18 02:27 |

`profile_latency.py` 更新、更大，应该是主文件。`latency_profile.py` 可能是旧版本。

---
