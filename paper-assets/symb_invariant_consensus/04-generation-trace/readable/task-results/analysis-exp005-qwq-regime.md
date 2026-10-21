# analysis exp005 qwq regime

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp005_qwq_regime_20260516T052554_result.json`
- **Structured JSON:** [`11fafa8fc869315a21b5.json`](../../sessions/11/11fafa8fc869315a21b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出已保存并注册：

**服务器文件**：
- `results/qwq_operating_regime.md` — 格式化报告
- `results/qwq_operating_regime.json` — 结构化数据

**Artifacts**：
- `art_20260516_877e3f` — MD 报告
- `art_20260516_b064a6` — JSON 数据

**与任务模板的主要差异**（基于实际文件验证）：

| 项目 | 任务模板 | 实际数据 |
|------|---------|---------|
| ProofWriter N | 16 | **17**（文件中实际完成 17 题） |
| PW multi-candidate | 18.75% (3/16) | **23.5% (4/17)**（多了 Q12） |
| PW SICA acc | X% | **82.4%** |
| PW SC acc | X% | **88.2%** |
| PW Δ | 0.0 | **−5.9pp**（SICA 反而更差） |
| FOLIO N | 10 | **2**（仅 live test，K=4 非 K=12） |
| Combined C0 | 3.6% | **2.6% effective / 10.3% nominal** |

关键发现：ProofWriter 上 SICA 不仅没有超越 SC，反而因为约束提取偏差（498_Q8：少数派 constraint score 38 > 多数派 27）比 SC 差 5.9pp。这比预期的"SICA≡SC"结论更强烈——reasoning model 下 SICA 可能有害。

---
