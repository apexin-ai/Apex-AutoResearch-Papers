# code fix ss s123 script

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_ss_s123_script_20260523T035019_result.json`
- **Structured JSON:** [`9afc0054d53178caf652.json`](../../sessions/9a/9afc0054d53178caf652.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。修改验证通过：

1. **`d048_ss_s123.sh`** — 已存在且参数正确（与 s456 一致，仅 seed/output-dir 不同），755 权限，无需重建
2. **错误 SS s123 块（73-124 行）已注释** — 保留原文便于审计，注释头标注了禁用原因
3. **新调用已插入** — `bash /root/turn_residual_gating/scripts/d048_ss_s123.sh`，在 ALL DONE 之前

diff 确认 s123 vs s456 仅有注释和换行格式差异，所有超参值完全一致。GPU 上运行的 s456 训练未受影响。

---
