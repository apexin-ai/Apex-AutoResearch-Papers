# prep qwen15b experiments

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_qwen15b_experiments_20260523T064539_result.json`
- **Structured JSON:** [`69fc16ae3d89a2ad69ed.json`](../../sessions/69/69fc16ae3d89a2ad69ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。汇总如下：

---

## 产出清单

### 模型
- **路径**: `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B-Instruct`
- **规格**: hidden_size=1536, 28 layers, 12 heads, model_type=qwen2
- **磁盘**: 2.9GB（数据盘，213GB 可用）

### 脚本

| 脚本 | 行数 | 用途 |
|------|------|------|
| `scripts/qwen15b_phase1_diag.sh` | 27 | Phase 1 GAR 诊断，复用 `run_phase1_gar_llama.py`，5 conversations × 10 turns |
| `scripts/qwen15b_tg_train.sh` | 30 | TG v7 训练，batch_size=4 grad_accum=2（等效 batch=8），seed=42，3 epochs |
| `scripts/qwen15b_eval.sh` | 178 | Base + TG eval，N=50，AR mode，beta=0/3/5，含 bootstrap CI + Wilcoxon |

### Dry-run 验证
- `bash -n` 语法检查：3 个脚本全部通过
- 模型配置读取：通过（CPU 加载 AutoConfig）
- 数据文件：`data/ultrachat_8k/`（61MB）和 `data/eval_200/eval_200.json`（1.2MB）均存在

### 预估 GPU 时间
- **Phase 1 诊断**: ~5-8 min（1.5B 比 7B 快 ~4x，生成 5 conversations + GAR 测量）
- **TG 训练**: ~45 min - 1h（8k 样本 × 3 epochs，batch=4，1.5B 显存需求低）
- **Eval**: ~30-40 min（50 conversations × 2 conditions × 3 beta，AR gen mode）

### 磁盘
- 根分区：17G/30G used（55%）
- 数据盘：38G/250G used（15%）

### 注意
- 训练脚本 batch_size=4, grad_accum=2（等效 global batch=8），比 7B 的 batch=1×accum=8 吞吐更高
- 训练超参（gar-target=0.5, lambda-gar=1.0, init-bias=1.5, gate-lr-multiplier=10）与 7B TG s123 保持一致
- GPU 当前被 SS s456 占用，脚本就绪待排队

---
