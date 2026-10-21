# code zeroshot baseline prep

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_zeroshot_baseline_prep_20260515T004650_result.json`
- **Structured JSON:** [`8bf880ac9e98896233cc.json`](../../sessions/8b/8bf880ac9e98896233cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。验证报告：

### 已完成

| 项目 | 状态 |
|------|------|
| openai SDK | 0.28.0 → 2.36.0，支持 `OPENAI_BASE_URL` 环境变量 |
| `_call_openai` 代码 | **无需修改** — `openai.OpenAI()` 在 v1.0+ 自动读取 `OPENAI_BASE_URL` 和 `OPENAI_API_KEY` |
| `--llm_model` 参数 | 已支持 |
| `--provider openai` | 已支持 |
| 数据文件 | `depth_0~3.jsonl` 各 5000 条，共 20000 条 |
| `scripts/run_zeroshot_baseline.sh` | 已创建，base_url 已配置 |
| `--help` dry-run | 通过，所有参数正常解析 |

### 待完成

| 项目 | 说明 |
|------|------|
| `OPENAI_API_KEY` | 需要设置 project secret 后注入环境变量 |
| 模型名确认 | 脚本默认用 `gpt-4o-mini`，需确认代理实际支持的模型列表（可在有 key 后 `curl http://47.94.22.126/v1/models` 验证） |

---
