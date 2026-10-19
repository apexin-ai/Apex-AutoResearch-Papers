# AgentHPOBench × Moss v2 问题账本

本账本只记录可复现的 Harness/adapter 问题。它不记录模型 API key、Vast key、
hidden label 或私有 evaluator 输出。每条记录必须绑定 source/artifact/round hash，
并区分协议问题、环境问题、模型问题和架构问题。

## 初始审计项

| ID | 状态 | 类型 | 复现条件 | 影响 | 处理原则 |
|---|---|---|---|---|---|
| AHP-001 | OPEN | 协议适配 | strict codec 拒绝合法的 unchanged configuration | 末轮保守交付无法与官方协议一致 | 增加显式 keep 语义；保留默认严格模式和 fallback 证据 |
| AHP-002 | OPEN | 执行账本 | provider/evaluator exact-once dispatch 尚未绑定正式 journal | 无法证明调用未遗漏或未重复 | 先补 reserve/start/terminal/recovery receipt，再开正式 entitlement |
| AHP-003 | OPEN | 环境 | 30 个异构任务的数据、checkpoint、Conda/CUDA 环境未在目标 GPU 验证 | 只能做离线或局部 smoke | Vast 上逐题隔离，先做 Q7 qualification |
| AHP-004 | OPEN | Harness 设计 | Builder proposal 通过后，下层 compiled Harness 的实际生效路径需要逐字段核验 | 可能出现 artifact 变化但执行行为未变 | 记录 compiled scaffold、operational fingerprint 和 runtime receipt |
| AHP-005 | OPEN | 任务边界 | free-form room-selector 不适合 scalar codec | 强行转换会改变官方 action semantics | 专用 codec 或排除该任务并预注册 fresh split |
| AHP-006 | OBSERVED | 环境依赖 | 当前系统 Python 缺少 `anthropic`，v2 全量 pytest 在 3 个旧测试收集阶段失败 | 不能把全量回归误报为通过 | 不修改 benchmark 合同；使用已安装依赖环境或由操作者显式安装锁定依赖后重跑 |

## 卡顿升级规则

同一 failure category 连续两次发生，或同一节点累计阻塞超过一个完整工作日，
标记为 `ARCHITECTURE_REVIEW`。使用 Stanford CS329A 的依赖/回滚模块检查：

1. 是否缺少显式前置输入或 checkpoint；
2. 是否把不可逆动作放进自由搜索；
3. 是否把局部成功错误合并为全局成功；
4. 是否有明确 stop/recovery 条件；
5. 修复是否只改变 L1 Harness，而没有扩大 evaluator、hidden data、budget、gate 或 sandbox 权限。

修复必须先在离线 fixture、negative canary 和单题 smoke 中验证，再恢复正式 lane。
