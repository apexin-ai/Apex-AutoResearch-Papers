# research codalab precheck

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_codalab-precheck_20260522T010732_result.json`
- **Structured JSON:** [`4698c9e840a60c483236.json`](../../sessions/46/4698c9e840a60c483236.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## CodaLab 预检结果

### 提交格式

Re-DocRED `evaluation.py` 期望**扁平 list** 格式：
```json
[{"title": "...", "h_idx": 0, "t_idx": 1, "r": "P27", "evidence": [0, 1]}, ...]
```

### 已有 codalab_submission.json — 两种格式共存

| 格式 | 目录 | 结构 | 与 CodaLab 兼容 |
|------|------|------|:-:|
| **新格式 (list)** — 5 个 | `plan_002_test_rsft_s43/s44`, `plan_006_*_test` (3个), `test_rsft_ced_s44` | `[{title, h_idx, t_idx, r, evidence}]` | ✅ |
| **旧格式 (dict)** — 8 个 | `test_eval_14b_rsft_s42`, `test_eval_14b_sft_s42`, `test_eval_1_7b_rsft_s42`, `test_eval_4b_sft_s42`, `test_eval_8b_rsft_s42`, `test_eval_8b_sft_s42`, `test_eval_llama_rsft_s42`, `test_eval_llama_sft_s42` | `{title: [{r, h, t, evidence}]}` | ❌ key 名 `h/t` ≠ `h_idx/t_idx`，且是 dict 非 list |

### 缺 codalab_submission.json 的 test eval 目录

| 目录 | 状态 |
|------|------|
| `test_eval_14b_sft_s42_no_evi` | 空目录 |
| `test_eval_1_7b_sft_s42` | 空目录 |
| `test_eval_1_7b_sft_s42_no_evi` | 仅有 log.txt |
| `test_eval_4b_rsft_s42` | 空目录 |
| `test_eval_4b_rsft_s42_v2` | 空目录 |
| `test_rsft_s44` | 仅有 metrics.json |

### 需要做的事

1. **格式转换**：8 个旧格式文件需要 `dict{title→[{r,h,t}]}` → `list[{title,h_idx,t_idx,r}]` 转换（`h`→`h_idx`, `t`→`t_idx`）
2. **缺失实验**：上述 6 个目录要么 eval 未完成、要么未生成 codalab 文件，需重跑 test inference
3. **提交流程**：手动提交——Re-DocRED CodaLab 网页上传 JSON 文件

---
