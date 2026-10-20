# code exp001b resampling

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp001b_resampling_20260521T075426_result.json`
- **Structured JSON:** [`30479d55e36925fb9ba3.json`](../../sessions/30/30479d55e36925fb9ba3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-001b 已启动并验证正常运行。总结：

**已完成：**
- `scripts/sample_resampling.py` — 生成了 3 组互不重叠的 200-item 样本（每组 10 subjects × 20 items），与 exp-001 也零重叠
  - `data/mmlu_items_exp001b_sample{1,2,3}.json`
- `scripts/generate_exp001b_design.py` — 3 组 × 432 conditions（1 model × 1 precision × 3 temps × 6 prompts × 6 seeds × 4 orderings）
  - `results/exp001b/sample{1,2,3}/design.csv`
- `scripts/run_exp001b.sh` — 主控脚本，3 组串行执行，每组 4 GPU 并行

**当前状态：**
- Master PID: `112600`
- Sample1 正在跑：GPU 0-3 PID `112700-112703`
- 4 GPU 均 ~88GB VRAM, 97-100% 利用率
- Shard 0 已完成 ~3 conditions（600 records / 21,600 target），输出格式与 exp-001 一致
- Few-shot 复用 `data/few_shot_exp001.json`（dev split 数据，与 test items 无关）

**预计时间：** 每组 ~1.5h，3 组串行约 4.5h。完成后各组自动合并为 `results/exp001b/sample{1,2,3}/all_results.jsonl`。

---
