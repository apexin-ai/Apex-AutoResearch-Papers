# code exp 047 qwen3 thinking prep

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-047-qwen3-thinking-prep_20260518T193103_result.json`
- **Structured JSON:** [`ec3b29050cb59b763d26.json`](../../sessions/ec/ec3b29050cb59b763d26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已就绪。C001 Dry-run 全部通过。

---

## exp-047 准备完成

### Dry-run 验证结果
| 检查项 | 状态 |
|--------|------|
| 模型路径 `/root/autodl-tmp/models/Qwen3-14B` (8 shards) | ✅ |
| 数据文件 `folio_full.json` (204题), `empty.json` | ✅ |
| Python/vllm imports | ✅ |
| vLLM 启动 (需 `VLLM_USE_FLASHINFER_SAMPLER=0`) | ✅ |
| Thinking mode (reasoning 字段分离) | ✅ |
| SICA pipeline 端到端 (folio_0: SICA=Unknown ✓, SC=Unknown ✓) | ✅ |
| cuda:2 空闲 | ✅ |
| port 8002 空闲 | ✅ |

### 关键发现
- **FlashInfer 兼容性**：这台机器 GPU sm < 75，必须加 `VLLM_USE_FLASHINFER_SAMPLER=0`（exp-028 脚本遗漏了，可能当时 vLLM 版本不同）
- **Thinking overhead**：K=2 单题 ~173s（trace=80s + extraction=93s），K=12 预估 ~340s/题，全 204 题约 19 小时
- **"Empty after stripping thinking" 警告**：exp-028 出现 143 次（~30% extraction），不影响最终结果因 K=12 冗余

### 部署命令

```bash
nohup bash /root/symb_invariant_consensus/scripts/run_exp047_qwen3_thinking_folio204.sh > /tmp/exp047_main.log 2>&1 &
```

脚本位置：`/root/symb_invariant_consensus/scripts/run_exp047_qwen3_thinking_folio204.sh`

配置：cuda:2, port 8002, K=12, T=0.7, max-tokens=8192, seed=42, Qwen3-14B thinking mode, FOLIO 204 题全量 run。

---
