# monitor strong model progress

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_strong_model_progress_20260515T160800_result.json`
- **Structured JSON:** [`7784268477127fbea05d.json`](../../sessions/77/7784268477127fbea05d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 强模型消歧实验 (mvp_strong_model_disambig)

**进程状态**: PID 141440 存活，已运行 12 分钟，正在处理 sanic_2

**进度**: 7/14 实例已完成，当前第 8 个

**test_pass**: 4/28 (14.3%) — 全部来自 cookiecutter_1

| 实例 | test_pass |
|------|-----------|
| black_1 | 0/4 |
| cookiecutter_1 | **4/4** |
| cookiecutter_2 | 0/4 |
| cookiecutter_3 | 0/4 |
| fastapi_2 | 0/4 |
| httpie_2 | 0/4 |
| luigi_5 | 0/4 |

所有 judge 分数均为 1（最低分）。无错误，运行正常。

---

## v2 实验

**进度**: 10/14 实例已完成（比强模型跑得快，已提前完成更多）

**test_pass**: 3/40 (7.5%)

---

**初步信号**：目前 test_pass 率极低，judge 分数全为 1。cookiecutter_1 是唯一在强模型下全部通过的实例。还剩 7 个实例（sanic_2 正在跑 + scrapy_2, scrapy_7, tornado_2, youtube-dl_1, youtube-dl_5, youtube-dl_20），最终结果需等完成后再评估 kill criteria。

---
