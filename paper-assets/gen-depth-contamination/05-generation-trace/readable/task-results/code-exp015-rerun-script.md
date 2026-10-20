# code exp015 rerun script

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp015-rerun-script_20260514T030213_result.json`
- **Structured JSON:** [`512aa6e76aa19c6a41c1.json`](../../sessions/51/512aa6e76aa19c6a41c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

dry-run 通过，参数解析正确。汇报：

**脚本路径**: `/root/autodl-tmp/gen-depth-contamination/scripts/run_exp015_neural_probe.py` (570行，本地+服务器同步)

**新增功能**:

| # | 功能 | 实现方式 |
|---|------|---------|
| 1 | 内存优化 | 三阶段流水线：Phase 1 加载文本 → Phase 2 加载 LLM 提取全部 embeddings → `del llm; gc.collect(); torch.cuda.empty_cache()` → Phase 3 训练 MLP（LLM 已释放） |
| 2 | OOM 自适应 batch | `extract_embeddings` 捕获 `torch.cuda.OutOfMemoryError`，自动减半 batch_size（最小=1），记录实际使用的 batch size |
| 3 | Bootstrap 95% CI | doc-level percentile bootstrap（1000 resamples），对所有 adjacent pairs 计算，输出 `{auc, ci_lower, ci_upper, boot_std}` |
| 4 | Permutation test | 500 permutations，shuffle binary labels，报告 p-value，覆盖全部 adjacent pairs |
| 5 | Peak VRAM logging | 每个 fold 前 `reset_peak_memory_stats()`，fold 后 `max_memory_allocated()` 记录；另外记录 embedding extraction 阶段的 peak VRAM |

**新增参数**: `--bootstrap_resamples 1000` `--permutation_resamples 500`

**命令行兼容**:
```bash
python scripts/run_exp015_neural_probe.py --device cuda:0 --embed_batch_size 16 \
  --data_dir data_exp001_pythia data_exp002_olmo data_exp017_qwen_cont \
  --label Pythia OLMo Qwen-cont
```

**预估 Peak VRAM**:
- Embedding extraction: Qwen2.5-1.5B fp16 ~3GB model + batch_size=16×max_length=512 的 KV cache/activations ≈ **5-7 GB**
- MLP training (LLM 已释放): MLP <10MB + embeddings in CPU numpy，GPU 仅放 MLP 参数+mini-batch ≈ **<500 MB**
- 总计 peak ≈ **5-7 GB**，24GB RTX 4090D 独占时绰绰有余

---
