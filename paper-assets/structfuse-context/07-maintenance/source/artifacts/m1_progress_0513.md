# M1 CodeQL Extraction Progress — 2026-05-13 16:28

## 进程状态
- **PID 577864**: 运行中，已运行 11h40m
- 启动时间: 2026-05-13 04:48
- 日志: `/tmp/m1_extraction.log`

## 提取进度
- **总 (repo, commit) 组**: 131
- **总 instances**: 59,136
- **已完成 repos (cleaned up)**: 33/131 (25.2%)
- **有产出文件的 repos**: 41（含 8 个正在处理中）
- **未开始 repos**: ~90

### 当前活跃 repos（最新进度）
| Repo | 进度 | 完成度 |
|------|------|--------|
| cantools/cantools | 1300/1440 | 90.3% |
| lepture/mistune | 650/729 | 89.2% |
| pygments/pygments | 1150/1430 | 80.4% |
| paramiko/paramiko | 700/920 | 76.1% |
| python-openxml/python-docx | 550/1686 | 32.6% |
| pyasn1/pyasn1 | 350/766 | 45.7% |
| seperman/deepdiff | 50/964 | 5.2% |
| kurtmckee/feedparser | 处理中 | — |

## 产出统计
- **JSON 文件**: 12,989 个
- **跳过 instances**: 3,067 (skip_log.jsonl)
- **产出占比**: (12,989 + 3,067) / 59,136 = 27.1%

## 磁盘状态
| 路径 | 大小 |
|------|------|
| /root/autodl-tmp/ | 160G / 169G (95%) |
| m1_extraction/ (产出) | 5.2G |
| m1_repos/ (克隆+CodeQL DB) | 19G |
| **剩余空间** | **~10G** |

**磁盘风险：仅剩 10GB，后续大仓库的 clone + CodeQL DB 创建可能导致磁盘满。需要关注。**

## 异常
1. **python/mypy CodeQL 查询全部失败**（exit code 2）— mypy 的 CodeQL DB 有问题，所有 instance 的 call_graph 查询均报错
2. **pdfminer/pdfminer clone 失败** — git clone 返回 128（仓库可能已被删除或迁移）
3. **pandas-dev/pandas clone 失败** — skip_log 中有多条 clone_failed 记录
4. **总 WARNING 数**: 18 条

## 预计完成时间
- 速率: ~2.8 repos/hour（33 repos / 11.7h）
- 剩余: ~98 repos
- **预计还需 ~35 小时（约 5/15 凌晨完成）**
- 注意: 大仓库会拉低速率；磁盘满可能提前终止
