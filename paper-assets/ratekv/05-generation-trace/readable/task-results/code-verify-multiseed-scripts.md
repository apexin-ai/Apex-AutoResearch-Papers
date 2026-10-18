# code verify multiseed scripts

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify_multiseed_scripts_20260516T064828_result.json`
- **Structured JSON:** [`fe4740ca9d038e9eeb9a.json`](../../sessions/fe/fe4740ca9d038e9eeb9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 dry-run 全部通过。汇报：

---

**Yi-1.5-9B**: 就绪
- 模型文件存在，k=2 (max_2bit=2)，gemma2=False
- dry-run PASS：3 seed 产生不同 calibration，同 seed 可复现

**Gemma-2-9B**: 就绪
- 模型文件存在，k=8 (max_2bit=8)，gemma2=True
- BOS prepend 逻辑完整（L174-213），`evaluate_perplexity_gemma2` 内置
- `patch_attention_gemma2` 从 `run_gemma2_full_pipeline.py:40` 导入，文件存在
- dry-run PASS

**CUDA device fix**: 已有
- L340: `os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)` 在任何 CUDA 操作前设置
- L341: `device = "cuda:0"` 始终用 cuda:0
- 不会出现 Mistral v1 的 cuda:N 越界问题

**推荐启动命令**:
```bash
# Yi 3-seed (k=2)
nohup python run_multi_seed_ppl.py --model yi --gpu 0 --batch-size 8 > /root/ratekv/logs/yi_multi_seed.log 2>&1 &

# Gemma-2 3-seed (k=8) — 等 Yi 跑完或用另一块 GPU
nohup python run_multi_seed_ppl.py --model gemma2 --gpu 0 --batch-size 8 > /root/ratekv/logs/gemma2_multi_seed.log 2>&1 &
```

默认 seeds=42,123,456，无需额外指定。两个都用 `--batch-size 8` 更安全（9B 模型 + profiling 显存开销大）。

---
