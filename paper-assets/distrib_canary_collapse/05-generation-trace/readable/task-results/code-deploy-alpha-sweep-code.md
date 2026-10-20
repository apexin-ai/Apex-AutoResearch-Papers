# code deploy alpha sweep code

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_deploy-alpha-sweep-code_20260514T185918_result.json`
- **Structured JSON:** [`28560964e53e4a62a917.json`](../../sessions/28/28560964e53e4a62a917.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成，验证通过。

**结果汇总：**
- 旧版（257行）已备份为 `iterative_train.py.bak.mvp`
- 新版（293行）已部署，`--help` 输出确认：
  - `--synthetic_ratio` ✓（Fraction of training data that is synthetic (0-1)）
  - `--accumulate` ✓（Pool all historical synthetic data instead of only the latest generation）
- import 无误，参数解析正常
- 新增功能：双向 mix_datasets、accumulate 模式、EXIT_CODE 哨兵

---
