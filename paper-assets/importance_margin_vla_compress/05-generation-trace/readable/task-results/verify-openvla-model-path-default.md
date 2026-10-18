# verify openvla model path default

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_openvla_model_path_default_20260525T003454_result.json`
- **Structured JSON:** [`00edec0095d84e76e98f.json`](../../sessions/00/00edec0095d84e76e98f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**确认：这 4 个实验全部用错了模型。**

日志铁证——所有实验都打印了：
```
[*] Loading OpenVLA from: /root/autodl-tmp/openvla-libero-object
```

具体情况：

| 实验 | --suite | 加载的模型 | 应该用的模型 |
|------|---------|-----------|------------|
| attn_k085_goal_seed42 | libero_goal | `openvla-libero-object` ❌ | `openvla-7b-finetuned-libero-goal` |
| attn_k085_spatial_seed42 | libero_spatial | `openvla-libero-object` ❌ | `openvla-7b-finetuned-libero-spatial` |
| random_k09_goal_seed42 | libero_goal | `openvla-libero-object` ❌ | `openvla-7b-finetuned-libero-goal` |
| random_k09_spatial_seed42 | libero_spatial | `openvla-libero-object` ❌ | `openvla-7b-finetuned-libero-spatial` |

**根因**：`eval_openvla_l2norm_libero.py` 中 `CHECKPOINT_PATH` 和 `UNNORM_KEY` 是模块级常量，硬编码为 `libero_object`。`parse_args()` 没有 `--model_path`/`--unnorm_key` 参数，也没有 suite→model 的映射逻辑。不管 `--suite` 传什么，永远加载 object 模型。

**结论**：westd-38929 上这 4 个 goal/spatial 实验的结果无效，需要 kill 后修改脚本重跑。另一台服务器上如果也有类似实验，同样无效。

---
