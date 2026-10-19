# check exp029 step1 urgent

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp029_step1_urgent_20260516T145902_result.json`
- **Structured JSON:** [`325bf5a36e868b48ecde.json`](../../sessions/32/325bf5a36e868b48ecde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp029 状态汇总

### 进程：**已死** (PID 861524 不存在)

### GPU：**空闲**
```
GPU 0: 0%, 0 MiB
GPU 1: 0%, 0 MiB
```

### W&B Run `x4bbiddh`：**crashed**，运行 4873s (~81分钟)

### 已产出 Metrics（共 2 个 step）：

**Step 0 (初始 eval)：**
| 指标 | 值 |
|------|-----|
| val-env/AlfworldSG/pass@1 | 10.71% |
| val-env/AlfworldSG/success | 10.71% |
| val-core/unknown/reward/mean@140 | 1.0714 |
| val-core/unknown/reward/best@140/mean | 10 |
| val-env/AlfworldSG/action_is_valid | 0.6544 |
| val-env/AlfworldSG/action_is_effective | 1.0 |
| val-env/AlfworldSG/num_actions | 45.33 |
| val-env/response_length | 7023.36 |

**Step 1 (第 1 轮训练后)：**
| 指标 | 值 |
|------|-----|
| train/AlfworldSG/success | 17.19% |
| train/AlfworldSG/pass@8 | 50% |
| train/AlfworldSG/action_is_valid | 0.6878 |
| train/AlfworldSG/action_is_effective | 0.9606 |
| train/AlfworldSG/num_actions | 41.72 |
| train/response_length | 7887.56 |
| critic/rewards/mean | 1.7188 |
| actor/pg_loss | -0.0 |
| actor/entropy | 0.0265 |
| actor/kl_loss | 0.0008 |
| actor/grad_norm | 0.9941 |
| perf/throughput | 452.03 tokens/s |
| perf/time_per_step | 1857s (~31min) |
| timing_s/gen | 1278s |
| timing_s/update_actor | 407.6s |

### 崩溃原因：**磁盘满**
日志末尾显示 `OSError: [Errno 28] No space left on device`，发生在 ALFWorld 环境加载 `fast_downward/libdownward.so` 到 `/tmp/` 时。训练完成 Step 1 后进入第二轮 rollout，ALFWorld 环境初始化写 `/tmp` 失败导致崩溃。

---
