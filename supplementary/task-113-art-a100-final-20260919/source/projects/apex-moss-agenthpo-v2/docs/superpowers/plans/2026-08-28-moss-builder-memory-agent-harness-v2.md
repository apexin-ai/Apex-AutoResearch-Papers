# Moss Builder Memory and Agent Task Harness V2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在最新 `main` 已有 rich Task Harness V2 上，补齐 Builder 的单题历史 Harness Memory、B-Frozen/B-online 隔离、Solver 动态工具调用与受控工作流、正式审计和 EdgeBench/ALE-Bench 接线，并保持旧实验证据可回放。

**Architecture:** 继续使用一个内容寻址的 `TaskHarnessArtifact`，其中 spec v1 保持不变，spec v2 继续承载 `interface / memory / capabilities / router / nodes`。动态 tool 能力通过扩展现有 `model_call` 节点的受控调用策略实现，工作流通过现有节点和 router/Workflow Registry 组织；不新增第二种 Harness artifact，也不要求新增 `agent_loop` 或 `workflow` 节点类型。外层仍固定为 `Task Harness → official evaluator → Builder Harness → commit/reject/rollback`，官方 evaluator 不进入 Solver 工具箱。

**Tech Stack:** Python 3.11+、dataclasses、JSON、hashlib、pathlib、OpenAI-compatible Responses API、pytest、EdgeBench/ALE-Bench 官方本地 evaluator。

---

## Latest-main baseline

最新 `main` 为 `bea29d3`，已经提供：

- spec v2 的 `interface`、`memory`、`capabilities`、`router`；
- `model_call / tool_call / skill_call / emit` 节点；
- 可进化的 role、Skill、Memory、工具声明与执行顺序；
- Builder 的 `changed_components` 记录；
- 最终模型节点不可删除的 benchmark 输出合同。

本计划不重复建立第二套 V2 artifact。仍需补齐的正式缺口是：

- Experiment 1 Builder 看不到 H0…Ht 的完整结构；
- B-Frozen/B-online 没有显式 Memory mode；
- Solver 只能执行 Builder 预先排好的静态工具节点，不能现场决定调用哪个工具；
- 多 Solver 模型节点仍复用一个 audit operation id；
- EdgeBench/ALE-Bench production 仍传入 `allowed_tools={}`；
- Responses transport 仍是 text-only。

## File map

**Create:**

- `optimization_lab/harness_builder/tool_registry.py`: 工具定义、权限、预算、路径隔离、调用 receipt。
- `optimization_lab/harness_builder/builder_memory.py`: B-Frozen/B-online 配置、清洗记录和 append-only 快照。
- `optimization_lab/harness_builder/agent_runtime.py`: 现有 `model_call` 节点内的动态 tool 循环与严格 JSON action transport。
- `optimization_lab/harness_builder/workflows.py`: 三个有边界工作流插件。
- `optimization_lab/harness_builder/experiment_one_tools.py`: EdgeBench/ALE-Bench 的公开 Tool Pack。
- `tests/test_tool_registry.py`
- `tests/test_agent_runtime.py`
- `tests/test_agent_workflows.py`
- `optimization_lab/harness_builder/manifests/experiment_one_edgebench_v2.json`
- `optimization_lab/harness_builder/manifests/experiment_one_alebench_v2.json`

**Modify:**

- `optimization_lab/harness_builder/dual_harness.py`
- `optimization_lab/harness_builder/builder_harness.py`
- `optimization_lab/harness_builder/experiment_one_audit.py`
- `optimization_lab/harness_builder/experiment_one_production.py`
- `optimization_lab/harness_builder/dual_runtime.py`
- `optimization_lab/openai_generator.py`
- `optimization_lab/harness_builder/__init__.py`
- `scripts/run_moss_experiment_one.py`
- `tests/test_dual_harness.py`
- `tests/test_dual_runtime.py`
- `tests/test_builder_harness.py`
- `tests/test_experiment_one_audit.py`
- `tests/test_experiment_one_production.py`
- `tests/test_experiment_one_cli.py`
- `tests/test_openai_responses_generator.py`
- `README.md`, `TEST.md`, `CLAUDE.md`, `PROGRESS.md`

## Task 1: Fix per-call audit identity

**Files:**
- Modify: `optimization_lab/harness_builder/experiment_one_audit.py:813-930`
- Modify: `optimization_lab/harness_builder/experiment_one_production.py:190-225`
- Test: `tests/test_experiment_one_audit.py`
- Test: `tests/test_experiment_one_production.py`

- [ ] **Step 1: Add the failing two-model-node regression test**

```python
def test_two_solver_nodes_receive_distinct_audit_operation_ids(tmp_path: Path) -> None:
    ids = ScopedOperationIdFactory("S1-B-round-02", "solver")
    assert ids.next("solve") == "S1-B-round-02-solver-solve-0000"
    assert ids.next("repair") == "S1-B-round-02-solver-repair-0001"
```

- [ ] **Step 2: Verify the current constant factory fails**

Run:

```bash
.venv/bin/python -m pytest -q tests/test_experiment_one_audit.py \
  tests/test_experiment_one_production.py -k "two_solver_nodes or operation_id"
```

Expected: FAIL because production currently returns the same `...-solver` id for every Solver call.

- [ ] **Step 3: Implement a deterministic scoped factory**

```python
@dataclass
class ScopedOperationIdFactory:
    round_id: str
    layer: str
    counter: int = 0

    def next(self, scope: str = "call") -> str:
        value = _safe_operation_id(
            f"{self.round_id}-{self.layer}-{scope}-{self.counter:04d}"
        )
        self.counter += 1
        return value
```

`AuditedGenerator` accepts the factory object and `TaskHarnessRuntime` passes the node id as scope. Replays use persisted results and do not regenerate ids or model calls.

- [ ] **Step 4: Run audit and production tests**

```bash
.venv/bin/python -m pytest -q tests/test_experiment_one_audit.py \
  tests/test_experiment_one_production.py -k "operation_id or replay"
```

Expected: PASS; every start/success pair has a unique id and completed replay makes zero delegate calls.

- [ ] **Step 5: Commit**

```bash
git add optimization_lab/harness_builder/experiment_one_audit.py \
  optimization_lab/harness_builder/experiment_one_production.py \
  tests/test_experiment_one_audit.py tests/test_experiment_one_production.py
git commit -m "fix: scope formal model call audit identities"
```

## Task 2: Give formal Builder full same-instance Harness history

**Files:**
- Modify: `optimization_lab/harness_builder/dual_harness.py:800-880`
- Modify: `optimization_lab/harness_builder/experiment_one_audit.py:95-180`
- Modify: `optimization_lab/harness_builder/builder_harness.py:630-670`
- Test: `tests/test_dual_harness.py`
- Test: `tests/test_experiment_one_audit.py`
- Test: `tests/test_builder_harness.py`

- [ ] **Step 1: Add failing visibility and leakage tests**

```python
def test_formal_builder_sees_full_h0_to_ht_specs_but_not_answers() -> None:
    view = experiment_one_builder_view(_inspection_with_h0_h1())
    assert [item["version"] for item in view["available_harnesses"]] == [1, 2]
    assert view["available_harnesses"][1]["spec"]["router"]["directive"]
    encoded = json.dumps(view, sort_keys=True)
    assert "RAW CANDIDATE" not in encoded
    assert "RAW MODEL OUTPUT" not in encoded
```

- [ ] **Step 2: Verify the formal projection currently drops history**

```bash
.venv/bin/python -m pytest -q tests/test_dual_harness.py \
  tests/test_experiment_one_audit.py tests/test_builder_harness.py \
  -k "available_harnesses or full_h0"
```

Expected: FAIL because `experiment_one_builder_view()` returns only current artifact and public runs.

- [ ] **Step 3: Project the complete current-instance experiment line**

```python
def experiment_line_artifacts(self) -> tuple[TaskHarnessArtifact, ...]:
    referenced = self.run_harness_hashes() | self.proposed_harness_hashes()
    artifacts = tuple(self.load_artifact(sha256) for sha256 in referenced)
    return tuple(sorted(artifacts, key=self.first_seen_order))
```

The workspace itself remains one benchmark/instance/seed experiment line. Each `available_harnesses` entry contains hash、version、parent、full public spec、`is_current`、public score/feedback summaries、commit/reject/rollback and adoption derived from append-only evidence. This preserves H1/H2 even if the Builder later branches from H0 to H3. Candidate content remains only `{sha256, length}` and node trace remains `{index, node_id, kind}`. Foreign workspace hashes are rejected.

- [ ] **Step 4: Update Builder prompt and run tests**

Builder text must say that `available_harnesses` contains only this instance lineage and may be selected by `source_sha256`.

```bash
.venv/bin/python -m pytest -q tests/test_dual_harness.py \
  tests/test_experiment_one_audit.py tests/test_builder_harness.py
```

Expected: PASS, including branching from H0 while H2 is current and rejecting a foreign lineage hash.

- [ ] **Step 5: Commit**

```bash
git add optimization_lab/harness_builder/dual_harness.py \
  optimization_lab/harness_builder/experiment_one_audit.py \
  optimization_lab/harness_builder/builder_harness.py \
  tests/test_dual_harness.py tests/test_experiment_one_audit.py tests/test_builder_harness.py
git commit -m "feat: expose same-instance Harness history to Builder"
```

## Task 3: Freeze instance-only Memory and isolate B-online

**Files:**
- Create: `optimization_lab/harness_builder/builder_memory.py`
- Modify: `optimization_lab/harness_builder/experiment_one_audit.py`
- Modify: `optimization_lab/harness_builder/experiment_one_production.py`
- Modify: `scripts/run_moss_experiment_one.py`
- Test: `tests/test_experiment_one_audit.py`
- Test: `tests/test_experiment_one_production.py`
- Test: `tests/test_experiment_one_cli.py`

- [ ] **Step 1: Add failing B-Frozen and B-online tests**

```python
def test_instance_only_rejects_cross_task_records() -> None:
    with pytest.raises(ValueError, match="instance-only"):
        BuilderMemoryConfig("instance_only", (_general_rule(),))

def test_cross_task_online_accepts_only_sanitized_rules() -> None:
    config = BuilderMemoryConfig("cross_task_online", (_general_rule(),))
    assert config.public_payload()["mode"] == "cross_task_online"

def test_online_snapshot_cannot_read_current_or_future_instance_records(tmp_path: Path) -> None:
    store = CrossTaskMemoryStore(tmp_path)
    snapshot = store.snapshot(before_order=3)
    assert all(record.source_order < 3 for record in snapshot.records)
```

- [ ] **Step 2: Confirm explicit mode is absent**

```bash
.venv/bin/python -m pytest -q tests/test_experiment_one_audit.py \
  tests/test_experiment_one_production.py tests/test_experiment_one_cli.py \
  -k "instance_only or cross_task_online"
```

Expected: FAIL because formal production has no `BuilderMemoryConfig`.

- [ ] **Step 3: Implement strict configuration**

```python
@dataclass(frozen=True)
class BuilderMemoryConfig:
    mode: Literal["instance_only", "cross_task_online"] = "instance_only"
    cross_task_records: tuple[Mapping[str, str], ...] = ()
```

`instance_only` requires an empty tuple. `cross_task_online` uses append-only `CrossTaskMemoryRecord` entries with an allowlist schema: `record_id / rule / source_benchmark / source_instance_hash / source_lineage_hash / source_round / source_order / distiller_version / sanitizer_version / record_sha256`. The rule is bounded plain text and rejects code fences, paths, candidate content, full Harness JSON, raw trace, hidden/private fields and identifiers that can reconstruct another instance. Production defaults to `instance_only`; only a B-online manifest can opt in, and Builder cannot change this experiment mode.

After a source instance finishes, an explicit post-instance distillation step uses a frozen distiller prompt/version to propose general rules. A deterministic sanitizer accepts or rejects each record and appends accepted records to the store. The next instance reads a content-addressed snapshot containing only records whose `source_order` is earlier than that instance; snapshot hash and provenance are written to the campaign receipt. B-Frozen never runs this reader.

- [ ] **Step 4: Verify new instances start empty**

```bash
.venv/bin/python -m pytest -q tests/test_experiment_one_audit.py \
  tests/test_experiment_one_production.py tests/test_experiment_one_cli.py -k "memory"
```

Expected: PASS; B-Frozen sees only its own H0…Ht, while B-online sees those plus sanitized general rules.

- [ ] **Step 5: Commit**

```bash
git add optimization_lab/harness_builder/experiment_one_audit.py \
  optimization_lab/harness_builder/experiment_one_production.py \
  scripts/run_moss_experiment_one.py tests/test_experiment_one_audit.py \
  tests/test_experiment_one_production.py tests/test_experiment_one_cli.py
git commit -m "feat: isolate frozen and online Builder memory"
```

## Task 4: Add the bounded Tool Registry

**Files:**
- Create: `optimization_lab/harness_builder/tool_registry.py`
- Modify: `optimization_lab/harness_builder/__init__.py`
- Test: `tests/test_tool_registry.py`

- [ ] **Step 1: Add failing permission, budget, path, and receipt tests**

```python
def test_registry_rejects_a_tool_outside_the_harness_allowlist(tmp_path: Path) -> None:
    registry = ToolRegistry(root=tmp_path, tools={"read_text": BoundTool.read_only(_read)})
    session = registry.bind(ToolPolicy(allow=("candidate_contract",), deny=(), max_calls=2))
    with pytest.raises(PermissionError, match="not allowed"):
        session.call("read_text", {"path": "task.txt"}, operation_id="r1-tool-0000")

def test_registry_stops_at_the_declared_call_budget(tmp_path: Path) -> None:
    session = _registry(tmp_path).bind(ToolPolicy(allow=("echo",), deny=(), max_calls=1))
    session.call("echo", {"text": "one"}, operation_id="r1-tool-0000")
    with pytest.raises(ToolBudgetError, match="call budget"):
        session.call("echo", {"text": "two"}, operation_id="r1-tool-0001")

def test_registry_rejects_paths_outside_the_run_root(tmp_path: Path) -> None:
    session = _registry(tmp_path).bind(ToolPolicy(allow=("read_text",), deny=(), max_calls=1))
    with pytest.raises(PermissionError, match="workspace root"):
        session.call("read_text", {"path": "../secret"}, operation_id="r1-tool-0000")

def test_registry_receipt_contains_hashes_not_file_contents(tmp_path: Path) -> None:
    receipt = _registry(tmp_path).bind(_policy()).call(
        "echo", {"text": "secret"}, operation_id="r1-tool-0000"
    ).receipt
    assert receipt.request_sha256 and receipt.result_sha256
    assert "secret" not in json.dumps(receipt.to_dict())
```

- [ ] **Step 2: Run the tests and verify RED**

```powershell
.\.venv\Scripts\python.exe -m pytest -q tests/test_tool_registry.py
```

Expected: collection fails because `tool_registry` does not exist.

- [ ] **Step 3: Implement immutable definitions and one bound session**

```python
@dataclass(frozen=True)
class ToolPolicy:
    allow: tuple[str, ...]
    deny: tuple[str, ...]
    max_calls: int
    max_output_bytes: int = 1_048_576
    timeout_seconds: int = 120

@dataclass(frozen=True)
class ToolCallResult:
    value: Any
    receipt: ToolCallReceipt

class ToolSession:
    def call(self, name: str, arguments: Mapping[str, Any], *, operation_id: str) -> ToolCallResult:
        definition = self._definitions.get(name)
        if definition is None or name not in self.policy.allow or name in self.policy.deny:
            raise PermissionError(f"Harness tool is not allowed: {name}")
        if self.calls_used >= self.policy.max_calls:
            raise ToolBudgetError("Task Harness tool call budget exhausted")
        self.calls_used += 1
        copied = _strict_json_copy(arguments, "tool arguments")
        definition.validate_arguments(copied)
        self.receipt_store.start(operation_id, name, copied, self.calls_used)
        try:
            value = definition.invoke_with_timeout(
                self.context, copied, timeout_seconds=self.policy.timeout_seconds
            )
            bounded = _bounded_json_copy(value, self.policy.max_output_bytes)
        except BaseException as exc:
            self.receipt_store.finish_error(operation_id, exc)
            raise
        receipt = self.receipt_store.finish_success(operation_id, bounded)
        return ToolCallResult(value=bounded, receipt=receipt)
```

`ToolRegistry.bind()` returns a new session per Task Harness run so budgets never leak across instances or rounds. The call budget is reserved before invocation, and started/success/error are append-only. Subprocess-backed tools use an OS-enforced timeout and terminate the child on expiry; bounded in-process tools are allowed only for audited pure operations that cannot block. Existing `Mapping[str, Callable]` tools are adapted as bounded in-memory tools for V1 compatibility.

Production receives three different roots: controller evidence, Solver-visible scratch, and evaluator-private. Path tools can resolve only inside Solver-visible scratch.

- [ ] **Step 4: Run Tool Registry and V1 compatibility tests**

```powershell
.\.venv\Scripts\python.exe -m pytest -q tests/test_tool_registry.py tests/test_dual_harness.py
```

Expected: PASS; existing static `tool_call` nodes continue to work.

- [ ] **Step 5: Commit**

```powershell
git add optimization_lab/harness_builder/tool_registry.py optimization_lab/harness_builder/__init__.py tests/test_tool_registry.py
git commit -m "feat: add bounded Task Harness tool registry"
```

## Task 5: Add one-request Responses tool-action transport

**Files:**
- Modify: `optimization_lab/openai_generator.py`
- Modify: `optimization_lab/harness_builder/experiment_one_audit.py`
- Test: `tests/test_openai_responses_generator.py`
- Test: `tests/test_experiment_one_audit.py`

- [ ] **Step 1: Add failing native, JSON, streaming, and no-retry tests**

```python
def test_agent_action_parses_native_function_call() -> None:
    result = _generator(_native_call("read_text", {"path": "task.txt"})).generate_agent_action(
        "inspect", model="gpt-test", tools=(_read_text_schema(),), protocol="native"
    )
    assert result.action == "tool"
    assert result.tool_name == "read_text"

def test_agent_action_parses_strict_json_fallback() -> None:
    result = _generator(_text('{"action":"final","content":"answer"}')).generate_agent_action(
        "finish", model="gpt-test", tools=(), protocol="json"
    )
    assert result.action == "final" and result.content == "answer"

def test_formal_agent_action_never_falls_back_after_provider_error() -> None:
    client = ScriptedClient(HTTPFailure(504), _text('{"action":"final","content":"late"}'))
    with pytest.raises(OpenAIResponsesError, match="status_code=504"):
        OpenAIResponsesGenerator(client=client, max_attempts=1, stream=True).generate_agent_action(
            "solve", model="gpt-test", tools=(), protocol="json"
        )
    assert len(client.responses.calls) == 1
```

- [ ] **Step 2: Run and verify RED**

```powershell
.\.venv\Scripts\python.exe -m pytest -q tests/test_openai_responses_generator.py tests/test_experiment_one_audit.py -k "agent_action or native_function or no_fallback"
```

Expected: FAIL because the transport only returns text.

- [ ] **Step 3: Implement typed actions and a separate protocol canary**

```python
@dataclass(frozen=True)
class ResponsesAgentAction:
    action: Literal["tool", "final"]
    content: str | None = None
    tool_name: str | None = None
    arguments: Mapping[str, Any] = field(default_factory=dict)
    call_id: str | None = None
    protocol: Literal["native", "json"] = "json"
    usage: Mapping[str, Any] = field(default_factory=dict)
```

`probe_tool_call_protocol()` is an explicit low-cost command/canary and writes its selected protocol to a receipt. A formal run receives the campaign-frozen protocol before the first Solver call. The protocol is external Runtime policy, is included in request hashes, and cannot be changed by Builder or a Task Harness proposal. `generate_agent_action()` performs exactly one provider request; API failure, textless response, invalid JSON, or invalid native call is surfaced and never triggers a second request or a protocol switch.

- [ ] **Step 4: Extend `AuditedGenerator` without exposing raw content**

`AuditedGenerator.generate_agent_action()` records one unique operation id, prompt hash, tool-schema hash, chosen protocol, action type and output hash. It delegates once and uses the same incomplete-operation fail-closed rule as `generate()`.

- [ ] **Step 5: Run transport and audit tests**

```powershell
.\.venv\Scripts\python.exe -m pytest -q tests/test_openai_responses_generator.py tests/test_experiment_one_audit.py
```

Expected: PASS, including streaming native events and strict JSON fallback.

- [ ] **Step 6: Commit**

```powershell
git add optimization_lab/openai_generator.py optimization_lab/harness_builder/experiment_one_audit.py tests/test_openai_responses_generator.py tests/test_experiment_one_audit.py
git commit -m "feat: support audited Responses tool actions"
```

## Task 6: Execute direct, dynamic-tool, workflow, and auto Task Harness paths

**Files:**
- Create: `optimization_lab/harness_builder/agent_runtime.py`
- Create: `optimization_lab/harness_builder/workflows.py`
- Modify: `optimization_lab/harness_builder/dual_harness.py`
- Modify: `optimization_lab/harness_builder/builder_harness.py`
- Modify: `optimization_lab/harness_builder/dual_runtime.py`
- Modify: `optimization_lab/harness_builder/__init__.py`
- Test: `tests/test_agent_runtime.py`
- Test: `tests/test_agent_workflows.py`
- Test: `tests/test_dual_harness.py`
- Test: `tests/test_dual_runtime.py`
- Test: `tests/test_builder_harness.py`

- [ ] **Step 1: Add failing schema and routing tests**

```python
@pytest.mark.parametrize("mode", ["direct", "agent_loop", "workflow", "auto"])
def test_v2_accepts_all_task_harness_execution_modes(mode: str) -> None:
    spec = TaskHarnessSpec.from_dict(_v2_spec(mode=mode))
    assert spec.router["mode"] == mode

def test_v1_rejects_dynamic_tool_fields_on_model_call() -> None:
    with pytest.raises(ValueError, match="schema 2"):
        TaskHarnessSpec.from_dict(_v1_spec_with_tool_mode_auto())

def test_builder_can_change_agent_loop_tools_and_budget() -> None:
    result = _builder_evolve(_proposal(changed_components=["capabilities", "router"]))
    assert result.status == "committed"
    assert _workspace().current().spec.capabilities["tool_policy"]["max_calls"] == 3
```

- [ ] **Step 2: Add failing execution tests**

```python
def test_agent_loop_may_call_a_tool_then_emit_final_candidate(tmp_path: Path) -> None:
    generator = ScriptedAgentGenerator(
        tool("candidate_contract", {}), final("strict candidate")
    )
    run = _runtime(generator, tmp_path).run(_agent_harness(), task="public task", model="m")
    assert run.candidate == "strict candidate"
    assert [event.kind for event in run.events] == ["agent_tool", "agent_final", "emit"]

def test_agent_loop_stops_before_exceeding_model_budget(tmp_path: Path) -> None:
    generator = ScriptedAgentGenerator(tool("echo", {"text": "again"}), tool("echo", {"text": "again"}))
    with pytest.raises(AgentBudgetError, match="model call budget"):
        _runtime(generator, tmp_path).run(_one_model_call_harness(), task="task", model="m")

def test_official_evaluator_is_not_registered_as_a_solver_tool(tmp_path: Path) -> None:
    assert "official_evaluator" not in _production_tool_registry(tmp_path).names()
```

- [ ] **Step 3: Run and verify RED**

```powershell
.\.venv\Scripts\python.exe -m pytest -q tests/test_agent_runtime.py tests/test_agent_workflows.py tests/test_dual_harness.py tests/test_dual_runtime.py tests/test_builder_harness.py -k "agent_loop or workflow or execution_mode or evaluator_is_not"
```

Expected: FAIL because V2 still supports only the static node sequence and existing `model_call` nodes cannot yet select tools at runtime.

- [ ] **Step 4: Extend the existing V2 schema, not the artifact envelope**

`TaskHarnessNode` keeps the existing node kinds and adds V2-only fields to `model_call`:

```python
tool_mode: Literal["none", "auto"] = "none"
tool_allowlist: tuple[str, ...] = ()
max_tool_calls: int = 0
response_mode: Literal["text", "strict_action_json"] = "text"
```

This keeps dynamic tool use inside the existing `TaskHarnessArtifact`; no second Solver/Agent artifact is introduced. The existing `TaskHarnessSpec.router` validates:

```python
{
    "mode": "direct" | "agent_loop" | "workflow" | "auto",
    "default_workflow": str | None,
    "allowed_workflows": list[str],
    "max_total_model_calls": int,
    "max_total_tool_calls": int,
    "max_total_steps": int
}
```

The existing `capabilities` validates `tool_policy`, timeout, and maximum output bytes. Effective permissions are the intersection of the model node allowlist, Task Harness capabilities, benchmark Tool Pack, and fixed campaign ceiling. Schema 1 remains byte-for-byte compatible and rejects the new fields.

- [ ] **Step 5: Implement the bounded Agent Loop**

```python
class AgentLoopRuntime:
    def run(self, request: AgentLoopRequest) -> AgentLoopResult:
        transcript: list[Mapping[str, Any]] = []
        for step_index in range(request.max_steps):
            action = request.generator.generate_agent_action(
                self._prompt(request, transcript),
                model=request.model,
                tools=request.tool_session.schemas(),
                protocol=request.protocol,
                scope=f"{request.node_id}-step-{step_index:04d}",
            )
            if action.action == "final":
                return AgentLoopResult(action.content, tuple(transcript))
            result = request.tool_session.call(
                action.tool_name,
                action.arguments,
                operation_id=request.operation_id_factory.next(
                    f"{request.node_id}-tool-{step_index:04d}"
                ),
            )
            transcript.append(self._public_tool_result(action, result))
        raise AgentBudgetError("Agent Loop exhausted its step budget without a final candidate")
```

Each transcript item contains action metadata and bounded public tool output; raw provider objects, hidden evaluator data, and unrestricted paths are never inserted.

- [ ] **Step 6: Implement three bounded workflows**

`WorkflowRegistry.default()` registers exactly three execution-order templates over existing model/tool/skill/emit nodes; it does not introduce a new node kind:

```python
WorkflowSpec("direct_solve", ("solve", "emit"))
WorkflowSpec("inspect_plan_execute", ("inspect", "plan", "execute", "emit"))
WorkflowSpec("implement_test_repair_verify", ("inspect", "implement", "public_check", "repair", "verify", "emit"))
```

`auto` performs one strict, audited Solver route action that chooses only among `allowed_workflows`; this consumes the enclosing model/step budget and uses the campaign-frozen transport. Python validates and records the choice but does not invent it. Each workflow declares semantic slots plus explicit node-id bindings; Gate rejects missing, renamed, duplicated, or incompatible bindings. A workflow may use a static model node or a dynamic-tool-enabled `model_call`, but cannot add tools or exceed the enclosing Harness budget.

- [ ] **Step 7: Bind output contracts to every final-producing path**

The existing authoritative output-contract block is appended to the final direct model call, Agent Loop final prompt, and workflow final step. Builder proposals that remove or shadow it fail the Gate.

- [ ] **Step 8: Run runtime tests and the old V1 suite**

```powershell
.\.venv\Scripts\python.exe -m pytest -q tests/test_agent_runtime.py tests/test_agent_workflows.py tests/test_dual_harness.py tests/test_dual_runtime.py tests/test_builder_harness.py
```

Expected: PASS, including old static V1 traces.

- [ ] **Step 9: Commit**

```powershell
git add optimization_lab/harness_builder/agent_runtime.py optimization_lab/harness_builder/workflows.py optimization_lab/harness_builder/dual_harness.py optimization_lab/harness_builder/builder_harness.py optimization_lab/harness_builder/dual_runtime.py optimization_lab/harness_builder/__init__.py tests/test_agent_runtime.py tests/test_agent_workflows.py tests/test_dual_harness.py tests/test_dual_runtime.py tests/test_builder_harness.py
git commit -m "feat: run tool-using Agent Task Harnesses"
```

## Task 7: Bind EdgeBench and ALE-Bench V2 tool packs

**Files:**
- Create: `optimization_lab/harness_builder/experiment_one_tools.py`
- Create: `optimization_lab/harness_builder/manifests/experiment_one_edgebench_v2.json`
- Create: `optimization_lab/harness_builder/manifests/experiment_one_alebench_v2.json`
- Modify: `optimization_lab/harness_builder/experiment_one_production.py`
- Modify: `scripts/run_moss_experiment_one.py`
- Test: `tests/test_experiment_one_production.py`
- Test: `tests/test_experiment_one_cli.py`
- Test: `tests/test_edgebench_official_adapter.py`
- Test: `tests/test_alebench_official_adapter.py`

- [ ] **Step 1: Add failing tool-pack and manifest tests**

```python
def test_edge_tool_pack_contains_only_public_bounded_tools(tmp_path: Path) -> None:
    pack = edgebench_tool_pack(tmp_path, submission_path="solution.py")
    assert set(pack.names()) == {"candidate_contract", "read_text", "write_candidate", "python_syntax_check"}

def test_ale_tool_pack_contains_only_public_bounded_tools(tmp_path: Path) -> None:
    pack = alebench_tool_pack(tmp_path, submission_path="main.cpp", compiler="g++")
    assert set(pack.names()) == {"candidate_contract", "read_text", "write_candidate", "cpp_compile_check"}

def test_v2_manifests_do_not_change_the_frozen_v1_manifests() -> None:
    assert _sha("experiment_one_edgebench.json") == FROZEN_MANIFEST_SHA256["edgebench"]
    assert _sha("experiment_one_alebench.json") == FROZEN_MANIFEST_SHA256["alebench"]
    assert load_manifest("experiment_one_edgebench_v2.json").harness_schema_version == 2
```

- [ ] **Step 2: Run and verify RED**

```powershell
.\.venv\Scripts\python.exe -m pytest -q tests/test_experiment_one_production.py tests/test_experiment_one_cli.py -k "tool_pack or v2_manifest or frozen_v1"
```

Expected: FAIL because production currently passes `allowed_tools={}` and the V2 manifests do not exist.

- [ ] **Step 3: Implement benchmark-specific public tools**

EdgeBench tools may read public task files, write only the designated candidate path, and run `python -m py_compile` in the per-round sandbox. ALE-Bench tools may do the same and run one bounded C++23 compile. Neither pack contains `sforge eval`, `public_eval`, a private evaluator, hidden tests, arbitrary network, or unrestricted shell.

- [ ] **Step 4: Add new V2 manifests with explicit budgets**

Both V2 H0 artifacts use `router.mode="auto"`, permit `direct_solve` and `inspect_plan_execute`, declare the benchmark tool allowlist, bind `instance_only` Builder Memory, and preserve the existing A/B/C mapping, models, public evaluator contract, and resource envelope. The old manifest bytes and frozen SHA values remain unchanged.

- [ ] **Step 5: Bind one tool session per round and cross-test cell**

`EdgeLineageRoundExecutor` and `ALELineageRoundExecutor` create an isolated run directory, bind the manifest policy, and pass the session to `TaskHarnessRuntime`. Cross-test uses the frozen Harness's policy against the target benchmark's own tool pack; no source-instance files are transferred.

- [ ] **Step 6: Run production and adapter tests**

```powershell
.\.venv\Scripts\python.exe -m pytest -q tests/test_experiment_one_production.py tests/test_experiment_one_cli.py tests/test_edgebench_official_adapter.py tests/test_alebench_official_adapter.py
```

Expected: PASS; V1 and V2 manifests are both loadable, and only V2 can enable tools.

- [ ] **Step 7: Commit**

```powershell
git add optimization_lab/harness_builder/experiment_one_tools.py optimization_lab/harness_builder/manifests/experiment_one_edgebench_v2.json optimization_lab/harness_builder/manifests/experiment_one_alebench_v2.json optimization_lab/harness_builder/experiment_one_production.py scripts/run_moss_experiment_one.py tests/test_experiment_one_production.py tests/test_experiment_one_cli.py tests/test_edgebench_official_adapter.py tests/test_alebench_official_adapter.py
git commit -m "feat: enable public tools for EdgeBench and ALE-Bench"
```

## Task 8: Complete replay, adoption, and error audit evidence

**Files:**
- Modify: `optimization_lab/harness_builder/dual_runtime.py`
- Modify: `optimization_lab/harness_builder/dual_harness.py`
- Modify: `optimization_lab/harness_builder/experiment_one_audit.py`
- Modify: `optimization_lab/harness_builder/experiment_one_production.py`
- Test: `tests/test_dual_runtime.py`
- Test: `tests/test_experiment_one_audit.py`
- Test: `tests/test_experiment_one_production.py`

- [ ] **Step 1: Add failing request-binding and replay tests**

```python
def test_round_request_hash_binds_actual_harness_tool_pack_policy_and_protocol() -> None:
    first = _request_hash(harness="a" * 64, tool_pack="b" * 64, policy="c" * 64, protocol="json")
    assert first != _request_hash(harness="d" * 64, tool_pack="b" * 64, policy="c" * 64, protocol="json")
    assert first != _request_hash(harness="a" * 64, tool_pack="e" * 64, policy="c" * 64, protocol="json")
    assert first != _request_hash(harness="a" * 64, tool_pack="b" * 64, policy="f" * 64, protocol="json")
    assert first != _request_hash(harness="a" * 64, tool_pack="b" * 64, policy="c" * 64, protocol="native")

def test_replay_does_not_repeat_model_tool_or_evaluator_calls(tmp_path: Path) -> None:
    first = _run_round(tmp_path)
    second = _run_round(tmp_path)
    assert second == first
    assert _call_counts(tmp_path) == {"builder": 1, "solver": 2, "tool": 1, "evaluator": 1}
```

- [ ] **Step 2: Add failing Harness-adoption evidence tests**

```python
def test_committed_harness_is_the_one_used_by_the_next_round(tmp_path: Path) -> None:
    round_one = _run_committing_round(tmp_path, "round-01")
    round_two = _run_round(tmp_path, "round-02")
    assert round_one.next_harness_sha256 == round_two.harness_sha256
    adoption = _adoption_receipt(tmp_path, prior_round="round-01", next_round="round-02")
    assert adoption["actually_used_next_round"] is True

def test_rejected_or_rolled_back_harness_is_not_marked_adopted(tmp_path: Path) -> None:
    receipt = _run_rejected_round(tmp_path)
    assert receipt["candidate_harness_sha256"]
    assert receipt["next_harness_sha256"] == receipt["used_harness_sha256"]
    assert _adoption_receipts(tmp_path) == ()
```

- [ ] **Step 3: Add failing formal-error tests**

```python
@pytest.mark.parametrize("stage", ["api", "solver_format", "harness_gate", "evaluator"])
def test_formal_errors_are_preserved_and_never_recorded_as_zero(stage: str, tmp_path: Path) -> None:
    with pytest.raises(RuntimeError):
        _run_failing_stage(stage, tmp_path)
    evidence = _error_evidence(tmp_path, stage)
    assert evidence["status"] == "error"
    assert evidence["score"] is None
    assert evidence["provider_attempts"] == 1
```

- [ ] **Step 4: Run and verify RED**

```powershell
.\.venv\Scripts\python.exe -m pytest -q tests/test_dual_runtime.py tests/test_experiment_one_audit.py tests/test_experiment_one_production.py -k "request_hash or replay_does_not or actually_used or never_recorded_as_zero"
```

Expected: FAIL because request identity and round receipts do not yet include every dynamic Harness binding.

- [ ] **Step 5: Persist the complete public execution identity**

The round request and solver result bind the used Harness SHA, Tool Pack SHA, execution-policy SHA, tool transport, output-contract SHA and real model/tool call counts. Public traces store node/tool ids, hashes, bounded status summaries, budget consumption and workflow selection; full tool content is not exposed to Builder.

- [ ] **Step 6: Record commit/reject/rollback and delayed adoption**

Round `t` immutably records the used Ht, Builder candidate Ht+1 and `next_harness_sha256`. Round `t+1` immutably records its `used_harness_sha256` plus a backlink to round `t`. Python then appends a separate content-addressed adoption receipt; it never rewrites the old round receipt. The Builder view derives `actually_used_next_round` from these immutable bindings, not from proposal text.

- [ ] **Step 7: Preserve formal failures without retry or zero conversion**

Every formal stage writes a sanitized error type/status and keeps `score=null`. Started-without-result operations remain fail closed; replay returns only completed durable results and never re-executes a model, tool, or evaluator call.

- [ ] **Step 8: Run audit and replay tests**

```powershell
.\.venv\Scripts\python.exe -m pytest -q tests/test_dual_runtime.py tests/test_experiment_one_audit.py tests/test_experiment_one_production.py
```

Expected: PASS.

- [ ] **Step 9: Commit**

```powershell
git add optimization_lab/harness_builder/dual_runtime.py optimization_lab/harness_builder/dual_harness.py optimization_lab/harness_builder/experiment_one_audit.py optimization_lab/harness_builder/experiment_one_production.py tests/test_dual_runtime.py tests/test_experiment_one_audit.py tests/test_experiment_one_production.py
git commit -m "feat: audit Harness adoption and tool execution"
```

## Task 9: Document, verify, smoke test, and publish

**Files:**
- Modify: `README.md`
- Modify: `TEST.md`
- Modify: `CLAUDE.md`
- Modify: `PROGRESS.md`
- Modify: `docs/superpowers/specs/2026-08-28-moss-builder-memory-agent-harness-v2-design.md`

- [ ] **Step 1: Update the architecture documentation**

Document the runtime boundary in plain language:

```text
fixed Builder Harness
→ inspect current instance H0…Ht, score, feedback and adoption evidence
→ propose a changed Task Harness
→ Python validates/probes/commits or rolls back
→ next round runs the committed Task Harness
→ Solver chooses direct answer or allowed tools inside bounded execution
→ external official evaluator scores the final candidate once
```

State explicitly that Solver is the model called by Task Harness, not the Harness itself; B-Frozen defaults to `instance_only`; only B-online enables sanitized cross-task Memory.

- [ ] **Step 2: Run the focused complete suite**

```powershell
.\.venv\Scripts\python.exe -m pytest -q tests/test_tool_registry.py tests/test_agent_runtime.py tests/test_agent_workflows.py tests/test_dual_harness.py tests/test_dual_runtime.py tests/test_builder_harness.py tests/test_experiment_one_audit.py tests/test_experiment_one_production.py tests/test_experiment_one_cli.py tests/test_openai_responses_generator.py tests/test_edgebench_official_adapter.py tests/test_alebench_official_adapter.py
```

Expected: PASS with zero failures.

- [ ] **Step 3: Run the repository regression suite**

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

Expected: PASS. If optional external dependencies cause skips, record the exact skip count; any failure blocks publication.

- [ ] **Step 4: Check repository safety**

```powershell
git status --short
git diff --check
git grep -n -I -E "(sk-[A-Za-z0-9_-]{16,}|LLM_API_KEY=[REDACTED]" -- . ':!docs/superpowers/plans/*'
```

Expected: only intended source/test/doc/manifest files are changed; no key, `.env`, AWS evidence, old experiment result, `.venv`, or `.codex-transfer-20260828` content is tracked.

- [ ] **Step 5: Commit documentation**

```powershell
git add README.md TEST.md CLAUDE.md PROGRESS.md docs/superpowers/specs/2026-08-28-moss-builder-memory-agent-harness-v2-design.md
git commit -m "docs: explain complete Moss Builder and Task Harness"
```

- [ ] **Step 6: Run a protocol canary on AWS without starting a campaign**

On the existing AWS Experiment One host, clone or fetch this branch into a new directory, use the injected `LLM_API_KEY` and `LLM_BASE_URL`, and run one low-output Responses tool-call canary. Freeze `native` or `json` in the V2 campaign receipt. A 504/API error is reported verbatim and is not retried.

- [ ] **Step 7: Run one EdgeBench and one ALE-Bench V2 smoke round**

Use new artifact roots so no old Experiment One evidence is overwritten. Confirm for each benchmark: H0 loads, the Solver path runs, any tool is allowlisted and audited, the final candidate satisfies the contract, the external official evaluator runs once, and the Builder's proposed next Harness is committed/rejected/rolled back with a durable receipt. Stop on the first formal error without retrying or writing score 0.

- [ ] **Step 8: Review the branch diff and commit history**

```powershell
git diff --stat origin/main...HEAD
git log --oneline --decorate origin/main..HEAD
```

Expected: the branch contains only the approved Moss V2 work and preserves all pre-existing `main` commits.

- [ ] **Step 9: Fast-forward local main and push the exact tested commit**

```powershell
git -C C:\Users\Huawei\Documents\Moss\apex-moss merge --ff-only codex/moss-agent-harness-v2
git -C C:\Users\Huawei\Documents\Moss\apex-moss push origin main
```

- [ ] **Step 10: Verify publication**

```powershell
git -C C:\Users\Huawei\Documents\Moss\apex-moss fetch origin main
git -C C:\Users\Huawei\Documents\Moss\apex-moss rev-parse HEAD
git -C C:\Users\Huawei\Documents\Moss\apex-moss rev-parse origin/main
```

Expected: both hashes are identical and the local untracked `.codex-transfer-20260828/` directory remains untouched.

## Final acceptance checklist

- [ ] Builder sees the complete public H0…Ht structure only for the current instance lineage.
- [ ] Builder never sees candidate answer text, raw model/node I/O, hidden tests, private evaluator fields, or another lineage.
- [ ] B-Frozen starts every new instance with `instance_only` and empty cross-task Memory.
- [ ] B-online must explicitly select `cross_task_online` and accepts only sanitized general rules.
- [ ] Solver can directly answer, dynamically call an allowlisted tool, or use a bounded workflow selected by the Task Harness.
- [ ] Builder can evolve role, prompt, tool permission, workflow, router, lower Task Harness current-instance session-memory policy, and budgets within the fixed campaign ceiling; it cannot change the experiment's `instance_only/cross_task_online` mode or transport protocol.
- [ ] Every model and tool call has a unique, replayable operation id.
- [ ] A committed Ht+1 is proven to be the Harness actually used in the next round.
- [ ] The official evaluator remains outside the Agent Loop and executes at most once per completed formal round.
- [ ] API, Solver, format, Gate, and evaluator errors are preserved, not retried, and never written as score 0.
- [ ] Old schema-1 artifacts, receipts, manifests, and Experiment One evidence remain readable and unchanged.
- [ ] EdgeBench and ALE-Bench smoke tests produce complete audit receipts in new AWS artifact roots.
- [ ] The tested commit is the exact commit pushed to `apexin-ai/apex-moss:main`.
