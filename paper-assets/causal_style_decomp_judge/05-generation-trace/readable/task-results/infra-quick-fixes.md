# infra quick fixes

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_quick_fixes_20260520T094856_result.json`
- **Structured JSON:** [`f4541014214ef77f8f3b.json`](../../sessions/f4/f4541014214ef77f8f3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline uses `cross-encoder/nli-deberta-v3-large` (HF name) but online resolution fails on AutoDL. The model loads fine from local path `/root/autodl-tmp/models/nli-deberta-v3-large/`. This needs a path update in the code or an HF cache symlink — flagging it below.

---

### 产出汇报

**1. NLI 模型: ✅**
- model.safetensors 1.74GB 已下载到 `/root/autodl-tmp/models/nli-deberta-v3-large/`
- 验证加载成功: **435.1M params**, tokenizer 正常
- ⚠️ `content_verification.py:127` 使用 HF 名 `cross-encoder/nli-deberta-v3-large`，AutoDL 网络无法在线解析。需改为本地路径 `/root/autodl-tmp/models/nli-deberta-v3-large` 或建 HF cache symlink

**2. ATE 方向修复: ✅ 已确认**
- 服务器 `ate_analysis.py` L31-47 已包含 `is_casual`/`score_formal`/`score_casual`/`np.where(is_casual, ...)` 方向统一逻辑

**3. Qwen3-32B: 🔄 下载中**
- 进程活跃，正在并行下载 shards 5-7 of 17
- shard 5: 60%, shard 6: 72%, ~1.1 MB/s
- 目标目录 `/root/autodl-tmp/models/Qwen3-32B/` 暂为空（ModelScope 下载完成后统一移入）
- 预计还需数小时

**4. data_prep.py URL: ✅ 已同步**
- 本地和服务器 BASE_URL 完全一致: `https://raw.githubusercontent.com/princeton-nlp/LLMBar/main/Dataset/LLMBar/Adversarial`
- 无需修改

---
