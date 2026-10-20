# deploy crossner download

**schema conform ie training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_crossner-download_20260512T101956_result.json`
- **Structured JSON:** [`86c55cddd2e948862f12.json`](../../sessions/86/86c55cddd2e948862f12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

### 汇报

**CrossNER 数据下载状态** — 5 个域均完整（train/dev/test 各 3 个文件）：

| 域 | train | dev | test |
|---|---|---|---|
| politics | 8,584 行 | 25,165 行 | 28,236 行 |
| science | 7,300 行 | 16,589 行 | 20,030 行 |
| music | 4,009 行 | 15,971 行 | 20,070 行 |
| literature | 3,882 行 | 14,903 行 | 16,573 行 |
| ai | 3,882 行 | 11,269 行 | 13,422 行 |

格式：`token\ttag`（BIO 标注），空行分隔句子。数据源：`github.com/zliucr/CrossNER`。

**代码加载验证** — `load_crossner` 全部通过：

| 域 | test 样本数 |
|---|---|
| politics | 651 |
| science | 543 |
| music | 465 |
| literature | 416 |
| ai | 431 |

无错误。

---
