# ops m1 progress check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_m1-progress-check_20260513T061620_result.json`
- **Structured JSON:** [`39fdd5bce3736bfdfb7f.json`](../../sessions/39/39fdd5bce3736bfdfb7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## M1 Extraction 状态

### 1. PID 存活
**PID 577864 存活**，运行 9h28m，状态 S（sleeping），命令：`bash scripts/run_m1_extraction.sh`

### 2. 进度
- **已产出文件**：10,374 个 JSON，覆盖 **36/131 repos**
- **跳过**：3,067 个 instance（主要是 clone_failed，如 pandas-dev）
- **当前活跃 8 个 repo**（最新进度）：

| Repo | 进度 | 剩余 |
|------|------|------|
| python-openxml/python-docx | 200/1686 | 1486 |
| cantools/cantools | 1000/1440 | 440 |
| pygments/pygments | 950/1430 | 480 |
| paramiko/paramiko | 400/920 | 520 |
| pyasn1/pyasn1 | 50/766 | 716 |
| lepture/mistune | 250/729 | 479 |
| andialbrecht/sqlparse | 400/459 | 59 |
| prettytable/prettytable | 100/276 | 176 |

活跃 repos 剩余 ~4,356 instances。

### 3. 磁盘
- **总量**：169G，**已用** 125G (74%)，**剩余 45G**
- m1_extraction 占 4.0G

### 4. 预估剩余时间
- 9.5h 处理了 36 repos，速率约 3.8 repos/h
- 剩余 95 repos 待处理（加上当前 8 个活跃 repos 的尾部）
- **预估还需 ~25-30 小时**，约 5月14日 下午完成
- 磁盘按当前 4G/36 repos 推算，131 repos 约需 ~15G，45G 剩余空间充足

---
