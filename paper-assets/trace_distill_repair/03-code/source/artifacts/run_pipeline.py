"""Driver script: BugsInPy setup -> trace collection -> segmentation."""
import json
import logging
import os
import sys
import time
import traceback

sys.path.insert(0, "/root/trace_distill_repair")

from bugsinpy_setup import BugsInPySetup
from trace_collector import TraceCollector
from structural_segmenter import StructuralSegmenter
from line_segmenter import LineSegmenter
from dtd_types import serialize_segment

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

WORKSPACE = "/root/trace_distill_repair/bugsinpy_workspace"
OUTPUT_DIR = "/root/trace_distill_repair/pipeline_output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Phase 1: Setup BugsInPy instances
setup = BugsInPySetup(workspace_dir=WORKSPACE)
instances = []
setup_results = {"success": [], "failed": []}

logger.info("=== PHASE 1: Setting up %d BugsInPy instances ===", len(setup.CANDIDATE_BUGS))
for project, bug_id, desc in setup.CANDIDATE_BUGS:
    key = f"{project}_{bug_id}"
    try:
        instance = setup.setup_instance(project, bug_id)
        instances.append(instance)
        setup_results["success"].append(key)
        logger.info("OK: %s", key)
    except Exception as e:
        setup_results["failed"].append({"key": key, "error": str(e)})
        logger.error("FAIL: %s -> %s", key, e)

logger.info("Phase 1 done: %d/%d success", len(setup_results["success"]), len(setup.CANDIDATE_BUGS))

# Phase 2: Trace collection
collector = TraceCollector(max_events=50000, max_depth=30)
trace_results = {"success": [], "failed": [], "traces": {}}

logger.info("=== PHASE 2: Collecting traces for %d instances ===", len(instances))
for inst in instances:
    key = f"{inst['project']}_{inst['bug_id']}"
    try:
        code_path = inst.get("buggy_dir", "")
        test_cmd = inst.get("test_command", "python -m pytest")

        # Find a python file in buggy_dir to use as code_path
        buggy_dir = inst["buggy_dir"]
        main_py = None
        for root, dirs, files in os.walk(buggy_dir):
            dirs[:] = [d for d in dirs if d not in (".git", "__pycache__", ".tox", "venv", "node_modules")]
            for f in sorted(files):
                if f.endswith(".py") and not f.startswith("test_") and f != "setup.py":
                    main_py = os.path.join(root, f)
                    break
            if main_py:
                break

        if not main_py:
            trace_results["failed"].append({"key": key, "error": "No Python file found in buggy_dir"})
            logger.error("FAIL trace %s: no Python file", key)
            continue

        events = collector.collect(main_py, test_cmd, timeout=120)

        if events:
            trace_results["success"].append(key)
            trace_results["traces"][key] = events
            # Save raw trace
            trace_file = os.path.join(OUTPUT_DIR, f"{key}_trace.json")
            with open(trace_file, "w") as f:
                json.dump([{
                    "event_type": e.event_type,
                    "function_name": e.function_name,
                    "filename": e.filename,
                    "lineno": e.lineno,
                    "call_depth": e.call_depth,
                } for e in events], f, indent=2)
            logger.info("OK trace %s: %d events", key, len(events))
        else:
            trace_results["failed"].append({"key": key, "error": "No events collected"})
            logger.warning("FAIL trace %s: 0 events", key)
    except Exception as e:
        trace_results["failed"].append({"key": key, "error": str(e)})
        logger.error("FAIL trace %s: %s", key, traceback.format_exc()[-300:])

logger.info("Phase 2 done: %d/%d success", len(trace_results["success"]), len(instances))

# Phase 3: Segmentation
struct_seg = StructuralSegmenter()
line_seg = LineSegmenter(window_size=5, stride=5)
seg_results = {"structural": {}, "line": {}}

logger.info("=== PHASE 3: Segmenting traces ===")
for key, events in trace_results["traces"].items():
    try:
        s_segs = struct_seg.segment(events)
        l_segs = line_seg.segment(events)

        seg_results["structural"][key] = {
            "num_segments": len(s_segs),
            "types": {},
        }
        for s in s_segs:
            t = s.segment_type
            seg_results["structural"][key]["types"][t] = seg_results["structural"][key]["types"].get(t, 0) + 1

        seg_results["line"][key] = {
            "num_segments": len(l_segs),
        }

        # Save segments
        s_file = os.path.join(OUTPUT_DIR, f"{key}_structural_segments.json")
        l_file = os.path.join(OUTPUT_DIR, f"{key}_line_segments.json")
        with open(s_file, "w") as f:
            json.dump([serialize_segment(s) for s in s_segs], f, indent=2)
        with open(l_file, "w") as f:
            json.dump([serialize_segment(s) for s in l_segs], f, indent=2)

        logger.info("OK seg %s: structural=%d, line=%d", key, len(s_segs), len(l_segs))
    except Exception as e:
        logger.error("FAIL seg %s: %s", key, e)

# Summary
summary = {
    "phase1_setup": {
        "total": len(setup.CANDIDATE_BUGS),
        "success": len(setup_results["success"]),
        "failed": len(setup_results["failed"]),
        "failed_list": setup_results["failed"],
    },
    "phase2_traces": {
        "total": len(instances),
        "success": len(trace_results["success"]),
        "failed": len(trace_results["failed"]),
        "failed_list": trace_results["failed"],
        "event_counts": {k: len(v) for k, v in trace_results["traces"].items()},
    },
    "phase3_segmentation": seg_results,
    "output_dir": OUTPUT_DIR,
}

summary_file = os.path.join(OUTPUT_DIR, "summary.json")
with open(summary_file, "w") as f:
    json.dump(summary, f, indent=2)

logger.info("=== SUMMARY ===")
logger.info("Phase 1: %d/%d instances set up", summary["phase1_setup"]["success"], summary["phase1_setup"]["total"])
logger.info("Phase 2: %d/%d traces collected", summary["phase2_traces"]["success"], summary["phase2_traces"]["total"])
logger.info("Phase 3: structural segments for %d instances, line segments for %d instances",
            len(seg_results["structural"]), len(seg_results["line"]))
logger.info("Output: %s", OUTPUT_DIR)
logger.info("Summary: %s", summary_file)
