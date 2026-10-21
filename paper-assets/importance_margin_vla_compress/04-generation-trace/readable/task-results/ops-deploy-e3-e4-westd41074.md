# ops deploy e3 e4 westd41074

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy_e3_e4_westd41074_20260523T065238_result.json`
- **Structured JSON:** [`19e320d5f68665898594.json`](../../sessions/19/19e320d5f68665898594.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都已完成。

---

## 结果汇总

### E3: Token Cosine Similarity

| Model | CV | #Tokens | MeanCosSim | Std | Min | Max |
|-------|-----|---------|-----------|------|------|------|
| π0.5 | 0.055 | 512 | **0.9545** | 0.0174 | 0.8511 | 0.9992 |
| SmolVLA | 0.314 | 128 | **0.7224** | 0.1413 | 0.1482 | 0.9710 |

验证了核心论点：低 CV → 高 cosine similarity（token 同质化），高 CV → 低 similarity（token 分化）。

产出：`artifacts/token_cosine_similarity.{pdf,png,json,npz}`

### E4: Inference Latency

**SmolVLA** (128 tokens, 1264 MB):
| keep_ratio | tokens | latency (ms) |
|-----------|--------|-------------|
| 1.00 | 128→128 | 164.77±5.85 |
| 0.95 | 128→120 | 162.25±2.46 |
| 0.90 | 128→114 | 164.46±3.11 |
| 0.70 | 128→88 | 163.01±2.19 |
| 0.50 | 128→64 | 162.98±1.78 |

**π0.5** (768 tokens, ~9500 MB):
| keep_ratio | tokens | latency (ms) |
|-----------|--------|-------------|
| 1.00 | 768→768 | 67.02±1.15 |
| 0.95 | 768→729 | 71.95±0.73 |
| 0.90 | 768→690 | 71.55±0.75 |
| 0.70 | 768→537 | 68.59±2.28 |
| 0.50 | 768→384 | **64.31±0.79** |

产出：`eval_results/inference_latency_all_models.{csv,json}`

### 修复记录
1. `smolvla_base/config.json`: `load_vlm_weights` 改为 false（跳过 VLM backbone 下载）
2. HF cache 补全 SmolVLM2-500M-Video-Instruct 的 preprocessor/tokenizer 配置文件
3. `analyze_token_cosine_similarity.py`: 修复 SmolVLA camera key 映射 + 改用 `predict_action_chunk` 触发 connector hook
4. `measure_inference_latency.py`: `make_pre_post_processors` 改为传 `policy.config` 而非 `policy`

---
