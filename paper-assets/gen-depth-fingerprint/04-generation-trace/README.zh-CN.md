[English](README.md) | **简体中文**

# 生成记录

**深度剖析：对基础大语言模型文本的递归生成深度进行分类**

[可读 Markdown](readable/README.zh-CN.md) · [JSON 目录](catalog.json) · [来源归档索引](trace-index.csv)

在 GitHub 上快速查看时，可先打开可读 Markdown 页面。各页面按顺序展示记录中的用户指令、助手回复、工具调用和工具结果。需要完整的机器可读记录时，可使用 JSON 链接。

## 包含的资料

| 来源 | 文件数 |
|---|---:|
| 对话日志 | 353 |
| 工作智能体执行日志 | 769 |
| 任务结果记录 | 734 |
| 上下文与循环记录 | 100 |

**182,339 条消息或事件 · 6,269 个用户消息边界 · 75,064 条工具调用记录.**

用户角色条目可能来自其他智能体或系统，该角色不代表内容由人类撰写。封装在用户消息中的工作智能体工具结果标记为 `tool_result`，不会开始新一轮对话。首条用户消息之前的记录保留为独立的无边界序列。并行来源的日志分别保存，不会交错合并。

原始记录保留录入时的语言。Markdown 是同一份脱敏来源的阅读形式，不翻译或概括研究过程。JSON 提供完整的规范化导出，保留归档条目、出现次数、SHA-256 和来源行信息。较大的对话轮次使用链接的 JSON 分块；两种导出均不缩短消息正文。

## 可读生成记录页面

Markdown 页面按来源类型分组，文件名描述记录的任务或协作流程；按哈希分片的 JSON 文件夹仅用于底层存储。

- **对话日志** (353): [第 1 页](browse/conversation-001.md) · [第 2 页](browse/conversation-002.md) · [第 3 页](browse/conversation-003.md)
- **工作智能体执行日志** (769): [第 1 页](browse/worker-001.md) · [第 2 页](browse/worker-002.md) · [第 3 页](browse/worker-003.md) · [第 4 页](browse/worker-004.md) · [第 5 页](browse/worker-005.md) · [第 6 页](browse/worker-006.md)
- **任务结果记录** (734): [第 1 页](browse/result-001.md) · [第 2 页](browse/result-002.md) · [第 3 页](browse/result-003.md) · [第 4 页](browse/result-004.md) · [第 5 页](browse/result-005.md)
- **上下文与循环记录** (100): [第 1 页](browse/history-001.md)
