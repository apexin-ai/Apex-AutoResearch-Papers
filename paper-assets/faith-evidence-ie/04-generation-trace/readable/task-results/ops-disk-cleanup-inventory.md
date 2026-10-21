# ops disk cleanup inventory

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk_cleanup_inventory_20260516T095627_result.json`
- **Structured JSON:** [`ad4663bb6c1ae953a742.json`](../../sessions/ad/ad4663bb6c1ae953a742.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry agent 结果已汇入，补充完整报告：

## 完整盘点结果

| 目录 | 大小 | Registry 实验 | 结论 | 最佳 F1 | 建议 |
|------|------|--------------|------|---------|------|
| `grpo_ced_g4_bf16/` | **16G** | `plan_015_grpo_g4_bf16` — killed (GPU 冲突) | 从未完成训练，未评估 | N/A | **可安全删除** |
| `grpo_ced_g8_bf16/` | **16G** | `plan_011_grpo_g8_bf16` + 多次 eval — success | GRPO 最佳结果，+12.1% over SFT | 0.455 | **可安全删除** — eval 全部完成并保存 |
| `dpo_output/` | **7.0G** | `plan_012_dpo_ced` — negative (过拟合) | 3ep 严重过拟合，-15.5% vs SFT | 0.343 | **可安全删除** |
| `dpo_output_1ep/` | **5.0G** | `plan_012_dpo_ced_1ep` — negative | 仅持平 SFT，DPO 方向已关闭 | 0.403 | **可安全删除** |
| `dpo_data/` | **13M** | 训练数据 (dpo_pairs.jsonl) | — | — | **保留** — 极小 |
| `eval_plan_012_dpo_ced/` | **7.5M** | eval 输出 | — | — | **保留** — 极小，含 metrics |

## 决策依据

- **grpo_ced_g4_bf16**：训练因 GPU 冲突被 kill，从未产生有效结果，从未被评估。零价值。
- **grpo_ced_g8_bf16**：是当前 GRPO 最佳模型（F1=0.455），但 eval 结果已完整保存在 `eval_results/grpo_g8_bf16/` 和 `eval_results/grpo_g8_bf16_ckpt100/`。除非需要从该 checkpoint 继续训练或做新 eval，模型文件本身已无用。
- **dpo_output / dpo_output_1ep**：DPO 方向已在 D061 decision 中关闭。结果明确为 negative。

## 磁盘紧迫性

```
/dev/md0  250G  244G  6.1G  98%  /root/autodl-tmp
```

**删除这 4 个目录可回收 ~44G，使用率从 98% 降至 ~80%。**

如确认删除，我可以执行 `rm -rf` 清理。

---
