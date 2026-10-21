# code exp 012 fix binoculars

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_012_fix_binoculars_20260515T125833_result.json`
- **Structured JSON:** [`474c3391bddebea33b3b.json`](../../sessions/47/474c3391bddebea33b3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法验证和 dry-run 均通过。

---

**修改清单**（文件 `scripts/exp012_ppl_depth_correlation.py`，356→384 行）：

| 行号(修改后) | 改动内容 |
|---|---|
| 22 | 依赖列表增加 `allenai/OLMo-1B-0724` |
| 25 | GPU 时间估算从 2 models → 3 models |
| 140 | `analyze_condition` 签名增加 `perf_ppl: dict[int, np.ndarray]` 参数 |
| 143 | `depths_present` 交集增加 `perf_ppl.keys()` |
| 149-150 | Binoculars ratio 分母从 `all_ref` 改为 `all_perf`（performer PPL） |
| 241-244 | `--obs_model` 替换为 `--bino_observer`（默认 Pythia-1.4b）+ `--bino_performer`（默认 OLMo-1B-0724） |
| 269 | dry-run 输出显示 3 个模型 |
| 270 | GPU 时间系数从 `* 2` 改为 `* 3` |
| 305-327 | 新增 Binoculars performer 模型加载 + PPL 计算块（独立 tokenizer） |
| 329-351 | Binoculars observer 模型加载（独立 tokenizer，从 `args.bino_observer` 读取） |
| 357 | `analyze_condition` 调用增加 `perf_ppls[cond]` 参数 |
| 372-374 | per-sample 输出 key 改为 `log_ppl_bino_obs` / `log_ppl_bino_perf` |

**Tokenizer 适配**：无需额外适配。`compute_log_perplexity_batch` 本身就接收独立的 `(model, tokenizer)` 对，各模型独立 tokenize 后计算标量 PPL，ratio 在标量层面相除，不存在 shared vocabulary 假设。

---
