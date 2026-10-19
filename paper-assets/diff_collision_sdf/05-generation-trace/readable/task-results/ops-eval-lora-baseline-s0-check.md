# ops eval lora baseline s0 check

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval_lora_baseline_s0_check_20260526T015751_result.json`
- **Structured JSON:** [`f1ecf2c585539facf0de.json`](../../sessions/f1/f1ecf2c585539facf0de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

1. **失败** — `KeyError: 'safelibero_object'`。模型加载成功（LoRA 注入完成），但 `libero` 包的 `BENCHMARK_MAPPING` 中没有 `safelibero_object` 这个 key，在启动 episode 前就崩溃了。无输出 JSON 文件。
2. **原因**：westd-45947 上的 libero 包可能缺少 SafeLIBERO benchmark 注册（其他服务器上可能有自定义注册代码但这台没同步）。
3. **Registry** 已更新：status=DONE, conclusion=failed, notes 记录了失败原因。
4. **Cron** 不存在（可能已被删除或在其他 session 创建），无需删除。

需要重跑的话，先检查 westd-45947 上 libero 包是否注册了 `safelibero_object` benchmark，或将 colliforce-vla 中的自定义 benchmark 注册代码同步过去。

---
