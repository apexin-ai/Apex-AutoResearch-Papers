# code exp002 benchmark cf gen

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp002_benchmark_cf_gen_20260521T004552_result.json`
- **Structured JSON:** [`999ee3c77e42a9eaa987.json`](../../sessions/99/999ee3c77e42a9eaa987.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## exp-002 结果报告

### 生成统计
| Benchmark | 输入样本 | 生成完成 | 生成模型 |
|-----------|---------|---------|---------|
| AlpacaEval | 100 | 100/100 | Qwen3-32B (vLLM) |
| MT-Bench | 80 | 80/80 | Qwen3-32B (vLLM) |

### Content Verification（BERTScore ≥ 0.92 AND NLI ≥ 0.90 联合门控）

| Benchmark | 对比类型 | BERTScore (mean±std) | NLI (mean±std) | Joint Pass Rate |
|-----------|---------|---------------------|----------------|-----------------|
| AlpacaEval | Original vs CF | 0.8594 ± 0.1093 | 0.8618 ± 0.3250 | **20/100 (20.0%)** |
| AlpacaEval | Original vs DR | 0.8438 ± 0.1229 | 0.8576 ± 0.3141 | **18/100 (18.0%)** |
| MT-Bench | Original vs CF | 0.8855 ± 0.0900 | 0.9152 ± 0.2469 | **26/80 (32.5%)** |
| MT-Bench | Original vs DR | 0.8842 ± 0.0905 | 0.9579 ± 0.1514 | **26/80 (32.5%)** |

### 关键发现
1. **Pass rate 偏低**：AlpacaEval 20%, MT-Bench 32.5%。BERTScore 均值都低于 0.92 阈值，说明 formality 重写对文本内容改动较大。
2. **NLI 方差极高**：AlpacaEval NLI std 达 0.33，表明部分样本 NLI 接近 0（完全无蕴含），另一部分接近 1。
3. **MT-Bench 优于 AlpacaEval**：可能因为 MT-Bench 响应更结构化，formality 改写更容易保持语义。
4. **DR pass rate ≈ CF pass rate**：双重改写未引入额外的内容偏移，RATE 协议一致性可接受。

### 修复记录
- `content_verification.py` 的 NLI pipeline device 判断有 bug：`device=0 if args.device == "cuda" else -1`，传 `--device cuda:0` 会 fallback 到 CPU。需改为支持 `cuda:N` 格式。
- NLI 模型 `cross-encoder/nli-deberta-v3-large` 在服务器上缓存不完整，通过 hf-mirror.com wget 手动下载 model.safetensors（1.7GB）解决。
- Blackwell GPU 需要 `LD_LIBRARY_PATH` 包含 `/root/miniconda3/lib/python3.12/site-packages/nvidia/cu13/lib` 以解决 libnvrtc-builtins.so.13.0 找不到的问题。

### 输出文件（westb-29275:/root/causal_style_decomp_judge/data/）
- `verified_alpacaeval.jsonl` — 100 records
- `verified_mtbench.jsonl` — 80 records

---
