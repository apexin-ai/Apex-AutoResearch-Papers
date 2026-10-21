# check c4 analysis compatibility

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_c4_analysis_compatibility_20260517T171021_result.json`
- **Structured JSON:** [`755fe66cdf734cff756f.json`](../../sessions/75/755fe66cdf734cff756f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks complete. Here's the report:

---

## 预检报告

### 1. 路径参数化 — **Y**

`analyze_generalize.py` 通过 `--exp` 参数选择实验目录，无硬编码 WikiText 路径。C4 分析只需：
```
python analyze_generalize.py --exp pythia1b_c4_a100_s42
```

### 2. C4 目录结构兼容 — **Y**（有注意项）

| 项目 | 状态 |
|------|------|
| gen_0 ~ gen_9 metrics.json | 全部存在 ✓ |
| gen_10 | 空目录（首次运行崩溃，EXIT_CODE=1，IncompleteRead） |
| `all_metrics.json` | 不存在，`assemble_all_metrics()` 会自动从 per-gen 文件组装 ✓ |
| 指标字段 | token_entropy, self_bleu, distinct_1/2/3, ece, effective_rank, perplexity, mauve, generation — 与 WikiText 完全一致 ✓ |

**config.json 标签错误**：`"dataset": "wikitext-103-v1"` 但实际 `"data_dir": "data/c4_5k"`。仅影响输出显示，不影响分析逻辑。

### 3. Threshold Onset 修复 — **一致，但两处均未修 σ 膨胀**

`analyze_generalize.py` → `method_ablation.py::threshold_lead` → `_onset_gen()`:
```python
base, sigma = s[0], np.std(s)   # σ 含退化值，阈值偏高
```

`analyze_opt1b_full.py::_onset()` 逻辑**完全相同**。两个 codepath 行为一致，C4 分析不会比 OPT 分析差，也不会触发新 bug。但如果要修正 σ 膨胀，两处都要改。

### 4. Pythia-1.4B — **Y，兼容**

- `pythia14b_wiki_a100_s42/`: gen_0~gen_3 完成（仍在跑），指标字段一致
- 分析脚本只读 metrics JSON，不加载模型，无模型名/路径依赖

### 需修复项

**仅 config.json 标签**（display-only bug）：`pythia1b_c4_a100_s42/config.json` 中 `dataset` 字段应为 `"c4_5k"`。

要我直接修这个 config.json 标签吗？另外，`generalize_pythia1b_c4_a100_s42_v2` 脚本在服务器上未找到——v2 实验可能用的是其他脚本名或已被清理。如果 v2 正在运行并写入同一目录，当前 gen_0-9 数据会被覆盖（不影响分析，只是数据来源变了）。

---
