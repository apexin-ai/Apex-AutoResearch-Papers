# diagnose dpo data reconstruction

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_dpo-data-reconstruction_20260523T012149_result.json`
- **Structured JSON:** [`19e0c57cfd79c9791cb8.json`](../../sessions/19/19e0c57cfd79c9791cb8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 文件存在性

| 文件/目录 | 路径 | 存在? | 大小/行数 | 说明 |
|-----------|------|-------|-----------|------|
| RSFT generations (4B) | `/root/autodl-tmp/rsft_generations_4b_sft_s44/` | ✅ | 216M, 4 shards, 24216 行 | 含 prompt, output, gold_triples, sents，每 doc 8 candidates |
| CED scores (4B) | `/root/autodl-tmp/rsft_scored_4b_sft_s44/rsft_scores.jsonl` | ✅ | 83M, 24216 行 | 含 ced_reward, f1_reward, combined_score |
| DPO 训练数据 (dpo_pairs.jsonl) | — | ❌ | — | 无任何 dpo*.jsonl 文件 |
| DPO 1ep checkpoint | `/root/autodl-tmp/dpo_output_1ep/` | ❌ | — | 目录已删除 |
| DPO 3ep checkpoint | — | ❌ | — | 从未找到任何 dpo_output 目录 |
| DPO 1ep eval 结果 | `/root/autodl-tmp/eval_results/dpo_ced_1ep_fixed/metrics_v2.json` | ✅ | 1.5KB | F1=40.3, Ign-F1=38.9, evi_f1=80.9 |
| DPO ckpt400 eval 结果 | `/root/autodl-tmp/eval_results/dpo_ced_ckpt400/` | ⚠️ | 空目录 | 目录存在但无文件 |
| SFT adapter (DPO 基座) | `/root/autodl-tmp/sft_output/` | ✅ | ~264MB | adapter_model.safetensors + tokenizer |
| Base model (Qwen3-4B) | `/root/autodl-tmp/models/Qwen3-4B/` | ✅ | ~7.5GB | 完整 |
| DPO data builder 代码 | `/root/autodl-tmp/freige/training/dpo_data_builder.py` | ✅ | 296 行 | 读取 generations + scores → dpo_pairs.jsonl |
| DPO trainer 代码 | `/root/autodl-tmp/freige/training/dpo_trainer.py` | ✅ | ~250 行 | base → merge SFT adapter → 新 LoRA → DPO |

## 重建可行性

**可重建?** YES

**重建步骤：**

1. **合并 generations shards**：`cat /root/autodl-tmp/rsft_generations_4b_sft_s44/shard_*/generations.jsonl > /root/autodl-tmp/rsft_generations_4b_sft_s44/generations.jsonl`

2. **构建 DPO pairs**（~1 分钟，纯 CPU）：
   ```bash
   python -m freige.training.dpo_data_builder \
       --input_dir /root/autodl-tmp/rsft_generations_4b_sft_s44 \
       --scores_path /root/autodl-tmp/rsft_scored_4b_sft_s44/rsft_scores.jsonl \
       --output_dir /root/autodl-tmp/dpo_data \
       --rank_by ced_reward --pair_k 1 --min_margin 0.05
   ```

3. **DPO 训练**（单卡 RTX 5090，1ep 约 1-2 小时；3ep 约 3-5 小时）：
   ```bash
   CUDA_VISIBLE_DEVICES=X python -m freige.training.dpo_trainer \
       --dpo_data_path /root/autodl-tmp/dpo_data/dpo_pairs.jsonl \
       --output_dir /root/autodl-tmp/dpo_output_3ep \
       --num_epochs 3
   ```

4. **Eval**（~1.5 小时）

**预估时间**：数据构建 ~5 分钟 + 训练 3ep ~3-5 小时 + eval ~1.5 小时 = **总计约 5-7 小时**

**预估磁盘**：DPO pairs ~10MB + checkpoint ~500MB = **<1GB**（93GB 可用，充裕）

**注意事项**：
- 需确认原始 DPO 训练的超参数（`--rank_by`, `--pair_k`, `--min_margin`, `--beta`, `--loss_type` 等），可查 wandb 历史 run `freige-dpo` 项目
- 原始 1ep eval 配置记录了 `model_path: /root/autodl-tmp/dpo_output_1ep/`，确认该 run 的超参数以保证可复现性

---
