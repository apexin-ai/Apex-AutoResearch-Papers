# verify d112 step3 step4 readiness

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_d112_step3_step4_readiness_20260519T032024_result.json`
- **Structured JSON:** [`7b91f09c75e316c93a22.json`](../../sessions/7b/7b91f09c75e316c93a22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出

### 1. Step 3/4 脚本就绪性

**Step 3** (`step3_k1_filter_and_train.sh`) — 脚本本身 OK，但不能运行：
- 模型路径 `/root/autodl-tmp/models/Qwen3-4B` ✅ 本地，存在
- SFT adapter `/root/autodl-tmp/sft_output_seed44` ✅ 存在（528MB adapter）
- CUDA_VISIBLE_DEVICES ✅ 正确设置（`${GPU:-${CUDA_VISIBLE_DEVICES:-0}}`）
- 无 HuggingFace 模型 ID，全部本地路径
- **阻塞问题**：训练数据 `/root/autodl-tmp/rsft_scored_4b_sft_s44/rsft_train.jsonl` **不存在**（目录为空）。这是 step 2 的输出，step 2 尚未完成。

**Step 4** (`step4_eval.sh`) — 脚本 OK，依赖 step 3 输出：
- 所有模型路径本地 ✅
- Eval 数据 `/root/autodl-tmp/data/docred/` ✅ 存在
- RSFT adapter 路径 `/root/autodl-tmp/rsft_output_4b_sft_s44` — step 3 产出，尚不存在（预期）
- 遵守了 C001（脚本注释提醒 nvidia-smi 检查）

**建议修复**：两个脚本都没设 `export HF_HUB_OFFLINE=1`。虽然路径全是本地的，但 transformers `from_pretrained()` 可能仍尝试连 HF Hub 检查更新。鉴于 step 2 已因 HF 网络不可达失败过，建议在两个脚本的 `export` 区域都加上 `export HF_HUB_OFFLINE=1` 作为安全措施。

### 2. experiment_plan.yaml 中 D112 状态

D112 条目存在（`plan_d112`，line 253），registry_id 为 `d112_rsft_s44_gen_shard0`（对应 step 1 生成阶段）。描述准确。

### 3. 需修复的问题清单

| # | 问题 | 严重度 | 状态 |
|---|------|--------|------|
| 1 | step 2 输出 `rsft_train.jsonl` 不存在，step 3 被阻塞 | 阻塞 | 等 step 2 完成 |
| 2 | step 3/4 缺 `HF_HUB_OFFLINE=1` | 低风险预防 | 建议加上 |

---
