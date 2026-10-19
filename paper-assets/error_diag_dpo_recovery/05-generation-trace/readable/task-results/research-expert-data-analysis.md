# research expert data analysis

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_expert-data-analysis_20260512T155912_result.json`
- **Structured JSON:** [`002898d76cf37797c32e.json`](../../sessions/00/002898d76cf37797c32e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析报告已保存到 `artifacts/expert_data_analysis.md`。核心发现：

- **3,119 条**成功轨迹，6 种 task type 全覆盖，JSON 结构为 `{id, game_file, conversations}`
- **轨迹长度**：有效步数 3~49（mean 9.8），pick_two_obj_and_place 最长（mean 15.2），pick_and_place_simple 最短（mean 8.3）
- **匹配 key**：1,395 个 unique task directory（去掉 trial 后缀），每个有 1~3 条 trial。与 failure trajectory 做 overlap 时按 task directory 匹配
- **Action 空间**：9 种核心动词（go/take/put/open/close/clean/cool/use/heat），go 占 53.4%。有 8 条噪声 action（quickly/turn/think/brainstorm）
- **Conversation 格式**：首 turn 固定 "OK"，后续 `"Thought: ...\nAction: ..."` 交替。构建 DPO pair 时跳过第一个 GPT turn

---
