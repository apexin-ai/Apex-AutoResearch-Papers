# verify eval script and paper

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_eval_script_and_paper_20260519T204510_result.json`
- **Structured JSON:** [`fceaa8b48e731b39ccab.json`](../../sessions/fc/fceaa8b48e731b39ccab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。汇总结果：

---

### 子任务 A: eval 脚本状态 — ✅ 可用（训练完成后即可一键启动）

**覆盖度检查：**
- Step 1: In-dist PPL — ✅ `eval_ppl_ood.py` on `data/human/eval_holdout.jsonl`
- Step 2: OOD PPL — ✅ OpenWebText + Wikipedia 并行 (GPU 0/1)
- Step 3: Downstream — ✅ lm_eval 5 benchmarks (arc_easy, arc_challenge, hellaswag, piqa, winogrande)

**文件存在性：**
- `eval_ppl_ood.py` ✅
- `data/human/eval_holdout.jsonl` ✅
- `data/eval_openwebtext.jsonl` ✅
- `data/eval_wikipedia.jsonl` ✅

**语法检查：** `bash -n` 通过，无语法错误

**模型目录：** `output/models/adaptive_fromscratch_seed42/` 存在（含 `config.json`, `step_metrics.jsonl`），但 `final/` 子目录尚不存在——训练完成后会生成，脚本引用 `${MODEL_PATH}` 指向 `final/`，合理。

**结论：** 脚本结构正确，所有依赖文件就位，训练完成后可直接 `bash scripts/run_seed42_full_eval.sh` 一键运行。

---

### 子任务 B: 论文编译 + Round 6 修改

**论文源码位置：** 不在 westd-41312 上，在本地 `docs/paper/`。

**Round 6 修改存在性（本地检查）：**

| 修改项 | 状态 | 位置 |
|--------|------|------|
| R3-N1: paired t-test | ✅ | `results.tex:16` — "paired $t(2)=-37.3$, $p<0.001$"；`limitations.tex:34` + `checklist.tex:48` 说明 N=3 限制 |
| R3-N2: τ sensitivity caveat | ✅ | `method.tex:131` — caveat 关于 ESS/micro-batch；`checklist.tex:45` — §5.3 sensitivity analysis for τ and n_min |
| R3-W1: self-contamination | ✅ | `experiments.tex:4` + `limitations.tex:2,4` — 明确讨论 self-contamination 及其局限性 |
| R3-W7: B=4 | ✅ | `experiments.tex:13` — "batch size 4"；`limitations.tex:7` — "batch size 4" 在 limitations 中也有提及 |

**论文编译：** 无法在 westd-41312 上编译（无 .tex 文件）。如需编译验证，需在本地或有 LaTeX 环境的机器上执行。

---
