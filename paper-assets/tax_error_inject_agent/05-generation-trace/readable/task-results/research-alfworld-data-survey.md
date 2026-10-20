# research alfworld data survey

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_alfworld-data-survey_20260514T044719_result.json`
- **Structured JSON:** [`5b7b9045d70c6d174236.json`](../../sessions/5b/5b7b9045d70c6d174236.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研报告已写入 `artifacts/alfworld_data_survey.md`。核心结论：

**任务**: 6 种任务类型，train 3,553 / valid_seen 140 / valid_unseen 134，max 50 步/episode。

**公开数据集**: HuggingFace 上有 u-10bei 的 2,502 条模板生成轨迹，但非真实环境执行，不适合 TaxEI 的 error injection 场景。

**收集方案**: 用 GPT-4o 在真实 ALFWorld 环境中 rollout，zero-shot 成功率 ~93%，收集 500 条成功轨迹约需 538 次 rollout，API 成本约 **$25-35**。建议写独立轻量 rollout 脚本，复用 verl-agent 的 prompt template 和 action projection。

**安装**: `pip install alfworld` + `alfworld-download`，要求 Python 3.9+，text-only 模式不需要 GPU。AutoDL 上需先 `source /etc/network_turbo` 再下载数据。

---
