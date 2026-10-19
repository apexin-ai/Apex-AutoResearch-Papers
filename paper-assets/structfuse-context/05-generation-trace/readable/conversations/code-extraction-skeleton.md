# code extraction skeleton

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_code_extraction_skeleton_20260512T100103.jsonl`
- **Structured JSON:** [`7c115ce0244db507541a.json`](../../sessions/7c/7c115ce0244db507541a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-12T10:04:39.828086+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/docs/IDEA_BRIEF.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_extraction_skeleton_20260512T100103",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/docs/IDEA_BRIEF.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-12T10:04:39.828588+00:00_

1	# Idea Brief: StructFuse: Data-Flow-Aware Contrastive Retrieval for Repository-Level Code Repair Context Selection
2	
3	
4	- **Idea ID**: `idea_006`
5	- **Created**: 2026-05-10
6	- **Approved**: 2026-05-12
7	- **Source**: web_research
8	- **Level**: top-tier
9	- **Target Venues**: EMNLP 2026 Main + Findings (ARR submission deadline: May 25, 2026; conference: Fall 2026; topic area: 'NLP and Code Models'; dual-targeting Main and Findings to de-risk rejection given empirical contribution type)
10	
11	## Seed Topic
12	
13	Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: NLP and Code Models.
14	
15	Direction: Code understanding and generation — repo-level comprehension, program repair, code reasoning, debugging, test generation, code-to-documentation, cross-language code transfer. NOT just code completion — focus on higher-level code reasoning tasks.
16	
17	Contribution type: METHOD ONLY. Propose new training methods, retrieval-augmented code repair, or inference algorithms for code tasks. Not a new benchmark or leaderboard entry.
18	
19	HARD CONSTRAINTS:
20	1. Compute: ≤200 H100-hours total. Code models are often evaluated zero-shot or few-shot — budget goes to SFT/LoRA if fine-tuning.
21	2. Time: ≤16 days. Build on existing code models (DeepSeek-Coder-V2, StarCoder2, CodeLlama, Qwen2.5-Coder) and frameworks (aider, SWE-agent, Moatless).
22	3. Eval: SWE-bench Verified, HumanEval/MBPP, CrossCodeEval, RepoBench, DebugBench, CodeContests.
23	
24	Look for: repo-level context compression for code understanding, retrieval-augmented repair with semantic code search, code reasoning via execution feedback, cross-repo transfer learning. Avoid: simple prompt templates for code completion.
25	
26	Tag: direction=code_models, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].
27	
28	## Generation Journey
29	
30	1. **Start** — 开始生成，seed: 'Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days fro
…[truncated 37855 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_extraction_skeleton_20260512T100103",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-12T10:04:39.828861+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction/codeql_queries",
  "description": "Create extraction directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_extraction_skeleton_20260512T100103",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction/codeql_queries",
    "description": "Create extraction directories"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-12T10:04:39.829010+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_extraction_skeleton_20260512T100103",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-12T10:04:39.829200+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction/codeql_queries/call_graph.ql",
  "content": "/**\n * @name 2-hop call graph extraction from buggy function\n * @description Extracts all functions within 2 call-graph hops (both caller and callee\n *              directions) of a specified buggy function. Outputs JSON-compatible tuples\n *              for downstream scope-bounded data-flow analysis.\n * @kind problem\n * @id structfuse/call-graph-2hop\n * @problem.severity recommendation\n * @precision medium\n * @tags structfuse call-graph extraction\n */\n\nimport python\nimport semmle.python.pointsto.PointsTo\n\n// Buggy function location injected via external predicates (populated by CLI --external).\n// Usage: codeql database analyze ... --external buggyFunctionName=&lt;name> --external buggyFileName=&lt;relpath>\nexternal string buggyFunctionName();\nexternal string buggyFileName();\n\n/**\n * Matches the single buggy function specified by external predicates.\n */\npredicate isBuggyFunction(Function f) {\n  f.getName() = buggyFunctionName() and\n  f.getLocation().getFile().getRelativePath() = buggyFileName()\n}\n\n/**\n * Direct call edge: `caller` contains a call site that resolves to `callee`.\n * Uses points-to analysis for call target resolution where available,\n * falls back to name-based matching for unresolved calls.\n */\npredicate directCallEdge(Function caller, Function callee) {\n  exists(CallNode call |\n    call.getScope() = caller and\n    (\n      // Points-to resolved: call target is known\n      exists(FunctionObject fo |\n        call.getFunction().pointsTo(fo) and\n        fo.getFunction() = callee\n      )\n      or\n      // Name-based fallback for unresolved calls within the same module\n      exists(NameNode nameNode |\n        call.getFunction() = nameNode and\n        callee.getName() = nameNode.getId() and\n        callee.getEnclosingModule() = caller.getEnclosingModule() and\n        not exists(FunctionObject fo | call.getFunction().pointsTo(fo))\n      )\n    )\n  ) and\n  caller != callee\n}\n\n/**\n * 1-hop: functions directly called by or calling the buggy function.\n */\npredicate hop1(Function f, string direction) {\n  exists(Function buggy |\n    isBuggyFunction(buggy) and\n    (\n      directCallEdge(buggy, f) and direction = \"callee\"\n      or\n      directCallEdge(f, buggy) and direction = \"caller\"\n    )\n  )\n}\n\n/**\n * 2-hop: functions one additional step from any 1-hop function.\n */\npredicate hop2(Function f, string direction) {\n  exists(Function mid |\n    hop1(mid, _) and\n    (\n      directCallEdge(mid, f) and direction = \"callee\"\n      or\n      directCallEdge(f, mid) and direction = \"caller\"\n    ) and\n    not isBuggyFunction(f) and\n    not hop1(f, _)\n  )\n}\n\n/**\n * All functions within 2 hops, with hop distance and direction.\n */\npredicate inScope(Function f, int hopDistance, string direction) {\n  isBuggyFunction(f) and hopDistance = 0 and direction = \"origin\"\n  or\n  hop1(f, direction) and hopDistance = 1\n  or\n  hop2(f, direction) and hopDistance = 2\n}\n\nfrom Function f, int hopDistance, string direction, File file, int startLine, int endLine\nwhere\n  inScope(f, hopDistance, direction) and\n  file = f.getLocation().getFile() and\n  startLine = f.getLocation().getStartLine() and\n  endLine = f.getLocation().getEndLine()\nselect\n  f.getName() as target_func,\n  hopDistance as hop_distance,\n  direction,\n  file.getRelativePath() as file_path,\n  startLine as start_line,\n  endLine as end_line\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_extraction_skeleton_20260512T100103",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction/codeql_queries/call_graph.ql",
    "content": "/**\n * @name 2-hop call graph extraction from buggy function\n * @description Extracts all functions within 2 call-graph hops (both caller and callee\n *              directions) of a specified buggy function. Outputs JSON-compatible tuples\n *              for downstream scope-bounded data-flow analysis.\n * @kind problem\n * @id structfuse/call-graph-2hop\n * @problem.severity recommendation\n * @precision medium\n * @tags structfuse call-graph extraction\n */\n\nimport python\nimport semmle.python.pointsto.PointsTo\n\n// Buggy function location injected via external predicates (populated by CLI --external).\n// Usage: codeql database analyze ... --external buggyFunctionName=&lt;name> --external buggyFileName=&lt;relpath>\nexternal string buggyFunctionName();\nexternal string buggyFileName();\n\n/**\n * Matches the single buggy function specified by external predicates.\n */\npredicate isBuggyFunction(Function f) {\n  f.getName() = buggyFunctionName() and\n  f.getLocation().getFile().getRelativePath() = buggyFileName()\n}\n\n/**\n * Direct call edge: `caller` contains a call site that resolves to `callee`.\n * Uses points-to analysis for call target resolution where available,\n * falls back to name-based matching for unresolved calls.\n */\npredicate directCallEdge(Function caller, Function callee) {\n  exists(CallNode call |\n    call.getScope() = caller and\n    (\n      // Points-to resolved: call target is known\n      exists(FunctionObject fo |\n        call.getFunction().pointsTo(fo) and\n        fo.getFunction() = callee\n      )\n      or\n      // Name-based fallback for unresolved calls within the same module\n      exists(NameNode nameNode |\n        call.getFunction() = nameNode and\n        callee.getName() = nameNode.getId() and\n        callee.getEnclosingModule() = caller.getEnclosingModule() and\n        not exists(FunctionObject fo | call.getFunction().pointsTo(fo))\n      )\n    )\n  ) and\n  caller != callee\n}\n\n/**\n * 1-hop: functions directly called by or calling the buggy function.\n */\npredicate hop1(Function f, string direction) {\n  exists(Function buggy |\n    isBuggyFunction(buggy) and\n    (\n      directCallEdge(buggy, f) and direction = \"callee\"\n      or\n      directCallEdge(f, buggy) and direction = \"caller\"\n    )\n  )\n}\n\n/**\n * 2-hop: functions one additional step from any 1-hop function.\n */\npredicate hop2(Function f, string direction) {\n  exists(Function mid |\n    hop1(mid, _) and\n    (\n      directCallEdge(mid, f) and direction = \"callee\"\n      or\n      directCallEdge(f, mid) and direction = \"caller\"\n    ) and\n    not isBuggyFunction(f) and\n    not hop1(f, _)\n  )\n}\n\n/**\n * All functions within 2 hops, with hop distance and direction.\n */\npredicate inScope(Function f, int hopDistance, string direction) {\n  isBuggyFunction(f) and hopDistance = 0 and direction = \"origin\"\n  or\n  hop1(f, direction) and hopDistance = 1\n  or\n  hop2(f, direction) and hopDistance = 2\n}\n\nfrom Function f, int hopDistance, string direction, File file, int startLine, int endLine\nwhere\n  inScope(f, hopDistance, direction) and\n  file = f.getLocation().getFile() and\n  startLine = f.getLocation().getStartLine() and\n  endLine = f.getLocation().getEndLine()\nselect\n  f.getName() as target_func,\n  hopDistance as hop_distance,\n  direction,\n  file.getRelativePath() as file_path,\n  startLine as start_line,\n  endLine as end_line\n"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-12T10:04:39.829382+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction/codeql_queries/call_graph.ql

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_extraction_skeleton_20260512T100103",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-12T10:04:39.829528+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction/codeql_queries/bounded_dataflow.ql",
  "content": "/**\n * @name Scope-bounded inter-procedural data-flow analysis\n * @description Tracks data-flow from parameters/return values of functions within\n *              2 call-graph hops of the buggy function to variable reads in the same\n *              scope. Sources and sinks are restricted BEFORE evaluation to prevent\n *              Cartesian-product blowup.\n * @kind path-problem\n * @id structfuse/bounded-dataflow\n * @problem.severity recommendation\n * @precision medium\n * @tags structfuse data-flow inter-procedural\n * @timeout 300\n * @ram 8192\n */\n\nimport python\nimport semmle.python.dataflow.new.DataFlow\nimport semmle.python.dataflow.new.TaintTracking\nimport semmle.python.pointsto.PointsTo\nimport semmle.python.ApiGraphs\n\n// -- Reuse call-graph scope predicates --\n\nexternal string buggyFunctionName();\nexternal string buggyFileName();\n\npredicate isBuggyFunction(Function f) {\n  f.getName() = buggyFunctionName() and\n  f.getLocation().getFile().getRelativePath() = buggyFileName()\n}\n\npredicate directCallEdge(Function caller, Function callee) {\n  exists(CallNode call |\n    call.getScope() = caller and\n    (\n      exists(FunctionObject fo |\n        call.getFunction().pointsTo(fo) and\n        fo.getFunction() = callee\n      )\n      or\n      exists(NameNode nameNode |\n        call.getFunction() = nameNode and\n        callee.getName() = nameNode.getId() and\n        callee.getEnclosingModule() = caller.getEnclosingModule() and\n        not exists(FunctionObject fo | call.getFunction().pointsTo(fo))\n      )\n    )\n  ) and\n  caller != callee\n}\n\npredicate hop1(Function f) {\n  exists(Function buggy |\n    isBuggyFunction(buggy) and\n    (directCallEdge(buggy, f) or directCallEdge(f, buggy))\n  )\n}\n\npredicate hop2(Function f) {\n  exists(Function mid |\n    hop1(mid) and\n    (directCallEdge(mid, f) or directCallEdge(f, mid)) and\n    not isBuggyFunction(f) and\n    not hop1(f)\n  )\n}\n\n/** Function is within 2 call-graph hops of the buggy function. */\npredicate inScopeFunction(Function f) {\n  isBuggyFunction(f) or hop1(f) or hop2(f)\n}\n\n// -- Scope-bounded data-flow configuration --\n\nmodule BoundedFlowConfig implements DataFlow::ConfigSig {\n  /**\n   * Sources: parameters and return values of in-scope functions only.\n   * This bounds the analysis BEFORE evaluation, preventing blowup.\n   */\n  predicate isSource(DataFlow::Node node) {\n    // Function parameters within scope\n    exists(Function f, Parameter p |\n      inScopeFunction(f) and\n      p = f.getAnArg() and\n      node.asExpr() = p.asName().getAFlowNode()\n    )\n    or\n    // Return values of in-scope functions (at call sites)\n    exists(Function f, CallNode call |\n      inScopeFunction(f) and\n      exists(FunctionObject fo |\n        fo.getFunction() = f and\n        call.getFunction().pointsTo(fo)\n      ) and\n      node.asCfgNode() = call\n    )\n  }\n\n  /**\n   * Sinks: variable reads within in-scope functions.\n   */\n  predicate isSink(DataFlow::Node node) {\n    exists(Function f, NameNode nameRead |\n      inScopeFunction(f) and\n      nameRead.getScope() = f and\n      nameRead.isLoad() and\n      node.asCfgNode() = nameRead\n    )\n  }\n}\n\nmodule BoundedFlow = DataFlow::Global&lt;BoundedFlowConfig>;\n\nimport BoundedFlow::PathGraph\n\nfrom BoundedFlow::PathNode source, BoundedFlow::PathNode sink, int pathLength\nwhere\n  BoundedFlow::flowPath(source, sink) and\n  // Approximate path length by counting intermediate nodes\n  pathLength = count(BoundedFlow::PathNode mid |\n    BoundedFlow::flowPath(source, mid) and\n    BoundedFlow::flowPath(mid, sink) and\n    mid != source and mid != sink\n  ) + 1\nselect\n  sink.getNode(),\n  source,\n  sink,\n  source.getNode().getLocation().getFile().getRelativePath() as source_file,\n  source.getNode().getEnclosingCallable().getName() as source_func,\n  source.getNode().getLocation().getStartLine() as source_line,\n  sink.getNode().getLocation().getFile().getRelativePath() as sink_file,\n  sink.getNode().getEnclosingCallable().getName() as sink_func,\n  sink.getNode().getLocation().getStartLine() as sink_line,\n  pathLength as path_length\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_extraction_skeleton_20260512T100103",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction/codeql_queries/bounded_dataflow.ql",
    "content": "/**\n * @name Scope-bounded inter-procedural data-flow analysis\n * @description Tracks data-flow from parameters/return values of functions within\n *              2 call-graph hops of the buggy function to variable reads in the same\n *              scope. Sources and sinks are restricted BEFORE evaluation to prevent\n *              Cartesian-product blowup.\n * @kind path-problem\n * @id structfuse/bounded-dataflow\n * @problem.severity recommendation\n * @precision medium\n * @tags structfuse data-flow inter-procedural\n * @timeout 300\n * @ram 8192\n */\n\nimport python\nimport semmle.python.dataflow.new.DataFlow\nimport semmle.python.dataflow.new.TaintTracking\nimport semmle.python.pointsto.PointsTo\nimport semmle.python.ApiGraphs\n\n// -- Reuse call-graph scope predicates --\n\nexternal string buggyFunctionName();\nexternal string buggyFileName();\n\npredicate isBuggyFunction(Function f) {\n  f.getName() = buggyFunctionName() and\n  f.getLocation().getFile().getRelativePath() = buggyFileName()\n}\n\npredicate directCallEdge(Function caller, Function callee) {\n  exists(CallNode call |\n    call.getScope() = caller and\n    (\n      exists(FunctionObject fo |\n        call.getFunction().pointsTo(fo) and\n        fo.getFunction() = callee\n      )\n      or\n      exists(NameNode nameNode |\n        call.getFunction() = nameNode and\n        callee.getName() = nameNode.getId() and\n        callee.getEnclosingModule() = caller.getEnclosingModule() and\n        not exists(FunctionObject fo | call.getFunction().pointsTo(fo))\n      )\n    )\n  ) and\n  caller != callee\n}\n\npredicate hop1(Function f) {\n  exists(Function buggy |\n    isBuggyFunction(buggy) and\n    (directCallEdge(buggy, f) or directCallEdge(f, buggy))\n  )\n}\n\npredicate hop2(Function f) {\n  exists(Function mid |\n    hop1(mid) and\n    (directCallEdge(mid, f) or directCallEdge(f, mid)) and\n    not isBuggyFunction(f) and\n    not hop1(f)\n  )\n}\n\n/** Function is within 2 call-graph hops of the buggy function. */\npredicate inScopeFunction(Function f) {\n  isBuggyFunction(f) or hop1(f) or hop2(f)\n}\n\n// -- Scope-bounded data-flow configuration --\n\nmodule BoundedFlowConfig implements DataFlow::ConfigSig {\n  /**\n   * Sources: parameters and return values of in-scope functions only.\n   * This bounds the analysis BEFORE evaluation, preventing blowup.\n   */\n  predicate isSource(DataFlow::Node node) {\n    // Function parameters within scope\n    exists(Function f, Parameter p |\n      inScopeFunction(f) and\n      p = f.getAnArg() and\n      node.asExpr() = p.asName().getAFlowNode()\n    )\n    or\n    // Return values of in-scope functions (at call sites)\n    exists(Function f, CallNode call |\n      inScopeFunction(f) and\n      exists(FunctionObject fo |\n        fo.getFunction() = f and\n        call.getFunction().pointsTo(fo)\n      ) and\n      node.asCfgNode() = call\n    )\n  }\n\n  /**\n   * Sinks: variable reads within in-scope functions.\n   */\n  predicate isSink(DataFlow::Node node) {\n    exists(Function f, NameNode nameRead |\n      inScopeFunction(f) and\n      nameRead.getScope() = f and\n      nameRead.isLoad() and\n      node.asCfgNode() = nameRead\n    )\n  }\n}\n\nmodule BoundedFlow = DataFlow::Global&lt;BoundedFlowConfig>;\n\nimport BoundedFlow::PathGraph\n\nfrom BoundedFlow::PathNode source, BoundedFlow::PathNode sink, int pathLength\nwhere\n  BoundedFlow::flowPath(source, sink) and\n  // Approximate path length by counting intermediate nodes\n  pathLength = count(BoundedFlow::PathNode mid |\n    BoundedFlow::flowPath(source, mid) and\n    BoundedFlow::flowPath(mid, sink) and\n    mid != source and mid != sink\n  ) + 1\nselect\n  sink.getNode(),\n  source,\n  sink,\n  source.getNode().getLocation().getFile().getRelativePath() as source_file,\n  source.getNode().getEnclosingCallable().getName() as source_func,\n  source.getNode().getLocation().getStartLine() as source_line,\n  sink.getNode().getLocation().getFile().getRelativePath() as sink_file,\n  sink.getNode().getEnclosingCallable().getName() as sink_func,\n  sink.getNode().getLocation().getStartLine() as sink_line,\n  pathLength as path_length\n"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-12T10:04:39.829771+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction/codeql_queries/bounded_dataflow.ql

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_extraction_skeleton_20260512T100103",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-12T10:04:39.829961+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction/extract_dataflow.py",
  "content": "\"\"\"\nStructFuse Stage 1: Data-flow extraction pipeline.\n\nFor each repo, runs CodeQL 2-phase analysis (call graph + bounded data-flow),\nfalls back to Beniget for intra-file def-use when CodeQL times out or has\ninsufficient coverage. Outputs JSON Lines with per-instance features.\n\nInput:  JSON file with list of {repo_path, buggy_file, buggy_function}\nOutput: JSONL files in output_dir, one per repo, plus merged all.jsonl\n\nDependencies: codeql CLI on PATH, beniget (pip install beniget)\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport subprocess\nimport tempfile\nimport time\nfrom multiprocessing import Pool\nfrom pathlib import Path\nfrom typing import Any\n\nimport ast\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(name)s: %(message)s\",\n)\nlog = logging.getLogger(\"extract_dataflow\")\n\nSCRIPT_DIR = Path(__file__).resolve().parent\nCALL_GRAPH_QL = SCRIPT_DIR / \"codeql_queries\" / \"call_graph.ql\"\nDATAFLOW_QL = SCRIPT_DIR / \"codeql_queries\" / \"bounded_dataflow.ql\"\n\n\n# ---------------------------------------------------------------------------\n# CodeQL helpers\n# ---------------------------------------------------------------------------\n\ndef create_codeql_database(repo_path: str, db_path: str, timeout: int) -> bool:\n    \"\"\"Create a CodeQL database for a Python repo. Returns True on success.\"\"\"\n    cmd = [\n        \"codeql\", \"database\", \"create\", db_path,\n        \"--language=python\",\n        \"--source-root\", repo_path,\n        \"--overwrite\",\n        \"--threads=0\",  # use all available cores\n    ]\n    try:\n        subprocess.run(\n            cmd, capture_output=True, text=True, timeout=timeout, check=True\n        )\n        return True\n    except (subprocess.TimeoutExpired, subprocess.CalledProcessError) as e:\n        log.warning(\"CodeQL database creation failed for %s: %s\", repo_path, e)\n        return False\n\n\ndef run_codeql_query(\n    db_path: str,\n    query_path: str,\n    output_csv: str,\n    buggy_function: str,\n    buggy_file: str,\n    timeout: int,\n    ram: int,\n) -> bool:\n    \"\"\"Run a CodeQL query with external predicates. Returns True on success.\"\"\"\n    cmd = [\n        \"codeql\", \"query\", \"run\",\n        \"--database\", db_path,\n        \"--output\", output_csv,\n        \"--format=csv\",\n        f\"--ram={ram}\",\n        f\"--timeout={timeout}\",\n        f\"--external=buggyFunctionName={buggy_function}\",\n        f\"--external=buggyFileName={buggy_file}\",\n        \"--threads=0\",\n        query_path,\n    ]\n    try:\n        subprocess.run(\n            cmd, capture_output=True, text=True, timeout=timeout + 60, check=True\n        )\n        return True\n    except (subprocess.TimeoutExpired, subprocess.CalledProcessError) as e:\n        log.warning(\"CodeQL query failed (%s): %s\", query_path, e)\n        return False\n\n\ndef parse_call_graph_csv(csv_path: str) -> list[dict]:\n    \"\"\"Parse call_graph.ql CSV output into list of function records.\"\"\"\n    results = []\n    if not os.path.exists(csv_path):\n        return results\n    with open(csv_path) as f:\n        for line in f:\n            line = line.strip()\n            if not line or line.startswith(\"target_func\"):\n                continue\n            parts = [p.strip().strip('\"') for p in line.split(\",\")]\n            if len(parts) >= 6:\n                results.append({\n                    \"target_func\": parts[0],\n                    \"hop_distance\": int(parts[1]),\n                    \"direction\": parts[2],\n                    \"file_path\": parts[3],\n                    \"start_line\": int(parts[4]),\n                    \"end_line\": int(parts[5]),\n                })\n    return results\n\n\ndef parse_dataflow_csv(csv_path: str) -> list[dict]:\n    \"\"\"Parse bounded_dataflow.ql CSV output into list of flow records.\"\"\"\n    results = []\n    if not os.path.exists(csv_path):\n        return results\n    with open(csv_path) as f:\n        for line in f:\n            line = line.strip()\n            if not line or line.startswith(\"source_file\"):\n                continue\n            parts = [p.strip().strip('\"') for p in line.split(\",\")]\n            if len(parts) >= 7:\n                results.append({\n                    \"source_file\": parts[0],\n                    \"source_func\": parts[1],\n                    \"source_line\": int(parts[2]) if parts[2].isdigit() else 0,\n                    \"sink_file\": parts[3],\n                    \"sink_func\": parts[4],\n                    \"sink_line\": int(parts[5]) if parts[5].isdigit() else 0,\n                    \"path_length\": int(parts[6]) if parts[6].isdigit() else 1,\n                })\n    return results\n\n\n# ---------------------------------------------------------------------------\n# Beniget fallback\n# ---------------------------------------------------------------------------\n\ndef beniget_extract(repo_path: str, buggy_file: str, buggy_function: str) -> dict:\n    \"\"\"\n    Intra-file def-use chain extraction via beniget.\n    Returns a dict with call_graph (empty) and dataflow_paths (intra-file only).\n    \"\"\"\n    try:\n        import beniget\n    except ImportError:\n        log.error(\"beniget not installed; pip install beniget\")\n        return {\"call_graph\": [], \"dataflow_paths\": []}\n\n    target_path = os.path.join(repo_path, buggy_file)\n    if not os.path.exists(target_path):\n        log.warning(\"Buggy file not found: %s\", target_path)\n        return {\"call_graph\": [], \"dataflow_paths\": []}\n\n    try:\n        with open(target_path) as f:\n            source = f.read()\n        tree = ast.parse(source, filename=buggy_file)\n    except SyntaxError:\n        log.warning(\"SyntaxError parsing %s\", target_path)\n        return {\"call_graph\": [], \"dataflow_paths\": []}\n\n    duc = beniget.DefUseChains()\n    duc.visit(tree)\n\n    # Build def-use edges within the buggy file\n    dataflow_paths = []\n    buggy_func_node = None\n    for node in ast.walk(tree):\n        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):\n            if node.name == buggy_function:\n                buggy_func_node = node\n                break\n\n    if buggy_func_node is None:\n        log.warning(\"Function %s not found in %s\", buggy_function, buggy_file)\n        return {\"call_graph\": [], \"dataflow_paths\": []}\n\n    # Collect all names defined in the buggy function and trace their uses\n    for node in ast.walk(buggy_func_node):\n        if isinstance(node, ast.Name):\n            try:\n                chain = duc.chains[node]\n            except KeyError:\n                continue\n            for user in chain.users():\n                user_node = user.node\n                dataflow_paths.append({\n                    \"source_file\": buggy_file,\n                    \"source_func\": buggy_function,\n                    \"source_line\": getattr(node, \"lineno\", 0),\n                    \"sink_file\": buggy_file,\n                    \"sink_func\": _enclosing_function_name(tree, user_node),\n                    \"sink_line\": getattr(user_node, \"lineno\", 0),\n                    \"path_length\": 1,\n                })\n\n    # Deduplicate\n    seen = set()\n    unique = []\n    for p in dataflow_paths:\n        key = (p[\"source_func\"], p[\"source_line\"], p[\"sink_func\"], p[\"sink_line\"])\n        if key not in seen:\n            seen.add(key)\n            unique.append(p)\n\n    return {\"call_graph\": [], \"dataflow_paths\": unique}\n\n\ndef _enclosing_function_name(tree: ast.AST, node: ast.AST) -> str:\n    \"\"\"Find the name of the function enclosing `node`, or '&lt;module>'.\"\"\"\n    # Build parent map\n    parent_map: dict[ast.AST, ast.AST] = {}\n    for parent in ast.walk(tree):\n        for child in ast.iter_child_nodes(parent):\n            parent_map[child] = parent\n    current = node\n    while current in parent_map:\n        current = parent_map[current]\n        if isinstance(current, (ast.FunctionDef, ast.AsyncFunctionDef)):\n            return current.name\n    return \"&lt;module>\"\n\n\n# ---------------------------------------------------------------------------\n# Per-repo processing\n# ---------------------------------------------------------------------------\n\ndef process_repo(args_tuple: tuple) -> dict[str, Any] | None:\n    \"\"\"\n    Process a single repo: CodeQL extraction with Beniget fallback.\n    Called by multiprocessing pool.\n    \"\"\"\n    instance, codeql_timeout, codeql_ram, min_reachable_files = args_tuple\n    repo_path = instance[\"repo_path\"]\n    buggy_file = instance[\"buggy_file\"]\n    buggy_function = instance[\"buggy_function\"]\n    instance_id = instance.get(\"instance_id\", os.path.basename(repo_path))\n\n    log.info(\"Processing %s: %s in %s\", instance_id, buggy_function, buggy_file)\n    start = time.time()\n\n    result = {\n        \"instance_id\": instance_id,\n        \"repo_path\": repo_path,\n        \"buggy_file\": buggy_file,\n        \"buggy_function\": buggy_function,\n        \"inter_procedural\": False,\n        \"extraction_method\": \"none\",\n        \"call_graph\": [],\n        \"dataflow_paths\": [],\n        \"extraction_time_s\": 0.0,\n        \"error\": None,\n    }\n\n    with tempfile.TemporaryDirectory(prefix=\"structfuse_\") as tmpdir:\n        db_path = os.path.join(tmpdir, \"codeql_db\")\n        cg_csv = os.path.join(tmpdir, \"call_graph.csv\")\n        df_csv = os.path.join(tmpdir, \"dataflow.csv\")\n\n        # Phase 1a: CodeQL database + call graph\n        codeql_ok = False\n        if create_codeql_database(repo_path, db_path, timeout=codeql_timeout):\n            if run_codeql_query(\n                db_path, str(CALL_GRAPH_QL), cg_csv,\n                buggy_function, buggy_file, codeql_timeout, codeql_ram,\n            ):\n                call_graph = parse_call_graph_csv(cg_csv)\n                reachable_files = len({r[\"file_path\"] for r in call_graph})\n\n                if reachable_files >= min_reachable_files:\n                    # Phase 1b: bounded data-flow\n                    if run_codeql_query(\n                        db_path, str(DATAFLOW_QL), df_csv,\n                        buggy_function, buggy_file, codeql_timeout, codeql_ram,\n                    ):\n                        dataflow_paths = parse_dataflow_csv(df_csv)\n                        result[\"call_graph\"] = call_graph\n                        result[\"dataflow_paths\"] = dataflow_paths\n                        result[\"inter_procedural\"] = True\n                        result[\"extraction_method\"] = \"codeql\"\n                        codeql_ok = True\n                    else:\n                        log.warning(\n                            \"%s: data-flow query failed/timed out, falling back\",\n                            instance_id,\n                        )\n                else:\n                    log.info(\n                        \"%s: only %d reachable files (min %d), falling back\",\n                        instance_id, reachable_files, min_reachable_files,\n                    )\n\n        # Beniget fallback\n        if not codeql_ok:\n            log.info(\"%s: using Beniget fallback\", instance_id)\n            beniget_result = beniget_extract(repo_path, buggy_file, buggy_function)\n            result[\"call_graph\"] = beniget_result[\"call_graph\"]\n            result[\"dataflow_paths\"] = beniget_result[\"dataflow_paths\"]\n            result[\"inter_procedural\"] = False\n            result[\"extraction_method\"] = \"beniget\"\n\n    result[\"extraction_time_s\"] = round(time.time() - start, 2)\n    return result\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"StructFuse Stage 1: extract data-flow features per repo\"\n    )\n    parser.add_argument(\"--repos-file\", required=True, help=\"JSON list of instances\")\n    parser.add_argument(\"--output-dir\", required=True, help=\"Output directory for JSONL\")\n    parser.add_argument(\"--num-workers\", type=int, default=4)\n    parser.add_argument(\"--codeql-timeout\", type=int, default=300, help=\"Seconds\")\n    parser.add_argument(\"--codeql-ram\", type=int, default=8192, help=\"MB\")\n    parser.add_argument(\"--min-reachable-files\", type=int, default=5)\n    args = parser.parse_args()\n\n    with open(args.repos_file) as f:\n        instances = json.load(f)\n    log.info(\"Loaded %d instances\", len(instances))\n\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    task_args = [\n        (inst, args.codeql_timeout, args.codeql_ram, args.min_reachable_files)\n        for inst in instances\n    ]\n\n    results: list[dict] = []\n    if args.num_workers <= 1:\n        for ta in task_args:\n            r = process_repo(ta)\n            if r:\n                results.append(r)\n    else:\n        with Pool(processes=args.num_workers) as pool:\n            for r in pool.imap_unordered(process_repo, task_args):\n                if r:\n                    results.append(r)\n\n    # Write per-instance JSONL\n    merged_path = os.path.join(args.output_dir, \"all.jsonl\")\n    with open(merged_path, \"w\") as fout:\n        for r in results:\n            fout.write(json.dumps(r, ensure_ascii=False) + \"\\n\")\n\n    # Statistics\n    total = len(results)\n    codeql_count = sum(1 for r in results if r[\"extraction_method\"] == \"codeql\")\n    beniget_count = sum(1 for r in results if r[\"extraction_method\"] == \"beniget\")\n    failed_count = sum(1 for r in results if r[\"extraction_method\"] == \"none\")\n    avg_time = sum(r[\"extraction_time_s\"] for r in results) / max(total, 1)\n    inter_proc = sum(1 for r in results if r[\"inter_procedural\"])\n\n    log.info(\"=\" * 60)\n    log.info(\"Extraction complete: %d instances\", total)\n    log.info(\"  CodeQL success:  %d (%.1f%%)\", codeql_count, 100 * codeql_count / max(total, 1))\n    log.info(\"  Beniget fallback:%d (%.1f%%)\", beniget_count, 100 * beniget_count / max(total, 1))\n    log.info(\"  Failed:          %d (%.1f%%)\", failed_count, 100 * failed_count / max(total, 1))\n    log.info(\"  Inter-procedural:%d (%.1f%%)\", inter_proc, 100 * inter_proc / max(total, 1))\n    log.info(\"  Avg time/repo:   %.1fs\", avg_time)\n    log.info(\"  Output: %s\", merged_path)\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_extraction_skeleton_20260512T100103",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction/extract_dataflow.py",
    "content": "\"\"\"\nStructFuse Stage 1: Data-flow extraction pipeline.\n\nFor each repo, runs CodeQL 2-phase analysis (call graph + bounded data-flow),\nfalls back to Beniget for intra-file def-use when CodeQL times out or has\ninsufficient coverage. Outputs JSON Lines with per-instance features.\n\nInput:  JSON file with list of {repo_path, buggy_file, buggy_function}\nOutput: JSONL files in output_dir, one per repo, plus merged all.jsonl\n\nDependencies: codeql CLI on PATH, beniget (pip install beniget)\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport subprocess\nimport tempfile\nimport time\nfrom multiprocessing import Pool\nfrom pathlib import Path\nfrom typing import Any\n\nimport ast\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(name)s: %(message)s\",\n)\nlog = logging.getLogger(\"extract_dataflow\")\n\nSCRIPT_DIR = Path(__file__).resolve().parent\nCALL_GRAPH_QL = SCRIPT_DIR / \"codeql_queries\" / \"call_graph.ql\"\nDATAFLOW_QL = SCRIPT_DIR / \"codeql_queries\" / \"bounded_dataflow.ql\"\n\n\n# ---------------------------------------------------------------------------\n# CodeQL helpers\n# ---------------------------------------------------------------------------\n\ndef create_codeql_database(repo_path: str, db_path: str, timeout: int) -> bool:\n    \"\"\"Create a CodeQL database for a Python repo. Returns True on success.\"\"\"\n    cmd = [\n        \"codeql\", \"database\", \"create\", db_path,\n        \"--language=python\",\n        \"--source-root\", repo_path,\n        \"--overwrite\",\n        \"--threads=0\",  # use all available cores\n    ]\n    try:\n        subprocess.run(\n            cmd, capture_output=True, text=True, timeout=timeout, check=True\n        )\n        return True\n    except (subprocess.TimeoutExpired, subprocess.CalledProcessError) as e:\n        log.warning(\"CodeQL database creation failed for %s: %s\", repo_path, e)\n        return False\n\n\ndef run_codeql_query(\n    db_path: str,\n    query_path: str,\n    output_csv: str,\n    buggy_function: str,\n    buggy_file: str,\n    timeout: int,\n    ram: int,\n) -> bool:\n    \"\"\"Run a CodeQL query with external predicates. Returns True on success.\"\"\"\n    cmd = [\n        \"codeql\", \"query\", \"run\",\n        \"--database\", db_path,\n        \"--output\", output_csv,\n        \"--format=csv\",\n        f\"--ram={ram}\",\n        f\"--timeout={timeout}\",\n        f\"--external=buggyFunctionName={buggy_function}\",\n        f\"--external=buggyFileName={buggy_file}\",\n        \"--threads=0\",\n        query_path,\n    ]\n    try:\n        subprocess.run(\n            cmd, capture_output=True, text=True, timeout=timeout + 60, check=True\n        )\n        return True\n    except (subprocess.TimeoutExpired, subprocess.CalledProcessError) as e:\n        log.warning(\"CodeQL query failed (%s): %s\", query_path, e)\n        return False\n\n\ndef parse_call_graph_csv(csv_path: str) -> list[dict]:\n    \"\"\"Parse call_graph.ql CSV output into list of function records.\"\"\"\n    results = []\n    if not os.path.exists(csv_path):\n        return results\n    with open(csv_path) as f:\n        for line in f:\n            line = line.strip()\n            if not line or line.startswith(\"target_func\"):\n                continue\n            parts = [p.strip().strip('\"') for p in line.split(\",\")]\n            if len(parts) >= 6:\n                results.append({\n                    \"target_func\": parts[0],\n                    \"hop_distance\": int(parts[1]),\n                    \"direction\": parts[2],\n                    \"file_path\": parts[3],\n                    \"start_line\": int(parts[4]),\n                    \"end_line\": int(parts[5]),\n                })\n    return results\n\n\ndef parse_dataflow_csv(csv_path: str) -> list[dict]:\n    \"\"\"Parse bounded_dataflow.ql CSV output into list of flow records.\"\"\"\n    results = []\n    if not os.path.exists(csv_path):\n        return results\n    with open(csv_path) as f:\n        for line in f:\n            line = line.strip()\n            if not line or line.startswith(\"source_file\"):\n                continue\n            parts = [p.strip().strip('\"') for p in line.split(\",\")]\n            if len(parts) >= 7:\n                results.append({\n                    \"source_file\": parts[0],\n                    \"source_func\": parts[1],\n                    \"source_line\": int(parts[2]) if parts[2].isdigit() else 0,\n                    \"sink_file\": parts[3],\n                    \"sink_func\": parts[4],\n                    \"sink_line\": int(parts[5]) if parts[5].isdigit() else 0,\n                    \"path_length\": int(parts[6]) if parts[6].isdigit() else 1,\n                })\n    return results\n\n\n# ---------------------------------------------------------------------------\n# Beniget fallback\n# ---------------------------------------------------------------------------\n\ndef beniget_extract(repo_path: str, buggy_file: str, buggy_function: str) -> dict:\n    \"\"\"\n    Intra-file def-use chain extraction via beniget.\n    Returns a dict with call_graph (empty) and dataflow_paths (intra-file only).\n    \"\"\"\n    try:\n        import beniget\n    except ImportError:\n        log.error(\"beniget not installed; pip install beniget\")\n        return {\"call_graph\": [], \"dataflow_paths\": []}\n\n    target_path = os.path.join(repo_path, buggy_file)\n    if not os.path.exists(target_path):\n        log.warning(\"Buggy file not found: %s\", target_path)\n        return {\"call_graph\": [], \"dataflow_paths\": []}\n\n    try:\n        with open(target_path) as f:\n            source = f.read()\n        tree = ast.parse(source, filename=buggy_file)\n    except SyntaxError:\n        log.warning(\"SyntaxError parsing %s\", target_path)\n        return {\"call_graph\": [], \"dataflow_paths\": []}\n\n    duc = beniget.DefUseChains()\n    duc.visit(tree)\n\n    # Build def-use edges within the buggy file\n    dataflow_paths = []\n    buggy_func_node = None\n    for node in ast.walk(tree):\n        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):\n            if node.name == buggy_function:\n                buggy_func_node = node\n                break\n\n    if buggy_func_node is None:\n        log.warning(\"Function %s not found in %s\", buggy_function, buggy_file)\n        return {\"call_graph\": [], \"dataflow_paths\": []}\n\n    # Collect all names defined in the buggy function and trace their uses\n    for node in ast.walk(buggy_func_node):\n        if isinstance(node, ast.Name):\n            try:\n                chain = duc.chains[node]\n            except KeyError:\n                continue\n            for user in chain.users():\n                user_node = user.node\n                dataflow_paths.append({\n                    \"source_file\": buggy_file,\n                    \"source_func\": buggy_function,\n                    \"source_line\": getattr(node, \"lineno\", 0),\n                    \"sink_file\": buggy_file,\n                    \"sink_func\": _enclosing_function_name(tree, user_node),\n                    \"sink_line\": getattr(user_node, \"lineno\", 0),\n                    \"path_length\": 1,\n                })\n\n    # Deduplicate\n    seen = set()\n    unique = []\n    for p in dataflow_paths:\n        key = (p[\"source_func\"], p[\"source_line\"], p[\"sink_func\"], p[\"sink_line\"])\n        if key not in seen:\n            seen.add(key)\n            unique.append(p)\n\n    return {\"call_graph\": [], \"dataflow_paths\": unique}\n\n\ndef _enclosing_function_name(tree: ast.AST, node: ast.AST) -> str:\n    \"\"\"Find the name of the function enclosing `node`, or '&lt;module>'.\"\"\"\n    # Build parent map\n    parent_map: dict[ast.AST, ast.AST] = {}\n    for parent in ast.walk(tree):\n        for child in ast.iter_child_nodes(parent):\n            parent_map[child] = parent\n    current = node\n    while current in parent_map:\n        current = parent_map[current]\n        if isinstance(current, (ast.FunctionDef, ast.AsyncFunctionDef)):\n            return current.name\n    return \"&lt;module>\"\n\n\n# ---------------------------------------------------------------------------\n# Per-repo processing\n# ---------------------------------------------------------------------------\n\ndef process_repo(args_tuple: tuple) -> dict[str, Any] | None:\n    \"\"\"\n    Process a single repo: CodeQL extraction with Beniget fallback.\n    Called by multiprocessing pool.\n    \"\"\"\n    instance, codeql_timeout, codeql_ram, min_reachable_files = args_tuple\n    repo_path = instance[\"repo_path\"]\n    buggy_file = instance[\"buggy_file\"]\n    buggy_function = instance[\"buggy_function\"]\n    instance_id = instance.get(\"instance_id\", os.path.basename(repo_path))\n\n    log.info(\"Processing %s: %s in %s\", instance_id, buggy_function, buggy_file)\n    start = time.time()\n\n    result = {\n        \"instance_id\": instance_id,\n        \"repo_path\": repo_path,\n        \"buggy_file\": buggy_file,\n        \"buggy_function\": buggy_function,\n        \"inter_procedural\": False,\n        \"extraction_method\": \"none\",\n        \"call_graph\": [],\n        \"dataflow_paths\": [],\n        \"extraction_time_s\": 0.0,\n        \"error\": None,\n    }\n\n    with tempfile.TemporaryDirectory(prefix=\"structfuse_\") as tmpdir:\n        db_path = os.path.join(tmpdir, \"codeql_db\")\n        cg_csv = os.path.join(tmpdir, \"call_graph.csv\")\n        df_csv = os.path.join(tmpdir, \"dataflow.csv\")\n\n        # Phase 1a: CodeQL database + call graph\n        codeql_ok = False\n        if create_codeql_database(repo_path, db_path, timeout=codeql_timeout):\n            if run_codeql_query(\n                db_path, str(CALL_GRAPH_QL), cg_csv,\n                buggy_function, buggy_file, codeql_timeout, codeql_ram,\n            ):\n                call_graph = parse_call_graph_csv(cg_csv)\n                reachable_files = len({r[\"file_path\"] for r in call_graph})\n\n                if reachable_files >= min_reachable_files:\n                    # Phase 1b: bounded data-flow\n                    if run_codeql_query(\n                        db_path, str(DATAFLOW_QL), df_csv,\n                        buggy_function, buggy_file, codeql_timeout, codeql_ram,\n                    ):\n                        dataflow_paths = parse_dataflow_csv(df_csv)\n                        result[\"call_graph\"] = call_graph\n                        result[\"dataflow_paths\"] = dataflow_paths\n                        result[\"inter_procedural\"] = True\n                        result[\"extraction_method\"] = \"codeql\"\n                        codeql_ok = True\n                    else:\n                        log.warning(\n                            \"%s: data-flow query failed/timed out, falling back\",\n                            instance_id,\n                        )\n                else:\n                    log.info(\n                        \"%s: only %d reachable files (min %d), falling back\",\n                        instance_id, reachable_files, min_reachable_files,\n                    )\n\n        # Beniget fallback\n        if not codeql_ok:\n            log.info(\"%s: using Beniget fallback\", instance_id)\n            beniget_result = beniget_extract(repo_path, buggy_file, buggy_function)\n            result[\"call_graph\"] = beniget_result[\"call_graph\"]\n            result[\"dataflow_paths\"] = beniget_result[\"dataflow_paths\"]\n            result[\"inter_procedural\"] = False\n            result[\"extraction_method\"] = \"beniget\"\n\n    result[\"extraction_time_s\"] = round(time.time() - start, 2)\n    return result\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"StructFuse Stage 1: extract data-flow features per repo\"\n    )\n    parser.add_argument(\"--repos-file\", required=True, help=\"JSON list of instances\")\n    parser.add_argument(\"--output-dir\", required=True, help=\"Output directory for JSONL\")\n    parser.add_argument(\"--num-workers\", type=int, default=4)\n    parser.add_argument(\"--codeql-timeout\", type=int, default=300, help=\"Seconds\")\n    parser.add_argument(\"--codeql-ram\", type=int, default=8192, help=\"MB\")\n    parser.add_argument(\"--min-reachable-files\", type=int, default=5)\n    args = parser.parse_args()\n\n    with open(args.repos_file) as f:\n        instances = json.load(f)\n    log.info(\"Loaded %d instances\", len(instances))\n\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    task_args = [\n        (inst, args.codeql_timeout, args.codeql_ram, args.min_reachable_files)\n        for inst in instances\n    ]\n\n    results: list[dict] = []\n    if args.num_workers <= 1:\n        for ta in task_args:\n            r = process_repo(ta)\n            if r:\n                results.append(r)\n    else:\n        with Pool(processes=args.num_workers) as pool:\n            for r in pool.imap_unordered(process_repo, task_args):\n                if r:\n                    results.append(r)\n\n    # Write per-instance JSONL\n    merged_path = os.path.join(args.output_dir, \"all.jsonl\")\n    with open(merged_path, \"w\") as fout:\n        for r in results:\n            fout.write(json.dumps(r, ensure_ascii=False) + \"\\n\")\n\n    # Statistics\n    total = len(results)\n    codeql_count = sum(1 for r in results if r[\"extraction_method\"] == \"codeql\")\n    beniget_count = sum(1 for r in results if r[\"extraction_method\"] == \"beniget\")\n    failed_count = sum(1 for r in results if r[\"extraction_method\"] == \"none\")\n    avg_time = sum(r[\"extraction_time_s\"] for r in results) / max(total, 1)\n    inter_proc = sum(1 for r in results if r[\"inter_procedural\"])\n\n    log.info(\"=\" * 60)\n    log.info(\"Extraction complete: %d instances\", total)\n    log.info(\"  CodeQL success:  %d (%.1f%%)\", codeql_count, 100 * codeql_count / max(total, 1))\n    log.info(\"  Beniget fallback:%d (%.1f%%)\", beniget_count, 100 * beniget_count / max(total, 1))\n    log.info(\"  Failed:          %d (%.1f%%)\", failed_count, 100 * failed_count / max(total, 1))\n    log.info(\"  Inter-procedural:%d (%.1f%%)\", inter_proc, 100 * inter_proc / max(total, 1))\n    log.info(\"  Avg time/repo:   %.1fs\", avg_time)\n    log.info(\"  Output: %s\", merged_path)\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-12T10:04:39.830267+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction/extract_dataflow.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_extraction_skeleton_20260512T100103",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-12T10:04:39.830460+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction/build_training_data.py",
  "content": "\"\"\"\nStructFuse Stage 1→2 bridge: build contrastive training data from data-flow features.\n\nReads extraction output (all.jsonl from extract_dataflow.py) and original repo code\nto produce contrastive training triples (query, positive, negatives) with feature vectors.\n\nOutput format: JSONL compatible with HuggingFace datasets.load_dataset(\"json\").\nEach line: {query, pos_code, neg_codes, features, metadata}\n\nDependencies: rank_bm25, numpy\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport random\nfrom collections import defaultdict\nfrom pathlib import Path\nfrom typing import Any\n\nimport numpy as np\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(name)s: %(message)s\",\n)\nlog = logging.getLogger(\"build_training_data\")\n\n\n# ---------------------------------------------------------------------------\n# File reading\n# ---------------------------------------------------------------------------\n\ndef read_file_content(repo_path: str, file_path: str) -> str | None:\n    \"\"\"Read a source file from repo, return content or None.\"\"\"\n    full = os.path.join(repo_path, file_path)\n    if not os.path.isfile(full):\n        return None\n    try:\n        with open(full, encoding=\"utf-8\", errors=\"replace\") as f:\n            return f.read()\n    except OSError:\n        return None\n\n\ndef collect_repo_files(repo_path: str) -> list[str]:\n    \"\"\"List all .py files in the repo (relative paths).\"\"\"\n    files = []\n    for root, _dirs, filenames in os.walk(repo_path):\n        for fname in filenames:\n            if fname.endswith(\".py\"):\n                rel = os.path.relpath(os.path.join(root, fname), repo_path)\n                files.append(rel)\n    return files\n\n\n# ---------------------------------------------------------------------------\n# BM25\n# ---------------------------------------------------------------------------\n\ndef build_bm25_index(documents: list[str]):\n    \"\"\"Build BM25 index over tokenized documents.\"\"\"\n    from rank_bm25 import BM25Okapi\n    tokenized = [doc.split() for doc in documents]\n    return BM25Okapi(tokenized)\n\n\ndef bm25_scores(bm25_index, query: str) -> np.ndarray:\n    return bm25_index.get_scores(query.split())\n\n\n# ---------------------------------------------------------------------------\n# Feature computation\n# ---------------------------------------------------------------------------\n\ndef compute_features(\n    instance: dict,\n    file_path: str,\n    bm25_score: float,\n    connected_files: dict[str, dict],\n) -> dict[str, float]:\n    \"\"\"\n    Compute feature vector for a (instance, file) pair.\n    Returns dict of normalized features.\n    \"\"\"\n    info = connected_files.get(file_path)\n    if info:\n        df_distance = info[\"min_path_length\"]\n        path_count = info[\"path_count\"]\n        dep_type = 1.0 if info.get(\"inter_procedural\", False) else 0.0\n    else:\n        df_distance = 999\n        path_count = 0\n        dep_type = 0.0\n\n    return {\n        \"dataflow_distance\": float(df_distance),\n        \"dataflow_path_count\": float(path_count),\n        \"dependency_type\": dep_type,\n        \"bm25_score\": float(bm25_score),\n        \"inter_procedural\": 1.0 if instance.get(\"inter_procedural\", False) else 0.0,\n    }\n\n\ndef normalize_features(instances: list[dict]) -> list[dict]:\n    \"\"\"Min-max normalize feature vectors across all instances.\"\"\"\n    if not instances:\n        return instances\n\n    keys = [\"dataflow_distance\", \"dataflow_path_count\", \"bm25_score\"]\n    all_features = []\n    for inst in instances:\n        all_features.append(inst[\"features\"])\n        for neg in inst.get(\"neg_features\", []):\n            all_features.append(neg)\n\n    mins = {k: float(\"inf\") for k in keys}\n    maxs = {k: float(\"-inf\") for k in keys}\n    for feat in all_features:\n        for k in keys:\n            v = feat.get(k, 0.0)\n            mins[k] = min(mins[k], v)\n            maxs[k] = max(maxs[k], v)\n\n    def norm(feat: dict) -> dict:\n        out = dict(feat)\n        for k in keys:\n            rng = maxs[k] - mins[k]\n            if rng > 0:\n                out[k] = (out[k] - mins[k]) / rng\n            else:\n                out[k] = 0.0\n        return out\n\n    for inst in instances:\n        inst[\"features\"] = norm(inst[\"features\"])\n        inst[\"neg_features\"] = [norm(nf) for nf in inst.get(\"neg_features\", [])]\n\n    return instances\n\n\n# ---------------------------------------------------------------------------\n# Negative sampling strategies\n# ---------------------------------------------------------------------------\n\ndef sample_negatives(\n    query: str,\n    positive_files: set[str],\n    connected_files: set[str],\n    all_files: list[str],\n    file_contents: dict[str, str],\n    bm25_index,\n    num_negatives: int,\n    hard_negative_ratio: float,\n) -> tuple[list[str], list[str]]:\n    \"\"\"\n    Sample negatives with a mix of strategies:\n    - hard_negative_ratio fraction: BM25-similar but structurally disconnected\n    - remaining: random from repo\n\n    Returns (neg_file_paths, neg_strategies).\n    \"\"\"\n    candidate_pool = [\n        f for f in all_files\n        if f not in positive_files and f in file_contents\n    ]\n    if not candidate_pool:\n        return [], []\n\n    num_hard = int(num_negatives * hard_negative_ratio)\n    num_random = num_negatives - num_hard\n\n    neg_files = []\n    neg_strategies = []\n\n    # Hard negatives: high BM25 but NOT in connected_files\n    if num_hard > 0 and bm25_index is not None:\n        disconnected = [f for f in candidate_pool if f not in connected_files]\n        if disconnected:\n            scores = bm25_scores(bm25_index, query)\n            file_to_idx = {f: i for i, f in enumerate(all_files)}\n            scored = [\n                (f, scores[file_to_idx[f]])\n                for f in disconnected\n                if f in file_to_idx and file_to_idx[f] < len(scores)\n            ]\n            scored.sort(key=lambda x: x[1], reverse=True)\n            for f, _ in scored[:num_hard]:\n                neg_files.append(f)\n                neg_strategies.append(\"bm25_hard\")\n\n    # Random negatives\n    remaining_pool = [f for f in candidate_pool if f not in set(neg_files)]\n    if remaining_pool and num_random > 0:\n        sample_size = min(num_random, len(remaining_pool))\n        for f in random.sample(remaining_pool, sample_size):\n            neg_files.append(f)\n            neg_strategies.append(\"random\")\n\n    return neg_files[:num_negatives], neg_strategies[:num_negatives]\n\n\n# ---------------------------------------------------------------------------\n# Instance building\n# ---------------------------------------------------------------------------\n\ndef build_instance(\n    extraction: dict,\n    repos_dir: str,\n    bm25_index,\n    all_files: list[str],\n    file_contents: dict[str, str],\n    num_negatives: int,\n    hard_negative_ratio: float,\n) -> dict[str, Any] | None:\n    \"\"\"Build a single training instance from extraction result.\"\"\"\n    repo_path = extraction[\"repo_path\"]\n    query = extraction.get(\"issue_text\", \"\")\n    if not query:\n        query = f\"Bug in {extraction['buggy_function']} at {extraction['buggy_file']}\"\n\n    # Identify data-flow-connected files and their properties\n    connected_files: dict[str, dict] = {}\n    for path_info in extraction.get(\"dataflow_paths\", []):\n        for key in (\"source_file\", \"sink_file\"):\n            fpath = path_info.get(key, \"\")\n            if not fpath:\n                continue\n            pl = path_info.get(\"path_length\", 1)\n            if fpath not in connected_files:\n                connected_files[fpath] = {\n                    \"min_path_length\": pl,\n                    \"path_count\": 1,\n                    \"inter_procedural\": extraction.get(\"inter_procedural\", False),\n                }\n            else:\n                connected_files[fpath][\"path_count\"] += 1\n                connected_files[fpath][\"min_path_length\"] = min(\n                    connected_files[fpath][\"min_path_length\"], pl\n                )\n\n    # Also include call-graph files\n    for cg in extraction.get(\"call_graph\", []):\n        fpath = cg.get(\"file_path\", \"\")\n        if fpath and fpath not in connected_files:\n            connected_files[fpath] = {\n                \"min_path_length\": cg.get(\"hop_distance\", 2),\n                \"path_count\": 1,\n                \"inter_procedural\": extraction.get(\"inter_procedural\", False),\n            }\n\n    # Always include the buggy file\n    buggy_file = extraction[\"buggy_file\"]\n    if buggy_file not in connected_files:\n        connected_files[buggy_file] = {\n            \"min_path_length\": 0,\n            \"path_count\": 1,\n            \"inter_procedural\": extraction.get(\"inter_procedural\", False),\n        }\n\n    # Positive: concatenated connected file contents, weighted by path distance\n    positive_files = set(connected_files.keys())\n    pos_parts = []\n    for fpath, info in sorted(connected_files.items(), key=lambda x: x[1][\"min_path_length\"]):\n        content = file_contents.get(fpath)\n        if content:\n            pos_parts.append(content)\n    if not pos_parts:\n        return None\n    pos_code = \"\\n\\n\".join(pos_parts)\n\n    # BM25 scores\n    scores_array = bm25_scores(bm25_index, query) if bm25_index else np.zeros(len(all_files))\n\n    # Negative sampling\n    neg_files, neg_strategies = sample_negatives(\n        query, positive_files, set(connected_files.keys()),\n        all_files, file_contents, bm25_index,\n        num_negatives, hard_negative_ratio,\n    )\n\n    neg_codes = []\n    neg_features = []\n    file_to_idx = {f: i for i, f in enumerate(all_files)}\n    for nf, strat in zip(neg_files, neg_strategies):\n        content = file_contents.get(nf, \"\")\n        neg_codes.append(content)\n        bm25_val = float(scores_array[file_to_idx[nf]]) if nf in file_to_idx and file_to_idx[nf] < len(scores_array) else 0.0\n        neg_features.append(compute_features(extraction, nf, bm25_val, connected_files))\n\n    # Positive features (using buggy_file as representative)\n    buggy_bm25 = float(scores_array[file_to_idx[buggy_file]]) if buggy_file in file_to_idx and file_to_idx[buggy_file] < len(scores_array) else 0.0\n    pos_features = compute_features(extraction, buggy_file, buggy_bm25, connected_files)\n\n    return {\n        \"instance_id\": extraction.get(\"instance_id\", \"\"),\n        \"query\": query,\n        \"pos_code\": pos_code,\n        \"neg_codes\": neg_codes,\n        \"features\": pos_features,\n        \"neg_features\": neg_features,\n        \"metadata\": {\n            \"inter_procedural\": extraction.get(\"inter_procedural\", False),\n            \"extraction_method\": extraction.get(\"extraction_method\", \"\"),\n            \"num_connected_files\": len(connected_files),\n            \"num_dataflow_paths\": len(extraction.get(\"dataflow_paths\", [])),\n            \"neg_strategies\": neg_strategies,\n        },\n    }\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Build contrastive training data from data-flow extractions\"\n    )\n    parser.add_argument(\"--dataflow-dir\", required=True,\n                        help=\"Directory containing all.jsonl from extract_dataflow.py\")\n    parser.add_argument(\"--repos-dir\", required=True,\n                        help=\"Root directory containing all repos\")\n    parser.add_argument(\"--output-file\", required=True,\n                        help=\"Output JSONL path\")\n    parser.add_argument(\"--num-negatives\", type=int, default=7)\n    parser.add_argument(\"--hard-negative-ratio\", type=float, default=0.5)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    args = parser.parse_args()\n\n    random.seed(args.seed)\n    np.random.seed(args.seed)\n\n    # Load extractions\n    dataflow_path = os.path.join(args.dataflow_dir, \"all.jsonl\")\n    extractions = []\n    with open(dataflow_path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                extractions.append(json.loads(line))\n    log.info(\"Loaded %d extractions\", len(extractions))\n\n    # Group by repo for BM25 index sharing\n    by_repo: dict[str, list[dict]] = defaultdict(list)\n    for ext in extractions:\n        by_repo[ext[\"repo_path\"]].append(ext)\n\n    training_instances = []\n\n    for repo_path, repo_extractions in by_repo.items():\n        log.info(\"Building training data for %s (%d instances)\", repo_path, len(repo_extractions))\n\n        all_files = collect_repo_files(repo_path)\n        if not all_files:\n            log.warning(\"No .py files in %s, skipping\", repo_path)\n            continue\n\n        # Cache file contents\n        file_contents: dict[str, str] = {}\n        for fp in all_files:\n            content = read_file_content(repo_path, fp)\n            if content:\n                file_contents[fp] = content\n\n        # Build BM25 index over repo files\n        doc_list = [file_contents.get(f, \"\") for f in all_files]\n        bm25_index = build_bm25_index(doc_list)\n\n        for ext in repo_extractions:\n            inst = build_instance(\n                ext, args.repos_dir, bm25_index, all_files, file_contents,\n                args.num_negatives, args.hard_negative_ratio,\n            )\n            if inst:\n                training_instances.append(inst)\n\n    # Normalize features\n    training_instances = normalize_features(training_instances)\n\n    # Write output\n    os.makedirs(os.path.dirname(os.path.abspath(args.output_file)), exist_ok=True)\n    with open(args.output_file, \"w\") as f:\n        for inst in training_instances:\n            f.write(json.dumps(inst, ensure_ascii=False) + \"\\n\")\n\n    # Statistics\n    total = len(training_instances)\n    inter_proc = sum(1 for i in training_instances if i[\"metadata\"][\"inter_procedural\"])\n    avg_pos_files = np.mean([i[\"metadata\"][\"num_connected_files\"] for i in training_instances]) if total else 0\n    hard_neg_count = sum(\n        sum(1 for s in i[\"metadata\"][\"neg_strategies\"] if s == \"bm25_hard\")\n        for i in training_instances\n    )\n    total_neg = sum(len(i[\"neg_codes\"]) for i in training_instances)\n\n    log.info(\"=\" * 60)\n    log.info(\"Training data built: %d instances\", total)\n    log.info(\"  Avg connected files/instance: %.1f\", avg_pos_files)\n    log.info(\"  Hard negative ratio:          %.2f\", hard_neg_count / max(total_neg, 1))\n    log.info(\"  Inter-procedural ratio:       %.2f\", inter_proc / max(total, 1))\n    log.info(\"  Output: %s\", args.output_file)\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_extraction_skeleton_20260512T100103",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction/build_training_data.py",
    "content": "\"\"\"\nStructFuse Stage 1→2 bridge: build contrastive training data from data-flow features.\n\nReads extraction output (all.jsonl from extract_dataflow.py) and original repo code\nto produce contrastive training triples (query, positive, negatives) with feature vectors.\n\nOutput format: JSONL compatible with HuggingFace datasets.load_dataset(\"json\").\nEach line: {query, pos_code, neg_codes, features, metadata}\n\nDependencies: rank_bm25, numpy\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport random\nfrom collections import defaultdict\nfrom pathlib import Path\nfrom typing import Any\n\nimport numpy as np\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(name)s: %(message)s\",\n)\nlog = logging.getLogger(\"build_training_data\")\n\n\n# ---------------------------------------------------------------------------\n# File reading\n# ---------------------------------------------------------------------------\n\ndef read_file_content(repo_path: str, file_path: str) -> str | None:\n    \"\"\"Read a source file from repo, return content or None.\"\"\"\n    full = os.path.join(repo_path, file_path)\n    if not os.path.isfile(full):\n        return None\n    try:\n        with open(full, encoding=\"utf-8\", errors=\"replace\") as f:\n            return f.read()\n    except OSError:\n        return None\n\n\ndef collect_repo_files(repo_path: str) -> list[str]:\n    \"\"\"List all .py files in the repo (relative paths).\"\"\"\n    files = []\n    for root, _dirs, filenames in os.walk(repo_path):\n        for fname in filenames:\n            if fname.endswith(\".py\"):\n                rel = os.path.relpath(os.path.join(root, fname), repo_path)\n                files.append(rel)\n    return files\n\n\n# ---------------------------------------------------------------------------\n# BM25\n# ---------------------------------------------------------------------------\n\ndef build_bm25_index(documents: list[str]):\n    \"\"\"Build BM25 index over tokenized documents.\"\"\"\n    from rank_bm25 import BM25Okapi\n    tokenized = [doc.split() for doc in documents]\n    return BM25Okapi(tokenized)\n\n\ndef bm25_scores(bm25_index, query: str) -> np.ndarray:\n    return bm25_index.get_scores(query.split())\n\n\n# ---------------------------------------------------------------------------\n# Feature computation\n# ---------------------------------------------------------------------------\n\ndef compute_features(\n    instance: dict,\n    file_path: str,\n    bm25_score: float,\n    connected_files: dict[str, dict],\n) -> dict[str, float]:\n    \"\"\"\n    Compute feature vector for a (instance, file) pair.\n    Returns dict of normalized features.\n    \"\"\"\n    info = connected_files.get(file_path)\n    if info:\n        df_distance = info[\"min_path_length\"]\n        path_count = info[\"path_count\"]\n        dep_type = 1.0 if info.get(\"inter_procedural\", False) else 0.0\n    else:\n        df_distance = 999\n        path_count = 0\n        dep_type = 0.0\n\n    return {\n        \"dataflow_distance\": float(df_distance),\n        \"dataflow_path_count\": float(path_count),\n        \"dependency_type\": dep_type,\n        \"bm25_score\": float(bm25_score),\n        \"inter_procedural\": 1.0 if instance.get(\"inter_procedural\", False) else 0.0,\n    }\n\n\ndef normalize_features(instances: list[dict]) -> list[dict]:\n    \"\"\"Min-max normalize feature vectors across all instances.\"\"\"\n    if not instances:\n        return instances\n\n    keys = [\"dataflow_distance\", \"dataflow_path_count\", \"bm25_score\"]\n    all_features = []\n    for inst in instances:\n        all_features.append(inst[\"features\"])\n        for neg in inst.get(\"neg_features\", []):\n            all_features.append(neg)\n\n    mins = {k: float(\"inf\") for k in keys}\n    maxs = {k: float(\"-inf\") for k in keys}\n    for feat in all_features:\n        for k in keys:\n            v = feat.get(k, 0.0)\n            mins[k] = min(mins[k], v)\n            maxs[k] = max(maxs[k], v)\n\n    def norm(feat: dict) -> dict:\n        out = dict(feat)\n        for k in keys:\n            rng = maxs[k] - mins[k]\n            if rng > 0:\n                out[k] = (out[k] - mins[k]) / rng\n            else:\n                out[k] = 0.0\n        return out\n\n    for inst in instances:\n        inst[\"features\"] = norm(inst[\"features\"])\n        inst[\"neg_features\"] = [norm(nf) for nf in inst.get(\"neg_features\", [])]\n\n    return instances\n\n\n# ---------------------------------------------------------------------------\n# Negative sampling strategies\n# ---------------------------------------------------------------------------\n\ndef sample_negatives(\n    query: str,\n    positive_files: set[str],\n    connected_files: set[str],\n    all_files: list[str],\n    file_contents: dict[str, str],\n    bm25_index,\n    num_negatives: int,\n    hard_negative_ratio: float,\n) -> tuple[list[str], list[str]]:\n    \"\"\"\n    Sample negatives with a mix of strategies:\n    - hard_negative_ratio fraction: BM25-similar but structurally disconnected\n    - remaining: random from repo\n\n    Returns (neg_file_paths, neg_strategies).\n    \"\"\"\n    candidate_pool = [\n        f for f in all_files\n        if f not in positive_files and f in file_contents\n    ]\n    if not candidate_pool:\n        return [], []\n\n    num_hard = int(num_negatives * hard_negative_ratio)\n    num_random = num_negatives - num_hard\n\n    neg_files = []\n    neg_strategies = []\n\n    # Hard negatives: high BM25 but NOT in connected_files\n    if num_hard > 0 and bm25_index is not None:\n        disconnected = [f for f in candidate_pool if f not in connected_files]\n        if disconnected:\n            scores = bm25_scores(bm25_index, query)\n            file_to_idx = {f: i for i, f in enumerate(all_files)}\n            scored = [\n                (f, scores[file_to_idx[f]])\n                for f in disconnected\n                if f in file_to_idx and file_to_idx[f] < len(scores)\n            ]\n            scored.sort(key=lambda x: x[1], reverse=True)\n            for f, _ in scored[:num_hard]:\n                neg_files.append(f)\n                neg_strategies.append(\"bm25_hard\")\n\n    # Random negatives\n    remaining_pool = [f for f in candidate_pool if f not in set(neg_files)]\n    if remaining_pool and num_random > 0:\n        sample_size = min(num_random, len(remaining_pool))\n        for f in random.sample(remaining_pool, sample_size):\n            neg_files.append(f)\n            neg_strategies.append(\"random\")\n\n    return neg_files[:num_negatives], neg_strategies[:num_negatives]\n\n\n# ---------------------------------------------------------------------------\n# Instance building\n# ---------------------------------------------------------------------------\n\ndef build_instance(\n    extraction: dict,\n    repos_dir: str,\n    bm25_index,\n    all_files: list[str],\n    file_contents: dict[str, str],\n    num_negatives: int,\n    hard_negative_ratio: float,\n) -> dict[str, Any] | None:\n    \"\"\"Build a single training instance from extraction result.\"\"\"\n    repo_path = extraction[\"repo_path\"]\n    query = extraction.get(\"issue_text\", \"\")\n    if not query:\n        query = f\"Bug in {extraction['buggy_function']} at {extraction['buggy_file']}\"\n\n    # Identify data-flow-connected files and their properties\n    connected_files: dict[str, dict] = {}\n    for path_info in extraction.get(\"dataflow_paths\", []):\n        for key in (\"source_file\", \"sink_file\"):\n            fpath = path_info.get(key, \"\")\n            if not fpath:\n                continue\n            pl = path_info.get(\"path_length\", 1)\n            if fpath not in connected_files:\n                connected_files[fpath] = {\n                    \"min_path_length\": pl,\n                    \"path_count\": 1,\n                    \"inter_procedural\": extraction.get(\"inter_procedural\", False),\n                }\n            else:\n                connected_files[fpath][\"path_count\"] += 1\n                connected_files[fpath][\"min_path_length\"] = min(\n                    connected_files[fpath][\"min_path_length\"], pl\n                )\n\n    # Also include call-graph files\n    for cg in extraction.get(\"call_graph\", []):\n        fpath = cg.get(\"file_path\", \"\")\n        if fpath and fpath not in connected_files:\n            connected_files[fpath] = {\n                \"min_path_length\": cg.get(\"hop_distance\", 2),\n                \"path_count\": 1,\n                \"inter_procedural\": extraction.get(\"inter_procedural\", False),\n            }\n\n    # Always include the buggy file\n    buggy_file = extraction[\"buggy_file\"]\n    if buggy_file not in connected_files:\n        connected_files[buggy_file] = {\n            \"min_path_length\": 0,\n            \"path_count\": 1,\n            \"inter_procedural\": extraction.get(\"inter_procedural\", False),\n        }\n\n    # Positive: concatenated connected file contents, weighted by path distance\n    positive_files = set(connected_files.keys())\n    pos_parts = []\n    for fpath, info in sorted(connected_files.items(), key=lambda x: x[1][\"min_path_length\"]):\n        content = file_contents.get(fpath)\n        if content:\n            pos_parts.append(content)\n    if not pos_parts:\n        return None\n    pos_code = \"\\n\\n\".join(pos_parts)\n\n    # BM25 scores\n    scores_array = bm25_scores(bm25_index, query) if bm25_index else np.zeros(len(all_files))\n\n    # Negative sampling\n    neg_files, neg_strategies = sample_negatives(\n        query, positive_files, set(connected_files.keys()),\n        all_files, file_contents, bm25_index,\n        num_negatives, hard_negative_ratio,\n    )\n\n    neg_codes = []\n    neg_features = []\n    file_to_idx = {f: i for i, f in enumerate(all_files)}\n    for nf, strat in zip(neg_files, neg_strategies):\n        content = file_contents.get(nf, \"\")\n        neg_codes.append(content)\n        bm25_val = float(scores_array[file_to_idx[nf]]) if nf in file_to_idx and file_to_idx[nf] < len(scores_array) else 0.0\n        neg_features.append(compute_features(extraction, nf, bm25_val, connected_files))\n\n    # Positive features (using buggy_file as representative)\n    buggy_bm25 = float(scores_array[file_to_idx[buggy_file]]) if buggy_file in file_to_idx and file_to_idx[buggy_file] < len(scores_array) else 0.0\n    pos_features = compute_features(extraction, buggy_file, buggy_bm25, connected_files)\n\n    return {\n        \"instance_id\": extraction.get(\"instance_id\", \"\"),\n        \"query\": query,\n        \"pos_code\": pos_code,\n        \"neg_codes\": neg_codes,\n        \"features\": pos_features,\n        \"neg_features\": neg_features,\n        \"metadata\": {\n            \"inter_procedural\": extraction.get(\"inter_procedural\", False),\n            \"extraction_method\": extraction.get(\"extraction_method\", \"\"),\n            \"num_connected_files\": len(connected_files),\n            \"num_dataflow_paths\": len(extraction.get(\"dataflow_paths\", [])),\n            \"neg_strategies\": neg_strategies,\n        },\n    }\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Build contrastive training data from data-flow extractions\"\n    )\n    parser.add_argument(\"--dataflow-dir\", required=True,\n                        help=\"Directory containing all.jsonl from extract_dataflow.py\")\n    parser.add_argument(\"--repos-dir\", required=True,\n                        help=\"Root directory containing all repos\")\n    parser.add_argument(\"--output-file\", required=True,\n                        help=\"Output JSONL path\")\n    parser.add_argument(\"--num-negatives\", type=int, default=7)\n    parser.add_argument(\"--hard-negative-ratio\", type=float, default=0.5)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    args = parser.parse_args()\n\n    random.seed(args.seed)\n    np.random.seed(args.seed)\n\n    # Load extractions\n    dataflow_path = os.path.join(args.dataflow_dir, \"all.jsonl\")\n    extractions = []\n    with open(dataflow_path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                extractions.append(json.loads(line))\n    log.info(\"Loaded %d extractions\", len(extractions))\n\n    # Group by repo for BM25 index sharing\n    by_repo: dict[str, list[dict]] = defaultdict(list)\n    for ext in extractions:\n        by_repo[ext[\"repo_path\"]].append(ext)\n\n    training_instances = []\n\n    for repo_path, repo_extractions in by_repo.items():\n        log.info(\"Building training data for %s (%d instances)\", repo_path, len(repo_extractions))\n\n        all_files = collect_repo_files(repo_path)\n        if not all_files:\n            log.warning(\"No .py files in %s, skipping\", repo_path)\n            continue\n\n        # Cache file contents\n        file_contents: dict[str, str] = {}\n        for fp in all_files:\n            content = read_file_content(repo_path, fp)\n            if content:\n                file_contents[fp] = content\n\n        # Build BM25 index over repo files\n        doc_list = [file_contents.get(f, \"\") for f in all_files]\n        bm25_index = build_bm25_index(doc_list)\n\n        for ext in repo_extractions:\n            inst = build_instance(\n                ext, args.repos_dir, bm25_index, all_files, file_contents,\n                args.num_negatives, args.hard_negative_ratio,\n            )\n            if inst:\n                training_instances.append(inst)\n\n    # Normalize features\n    training_instances = normalize_features(training_instances)\n\n    # Write output\n    os.makedirs(os.path.dirname(os.path.abspath(args.output_file)), exist_ok=True)\n    with open(args.output_file, \"w\") as f:\n        for inst in training_instances:\n            f.write(json.dumps(inst, ensure_ascii=False) + \"\\n\")\n\n    # Statistics\n    total = len(training_instances)\n    inter_proc = sum(1 for i in training_instances if i[\"metadata\"][\"inter_procedural\"])\n    avg_pos_files = np.mean([i[\"metadata\"][\"num_connected_files\"] for i in training_instances]) if total else 0\n    hard_neg_count = sum(\n        sum(1 for s in i[\"metadata\"][\"neg_strategies\"] if s == \"bm25_hard\")\n        for i in training_instances\n    )\n    total_neg = sum(len(i[\"neg_codes\"]) for i in training_instances)\n\n    log.info(\"=\" * 60)\n    log.info(\"Training data built: %d instances\", total)\n    log.info(\"  Avg connected files/instance: %.1f\", avg_pos_files)\n    log.info(\"  Hard negative ratio:          %.2f\", hard_neg_count / max(total_neg, 1))\n    log.info(\"  Inter-procedural ratio:       %.2f\", inter_proc / max(total, 1))\n    log.info(\"  Output: %s\", args.output_file)\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-12T10:04:39.830869+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction/build_training_data.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_extraction_skeleton_20260512T100103",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-12T10:04:39.831034+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_extraction_skeleton_20260512T100103",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-12T10:04:39.831168+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_extraction_skeleton_20260512T100103",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-12T10:04:39.831293+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "StructFuse extraction module",
  "type": "intermediate",
  "description": "Stage 1 data extraction code skeleton: CodeQL queries (call_graph.ql, bounded_dataflow.ql), extract_dataflow.py (CodeQL+Beniget pipeline), build_training_data.py (contrastive training data builder)",
  "project": "faith-evidence-ie",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction",
  "tags": "['structfuse', 'stage1', 'codeql', 'extraction', 'code']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_extraction_skeleton_20260512T100103",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "StructFuse extraction module",
    "type": "intermediate",
    "description": "Stage 1 data extraction code skeleton: CodeQL queries (call_graph.ql, bounded_dataflow.ql), extract_dataflow.py (CodeQL+Beniget pipeline), build_training_data.py (contrastive training data builder)",
    "project": "faith-evidence-ie",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction",
    "tags": "['structfuse', 'stage1', 'codeql', 'extraction', 'code']"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-12T10:04:39.831424+00:00_

Error executing tool register_artifact: [Errno 21] Is a directory: '/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_extraction_skeleton_20260512T100103",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-12T10:04:39.831546+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "StructFuse call_graph.ql",
  "type": "intermediate",
  "description": "CodeQL query for 2-hop call graph extraction from buggy function (Phase 1a)",
  "project": "faith-evidence-ie",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction/codeql_queries/call_graph.ql",
  "tags": "['structfuse', 'stage1', 'codeql']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_extraction_skeleton_20260512T100103",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "StructFuse call_graph.ql",
    "type": "intermediate",
    "description": "CodeQL query for 2-hop call graph extraction from buggy function (Phase 1a)",
    "project": "faith-evidence-ie",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction/codeql_queries/call_graph.ql",
    "tags": "['structfuse', 'stage1', 'codeql']"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-12T10:04:39.831737+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260512_a7cf03\", \"name\": \"StructFuse call_graph.ql\", \"type\": \"intermediate\", \"description\": \"CodeQL query for 2-hop call graph extraction from buggy function (Phase 1a)\", \"path\": \"projects/faith-evidence-ie/artifacts/_project/intermediate/call_graph.ql\", \"url\": null, \"project\": \"faith-evidence-ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-12T10:04:17.924200+00:00\", \"tags\": [\"structfuse\", \"stage1\", \"codeql\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_extraction_skeleton_20260512T100103",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-12T10:04:39.831876+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "StructFuse bounded_dataflow.ql",
  "type": "intermediate",
  "description": "CodeQL query for scope-bounded inter-procedural data-flow analysis (Phase 1b)",
  "project": "faith-evidence-ie",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction/codeql_queries/bounded_dataflow.ql",
  "tags": "['structfuse', 'stage1', 'codeql', 'dataflow']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_extraction_skeleton_20260512T100103",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "StructFuse bounded_dataflow.ql",
    "type": "intermediate",
    "description": "CodeQL query for scope-bounded inter-procedural data-flow analysis (Phase 1b)",
    "project": "faith-evidence-ie",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction/codeql_queries/bounded_dataflow.ql",
    "tags": "['structfuse', 'stage1', 'codeql', 'dataflow']"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-12T10:04:39.832038+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260512_99f4ec\", \"name\": \"StructFuse bounded_dataflow.ql\", \"type\": \"intermediate\", \"description\": \"CodeQL query for scope-bounded inter-procedural data-flow analysis (Phase 1b)\", \"path\": \"projects/faith-evidence-ie/artifacts/_project/intermediate/bounded_dataflow.ql\", \"url\": null, \"project\": \"faith-evidence-ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-12T10:04:19.846492+00:00\", \"tags\": [\"structfuse\", \"stage1\", \"codeql\", \"dataflow\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_extraction_skeleton_20260512T100103",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-12T10:04:39.832191+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "StructFuse extract_dataflow.py",
  "type": "intermediate",
  "description": "Main extraction pipeline: CodeQL 2-phase analysis with Beniget fallback, multiprocessing parallel, JSONL output",
  "project": "faith-evidence-ie",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction/extract_dataflow.py",
  "tags": "['structfuse', 'stage1', 'extraction', 'pipeline']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_extraction_skeleton_20260512T100103",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "StructFuse extract_dataflow.py",
    "type": "intermediate",
    "description": "Main extraction pipeline: CodeQL 2-phase analysis with Beniget fallback, multiprocessing parallel, JSONL output",
    "project": "faith-evidence-ie",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction/extract_dataflow.py",
    "tags": "['structfuse', 'stage1', 'extraction', 'pipeline']"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-12T10:04:39.832338+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260512_21d6b6\", \"name\": \"StructFuse extract_dataflow.py\", \"type\": \"intermediate\", \"description\": \"Main extraction pipeline: CodeQL 2-phase analysis with Beniget fallback, multiprocessing parallel, JSONL output\", \"path\": \"projects/faith-evidence-ie/artifacts/_project/intermediate/extract_dataflow.py\", \"url\": null, \"project\": \"faith-evidence-ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-12T10:04:22.339431+00:00\", \"tags\": [\"structfuse\", \"stage1\", \"extraction\", \"pipeline\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_extraction_skeleton_20260512T100103",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-12T10:04:39.832472+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "StructFuse build_training_data.py",
  "type": "intermediate",
  "description": "Contrastive training data builder: BM25 hard negatives, feature vectors, HuggingFace-compatible JSONL output",
  "project": "faith-evidence-ie",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction/build_training_data.py",
  "tags": "['structfuse', 'stage1', 'training-data', 'contrastive']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_extraction_skeleton_20260512T100103",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "StructFuse build_training_data.py",
    "type": "intermediate",
    "description": "Contrastive training data builder: BM25 hard negatives, feature vectors, HuggingFace-compatible JSONL output",
    "project": "faith-evidence-ie",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/code/extraction/build_training_data.py",
    "tags": "['structfuse', 'stage1', 'training-data', 'contrastive']"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-12T10:04:39.832646+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260512_51f682\", \"name\": \"StructFuse build_training_data.py\", \"type\": \"intermediate\", \"description\": \"Contrastive training data builder: BM25 hard negatives, feature vectors, HuggingFace-compatible JSONL output\", \"path\": \"projects/faith-evidence-ie/artifacts/_project/intermediate/build_training_data.py\", \"url\": null, \"project\": \"faith-evidence-ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-12T10:04:23.854442+00:00\", \"tags\": [\"structfuse\", \"stage1\", \"training-data\", \"contrastive\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_extraction_skeleton_20260512T100103",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-12T10:04:39.832841+00:00_

4 个文件已创建并注册。文件结构：

```
artifacts/code/extraction/
├── codeql_queries/
│   ├── call_graph.ql          # Phase 1a: 2-hop call graph (caller+callee 双向)
│   └── bounded_dataflow.ql    # Phase 1b: scope-bounded inter-procedural data-flow
├── extract_dataflow.py        # 主 pipeline: CodeQL → Beniget fallback → JSONL
└── build_training_data.py     # 对比训练数据: (query, pos, negatives) + 特征向量
```

各文件要点：

**call_graph.ql** — 通过 external predicate 接收 buggy function 位置，用 points-to 分析解析调用关系，手动展开 2 层（`hop1`/`hop2` predicates），输出函数名、hop distance、方向、文件路径和行号。

**bounded_dataflow.ql** — 使用 module-based `DataFlow::ConfigSig` 配置，sources 限制为 `inScopeFunction` 的 parameters 和 return values，sinks 限制为同范围函数的 variable reads。`@timeout 300` / `@ram 8192` pragma 控制资源。`@kind path-problem` 获取完整路径。

**extract_dataflow.py** — `multiprocessing.Pool` 并行处理 repos；每个 repo 依次创建 CodeQL DB → 运行 call_graph.ql → 检查 reachable files ≥ min_reachable_files → 运行 bounded_dataflow.ql；失败时 fallback 到 `beniget` 做 intra-file def-use；输出带 `inter_procedural` 标记的 JSONL。

**build_training_data.py** — 按 repo 分组构建 BM25 索引；hard negatives = BM25 高分但 data-flow 不可达；特征向量含 dataflow_distance / path_count / dependency_type / bm25_score / inter_procedural；全局 min-max 归一化；输出 HuggingFace datasets 兼容格式。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_extraction_skeleton_20260512T100103"
}
```

</details>

---
