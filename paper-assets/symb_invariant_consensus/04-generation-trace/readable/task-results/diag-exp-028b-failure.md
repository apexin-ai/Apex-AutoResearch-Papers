# diag exp 028b failure

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp-028b-failure_20260519T032113_result.json`
- **Structured JSON:** [`62427448c1097de2848c.json`](../../sessions/62/62427448c1097de2848c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### 失败根因：资源冲突（非 OOM）

**exp058 在 11:12 部署到 cuda:3 + port 8003，直接杀死了 exp028b 的 vLLM 服务。**

证据链：
1. exp028b 的 vLLM (PID 99897) 已死，`ps -p 99897` 无结果
2. GPU 3 当前进程 PID 149906 是 exp058 的 Mistral-7B EngineCore（父进程 149633，启动于 11:12）
3. exp058 的启动命令明确使用 `CUDA_VISIBLE_DEVICES=3 --port 8003`，与 exp028b 完全冲突
4. vLLM 日志最后一条记录停在 11:12:10，之后无新日志
5. GPU KV cache usage 仅 ~5-8%，不存在 OOM 问题

### 进度与数据恢复

| 项目 | 状态 |
|------|------|
| 完成进度 | 166/204 (81%) |
| 中间结果 | `intermediates/folio_0~folio_165` 共 166 个 JSON 完整保存 |
| 最终结果 | `exp028b_results.json` 仅 2 条（未来得及写入完整结果） |
| 剩余工作 | 38 题，预计 ~90 min |

### 残留进程

exp028b 无残留进程。cuda:3 当前被 exp058 占用：
- PID 149633: vLLM APIServer (Mistral-7B, port 8003)
- PID 149906: VLLM::EngineCore, 88104 MiB

### 重试建议

值得重试。实验支持 resume（`--save-intermediates` + 自动跳过已完成），只需跑剩余 38 题。但需等 exp058 完成后释放 cuda:3 和 port 8003，或改用其他 GPU/端口。

---
