# research check openvla suite support

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_check-openvla-suite-support_20260520T224913_result.json`
- **Structured JSON:** [`bd02e6c530645d436465.json`](../../sessions/bd/bd02e6c530645d436465.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### eval_openvla_libero.py — 部分支持 suite 切换

**已支持：**
- `--suite` 参数（默认 `libero_object`）
- `SUITE_MAX_STEPS` 覆盖 4 个 suite：`libero_spatial`(280), `libero_object`(280), `libero_goal`(300), `libero_10`(520)
- LIBERO benchmark 加载使用 `benchmark_dict[args.suite]()`，动态切换

**需要修改的 2 个硬编码问题：**

| 行号 | 问题 | 当前值 | 应改为 |
|------|------|--------|--------|
| ~31 | `CHECKPOINT_PATH` 硬编码 | `"/root/autodl-tmp/openvla-libero-object"` | 添加 `--model_path` 参数 |
| ~32 | `UNNORM_KEY` 硬编码 | `"libero_object"` | 从 `dataset_statistics.json` 自动读取（参考 ACIS 脚本: `next(iter(model.norm_stats.keys()))`） |

### eval_openvla_acis_prune.py — 已完全支持

- `--suite` 参数 + `--model_path` 参数（required）
- `unnorm_key` 自动从模型 stats 推断（line 152）
- 无需修改

### eval_openvla_l2norm_libero.py — 不存在

服务器上无此文件。

### 服务器上现有 OpenVLA checkpoint

只有 `/root/autodl-tmp/openvla-libero-object`，其 `dataset_statistics.json` 只包含 `libero_object` 的 stats。要跑其他 suite，需下载对应的 fine-tuned checkpoint（OpenVLA 官方为每个 LIBERO suite 单独发布了 checkpoint）。

### LIBERO 支持的 suite

标准 4 个 suite，每个 10 tasks：
- `libero_spatial` — 空间关系任务
- `libero_object` — 物体操作任务  
- `libero_goal` — 目标导向任务
- `libero_10` (也叫 libero_long) — 长序列任务

### 总结：扩展到全 4 suite 需要

1. **eval_openvla_libero.py**: 加 `--model_path` 参数，UNNORM_KEY 改为自动推断（约 5 行改动）
2. **下载 checkpoint**: `openvla-libero-spatial`, `openvla-libero-goal`, `openvla-libero-10`（HuggingFace `openvla/openvla-7b-finetuned-libero-*`）
3. **eval_openvla_acis_prune.py**: 无需改动，直接可用

---
