# viz fig1 paperbanana retry

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_fig1_paperbanana_retry_20260523T044424_result.json`
- **Structured JSON:** [`186aed5494ce1e1ba24a.json`](../../sessions/18/186aed5494ce1e1ba24a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果**：
- `artifacts/fig1_overview_pb.png` — 303KB, 4159×1171px
- `artifacts/fig1_overview_pb.pdf` — 322KB

**过程摘要**：
- TUM 代理（`http://47.94.22.126/v1`）+ `gpt-4o` 作为 VLM 成功绕过 Google Gemini API 封锁
- Patch 了 OpenRouterVLM 的 `base_url` 从环境变量读取（`OPENROUTER_BASE_URL`）
- 使用 `plot` 命令（`STATISTICAL_PLOT` 类型）走 matplotlib 代码生成路径，避免了 image-gen API 依赖
- 3 轮迭代全部完成（Planning → Styling → Code Gen × 3 + Critic × 3），总耗时约 90 秒
- 每轮 Critic 反馈：iter1 修字体/inset/标注 → iter2 修标注措辞/inset 大小/流程图间距 → iter3 最终输出

---
