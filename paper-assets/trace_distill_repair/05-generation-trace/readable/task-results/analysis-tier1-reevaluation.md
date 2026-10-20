# analysis tier1 reevaluation

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tier1_reevaluation_20260515T122046_result.json`
- **Structured JSON:** [`797bc80e753ee889ba61.json`](../../sessions/79/797bc80e753ee889ba61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整分析。

---

## 完整 33 实例分类表

| instance_id | patch_file | file_lines | struct_keep | line_keep | n_changed_files | tier | reason |
|---|---|---|---|---|---|---|---|
| black_1 | black.py | 6376 | 2 | 1 | 1 | Exclude | 零鉴别力（reviewer 标注） |
| cookiecutter_1 | cookiecutter/generate.py | 380 | 6 | 11 | 1 | **Tier 1** | |
| cookiecutter_2 | cookiecutter/hooks.py | 127 | 6 | 8 | 1 | **Tier 1** | |
| cookiecutter_3 | cookiecutter/prompt.py | 242 | 2 | 2 | 1 | **Tier 1** | |
| fastapi_1 | fastapi/applications.py | 691 | 5 | 15 | 5 | Exclude | 多文件 patch（5 files） |
| fastapi_2 | fastapi/routing.py | 991 | 3 | 19 | 1 | **Tier 1** | |
| httpie_1 | httpie/downloads.py | 435 | 0 | 0 | 1 | Tier 2 | both keeps=0 |
| httpie_2 | httpie/client.py | 147 | 0 | 0 | 2 | Exclude | 多文件 patch（2 files） |
| luigi_1 | luigi/server.py | 369 | 0 | 9 | 1 | Tier 2 | struct_keep=0 |
| luigi_10 | luigi/scheduler.py | 1290 | 0 | 0 | 1 | Tier 2 | both keeps=0 |
| luigi_14 | luigi/scheduler.py | 1128 | 0 | 0 | 1 | Tier 2 | both keeps=0 |
| luigi_2 | luigi/contrib/beam_dataflow.py | 479 | 0 | 3 | 1 | Tier 2 | struct_keep=0 |
| luigi_5 | luigi/util.py | 435 | 1 | 6 | 1 | **Tier 1** | |
| sanic_1 | sanic/app.py | 1438 | 0 | 1 | 1 | Tier 2 | struct_keep=0 |
| sanic_2 | sanic/server.py | 1013 | 2 | 2 | 1 | **Tier 1** | |
| scrapy_1 | scrapy/spidermiddlewares/offsite.py | 72 | 0 | 0 | 1 | Tier 2 | both keeps=0 |
| scrapy_2 | scrapy/utils/datatypes.py | 330 | 2 | 2 | 1 | **Tier 1** | |
| scrapy_3 | scrapy/downloadermiddlewares/redirect.py | 106 | 0 | 0 | 1 | Tier 2 | both keeps=0 |
| scrapy_4 | scrapy/contracts/__init__.py | 162 | 0 | 1 | 1 | Tier 2 | struct_keep=0 |
| scrapy_7 | scrapy/http/request/form.py | 203 | 2 | 3 | 1 | **Tier 1** | |
| thefuck_1 | thefuck/rules/pip_unknown_command.py | 19 | 0 | 1 | 1 | Tier 2 | struct_keep=0 |
| thefuck_2 | thefuck/utils.py | 337 | 0 | 0 | 1 | Tier 2 | both keeps=0 |
| thefuck_4 | thefuck/shells/fish.py | 113 | 0 | 0 | 1 | Tier 2 | both keeps=0 |
| tornado_1 | tornado/websocket.py | 1656 | 0 | 0 | 1 | Tier 2 | both keeps=0 |
| tornado_2 | tornado/http1connection.py | 833 | 1 | 2 | 1 | **Tier 1** | |
| tornado_4 | tornado/web.py | 3582 | 0 | 0 | 1 | Tier 2 | both keeps=0, file>3000 |
| tornado_5 | tornado/ioloop.py | 1223 | 0 | 0 | 1 | Tier 2 | both keeps=0 |
| tornado_7 | tornado/ioloop.py | 1128 | 0 | 5 | 1 | Tier 2 | struct_keep=0 |
| youtube-dl_1 | youtube_dl/utils.py | 3887 | 3 | 22 | 1 | Tier 2 | file>3000 |
| youtube-dl_10 | youtube_dl/utils.py | 1770 | 0 | 11 | 1 | Tier 2 | struct_keep=0 |
| youtube-dl_2 | youtube_dl/extractor/common.py | 2624 | 1 | 20 | 1 | **Tier 1** | |
| youtube-dl_20 | youtube_dl/utils.py | 3824 | 1 | 10 | 1 | Tier 2 | file>3000 |
| youtube-dl_5 | youtube_dl/utils.py | 2971 | 4 | 72 | 1 | **Tier 1** | |

---

## 汇总

### Tier 1（11 个）

| instance_id | file_lines | struct_keep | line_keep |
|---|---|---|---|
| youtube-dl_5 | 2971 | 4 | 72 |
| cookiecutter_1 | 380 | 6 | 11 |
| cookiecutter_2 | 127 | 6 | 8 |
| fastapi_2 | 991 | 3 | 19 |
| youtube-dl_2 | 2624 | 1 | 20 |
| luigi_5 | 435 | 1 | 6 |
| scrapy_7 | 203 | 2 | 3 |
| cookiecutter_3 | 242 | 2 | 2 |
| sanic_2 | 1013 | 2 | 2 |
| scrapy_2 | 330 | 2 | 2 |
| tornado_2 | 833 | 1 | 2 |

### Exclude（3 个）
- **black_1** — 零鉴别力
- **fastapi_1** — 5 文件 patch
- **httpie_2** — 2 文件 patch

### Tier 2（19 个）
剩余 19 个，其中接近 Tier 1 的：

| instance_id | file_lines | struct_keep | line_keep | 差距 |
|---|---|---|---|---|
| **youtube-dl_1** | 3887 | 3 | 22 | 仅 file>3000（超 887 行），keeps 很高 |
| **youtube-dl_20** | 3824 | 1 | 10 | 仅 file>3000（超 824 行），keeps 尚可 |
| **luigi_1** | 369 | 0 | 9 | 仅缺 struct_keep，line_keep=9 |
| **youtube-dl_10** | 1770 | 0 | 11 | 仅缺 struct_keep，line_keep=11 |
| **tornado_7** | 1128 | 0 | 5 | 仅缺 struct_keep |

---

## 建议的验证候选（3 个，从 Tier 1 选）

优先 struct_keep + line_keep 都高、文件适中：

1. **cookiecutter_1**（sk=6, lk=11, 380 行）— 两项 keep 都高，文件紧凑，鉴别力最佳
2. **youtube-dl_5**（sk=4, lk=72, 2971 行）— line_keep 极高（72），structural 也好，最能体现 distill 效果
3. **cookiecutter_2**（sk=6, lk=8, 127 行）— 最小文件，struct_keep 最高，与 cookiecutter_1 构成同项目对照

如果想要跨项目多样性，可以用 **fastapi_2**（sk=3, lk=19, 991 行）替换 cookiecutter_2。

---
