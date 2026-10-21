# research nli ablation prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_nli_ablation_prep_20260518T024839_result.json`
- **Structured JSON:** [`125fd4abbb87c334fe2d.json`](../../sessions/12/125fd4abbb87c334fe2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息已经足够，汇总报告：

---

## Plan_010 NLI Model Ablation 准备度评估

### 1. 模型可用性

| 模型 | 状态 | 位置 |
|------|------|------|
| `cross-encoder/nli-deberta-v3-base` | **已下载** (715MB) | `/root/autodl-tmp/.hf_cache/hub/models--cross-encoder--nli-deberta-v3-base/` |
| `cross-encoder/nli-deberta-v3-large` | **未下载** | HF cache 中不存在 |

**重要发现：当前代码默认已经是 base，不是 large。**

- `ced_reward.py:22` → `DEFAULT_NLI_MODEL = "cross-encoder/nli-deberta-v3-base"`
- `rsft_score_filter.py:490` → `default="cross-encoder/nli-deberta-v3-base"`
- `ced_reranker.py:286` → `default="cross-encoder/nli-deberta-v3-base"`

也就是说：**plan_010 的 ablation 方向可能需要反过来**——需要下载 large 来对比 base，而非下载 base 来对比 large。

`ced_reranker.py` docstring 中写的 `deberta-v3-large-zeroshot-v2.0` 是 MoritzLaurer 的 zero-shot 分类模型（不是 cross-encoder NLI），只出现在注释示例中，不是当前默认。

### 2. 代码改动量

**零代码改动。** `rsft_score_filter.py` 和 `ced_reranker.py` 都已支持 `--nli_model_path` 参数，直接传 `cross-encoder/nli-deberta-v3-large` 即可切换。

### 3. GPU 时间预估

| 步骤 | base (184M params) | large (~435M params) |
|------|----|----|
| CED NLI scoring | ~15-20 min | ~35-45 min |
| RSFT 训练 | ~2h (不变) | ~2h (不变) |
| Eval | ~1h (不变) | ~1h (不变) |
| **总计** | ~3.5h | ~3.5-4h |

NLI scoring 是 DeBERTa 推理，base→large 约 2-2.5x 慢，但绝对时间不长。RSFT 训练和 eval 与 NLI 模型选择无关。

### 4. 阻塞项

| 阻塞项 | 严重性 | 解法 |
|--------|--------|------|
| `cross-encoder/nli-deberta-v3-large` 未下载 | **中** | 需下载 ~1.7GB；服务器 HuggingFace **网络不可达**（刚确认连接超时），需通过镜像或离线传输 |
| 网络不可达 | **高** | 服务器无法访问 huggingface.co，需要用 `hf-mirror.com` 或手动传模型文件 |

**结论：** 代码 ready，唯一阻塞是服务器无法从 HuggingFace 下载 large 模型。需要配置 HF 镜像（`HF_ENDPOINT=https://hf-mirror.com`）或从外部下载后 scp 上传。

---
