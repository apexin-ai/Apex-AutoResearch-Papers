# exp exp 005 deltanet eval hgrn fix

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_exp-005-deltanet-eval-hgrn-fix_20260522T155530_result.json`
- **Structured JSON:** [`692e88344afb6201444d.json`](../../sessions/69/692e88344afb6201444d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

HGRN 下载在 93%，CDN 限流严重（59 KiB/s）。aria2c 会自动重试，让它在后台继续。

当前状态汇总：

**Task A - DeltaNet 评估：已完成**
- 模型：340M-20B-DeltaNet-hybrid-3-1
- lambada_openai: acc=0.3536, ppl=30.45
- arc_easy: acc=0.6010, acc_norm=0.5198
- 结果已保存到 `/root/entrainment_gated_ft/results/exp005_zoo_expansion/DeltaNet_hybrid-3-1/`
- Registry 已更新（exp-005-dn-eval）
- 注意：修复了 fla 0.5.0 与 transformers 5.8.1 的兼容性问题（`_tied_weights_keys` list→dict），创建了 `scripts/patch_fla_eval.py`，后续 fla 模型评估都应通过此脚本运行

**Task B - HGRN 下载加速：进行中**
- aria2c 多线程下载从原来的 ~80 KB/s 加速到峰值 3.1 MiB/s（~40 倍）
- 当前 93% 完成（1.1GiB/1.2GiB），CDN 限流后降至 ~60-130 KiB/s
- 预计还需 10-20 分钟完成
- 下载完成后需验证文件完整性并删除 `.aria2` 控制文件

---
