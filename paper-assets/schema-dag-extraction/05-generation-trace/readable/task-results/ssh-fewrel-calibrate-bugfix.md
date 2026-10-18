# ssh fewrel calibrate bugfix

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fewrel-calibrate-bugfix_20260515T104553_result.json`
- **Structured JSON:** [`9825f47c378ad5d3c0ca.json`](../../sessions/98/9825f47c378ad5d3c0ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证结果：

- `import torch` 仅在 `stage_preprocess` (line 196) 中
- `from vllm` 仅在 `run_re_extraction` (line 85-86) 中
- `stage_extract` → `run_re_extraction` → vLLM first，无 torch
- `--stage all` 模式：preprocess 在主进程（含 torch），extract 通过 subprocess 启动（干净进程，vLLM first）

## 修复总结

**Bug 1** — `run_fewrel_formal.py:335`: `--model_path` 默认值改为 `/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/`

**Bug 2** — `run_fewrel_formal.py` 拆分为两阶段：
- `stage_preprocess()` (line 153): CPU 工作（数据加载、BCS、batch 分组），`import torch` 仅在此阶段
- `stage_extract()` (line 299): 读取 preprocess JSON，调用 `run_re_extraction()`（vLLM first）
- `--stage all`（默认）: preprocess 在主进程执行，extract 通过 `subprocess.run()` 在独立进程执行，避免 torch/vLLM fork 死锁

**Bug 3** — `calibrate.py` RE 任务两端修复：
- `build_confusion_matrix()`: 新增 `task` 参数。RE 模式直接比较 `gold["relation_type"]` vs `pred["relation"]`，不走 text overlap
- `run_calibration()` prediction parsing: RE 用 `preds.get("relation", "")`（而非 `preds.get("entities", [])`）
- `run_calibration()` gold labels: RE 用 `[{"relation_type": ...}]`（而非 `{"text": "", "type": ...}`）
- 传递 `task=task` 给 `build_confusion_matrix`

所有测试通过（RE confusion matrix、NER confusion matrix、import check）。

---
