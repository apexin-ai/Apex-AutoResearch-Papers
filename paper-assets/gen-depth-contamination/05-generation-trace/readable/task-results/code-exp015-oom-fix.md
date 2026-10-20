# code exp015 oom fix

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp015-oom-fix_20260515T043946_result.json`
- **Structured JSON:** [`e0bbbcbf3fababd59328.json`](../../sessions/e0/e0bbbcbf3fababd59328.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。以下是完整产出。

---

## 1. OOM 瓶颈分析

**原因**：并发执行。exp-006 占 15.2GB + exp-015 embedding extraction ~5-9GB > 24GB。

代码本身的 v2 设计已经是"先提取 embedding 再释放 LLM"，对单模型已够用。真正缺失的是：
- **不支持多模型**：`--model_path` 只接受一个值，无法一次跑 3 个模型族
- **无法 sequential 加载/释放**：如果手动跑 3 次，结果会覆盖（同一个 output 文件）

## 2. 修复措施

| # | 改动 | 原因 |
|---|------|------|
| 1 | `--model_path` 改为 `nargs="+"`, 与 `--data_dir`/`--label` 1:1 配对 | 支持 3 个模型族一次跑完 |
| 2 | 按 model_path 分组，sequential 加载 → 提取 → 释放 → 下一个 | 任意时刻 GPU 上只有 1 个 LLM |
| 3 | `embed_batch_size` 默认 16→8 | 24GB 安全余量 |
| 4 | `extract_embeddings` 中加 `del inputs, out, hidden, mask, pooled` | 减少 batch 间 peak VRAM |
| 5 | 加 `log_gpu_mem()` 在模型加载后/释放后/MLP 训练前 | 可观测性 |
| 6 | CUDA 调用改用 `device.startswith("cuda")` 守卫 | 修复 `--device cpu` dry-run crash |
| 7 | `device_map` 根据 device 选择 `"auto"` 或 `"cpu"` | 同上 |
| 8 | 结果中加 `model_path` 字段 | 区分不同模型族的结果 |

## 3. 关键代码差异

**argparse** (旧 → 新):
```python
# 旧: 单一模型
--model_path  type=str, default="...Qwen..."
# 新: 多模型, 与 data_dir/label 配对
--model_path  type=str, nargs="+", default=[Pythia, OLMo, Qwen]
```

**main() Phase 2** (旧 → 新):
```python
# 旧: 一个 LLM 处理所有 dataset
llm = AutoModelForCausalLM.from_pretrained(args.model_path, ...)
for ds in dataset_info:
    emb = extract_embeddings(llm, ...)
del llm

# 新: 按 model 分组, sequential 加载/释放
for model_path, datasets in model_groups.items():
    llm = AutoModelForCausalLM.from_pretrained(model_path, ...)
    for ds in datasets:
        emb = extract_embeddings(llm, ...)
    del llm, tokenizer; gc.collect(); torch.cuda.empty_cache()
```

## 4. Dry-run 结果

**配置**: Pythia-1.4B, 5 samples/depth, max_depth=2, batch_size=2, GPU (与 exp-006 共存)

| 阶段 | Peak VRAM |
|------|-----------|
| 模型加载 | 2.63 GB |
| Embedding extraction | 2.91 GB |
| 模型释放后 | 0.01 GB |
| MLP training | 40.8 MB |

**独占 GPU 预估** (batch_size=8, 30K samples, max_length=512):

| 模型 | Weight (fp16) | hidden_dim | 预估 Peak VRAM |
|------|--------------|------------|---------------|
| OLMo-1B | ~2.0 GB | 2048 | ~5-7 GB |
| Pythia-1.4B | ~2.6 GB | 2048 | ~6-8 GB |
| Qwen2.5-1.5B | ~3.0 GB | 1536 | ~7-9 GB |

三个模型 sequential 处理，任意时刻 peak < 10GB，远低于 24GB 上限。即使 batch_size=8 偶尔 OOM，自动减半机制兜底。

## 5. 推荐运行命令

```bash
# 确保 exp-006 已结束或不再占 GPU
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/gen-depth-contamination

# 3 个模型族 full run (默认参数即可)
nohup python3 scripts/run_exp015_neural_probe.py \
  > ~/runs/gen-depth-contamination/exp015_v3.log 2>&1 &

# 或者更保守 (batch_size=4):
nohup python3 scripts/run_exp015_neural_probe.py \
  --embed_batch_size 4 \
  > ~/runs/gen-depth-contamination/exp015_v3.log 2>&1 &
```

脚本备份在 `scripts/run_exp015_neural_probe_v2_backup.py`。

---
