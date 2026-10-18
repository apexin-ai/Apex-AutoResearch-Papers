# deploy batch s46 4gpu

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_batch_s46_4gpu_20260528T085356_result.json`
- **Structured JSON:** [`3174a1612b5f7005adb7.json`](../../sessions/31/3174a1612b5f7005adb7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部部署成功。

### 部署结果

| exp_id | GPU | PID | 状态 |
|--------|-----|-----|------|
| eval_pi05_l2norm_k095_long_seed46_strict_w27 | westd-27271 cuda:1 | 616102 | ✅ 已启动 |
| eval_pi05_random_k095_long_seed46_strict_w41 | westd-41074 cuda:0 | 898746 | ✅ 已启动 |
| eval_pi05_random_k05_long_seed46_strict_w41 | westd-41074 cuda:2 | 899098 | ✅ 已启动 |
| eval_pi05_attn_k095_long_seed46_strict_w38 | westd-38929 cuda:3 | 457257 | ✅ 已启动 |

### w41 利用率

| GPU | Util | Memory |
|-----|------|--------|
| 0 | 0% | 1 MiB / 97887 MiB (刚提交，尚未加载) |
| 1 | 36% | 10464 MiB / 97887 MiB |
| 2 | 0% | 1 MiB / 97887 MiB (刚提交，尚未加载) |
| 3 | 0% | 10047 MiB / 97887 MiB |

### w41 现有实验进度

- **random k=0.7 s46** (cuda:1): Task 8, 总进度 288/450=**64.0%**, 134.5min
- **l2norm k=0.85 s46** (cuda:3): Task 3, 总进度 139/150=**92.7%**, 36.5min

---
