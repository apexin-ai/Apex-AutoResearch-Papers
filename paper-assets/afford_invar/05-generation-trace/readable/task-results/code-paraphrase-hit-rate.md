# code paraphrase hit rate

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_paraphrase-hit-rate_20260519T222554_result.json`
- **Structured JSON:** [`de6daad47afa5a793a0b.json`](../../sessions/de/de6daad47afa5a793a0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

---

## 1. 训练状态

**Phase 1 训练已崩溃，未进入训练循环。**

- 错误：`unrecognized arguments: --adapter_tmp_dir /root/afford_invar/adapter_tmp`
- 崩溃时间：2026-05-20 06:03:30
- `FinetuneAffordConfig` 没有 `adapter_tmp_dir` 参数，启动命令传了一个脚本不认识的参数

之前的 **dryrun_v3** 成功跑了 10 步（max_steps=10），数据集为 `libero_goal_no_noops`。

## 2. Paraphrase Hit/Miss Rate

**日志中没有 hit/miss rate 信息。** 代码没有打印匹配统计。

### 匹配逻辑分析（`finetune_afford.py:150-162`）

```python
# load_paraphrases: key = entry["original"].lower().strip()
# AffordRLDSBatchTransform: instruction_text = rlds_batch["task"]["language_instruction"].decode().lower()
# 查找: paraphrase_map.get(instruction_texts[b].strip(), [])
# 未命中时: fallback 到 instruction_texts[b] (即重复原始指令)
```

- 匹配方式：**精确字符串匹配**（lowercase + strip）
- paraphrases.json 共 130 个 task（libero_goal 10 个、libero_spatial 10 个、libero_object 10 个等）
- dryrun_v3 日志显示 "Loaded paraphrases for 112 tasks"——这是去重后的 unique original instructions 数量

由于 `load_paraphrases` 和 `AffordRLDSBatchTransform` 都做了 `.lower().strip()`，只要 RLDS 数据中的 `language_instruction` 与 paraphrases.json 的 `original` 字段文本一致（不区分大小写），就能命中。LIBERO 数据集的指令文本是固定的，**理论上 hit rate 应为 100%**（前提是 paraphrases.json 覆盖了所有 task）。

## 3. Dryrun Loss 趋势（最近成功的 10 步）

| Step | L_act | L_consist | L_total |
|------|-------|-----------|---------|
| 0 | 0.5156 | 0.3518 | 0.4616 |
| 5 | 1.2891 | 0.0247 | 1.2074 |
| 10 | 0.9531 | 0.0045 | 0.8642 |

L_consist 快速下降（0.35 → 0.005），说明 paraphrase consistency loss 正常工作，间接验证 paraphrase 匹配在生效。

## 4. 建议

1. **修复启动错误**：从启动命令中移除 `--adapter_tmp_dir` 参数，或在 `FinetuneAffordConfig` 中添加该字段
2. **添加 hit rate 监控**：在 `build_paraphrase_inputs` 中加一个计数器统计 miss 次数，每 N 步打印一次 hit rate，可以明确回答 reviewer 的问题
3. **重新启动训练**

---
