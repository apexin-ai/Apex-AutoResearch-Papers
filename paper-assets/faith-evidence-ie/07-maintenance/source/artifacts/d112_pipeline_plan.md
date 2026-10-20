# D112 Pipeline Plan: RSFT from SFT s44

## 概述
验证 RSFT 在最强 SFT seed（s44, ign_f1=0.4734）上的效果。之前所有 4B RSFT 都基于 SFT s42（最弱 seed, ign_f1≈0.40）。

## 脚本位置
`/root/autodl-tmp/scripts/d112/` 下 4 个脚本

## Pipeline 步骤

### Step 1: 候选生成
**脚本**: `step1_generate_candidates.sh`
**命令**:
```bash
# 4-GPU 并行（推荐，总计约 3-4h）
GPU=0 SHARD=0 bash step1_generate_candidates.sh &
GPU=1 SHARD=1 bash step1_generate_candidates.sh &
GPU=2 SHARD=2 bash step1_generate_candidates.sh &
GPU=3 SHARD=3 bash step1_generate_candidates.sh &
wait

# 或单 GPU（约 12-16h）
GPU=0 bash step1_generate_candidates.sh
```
**参数**: N=8, temperature=0.7, top_p=0.95, batch_size=1, max_new_tokens=1024, seed=42
**输入**: base=Qwen3-4B, adapter=sft_output_seed44, data=DocRED train_annotated (3053 docs)
**输出**: `/root/autodl-tmp/rsft_generations_4b_sft_s44/`
**预估时间**: 4-GPU 并行 ~3-4h, 单 GPU ~12-16h
**GPU**: 每个 shard 1 GPU（4 GPU 最优）

### Step 2: CED 打分 + k=1 筛选
**脚本**: `step2_ced_score.sh`
**命令**:
```bash
GPU=0 bash step2_ced_score.sh
```
**参数**: CED scoring (format_w=0.2, f1_w=0.4, ced_w=0.4), selection_strategy=top_k, k=1, tau=0.5
**NLI 模型**: cross-encoder/nli-deberta-v3-base（HF cache 已有）
**输入**: step1 输出目录（load_generations 自动合并 shard_*/generations.jsonl）
**输出**: `/root/autodl-tmp/rsft_scored_4b_sft_s44/`
**预估时间**: ~30-60 min
**GPU**: 1 GPU（NLI deberta-base 很小）
**预期产出**: ~2700-2800 条训练样本（k=1, 每 doc 最多 1 条）

### Step 3: RSFT 训练
**脚本**: `step3_k1_filter_and_train.sh`
**命令**:
```bash
GPU=0 bash step3_k1_filter_and_train.sh
```
**参数**: lr=2e-5, epochs=3, batch_size=4, grad_accum=4 (eff_batch=16), warmup=100, LoRA r=64 alpha=128 dropout=0.05, QLoRA 4-bit, max_length=2048, seed=42
**输入**: step2 的 rsft_train.jsonl + SFT s44 adapter（merge 后重新 LoRA）
**输出**: `/root/autodl-tmp/rsft_output_4b_sft_s44/`
**预估时间**: ~1.5-2h（~2700 samples, 3 epochs, QLoRA 单卡）
**GPU**: 1 GPU
**W&B run**: d112-rsft-ced-k1-from-sft-s44

### Step 4: 评估
**脚本**: `step4_eval.sh`
**命令**:
```bash
# 先确认 GPU 空闲 (C001)
nvidia-smi
GPU=0 bash step4_eval.sh
```
**参数**: D076 protocol, batch_size=4, max_new_tokens=1024, seed=42, no-quantize (bf16 full precision)
**加载链**: base Qwen3-4B → merge SFT s44 → load RSFT adapter
**输出**: `/root/autodl-tmp/eval_results/d112_rsft_from_sft_s44/`
**预估时间**: ~20-30 min
**GPU**: 1 GPU（eval 前需确认显存空闲 < 2GB, C001）

## 依赖关系
```
Step 1 (生成) → Step 2 (打分) → Step 3 (训练) → Step 4 (评估)
```
Step 1 可 4-GPU 并行加速。Step 2-4 串行，各需 1 GPU。

## 总预估时间
- 4-GPU 生成: ~3-4h + 打分 ~1h + 训练 ~2h + eval ~0.5h = **~6.5-7.5h**
- 单 GPU 全程: ~12-16h + 1h + 2h + 0.5h = **~15.5-19.5h**

## 关键路径验证
| 输入 | 路径 | 状态 |
|------|------|------|
| Base model | /root/autodl-tmp/models/Qwen3-4B | ✅ 存在 |
| SFT s44 adapter | /root/autodl-tmp/sft_output_seed44 | ✅ 存在 |
| DocRED data | /root/autodl-tmp/data/docred | ✅ 3053 docs |
| NLI model | cross-encoder/nli-deberta-v3-base | ✅ HF cache |

## Canonical s42 参数对照
所有超参与 canonical s42 RSFT pipeline 完全一致（参照 rsft_gen_shard0..3.sh + rsft_scored_s0 的 rsft_report.json），仅替换 SFT adapter 路径和输出目录。
