# run frontier sc claude

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_frontier_sc_claude_20260521T061115_result.json`
- **Structured JSON:** [`df20562e55040ed70291.json`](../../sessions/df/df20562e55040ed70291.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已启动并运行正常。总结：

- **脚本**: `run_frontier_sc.py` 部署到 `autodl-5090:/root/autodl-tmp/struct_self_consist_ie/code/`
- **关键修复**: entity 匹配从 offset-based `(start, end, type)` 改为 text-based `(text.lower(), type)`，解决了 API 模型无法精确预测字符偏移的问题
- **PID**: 6302
- **Registry**: `exp_frontier_sc_claude_sonnet4` (RUNNING)
- **进度**: 5/200 实例完成，数据质量已验证（fewnerd_test_00000 greedy_f1=0.8889）
- **预估时间**: ~2h（200 instances × 8 samples × ~3-5s/call）

监控命令：
```bash
wc -l output/frontier_sc_claude_sonnet4/checkpoint.jsonl
tail -3 logs/frontier_sc_claude_sonnet4.log
```

---
