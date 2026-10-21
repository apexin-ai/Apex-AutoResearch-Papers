# research docred sft data feasibility

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_docred_sft_data_feasibility_20260515T165545_result.json`
- **Structured JSON:** [`623469616773fa7b90e4.json`](../../sessions/62/623469616773fa7b90e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完成。报告：

# 可行性报告

## Part 1: cuda:1 状态 — **不干净**
```
PID    283829, mem=17442 MiB, util=85%, etime=29:39
CMD:   python3 run_constrained_extraction.py --mode full_s1 --dataset docred
       --data_path data/docred/dev.json --device cuda:0 --batch_size 1 --max_new_tokens 4096
```
进程已运行 30 分钟，**不是刚杀掉的残留**——很可能是 W1 DocRED CF-fallback 实验仍在 cuda:1 上跑（命令里写 `--device cuda:0` 但实际显示在 GPU 1，说明启动时设了 `CUDA_VISIBLE_DEVICES=1`）。需 Director 确认：是要保留这个 inference job，还是杀掉？

## Part 2: DocRED SFT 数据生成可行性

### SciERC SFT 格式（已有参考实现）
- 脚本：`scripts/prepare_sft_data_scierc.py`（230 行，结构清晰）
- 训练样本：1762 条 sentence-level（350 docs × ~5 sents，过滤 0-entity 后）
- 格式：`{prompt, completion, doc_id, n_entities, n_relations}` JSONL
- prompt = Qwen3 chat template（system+user, `enable_thinking=False`，含空 `&lt;think>` block）
- completion = compact gold JSON
- **关键设计**：prompt/completion 模板从 `run_constrained_extraction.py` 完全复用（SCIERC_SYSTEM/SCIERC_USER_TEMPLATE），保证 train/eval byte-identical

### DocRED 数据现状
- `train_annotated.json`: 13 MB ≈ 3053 docs（标准 DocRED）
- `dev.json`: 4.3 MB ≈ 1000 docs
- `ontology_constraints_docred.json`: 已有，包含 96 relations + 6 entity types (PER/ORG/LOC/TIME/NUM/MISC) + 训练数据导出的 valid_pairs
- `rel_info.json`: 96 个 P-id → 关系名映射
- `run_constrained_extraction.py:120-160` 已有 `load_docred_data()` 实现 + DocRED prompt builder（document-level, 不分句）

### 适配工作量
**新脚本 `prepare_sft_data_docred.py` 需要做的事**：
1. 复用 `load_docred_data()` 逻辑（直接 import 或拷贝）
2. 复用 `build_messages("docred", ...)` 拼 prompt（已存在）
3. 加载 `ontology_constraints_docred.json` 取 `relation_types` 传给 build_messages
4. 同样的 chat template rendering + compact JSON completion 序列化
5. 同样的 skip-empty 过滤逻辑

**核心 80% 代码可直接复用 SciERC 版本，只换 loader + relation_types 来源。**

### Prompt/Completion 长度预估
| 部分 | 字符 | tokens |
|---|---|---|
| Boilerplate (entity types, schema 提示) | ~500 | ~150 |
| 96 relations list (`- {name}\n`) | ~2400 | ~600 |
| Document text (~200 tokens, doc-level) | ~1000 | ~250 |
| **Prompt total** | | **~1000-1200** |
| Completion: 19 entities + 12 relations gold JSON | ~2800 | ~700-900 |
| **Sample total** | | **~1700-2100** |

### 关键风险
1. **`max_length=2048` 需要上调至 ≥3072（建议 4096）**——SciERC 的 2048 不够 DocRED
2. **训练显存**：seq_len 4096 vs SciERC 的 ~512，per-token 计算量 ~8x。bs=4 grad_accum=4 可能 OOM，建议 bs=2 / grad_accum=8 起步，或先 dry-run 测一下
3. **训练时长**：3053 docs × 3 epochs / (bs=2×ga=8=eff_bs=16) ≈ 572 steps。SciERC 是 1762/16×3≈330 steps 用了 688s。DocRED 序列更长（4x），估计 **40-60 分钟 / single GPU**
4. **数据量充足，无需采样**——3053 docs 比 SciERC 350 大很多，应该能学得更好
5. **96 relations 长 prompt 会放大 violation 的影响**——这正是 composability 评估关心的点，符合 W5 目的

### 预估工作量
- 写 `prepare_sft_data_docred.py`: **0.5h**（复用度高）
- 数据生成运行: **2-3 min**（CPU-bound, tokenizer pass）
- 适配 `train_lora_docred.py`（建议新建而非改 SciERC 版）: **0.5h**（改 data_files 路径 + max_length + 可能调 batch）
- LoRA 训练运行: **40-60 min** 单卡
- merge + 评估: **~10 min**

**总计：~1.5h 开发 + ~1h GPU 时间**

### 建议
**直接适配，无需新方案。** 现有 SciERC pipeline 设计良好，只需要替换数据 loader 和扩大 max_length。建议步骤：
1. 先等 Director 决定 cuda:1 那个 DocRED 进程的去留
2. 起 `prepare_sft_data_docred.py`（基于 SciERC 版改）→ 生成 jsonl
3. dry_run 验证 prompt 渲染正确（特别是 96-relation list 顺序稳定性）
4. 起 `train_lora_docred.py`，先 `--dry_run` 测显存峰值，再正式 3 epochs
5. 评估同 SciERC 流程：unconstrained → full_s1，看 violation 下降

---
