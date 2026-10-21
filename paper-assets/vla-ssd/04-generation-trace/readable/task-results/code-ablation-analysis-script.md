# code ablation analysis script

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ablation_analysis_script_20260517T200820_result.json`
- **Structured JSON:** [`20aa0a8c041854615039.json`](../../sessions/20/20aa0a8c041854615039.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已部署到 `/root/vla-ssd/scripts/analyze_ablation_50demos.py` 并通过 dry-run 验证。

main 文件不存在时优雅退出，打印 "waiting for main experiment"。一旦 `action_probe_50demos.json` 就绪，执行：

```bash
/root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/analyze_ablation_50demos.py
```

即可输出完整 4-condition 分析（summary table + bootstrap CI + specificity check + 两张 PDF figure + combined JSON）。

---
