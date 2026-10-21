# supplement p1 missing scripts

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_supplement_p1-missing-scripts_20260520T060127_result.json`
- **Structured JSON:** [`58a960646934873ff67d.json`](../../sessions/58/58a960646934873ff67d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## 拷贝结果

### 7/7 脚本成功拷贝

| 文件 | 来源 | 状态 |
|------|------|------|
| `analyze_prompt_types.py` | `/root/gen-depth-fingerprint/analyze_prompt_types.py` | OK |
| `analyze_instruct.py` | `/root/gen-depth-fingerprint/analyze_instruct.py` | OK |
| `eval_exp052_instruct.py` | `/root/gen-depth-fingerprint/eval_exp052_instruct.py` | OK |
| `cross_ref_analysis.py` | `/root/gen-depth-fingerprint/cross_ref_analysis.py` | OK |
| `seed_demeaning_logo.py` | `/root/gen-depth-fingerprint/seed_demeaning_logo.py` | OK |
| `eval_independent_seed.py` | `/root/gen-depth-fingerprint/eval_independent_seed.py` | OK |
| `ddr_temp_analysis.py` | `/root/gen-depth-fingerprint/ddr_temp_analysis.py` | OK |

### Llama 数据
- `features_llama-3.2-3b-instruct.csv` — 4,974 条记录（1000 seeds × 5 depths），679KB

### 匿名化修改

| 脚本 | 修改项 |
|------|--------|
| `analyze_prompt_types.py` | `/root/autodl-tmp/models/pythia-410m/...` → 环境变量 `REF_MODEL_PATH` + 相对路径回退；`PROJECT_ROOT` 改为 `parent.parent`（指向 supplement 根） |
| `cross_ref_analysis.py` | 中文 docstring `plan-003 跨家族参考模型分析` → 英文；`project_root` 改为 `parent.parent` |
| `ddr_temp_analysis.py` | `DATA = "/root/gen-depth-fingerprint/data"` → `os.path.join(ROOT, "..", "data")` 相对路径 |
| `eval_exp052_instruct.py` | 输出路径 `results/exp052_instruct_eval.json` → `results/instruct_eval.json`；路径改为相对引用 |
| `seed_demeaning_logo.py` | 数据/结果路径改为 `../data/` / `../results/` 相对路径 |
| `eval_independent_seed.py` | 同上，相对路径 |
| `analyze_instruct.py` | 无硬编码路径，无需修改 |

所有脚本均无 API key、个人信息或中文注释残留。`code/README.md` 和 `data/README.md` 已更新。

---
