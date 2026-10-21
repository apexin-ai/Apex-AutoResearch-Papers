# research paper patch status

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper_patch_status_20260518T014706_result.json`
- **Structured JSON:** [`a953bdd3ef4fcbda218e.json`](../../sessions/a9/a953bdd3ef4fcbda218e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有 `register_artifact` 工具可用。报告已写入本地路径。

---

## 审计结果摘要

**已写入论文的数据（完整）：**
- 3 模型 budget curve 完整数据（Qwen-7B / DeepSeek / Qwen-1.5B × tail-256/512/1024/2048）
- Phase transition、convergence、scale inversion 叙事
- 3 模型 head-tail gap 表格（15.5–22.6pp）
- Non-monotonicity 已正确修正为 "仅 DeepSeek, -1.5pp"

**缺失：**
1. **P1（立即可做）**: CodeLlama-13B tail-512=97.5% 未写入 Table 6
2. **P2（等实验）**: CL-13B tail-256 和 tail-1024 还在跑
3. **P3**: 正文多处 "three models" 需改为 "four models"（待 P2）
4. **P4**: Budget curve figure 需更新为 4-model 版本
5. **P5**: CL-13B head-2048 数据缺失，无法填 head-tail gap 表

报告已写到 `artifacts/paper_patch_audit/paper_patch_status.md`。

---
