# diagnose exp 14b inference fewnerd exit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_14b_inference_fewnerd_exit_20260520T192142_result.json`
- **Structured JSON:** [`7aeabc56ec887f05fd98.json`](../../sessions/7a/7aeabc56ec887f05fd98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**进程 217960 尚未退出，仍在正常运行。**

当前状态：
- **FewNERD N=2 正在进行中** — 82% (61628/75296 prompts)，75296 = 37648 实例 × 2 采样，吻合 N=2
- Kill 监控脚本尚未触发（日志为空），因为还没到 N=8

已完成的推理：

| 数据集 | N=1 | N=2 | N=4 | N=8 | N=16 |
|--------|-----|-----|-----|-----|------|
| CoNLL2003 | ✅ | ✅ | ✅ | ✅ | ✅ |
| SciERC | ✅ | ✅ | ✅ | ✅ | ✅ |
| FewNERD | ✅ (170MB) | 🔄 82% | ❌ | ❌ | ❌ |

输出路径：`/root/autodl-tmp/struct_self_consist_ie/output/14b_final_inference/`

不需要更新 registry，进程正常运行中。预计 FewNERD N=2 再需约 20 分钟完成，之后继续 N=4 → N=8，到 N=8 完成后 kill 监控脚本会触发终止进程。

---
