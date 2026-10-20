# code d066 beam sweep fix

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d066_beam_sweep_fix_20260519T153141_result.json`
- **Structured JSON:** [`c45613fb0641b1832229.json`](../../sessions/c4/c45613fb0641b1832229.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**westd-21461 SciERC 脚本**：已验证正确，无需修改。

**westd-16980 DocRED 脚本**修改了 4 处：
1. `BEAMS=(1 2 4 8)` → `BEAMS=(2 8)`（k=1/4 复用 d064）
2. 添加 `--max_docs 200` 参数（`run_constrained_extraction.py` 原生支持，无需生成子集文件）
3. 输出文件名加 `_200` 后缀区分：`{model}_docred_200_beam{k}_{mode}.jsonl`
4. 完成检查阈值从 998 改为 200

语法验证通过。预估 wall time 从 ~32h 降到 ~3-4h。报告已写入 `d066_beam_sweep_fix.md`。

GPU 空闲后启动命令：
```bash
nohup bash scripts/d066_beam_sweep_docred.sh > /root/autodl-tmp/schema_outputs/d066_beam_sweep/d066_docred_main.log 2>&1 &
```

---
