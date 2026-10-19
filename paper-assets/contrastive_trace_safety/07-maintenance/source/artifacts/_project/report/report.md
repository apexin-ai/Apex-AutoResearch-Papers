# OT-7B Bootstrap W-Matching Audit

**Date**: 2026-05-17
**Auditor**: Worker Agent

## Part 1: Current Bootstrap W Configuration

- HS 用的 W: **3** (best_w from Phase 3 temporal probe sweep)
- Text 用的 W: **3** (same best_w passed to `make_text_temporal_features`)
- 判定: **MATCHED**

### 代码证据

`exp_ot7b_full_pipeline.py` line 506, `phase5_bootstrap(train, test, best_layer, best_w)`:
```python
X_train_hs, y_train_hs = make_temporal_features(train, best_layer, best_w)   # W=3
X_train_text, y_train_text = make_text_temporal_features(train, best_w)       # W=3
```

Test predictions also use `best_w` for both:
```python
X_hs = build_window_features_single(hs[:n], best_w, HIDDEN_DIM)    # W=3
X_text = build_window_features_single(emb[:n], best_w, TEXT_DIM)    # W=3
```

`exp_ot7b_continue_p4.py` calls `phase5_bootstrap(train, test, BEST_LAYER=0, BEST_W=3)`.

### "Text best W=25" 的来源

Phase 4 text probe sweep 的独立结果 (not used in bootstrap):
| W | Text bal_acc |
|---|-------------|
| 1 | 0.5810 |
| 3 | 0.5789 |
| 5 | 0.5690 |
| 10 | 0.5826 |
| 15 | 0.5892 |
| 20 | 0.6091 |
| 25 | 0.6141 |

Text best W=25 (bal_acc=0.6141)，但 bootstrap 比较正确使用了 **W=3 for both**，不存在 mismatch。

### Bootstrap 结果 (W=3, 1000 resamples, Bonferroni alpha=0.017)

| Metric | HS | Text | Delta | CI 95% | p-value | Bonf. Sig |
|--------|-----|------|-------|--------|---------|-----------|
| bal_acc | 0.7373 | 0.6558 | +0.0815 | [0.0284, 0.1359] | 0.001 | Yes |
| precision | 0.4249 | 0.3459 | +0.0790 | [-0.0050, 0.1582] | 0.056 | No |
| pre_cp_fpr | 0.1877 | 0.2709 | -0.0832 | [-0.1398, -0.0236] | 0.007 | Yes |

## Part 2: R1-8B Bootstrap Configuration (一致性检查)

### R1-8B 专用 bootstrap (`r1_8b_bootstrap_hs_text.py`)
- HS 用的 W: **15**
- Text 用的 W: **15**
- 是否 matched: **YES**

### 跨模型 bootstrap (`acc_precision_bootstrap/run_bootstrap.py`)
| Model | HS W | Text W | Matched? |
|-------|------|--------|----------|
| R1-8B | 15 | 15 | YES |
| R1-32B | 10 | 10 | YES |
| QwQ-32B | 5 | 5 | YES |

所有模型的 bootstrap 都使用 same-W 进行 HS vs Text paired comparison。**完全一致。**

## Part 3: 补跑结果

**不需要补跑。** 当前 bootstrap 已经是 matched W=3，配置合法。

## Part 4: Layer 0 定义

### OT-7B layer 0 = transformer block 0 output (NOT embedding)

代码证据 (`exp_ot7b_full_pipeline.py` line 101):
```python
hs = hidden_states[layer_idx + 1][0, pos, :]
```

HuggingFace `output.hidden_states` 返回:
- `hidden_states[0]` = embedding output
- `hidden_states[1]` = transformer block 0 output
- `hidden_states[N]` = transformer block N-1 output

`layer_idx + 1` 跳过了 embedding，所以 `layer_idx=0` 对应 `hidden_states[1]` = **transformer block 0 output**。

### 其他模型 layer 0 定义一致性

| File | Indexing | Layer 0 = |
|------|----------|-----------|
| `exp_ot7b_full_pipeline.py` | `hidden_states[layer_idx + 1]` | transformer block 0 |
| `exp_001a_extract_r1_32b.py` | `hidden_states[layer_idx + 1]` | transformer block 0 |
| `exp_001b_extract_qwq.py` | `hidden_states[layer_idx + 1]` | transformer block 0 |
| `src/extract_hidden_states.py` (R1-8B) | `hidden_states[layer_num + 1]` | transformer block 0 |

R1-8B 代码注释明确: "hidden_states[0] = embeddings, hidden_states[i] = layer i output", "hidden_states[layer_num + 1] because index 0 is the embedding"

**所有模型 layer 0 定义一致: transformer block 0 output。**

### Layer Sweep 覆盖范围

| Model | Layers Extracted | Layers Swept | Includes Layer 0 | Best Layer |
|-------|-----------------|-------------|-------------------|------------|
| R1-8B | 12-24 (13 layers) | 12-24 | **NO** | 14 (of 12-24) |
| R1-32B | 0-63 (all 64) | 0-63 | YES | 2 |
| QwQ-32B | 0-63 (all 64) | 0-63 | YES | 1 |
| OT-7B | 0-27 (all 28) | 0-27 | YES | 0 |

### 不一致性 (IMPORTANT)

**R1-8B 是唯一没有提取/扫描 early layers (0-11) 的模型。**

- R1-32B、QwQ、OT-7B 都在 early layers (0-6) 找到最佳信号
- R1-8B 的 "best layer=14" 是 layers 12-24 范围内的最佳，但 early layers 从未被评估
- 如果 R1-8B 也在 early layer 表现最佳，当前报告的 best_layer 和 best_depth 可能不准确
- 这对论文中 "best layer depth %" 的跨模型比较有影响

## 结论

1. **Bootstrap W-matching: PASS** - OT-7B bootstrap 在 W=3 下 HS vs Text 是 matched 的，合法。所有模型的 bootstrap 都使用 same-W。
2. **Layer 0 定义: CONSISTENT** - 所有模型 layer 0 = transformer block 0 output（非 embedding），定义一致。
3. **Layer sweep 覆盖: R1-8B INCONSISTENCY** - R1-8B 仅提取 layers 12-24，无法评估 early layers。其他三个模型都在 early layers (0-6) 找到最佳性能。建议对 R1-8B 补提取 early layers 并重新做 layer sweep，或在论文中注明 R1-8B 的 layer sweep 范围限制。
