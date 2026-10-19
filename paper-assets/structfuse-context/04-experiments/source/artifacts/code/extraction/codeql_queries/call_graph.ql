/**
 * @name 2-hop call graph extraction from buggy function
 * @description Extracts all functions within 2 call-graph hops (both caller and callee
 *              directions) of a specified buggy function. Outputs JSON-compatible tuples
 *              for downstream scope-bounded data-flow analysis.
 * @kind problem
 * @id structfuse/call-graph-2hop
 * @problem.severity recommendation
 * @precision medium
 * @tags structfuse call-graph extraction
 */

import python
import semmle.python.pointsto.PointsTo

// Buggy function location injected via external predicates (populated by CLI --external).
// Usage: codeql database analyze ... --external buggyFunctionName=<name> --external buggyFileName=<relpath>
external string buggyFunctionName();
external string buggyFileName();

/**
 * Matches the single buggy function specified by external predicates.
 */
predicate isBuggyFunction(Function f) {
  f.getName() = buggyFunctionName() and
  f.getLocation().getFile().getRelativePath() = buggyFileName()
}

/**
 * Direct call edge: `caller` contains a call site that resolves to `callee`.
 * Uses points-to analysis for call target resolution where available,
 * falls back to name-based matching for unresolved calls.
 */
predicate directCallEdge(Function caller, Function callee) {
  exists(CallNode call |
    call.getScope() = caller and
    (
      // Points-to resolved: call target is known
      exists(FunctionObject fo |
        call.getFunction().pointsTo(fo) and
        fo.getFunction() = callee
      )
      or
      // Name-based fallback for unresolved calls within the same module
      exists(NameNode nameNode |
        call.getFunction() = nameNode and
        callee.getName() = nameNode.getId() and
        callee.getEnclosingModule() = caller.getEnclosingModule() and
        not exists(FunctionObject fo | call.getFunction().pointsTo(fo))
      )
    )
  ) and
  caller != callee
}

/**
 * 1-hop: functions directly called by or calling the buggy function.
 */
predicate hop1(Function f, string direction) {
  exists(Function buggy |
    isBuggyFunction(buggy) and
    (
      directCallEdge(buggy, f) and direction = "callee"
      or
      directCallEdge(f, buggy) and direction = "caller"
    )
  )
}

/**
 * 2-hop: functions one additional step from any 1-hop function.
 */
predicate hop2(Function f, string direction) {
  exists(Function mid |
    hop1(mid, _) and
    (
      directCallEdge(mid, f) and direction = "callee"
      or
      directCallEdge(f, mid) and direction = "caller"
    ) and
    not isBuggyFunction(f) and
    not hop1(f, _)
  )
}

/**
 * All functions within 2 hops, with hop distance and direction.
 */
predicate inScope(Function f, int hopDistance, string direction) {
  isBuggyFunction(f) and hopDistance = 0 and direction = "origin"
  or
  hop1(f, direction) and hopDistance = 1
  or
  hop2(f, direction) and hopDistance = 2
}

from Function f, int hopDistance, string direction, File file, int startLine, int endLine
where
  inScope(f, hopDistance, direction) and
  file = f.getLocation().getFile() and
  startLine = f.getLocation().getStartLine() and
  endLine = f.getLocation().getEndLine()
select
  f.getName() as target_func,
  hopDistance as hop_distance,
  direction,
  file.getRelativePath() as file_path,
  startLine as start_line,
  endLine as end_line
