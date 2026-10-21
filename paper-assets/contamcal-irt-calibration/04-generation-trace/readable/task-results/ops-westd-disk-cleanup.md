# ops westd disk cleanup

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-disk-cleanup_20260522T131140_result.json`
- **Structured JSON:** [`55f3110f0a3cbf7d900d.json`](../../sessions/55/55f3110f0a3cbf7d900d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总分析完成。以下是结果：

## 磁盘状态

| 项目 | 大小 |
|------|------|
| 数据盘总量 | 250GB |
| 已用 | 248GB |
| **剩余** | **2.3GB (100%)** |

## 空间占用分布

| 目录 | 大小 |
|------|------|
| models/ (base models) | 131GB |
| exp001/checkpoints/ | 63GB |
| .hf_cache/ | 31GB |
| 其中 Falcon3-7B-Base cache | 14GB |
| 其中 Yi-1.5-9B cache | 17GB |

## save_total_limit 检查

- `save_total_limit = 1`，`save_strategy = "epoch"` — Trainer 只保留最新 1 个 checkpoint，每个 epoch 结束时先存新再删旧。

## 计划清理目标的实际情况

- `/tmp/yi15_dryrun/` — 存在但 **0 字节**
- Falcon3 中间 checkpoint-XXXX/ 目录 — **不存在**，所有 Falcon3 目录都很干净（仅含 lora_adapter/ + .done + train_config.json）
- 所有 checkpoint-XXXX/ 都在 lora_adapter/ 内部，是 Trainer 保存的最终 adapter 权重，不可删

**计划中的清理目标实际释放空间为 0。**

## Yi 训练风险评估

Yi-1.5-9B checkpoint 预计 ~650-800MB（参考 gemma-2-9b 为 652MB/checkpoint）。save_total_limit=1 下 epoch 切换时峰值 ~1.3-1.6GB（新旧共存）。2.3GB 剩余可以勉强完成，但余量仅 ~700MB，有风险。

## 建议

**最大可清理目标：Falcon3-7B-Base HF cache（14GB）**

路径：`/root/autodl-tmp/.hf_cache/Falcon3-7B-Base/`

Falcon3 所有 4 个 dosage（d000/d005/d025/d050）训练已完成（.done 标记），LoRA adapter 已保存。这 14GB 是基座模型缓存，未来 eval 时可重新下载。Yi-1.5-9B cache（17GB）正在被训练进程使用，不可删。

**是否删除 Falcon3 cache？** 这不在原始计划中，需要你确认。

---
