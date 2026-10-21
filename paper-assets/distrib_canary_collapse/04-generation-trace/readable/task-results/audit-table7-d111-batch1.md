# audit table7 d111 batch1

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_table7_d111_batch1_20260520T004801_result.json`
- **Structured JSON:** [`0d712fc0aa856364693b.json`](../../sessions/0d/0d712fc0aa856364693b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入 `artifacts/table7_d111_audit_batch1.md`。

核心结果：

| 实验 | K≥3 旧→新 | K≥4 旧→新 |
|------|-----------|-----------|
| Pythia-6.9B s42 | 8/8→**5/8** (↓3) | 3/8→**1/8** (↓2) |
| Qwen3.5-0.8B s42 | 8/8→8/8 (不变) | 6/8→**3/8** (↓3) |
| Pythia-1.4B s42 | 2/8→2/8 (不变) | 0/8→0/8 (不变) |
| Pythia-1.4B s43 | 6/8→**7/8** (↑1) | 3/8→3/8 (不变) |

主要发现：
- **diff_xcorr 几乎全军覆没**：32 个 pair 中只有 4 个 diff lag > 0，D111 实质上取消了 diff_xcorr 的 consensus 贡献
- **Pythia-6.9B 受影响最大**：naive lag 也大多为负，K≥3 从 8/8 降到 5/8
- **Qwen3.5 K≥3 不变**：靠 TY(6/8) 和 PermG(8/8) 补偿了 xcorr 损失，但 K≥4 腰斩
- **Pythia-1.4B s42/s43 实际路径在 westd-19828**（非任务指定的 17855），Pythia-6.9B 在 `scale_check/` 而非 `generalize/`

---
