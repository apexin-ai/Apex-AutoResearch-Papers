# code baseline large and rename

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_baseline_large_and_rename_20260514T195436_result.json`
- **Structured JSON:** [`ede4c7f302ae6e69563a.json`](../../sessions/ed/ede4c7f302ae6e69563a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项任务全部完成。

**任务 1 — 重命名 dcol_train.py → dcol_feature_mlp.py**
- 本地：`artifacts/dcol_train.py` → `artifacts/dcol_feature_mlp.py` ✅
- 远程：`src/dcol_train.py` → `src/dcol_feature_mlp.py` ✅
- 引用更新：ROADMAP.md (3处)、task_context/reviewer.md (1处) ✅

**任务 2 — baseline_ce_classification.py 支持 DeBERTa-v3-large**
- `--model_name_or_path` → 拆分为 `--model_name`（默认 `microsoft/deberta-v3-large`）+ `--model_path`（默认 `/root/autodl-tmp/models/deberta-v3-large`）
- `hidden_size` 原本就是动态从 `encoder.config.hidden_size` 获取，无需改
- `model_tag` 改用 `args.model_name` 判断

**任务 3 — baseline_coral.py 支持 DeBERTa-v3-large**
- 同上修改逻辑

**远程验证结果**
- 重命名：`dcol_feature_mlp.py` 存在，`dcol_train.py` 已删除 ✅
- CE dry-run：参数解析正确，50 samples 加载正确，DeBERTa-v3-large 390 weights 加载成功 ✅
- CORAL dry-run：同上 ✅
- CPU 前向传播极慢未完成（435M参数模型，GPU训练时不会有此问题）

---
