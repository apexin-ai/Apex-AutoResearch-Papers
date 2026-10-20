# ops logic preflight

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_logic_preflight_20260515T220826_result.json`
- **Structured JSON:** [`a881a3f127d6fc852a8f.json`](../../sessions/a8/a881a3f127d6fc852a8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有检查完成。

---

## Pre-flight 检查报告

### 1. Z3 MaxSAT 60s 硬超时 — **PASS**
- `z3_maxsat.py:439` — `solve()` 默认参数 `hard_timeout_s: int = 60`
- `z3_maxsat.py:472` — `threading.Timer(hard_timeout_s, _watchdog)` 实现 60s 看门狗
- `z3_maxsat.py:445` — `opt.set("timeout", timeout_ms)` Z3 solver 内部超时 10000ms
- `pipeline.py:88` 调用 `solve()` 未覆盖 `hard_timeout_s`，使用 60s 默认值

### 2. vLLM 进程状态 — **PASS**
- QwQ-32B 在 port 8000 正常运行，`max_model_len=16384`

### 3. 数据文件就位 — **PASS**
- `proofwriter_30.json`: 30 条，keys=`[id, problem, solution, answer, level]`
- `folio_30.json`: 30 条，keys=`[id, problem, solution, answer, level, premises, conclusion, premises_fol, conclusion_fol]`
- `proofwriter_subset.json` / `folio_subset.json` 已存在且大小一致（loader 引用 `_subset.json`）

### 4. 实验命令确认 — **PASS**
- 逻辑域实验用 **`eval_proofwriter.py`** 和 **`eval_folio.py`**（不是 `run_full_mvp.py`）
- `LOGIC_EXTRACTION_PROMPT`（constraint_extractor.py:56）、`LOGIC_PROMPT`（trace_generator.py:24）、`FOLIO_PROMPT`（trace_generator.py:34）均存在
- `--save-intermediates` 两个脚本都支持
- Pipeline 自动检测 domain：`dataset=="proofwriter"` → `domain="logic"`，`dataset=="folio"` → `domain="folio"`，constraint_extractor.domain 都设为 `"logic"`
- **注意**：`eval_proofwriter.py` 的 `--max-tokens` 默认值是 4096，需显式指定 16384

### 5. 清理 v3 残留 — **PASS**
- 无 aime/v3 相关进程
- tmux session `sica_aime30_v3` 已清理

---

## 启动命令

**ProofWriter-30:**
```bash
cd /root/symb_invariant_consensus && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
python eval_proofwriter.py \
  --n-problems 30 --k 12 --max-tokens 16384 --seed 42 \
  --save-intermediates --output results/proofwriter_30_eval.json
```

**FOLIO-30:**
```bash
cd /root/symb_invariant_consensus && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
python eval_folio.py \
  --n-problems 30 --k 12 --seed 42 \
  --save-intermediates --output results/folio_30_eval.json
```

---
