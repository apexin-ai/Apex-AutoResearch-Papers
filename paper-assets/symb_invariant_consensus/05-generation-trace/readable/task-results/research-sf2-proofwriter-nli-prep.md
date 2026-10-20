# research sf2 proofwriter nli prep

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_sf2-proofwriter-nli-prep_20260520T133703_result.json`
- **Structured JSON:** [`aa9c30fce1717057ebc3.json`](../../sessions/aa/aa9c30fce1717057ebc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕。以下是完整实验方案。

---

## SF-2: DeBERTa NLI on ProofWriter 实验方案

### 1. 现有资源盘点

| 资源 | 路径 | 状态 |
|------|------|------|
| ProofWriter 数据 | `data/proofwriter_full.json` | 600题, OWA-D5, True/False/Unknown |
| SC traces (Mistral-7B) | `results/exp046_mistral_7b_pw600/` | 600题, k=12, SC=39.33%, SICA=36.5% |
| SC traces (Qwen2.5-7B) | `results/exp065_qwen7b_pw600/` | 600题, 可做跨模型 |
| DeBERTa-large-mnli | `/root/models/deberta-large-mnli` | 已下载 |
| FOLIO R 脚本 | `direction_r_deberta.py` | 需适配 |
| sc_answer_matrix.json | **不存在** (PW实验未生成) | 需从intermediates提取 |

### 2. 数据格式差异

| | FOLIO | ProofWriter |
|---|---|---|
| 分隔标记 | `"Determine whether the following conclusion is true, false, or uncertain:"` | `"Determine whether the following statement is true, false, or unknown:"` |
| 前缀 | `"Given the following premises:\n"` | 无前缀，直接是 context |
| Answer | True/False/Unknown | True/False/Unknown (一致) |
| NLI mapping | entailment→True, contradiction→False, neutral→Unknown | 同上 (无需改) |

### 3. 需要的修改

**Step A — 生成 `sc_answer_matrix.json`**：从 exp046 intermediates (600个JSON文件) 提取每题的 trace-level answer 列表。每个 intermediate 文件的 `sica_result.traces[i].answer` 即原始答案。输出格式与 FOLIO 的 sc_answer_matrix.json 一致：
```json
{"problem_id": {"answers": ["True", "Unknown", ...], "ground_truth": "True"}}
```

**Step B — 新建 `direction_r_deberta_proofwriter.py`**（基于 `direction_r_deberta.py`）：
- `parse_problem()`: 用 `"Determine whether the following statement is true, false, or unknown:\n"` 作为分隔标记（替换 FOLIO 的 `"conclusion is true, false, or uncertain"`）
- 路径改为 ProofWriter: `proofwriter_full.json`, `exp046_results.json`, 生成的 `sc_answer_matrix.json`
- 输出目录: `results/direction_r_nli_pw600/`
- 其他逻辑不变（R1 standalone, R2 verifier, R3 combo）

### 4. 运行参数

| 参数 | 值 |
|------|-----|
| 服务器 | westd-25068 |
| GPU | 需要 (DeBERTa-large 406M 推理) |
| 模型路径 | `/root/models/deberta-large-mnli` |
| 数据量 | 600 题 |
| SC baseline | exp046, Mistral-7B, k=12 |
| 预计耗时 | ~2-3 分钟 (600题 × ~0.3s/题 on GPU) |

### 5. 预期产出

与 FOLIO R 实验对应的完整指标：
- **R1**: DeBERTa standalone accuracy on PW600
- **R2**: DeBERTa-as-verifier (agree/disagree with SC, correction analysis)
- **R3**: Combo (DeBERTa vote weight=1,3 加入 SC 投票)
- Per-label breakdown (True/False/Unknown)
- Baselines: SC=39.33%, SICA=36.5%

### 6. 注意事项

- exp046 intermediates 有 600 个文件，全覆盖，无缺失
- 部分 trace 的 answer 为空字符串（提取失败），需过滤处理（与 FOLIO sc_answer_matrix 行为一致）
- 如果还需要跨模型验证，exp065 (Qwen2.5-7B) 也有完整 PW600 traces，可后续复制同样流程

是否开始写脚本并执行？

---
