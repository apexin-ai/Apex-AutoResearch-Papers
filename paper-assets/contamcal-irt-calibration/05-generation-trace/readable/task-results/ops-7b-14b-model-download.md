# ops 7b 14b model download

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_7b-14b-model-download_20260518T061910_result.json`
- **Structured JSON:** [`60ccca52bdda1c02eb24.json`](../../sessions/60/60ccca52bdda1c02eb24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总完毕。

---

## 磁盘空间

| 分区 | 总量 | 已用 | 可用 |
|------|------|------|------|
| `/root` (overlay) | 30G | 19G | 12G |
| `/root/autodl-tmp` | 169G | 119G | **51G** |

需要 ~58GB，缺口 ~7GB。`/root/autodl-tmp` 中可清理候选：

| 目录 | 大小 | 说明 |
|------|------|------|
| `structfuse/` | 13G | 不同项目 |
| `gpt2-ms/` | 4.9G | GPT-2 medium |
| `alfworld_data/` | 2.2G | 不同项目 |
| `exp001/checkpoints/` | 34G | 旧 SFT checkpoints |
| `gpt2-small/` | 478M | GPT-2 small |

清理 `structfuse` + `gpt2-ms` 即可腾出 ~18GB，总可用达 69GB > 58GB。

---

## HF Token

**未找到 HF token**（`/root/.cache/huggingface/token` 不存在）。

- Qwen2.5-7B、Qwen2.5-14B：公开模型，无需 token
- **Llama-3.1-8B：gated model，需要 HF token 才能下载**，否则会报 401

---

## SFT 数据

SFT 训练数据**已存在**于 `/root/autodl-tmp/exp001/sft_data/`：
- `sft_dosage_000.jsonl` ~ `sft_dosage_100.jsonl`（5 个 dosage level）
- `contamination_labels_{mmlu,gsm8k,arc_challenge}_{d005,d025,d050,d100}.json`
- `data_meta.json`
- 另有 QC 过滤版：`sft_data_qc_filtered/`（360MB）

数据是纯文本 SFT 格式，与模型无关，7B/14B/8B 可直接复用。

---

## Evaluation 数据

HF cache 中有 MMLU、GSM8K、ARC 的 dataset metadata（仅指针，实际数据会在首次加载时下载，体积不大）。

---

## 需要你确认的事项

1. **清理哪些目录腾空间？** 建议至少清 `structfuse/`（13G）+ `gpt2-ms/`（4.9G），我不会自行删除。
2. **Llama-3.1-8B 是否需要？** 如果需要，请提供 HF token；或者可以先只下载 Qwen2.5-7B + Qwen2.5-14B（共 ~42GB，当前空间够）。
3. **是否需要保留 `exp001/checkpoints/`（34G）？** 如果这些旧 checkpoint 不再需要，清理后空间非常充裕。

---
