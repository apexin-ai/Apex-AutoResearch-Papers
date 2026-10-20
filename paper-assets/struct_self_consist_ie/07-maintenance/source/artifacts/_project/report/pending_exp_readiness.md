# Pending Experiment Readiness Report

**Date:** 2026-05-15  
**Server:** autodl-5090 (4× RTX 5090 32GB)  
**Disk:** 92GB free on `/root/autodl-tmp/` (64% used)  
**GPU Status:** GPU 0 occupied (30GB used), GPUs 1-3 free

---

## 1. exp_017_llama_conll_n16_r1024 (seed=42)

**状态: ⚠️ 需要运行 — r1024 变体缺失**

- **模型:** ✅ `/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-conll2003-merged/` (15GB)
- **数据:** ✅ `/root/autodl-tmp/struct_self_consist_ie/data/conll2003/` (test.json, train.json, dev.json)
- **代码:** ✅ `run_mvp_pilot.py` 支持 `--dataset conll2003 --subtask ner`
- **已有基础结果:** ✅ `exp_017_llama_conll_n16` (seed=42) 已完成 — greedy F1=0.9267, SJ ρ=0.4642, PASS
- **r1024 输出:** ❌ 无输出目录（registry 状态 PREPARING/killed）

**运行命令:**
```bash
cd /root/autodl-tmp/struct_self_consist_ie
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
python code/run_mvp_pilot.py \
    --model_path checkpoints/llama3.1-8b-conll2003-merged \
    --data_dir data/conll2003 \
    --dataset conll2003 --subtask ner \
    --n_samples 16 --temperature 1.0 --max_tokens 1024 \
    --seed 42 --collect_logprobs \
    --output_dir output/exp_017_llama_conll_n16_r1024
```

**预计运行时间:** ~2-4 小时（3453 instances × N=16, LLaMA-8B 单卡推理）  
**阻塞项:** 无

---

## 2. exp_017_llama_conll_n16_s456_r1024 (seed=456)

**状态: ⚠️ 需要运行 — r1024 变体缺失**

- **模型:** ✅ 同上
- **数据:** ✅ 同上
- **代码:** ✅ 同上
- **已有基础结果:** ✅ `exp_017_llama_conll_n16_s456` (seed=456) 已完成 — greedy F1=0.9267, SJ ρ=0.4552, PASS
- **r1024 输出:** ❌ 输出目录存在但为空（registry 状态 PREPARING/killed）

**运行命令:**
```bash
cd /root/autodl-tmp/struct_self_consist_ie
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
python code/run_mvp_pilot.py \
    --model_path checkpoints/llama3.1-8b-conll2003-merged \
    --data_dir data/conll2003 \
    --dataset conll2003 --subtask ner \
    --n_samples 16 --temperature 1.0 --max_tokens 1024 \
    --seed 456 --collect_logprobs \
    --output_dir output/exp_017_llama_conll_n16_s456_r1024
```

**预计运行时间:** ~2-4 小时  
**阻塞项:** 无

**注:** seed=123 的 r1024 变体 (`exp_017_llama_conll_n16_s123_r1024`) 已完成，有 3453 instances 的完整结果。

---

## 3. exp008_re_n16

**状态: ✅ 已完成（registry 状态过期）**

- **Registry 状态:** PREPARING/killed（过期）
- **实际输出:** 
  - `exp008_re_n16/`: report.json + samples.jsonl (551 instances, SciERC RE, N=16, verdict=MARGINAL)
  - `exp_008_re_n16_v2/`: report.json + run.log + samples.jsonl (551 instances, 完整结果)
  - `exp_008_re_seed123/`: 同样已完成
- **关键指标 (exp008_re_n16):** greedy F1=0.4289, oracle F1=0.6466, SJ ρ_cond=0.3721, logprob ρ=0.3012
- **结论:** 实验已完成，无需重跑。可能需要更新 registry 状态为 DONE。

---

## 4. exp_007_ner_llama

**状态: ✅ 已完成（不同命名）**

- **Registry 状态:** `exp_007_ner_llama` 为 PREPARING/killed（过期），但实际实验以不同命名完成：
  - `exp_007_llama_n16` (seed=42): DONE/success
  - `exp_007_llama_n16_r1024` (seed=42): DONE, 完整结果 (report.json + samples.jsonl + run.log)
  - `exp_007_llama_seed123`: DONE
  - `exp_007_llama_seed456`: DONE
- **结论:** 所有变体已完成，无需重跑。

---

## 5. exp_002_merge_conll2003

**状态: ✅ 已完成（不同命名）**

- **Registry 状态:** `exp_002_merge_conll2003` 为 PREPARING/killed（过期），实际实验已完成：
  - `exp_002_conll_n16` (seed=42): DONE/success
  - `exp_002_conll_n16_r1024` (seed=42): DONE, 完整结果
- **结论:** 已完成，无需重跑。

---

## 综合摘要

| 实验 | 状态 | 可立即运行 | 阻塞项 |
|------|------|------------|--------|
| exp_017 seed=42 r1024 | ⚠️ 缺失 | ✅ 是 | 无 |
| exp_017 seed=456 r1024 | ⚠️ 缺失 | ✅ 是 | 无 |
| exp_017 seed=123 r1024 | ✅ 已完成 | — | — |
| exp008_re_n16 | ✅ 已完成 | — | — |
| exp_007_ner_llama | ✅ 已完成 | — | — |
| exp_002_merge_conll2003 | ✅ 已完成 | — | — |

**需要 GPU 时间的实验:** 2 个（exp_017 seed=42 和 seed=456 的 r1024 变体）  
**预计总 GPU 时间:** ~4-8 小时（可在 2 张空闲 GPU 上并行运行）  
**资源就绪:** 模型、数据、代码均已到位，GPU 1-3 空闲可用

## Checkpoints 清单

| 模型 | 路径 | 大小 |
|------|------|------|
| LLaMA-3.1-8B CoNLL merged | `checkpoints/llama3.1-8b-conll2003-merged/` | 15GB |
| LLaMA-3.1-8B SciERC merged | `checkpoints/llama3.1-8b-scierc-merged/` | — |
| Qwen3-8B CoNLL merged | `checkpoints/qwen3-8b-conll2003-merged/` | — |
| Qwen3-8B SciERC merged (v2) | `checkpoints/qwen3-8b-scierc-merged-v2/` | — |
| Qwen3-8B WNUT17 merged | `checkpoints/qwen3-8b-wnut17-merged/` | — |
