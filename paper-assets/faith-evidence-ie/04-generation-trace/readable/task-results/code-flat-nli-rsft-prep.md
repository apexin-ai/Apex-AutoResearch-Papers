# code flat nli rsft prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_flat_nli_rsft_prep_20260515T131149_result.json`
- **Structured JSON:** [`9bf7b5fa78bd85443279.json`](../../sessions/9b/9bf7b5fa78bd85443279.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。

---

## 汇总

### 1. flat-NLI 模式支持状态

**当前不支持**，但改动很小（~15 行）。

**现状**：
- `rsft_score_filter.py` 硬编码调用 `ced_model.compute_ced_reward(claim, cited_sents, hard_neg_sents, tau)` → contrastive margin: `R = max(0, p_pos − p_neg) × I(p_pos > τ)`
- 无 `--scoring_mode` 参数，无 `flat_nli` 引用

**已有基础**：
- `ced_reward.py` 底部已有 `compute_flat_nli_reward(claim, cited_evidence_sents, tau)` 方法 → `R = p_pos × I(p_pos > τ)`，只需 1 次 NLI 推理，不需 hard negatives

**改动方案**（4 处，不新建文件）：

| 位置 | 改动 |
|------|------|
| `rsft_score_filter.py` argparser (~L540) | 新增 `--scoring_mode {ced,flat_nli}` 参数，默认 `ced` |
| `compute_ced_reward_for_record()` (~L98-160) | `if scoring_mode == "flat_nli"`: 调用 `ced_model.compute_flat_nli_reward()` 代替 `compute_ced_reward()`，跳过 hard_neg 查找 |
| `score_all_records()` (~L320) | 透传 `scoring_mode` 参数 |
| `main()` (~L560) | 传 `args.scoring_mode` |

### 2. 数据复用

**确认可复用**。

- `generations.jsonl`：21968 条，207MB，包含 `parsed_triples / gold_triples / sents` — flat-NLI 打分所需字段齐全
- 只需重新打分 + 筛选，不需要重新生成

### 3. GPU 时间估算

| 阶段 | 估算 | 依据 |
|------|------|------|
| flat-NLI scoring (21968 samples) | **~3-4 min** | CED scoring (同样 21952 samples) 耗时 ~6 min（`mvp2_rsft_ced_scoring`: 05:27→05:33）；flat-NLI 省去所有 hard_neg 推理，约快 40-50% |
| RSFT training | **~2h (1ep) / ~6h (3ep)** | top_k=3 选出 ~8000 samples；r1 (2718 samples, 3ep) = 2h；r2a (2548 samples, 1ep) 效果与 r1 持平，推荐 1ep |
| Eval (985 docs) | **~1.7h** | r2a eval: 5967s, r2b eval: 5862s |
| **总计** | **~4h (1ep 方案)** | scoring 5min + training 2h + eval 1.7h |

### 4. 阻塞项

**无硬阻塞**。唯一前置：`rsft_score_filter.py` 的 ~15 行改动。数据、模型（NLI DeBERTa-v3-base 已缓存）、GPU 基础设施全部就绪。

---
