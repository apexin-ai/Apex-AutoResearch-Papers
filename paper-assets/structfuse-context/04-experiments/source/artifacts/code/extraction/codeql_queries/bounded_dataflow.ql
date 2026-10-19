/**
 * @name Scope-bounded inter-procedural data-flow analysis
 * @description Tracks data-flow from parameters/return values of functions within
 *              2 call-graph hops of the buggy function to variable reads in the same
 *              scope. Sources and sinks are restricted BEFORE evaluation to prevent
 *              Cartesian-product blowup.
 * @kind path-problem
 * @id structfuse/bounded-dataflow
 * @problem.severity recommendation
 * @precision medium
 * @tags structfuse data-flow inter-procedural
 * @timeout 300
 * @ram 8192
 */

import python
import semmle.python.dataflow.new.DataFlow
import semmle.python.dataflow.new.TaintTracking
import semmle.python.pointsto.PointsTo
import semmle.python.ApiGraphs

// -- Reuse call-graph scope predicates --

external string buggyFunctionName();
external string buggyFileName();

predicate isBuggyFunction(Function f) {
  f.getName() = buggyFunctionName() and
  f.getLocation().getFile().getRelativePath() = buggyFileName()
}

predicate directCallEdge(Function caller, Function callee) {
  exists(CallNode call |
    call.getScope() = caller and
    (
      exists(FunctionObject fo |
        call.getFunction().pointsTo(fo) and
        fo.getFunction() = callee
      )
      or
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

predicate hop1(Function f) {
  exists(Function buggy |
    isBuggyFunction(buggy) and
    (directCallEdge(buggy, f) or directCallEdge(f, buggy))
  )
}

predicate hop2(Function f) {
  exists(Function mid |
    hop1(mid) and
    (directCallEdge(mid, f) or directCallEdge(f, mid)) and
    not isBuggyFunction(f) and
    not hop1(f)
  )
}

/** Function is within 2 call-graph hops of the buggy function. */
predicate inScopeFunction(Function f) {
  isBuggyFunction(f) or hop1(f) or hop2(f)
}

// -- Scope-bounded data-flow configuration --

module BoundedFlowConfig implements DataFlow::ConfigSig {
  /**
   * Sources: parameters and return values of in-scope functions only.
   * This bounds the analysis BEFORE evaluation, preventing blowup.
   */
  predicate isSource(DataFlow::Node node) {
    // Function parameters within scope
    exists(Function f, Parameter p |
      inScopeFunction(f) and
      p = f.getAnArg() and
      node.asExpr() = p.asName().getAFlowNode()
    )
    or
    // Return values of in-scope functions (at call sites)
    exists(Function f, CallNode call |
      inScopeFunction(f) and
      exists(FunctionObject fo |
        fo.getFunction() = f and
        call.getFunction().pointsTo(fo)
      ) and
      node.asCfgNode() = call
    )
  }

  /**
   * Sinks: variable reads within in-scope functions.
   */
  predicate isSink(DataFlow::Node node) {
    exists(Function f, NameNode nameRead |
      inScopeFunction(f) and
      nameRead.getScope() = f and
      nameRead.isLoad() and
      node.asCfgNode() = nameRead
    )
  }
}

module BoundedFlow = DataFlow::Global<BoundedFlowConfig>;

import BoundedFlow::PathGraph

from BoundedFlow::PathNode source, BoundedFlow::PathNode sink, int pathLength
where
  BoundedFlow::flowPath(source, sink) and
  // Call-graph hop distance: same function=0, direct call edge=1, otherwise=2
  pathLength =
    if source.getNode().getEnclosingCallable() = sink.getNode().getEnclosingCallable()
    then 0
    else if exists(Function sf, Function tf |
      sf.getName() = source.getNode().getEnclosingCallable().getName() and
      tf.getName() = sink.getNode().getEnclosingCallable().getName() and
      sf.getLocation().getFile().getRelativePath() = source.getNode().getLocation().getFile().getRelativePath() and
      tf.getLocation().getFile().getRelativePath() = sink.getNode().getLocation().getFile().getRelativePath() and
      (directCallEdge(sf, tf) or directCallEdge(tf, sf))
    )
    then 1
    else 2
select
  sink.getNode(),
  source,
  sink,
  source.getNode().getLocation().getFile().getRelativePath() as source_file,
  source.getNode().getEnclosingCallable().getName() as source_func,
  source.getNode().getLocation().getStartLine() as source_line,
  sink.getNode().getLocation().getFile().getRelativePath() as sink_file,
  sink.getNode().getEnclosingCallable().getName() as sink_func,
  sink.getNode().getLocation().getStartLine() as sink_line,
  pathLength as path_length
