# research 4b rsft canonical path

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_4b_rsft_canonical_path_20260519T131522_result.json`
- **Structured JSON:** [`3a9358350289bffdcaf7.json`](../../sessions/3a/3a9358350289bffdcaf7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告：4B RSFT s42 Canonical Checkpoint 搜索结果

### 所有 rsft_output 目录汇总

| 目录 | 基础模型 | Seed | Adapter 大小 | 时间戳 | Checkpoints |
|------|---------|------|-------------|--------|-------------|
| `rsft_output_ced_s43` | Qwen3-4B | **43** | 528MB | **May 16**（最早） | 350, 400, 450, 500, 510 |
| `rsft_output_qwen3_1_7b_k1` | Qwen3-1.7B | 42 | 278MB | May 18 15:38 | 550, 567 |
| `rsft_output_llama_3_1_8b_k1` | Llama-3.1-8B | 42 | 671MB | May 18 16:06 | 1100, 1107 |
| `rsft_output_qwen3_8b_k1` | Qwen3-8B | 42 | 698MB | May 18 16:11 | 1100, 1134 |
| `rsft_output_random_k1` | Qwen3-4B | **42** | 528MB | May 19 00:10 | 1000, 1020 |
| `rsft_output_4b_sft_s44` | Qwen3-4B | 42 | 264MB | May 19 15:28 | 400-567 |
| `rsft_output_4b_sft_s44_bf16` | Qwen3-4B | — | symlinks→567 | May 19 21:02 | 400-567 |
| `rsft_output_qwen3_1_7b_k1_s43` | Qwen3-1.7B | — | — | — | — |
| `rsft_output_qwen3_1_7b_k1_s44` | Qwen3-1.7B | — | — | — | — |
| `rsft_output_qwen3_8b_k1_s43` | Qwen3-8B | — | — | — | — |
| `rsft_output_qwen3_8b_k1_s44` | Qwen3-8B | — | — | — | — |
| `rsft_output_llama_3_1_8b_k1_s43` | Llama-3.1-8B | — | — | — | — |

### 结论：Canonical 4B RSFT s42 checkpoint **不存在**

服务器上没有找到符合 "4B + CED scoring + seed 42 + s42 SFT adapter" 的目录。不存在 `rsft_output/`（无后缀）或 `rsft_output_qwen3_4b_k1/`。

**最接近的两个候选都不匹配：**

1. **`rsft_output_ced_s43`** — 4B + CED scoring，但 `training_args` 确认 seed=**43**（不是 42）。这是最早的目录（May 16），时间上确实是第一个 RSFT 实验。
2. **`rsft_output_random_k1`** — 4B + seed=42，但脚本注释明确说是 "Random RSFT k=1 baseline (Claim 3 ablation: random vs CED scoring)"，训练数据来自 `rsft_random_k1/rsft_train.jsonl`，不是 CED 数据。

**其他线索：**
- `eval_test_set.sh` 引用 `rsft_output_s43`（已不存在，大概率是 `rsft_output_ced_s43` 改名前的路径），注释写的是 "RSFT-CED s43, dev rel_f1=0.4683"，说明项目把 s43 当作 4B 的 canonical 结果用于 test set 提交。
- 其他 scale 的 canonical s42 命名是 `rsft_output_{model}_k1`（无 seed 后缀），4B 没有对应目录。
- `rsft_trainer.py` 的 `--output_dir` 是 required 参数，默认示例是 `./rsft_output`，但没有找到这个路径。

**推测：** 原始 4B s42 CED RSFT 可能从未被训练过（项目最早的实验直接用了 seed=43），或者输出目录已被删除/覆盖。项目实际上用 `rsft_output_ced_s43`（seed 43）作为 4B 的 canonical 结果。

---
