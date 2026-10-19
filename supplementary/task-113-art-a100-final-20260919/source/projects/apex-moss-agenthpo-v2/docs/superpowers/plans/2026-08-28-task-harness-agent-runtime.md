# Moss Task Harness Agent Runtime Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended; or superpowers:executing-plans) to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在最新 `origin/main` 基线上，把已有的 V2 Task Harness 接成一个受控的工具型 Agent Harness，同时保持 Solver、工具和官方 evaluator 的责任边界。

**Architecture:** 继续复用 `TaskHarnessArtifact` 和内容寻址 lineage。Solver 模型只能返回受限的 JSON action（`tool` 或 `emit`），由固定 Python runtime 校验并调用 `ToolSession`；工具只能来自固定 registry，官方 evaluator 不进入 registry。旧的静态节点流程保持兼容，新 Agent 模式由 V2 `capabilities`/`router` 显式开启。

**Tech Stack:** Python 3.11+, dataclasses, JSON, pathlib, pytest.

---

### Task 1: 定义受限 Agent action 和失败语义

**Files:**
- Create: `optimization_lab/harness_builder/agent_runtime.py`
- Test: `tests/test_agent_runtime.py`

- [ ] **Step 1:** 写失败测试：验证 `emit`、合法 `tool`、未知工具、非法 JSON、重复 operation id 和预算耗尽的行为。
- [ ] **Step 2:** 运行聚焦测试，确认因模块不存在而失败：`python -m pytest -q tests/test_agent_runtime.py`。
- [ ] **Step 3:** 实现 `AgentAction`、`AgentTurn` 和 `AgentRuntime`，只接受 `{"action":"tool","tool":...,"arguments":...,"operation_id":...}` 或 `{"action":"emit","candidate":...}`。
- [ ] **Step 4:** 运行测试并确认通过。
- [ ] **Step 5:** 提交 `feat: add bounded Task Harness agent runtime`。

### Task 2: 将 Agent 模式接入现有 Task Harness Runtime

**Files:**
- Modify: `optimization_lab/harness_builder/dual_harness.py`
- Modify: `optimization_lab/harness_builder/__init__.py`
- Test: `tests/test_dual_harness.py`

- [ ] **Step 1:** 增加失败测试：V2 artifact 在 `capabilities.agent_mode=true` 时可运行动态 tool loop；静态 V1/V2 artifact 行为不变。
- [ ] **Step 2:** 实现显式 agent 节点配置和最大轮数边界，最终候选只能由 `emit` 产生。
- [ ] **Step 3:** 将每次模型 turn 和工具 receipt 接入公开 trace 摘要，不暴露参数/输出正文。
- [ ] **Step 4:** 运行 dual harness 回归测试。
- [ ] **Step 5:** 提交 `feat: connect agent runtime to Task Harness`。

### Task 3: 文档、审计和 Linux 验证

**Files:**
- Modify: `README.md`
- Modify: `PROGRESS.md`
- Test: `tests/test_tool_registry.py`, `tests/test_dual_harness.py`, `tests/test_agent_runtime.py`

- [ ] **Step 1:** 运行聚焦测试和 `git diff --check`。
- [ ] **Step 2:** 明确并发 operation id、daemon callable timeout 和 subprocess descendant cleanup 的已知边界，不宣称已完成严格崩溃一致性审计。
- [ ] **Step 3:** 在 AWS Linux 环境运行同一测试集。
- [ ] **Step 4:** 提交并重新 `git fetch --prune origin`，确认 `origin/main` 没有新提交后再同步到 `main`。
