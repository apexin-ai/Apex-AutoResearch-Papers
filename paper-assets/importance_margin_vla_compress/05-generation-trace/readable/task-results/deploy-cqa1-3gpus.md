# deploy cqa1 3gpus

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1_3gpus_20260527T080616_result.json`
- **Structured JSON:** [`6f64056223932d16e433.json`](../../sessions/6f/6f64056223932d16e433.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU0 正在加载模型，启动正常。

**部署结果：**

| 实验 | GPU | 状态 |
|------|-----|------|
| `eval_pi05_random_k07_long_seed42_strict` | GPU0 | ✅ 已提交, pid=102057, 模型加载中 |
| `eval_pi05_random_k05_long_seed42_strict` | GPU1 | ❌ 被 OpenVLA Attn k=0.95 Goal v2 占用, ~4h 后释放 |
| `eval_pi05_l2norm_k095_long_seed42_strict` | GPU2 | ❌ 被 π0.5 L2norm k=0.85 strict 占用, ~6-8h 后释放 |

Registry 中无 `eval_pi05_l2norm_k095_long_seed42_strict` 条目，可直接创建。

**时间估算**（距截止 ~24h）：
- GPU1 空出 ~4h + 实验 ~8h = ~12h → 充裕
- GPU2 空出 ~8h + 实验 ~8h = ~16h → 可行

**选项：**
1. 等 GPU1/GPU2 自然释放后自动部署（时间足够）
2. Kill GPU1/GPU2 现有实验立即部署（会丢失 OpenVLA Goal 数据和 k=0.85 strict 数据）
3. 部署到 westd-27271 或其他有空闲 GPU 的服务器

怎么处理？

---
