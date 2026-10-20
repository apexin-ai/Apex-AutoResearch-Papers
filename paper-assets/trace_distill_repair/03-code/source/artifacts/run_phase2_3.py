"""Phase 2+3 only: trace collection and segmentation on existing instances."""
import json
import logging
import os
import sys

sys.path.insert(0, "/root/trace_distill_repair")

from trace_collector import TraceCollector
from structural_segmenter import StructuralSegmenter
from line_segmenter import LineSegmenter
from dtd_types import serialize_segment, serialize_event
from bugsinpy_setup import BugsInPySetup

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s",
                    handlers=[logging.StreamHandler(sys.stdout)])
logger = logging.getLogger(__name__)
sys.stdout.reconfigure(line_buffering=True)

WORKSPACE = "/root/trace_distill_repair/bugsinpy_workspace"
OUTPUT_DIR = "/root/trace_distill_repair/pipeline_output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

setup = BugsInPySetup(workspace_dir=WORKSPACE)
setup._ensure_repo()

# Gather ready instances
instances = []
for project, bug_id, desc in setup.CANDIDATE_BUGS:
    key = f"{project}_{bug_id}"
    buggy_dir = os.path.join(WORKSPACE, "instances", key, "buggy")
    if not os.path.isdir(buggy_dir) or not os.path.isdir(os.path.join(buggy_dir, ".git")):
        logger.info("SKIP %s (not set up)", key)
        continue
    bug_dir = os.path.join(setup.repo_dir, "projects", project, "bugs", str(bug_id))
    bug_info = setup._read_bug_info(bug_dir)
    test_file = bug_info.get("test_file", "")
    test_cmd = bug_info.get("test_command", "")
    if not test_cmd:
        if test_file:
            # test_file can be semicolon-separated
            files = test_file.replace(";", " ")
            test_cmd = f"python -m pytest {files}"
        else:
            test_cmd = "python -m pytest"

    instances.append({
        "project": project, "bug_id": bug_id,
        "buggy_dir": buggy_dir, "test_command": test_cmd, "bug_info": bug_info,
    })

logger.info("Found %d ready instances", len(instances))

# Phase 2: Trace collection
collector = TraceCollector()
trace_results = {"success": [], "failed": [], "traces": {}}

logger.info("=== PHASE 2: Collecting traces for %d instances ===", len(instances))
for inst in instances:
    key = f"{inst['project']}_{inst['bug_id']}"
    buggy_dir = inst["buggy_dir"]
    test_cmd = inst["test_command"]
    try:
        main_py = None
        for root, dirs, files in os.walk(buggy_dir):
            if ".git" in dirs:
                dirs.remove(".git")
            for f in sorted(files):
                if f.endswith(".py") and not f.startswith("test_") and f != "setup.py":
                    main_py = os.path.join(root, f)
                    break
            if main_py:
                break

        if not main_py:
            trace_results["failed"].append({"key": key, "error": "No Python file found"})
            logger.error("FAIL trace %s: no Python file", key)
            continue

        events = collector.collect(main_py, test_cmd, timeout=120, project_root=buggy_dir)

        if events:
            trace_results["success"].append(key)
            trace_results["traces"][key] = events
            trace_file = os.path.join(OUTPUT_DIR, f"{key}_trace.json")
            with open(trace_file, "w") as f:
                json.dump([serialize_event(e) for e in events], f)
            logger.info("OK trace %s: %d events", key, len(events))
        else:
            trace_results["failed"].append({"key": key, "error": "No events collected"})
            logger.warning("FAIL trace %s: 0 events", key)
    except Exception as e:
        trace_results["failed"].append({"key": key, "error": str(e)[:200]})
        logger.error("FAIL trace %s: %s", key, str(e)[:200])

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

        seg_results["line"][key] = {"num_segments": len(l_segs)}

        s_file = os.path.join(OUTPUT_DIR, f"{key}_structural_segments.json")
        l_file = os.path.join(OUTPUT_DIR, f"{key}_line_segments.json")
        with open(s_file, "w") as f:
            json.dump([serialize_segment(s) for s in s_segs], f)
        with open(l_file, "w") as f:
            json.dump([serialize_segment(s) for s in l_segs], f)

        logger.info("OK seg %s: structural=%d, line=%d", key, len(s_segs), len(l_segs))
    except Exception as e:
        logger.error("FAIL seg %s: %s", key, e)

# Summary
summary = {
    "phase1_setup": {"total": 45, "success": len(instances), "failed": 45 - len(instances)},
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

with open(os.path.join(OUTPUT_DIR, "summary.json"), "w") as f:
    json.dump(summary, f, indent=2)

logger.info("=== FINAL SUMMARY ===")
logger.info("Phase 1: %d/45 instances ready", len(instances))
logger.info("Phase 2: %d/%d traces collected", len(trace_results["success"]), len(instances))
if trace_results["traces"]:
    avg_events = sum(len(v) for v in trace_results["traces"].values()) / len(trace_results["traces"])
    logger.info("Avg trace events: %.0f", avg_events)
logger.info("Phase 3: %d structural, %d line", len(seg_results["structural"]), len(seg_results["line"]))
logger.info("Output: %s", OUTPUT_DIR)
