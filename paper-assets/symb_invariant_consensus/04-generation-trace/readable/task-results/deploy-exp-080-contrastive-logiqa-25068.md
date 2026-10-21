# deploy exp 080 contrastive logiqa 25068

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_exp-080-contrastive-logiqa-25068_20260519T200214_result.json`
- **Structured JSON:** [`52237bf08b8d8e011204.json`](../../sessions/52/52237bf08b8d8e011204.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。总结：

**exp-080 已提交运行**
- 服务器: westd-25068, cuda:0, PID 279841
- 复用已有 vLLM Mistral-7B (port 8000)
- 代码改动: `run_contrastive.py` 新增 LogiQA 支持（8处修改）
  - `CONTRASTIVE_PROMPT_LOGIQA` 多选题 prompt
  - `--dataset logiqa` / `--limit` 参数
  - `generator.domain = "multichoice"` 多选答案提取
  - trace 答案归一化为 A/B/C/D 字母（修复了首次 dry-run 发现的候选项混乱问题）
  - 选项字母映射为完整选项文本传入 prompt
- Dry-run 3题验证通过: 2/3 correct, 无 crash
- 备份: `run_contrastive.py.bak_pre080`
- FOLIO 支持未被破坏（所有改动通过 `--dataset` 参数区分）
- Cron 每小时 :23 自动检查进度
- 预计运行 ~3-5 小时（200题 × ~60s/题）

---
