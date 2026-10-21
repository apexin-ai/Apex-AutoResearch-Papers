# fix bootstrap add long suite

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_bootstrap_add_long_suite_20260522T151040_result.json`
- **Structured JSON:** [`ef533a93529970bc899c.json`](../../sessions/ef/ef533a93529970bc899c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**脚本修改完成：**
- `--suite` choices 已添加 `"long"`（L356）
- CKPT 映射已添加 openvla long（L27）和 tracvla long（L37）
- Wrapper 脚本已创建：`run_bootstrap_long_cuda0.sh`（OpenVLA）、`run_bootstrap_long_cuda1.sh`（TracVLA）

**Dry-run 结果 — 两项缺失阻塞 long suite 运行：**

| 缺失项 | 预期路径 |
|--------|---------|
| Long 数据集 | `/root/autodl-tmp/vla-ssd/data/libero/libero_long/` |
| OpenVLA Long checkpoint | `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-long` |

TracVLA long 的 checkpoint 没问题（用通用的 `tracevla-phi3v`）。

**当前 batch 进度：**
- **cuda0**: 仍在运行（bootstrap 10000 iterations 阶段）
- **cuda1**: 已完成，但 `tracvla_object_untrained` 失败 — `DynamicCache.from_legacy_cache` AttributeError（transformers 版本兼容性问题）

---
