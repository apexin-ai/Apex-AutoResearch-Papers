"""Unit tests for the collapse-aware PI controller."""

import unittest
from controller import ControllerConfig, CollapseAwareController


class TestSteadyState(unittest.TestCase):
    """r_t == r_target every step → w should stay at w_init."""

    def test_constant_at_target(self):
        cfg = ControllerConfig(r_target=50.0, w_init=0.5)
        ctrl = CollapseAwareController(cfg)

        for _ in range(20):
            w = ctrl.step(50.0)

        self.assertAlmostEqual(w, 0.5, places=10)

    def test_no_drift_over_many_steps(self):
        cfg = ControllerConfig(r_target=80.0, w_init=0.3)
        ctrl = CollapseAwareController(cfg)

        for _ in range(100):
            w = ctrl.step(80.0)

        self.assertAlmostEqual(w, 0.3, places=10)


class TestRankDrop(unittest.TestCase):
    """Decreasing rank → w should increase (more real data)."""

    def test_monotonic_drop_increases_w(self):
        cfg = ControllerConfig(Kp=0.01, Ki=0.005, r_target=50.0, w_init=0.5)
        ctrl = CollapseAwareController(cfg)

        ranks = [50.0, 48.0, 46.0, 44.0, 42.0, 40.0]
        ws = []
        for r in ranks:
            ws.append(ctrl.step(r))

        for i in range(2, len(ws)):
            self.assertGreater(ws[i], ws[i - 1],
                               f"w should increase as rank drops: step {i}")

    def test_large_drop_produces_larger_response(self):
        cfg = ControllerConfig(Kp=0.01, Ki=0.005, r_target=50.0, w_init=0.5)

        ctrl_small = CollapseAwareController(cfg)
        ctrl_small.step(50.0)
        w_small = ctrl_small.step(48.0)

        ctrl_large = CollapseAwareController(cfg)
        ctrl_large.step(50.0)
        w_large = ctrl_large.step(40.0)

        self.assertGreater(w_large, w_small)


class TestRankRecovery(unittest.TestCase):
    """Rank drops then recovers → w should return toward w_init."""

    def test_recovery_reduces_w(self):
        cfg = ControllerConfig(Kp=0.01, Ki=0.005, r_target=50.0, w_init=0.5)
        ctrl = CollapseAwareController(cfg)

        drop = [50.0, 45.0, 40.0, 35.0]
        for r in drop:
            ctrl.step(r)

        w_peak = ctrl.get_state()["w"]
        self.assertGreater(w_peak, 0.5)

        recover = [40.0, 45.0, 50.0, 50.0, 50.0, 50.0, 50.0]
        ws_recover = []
        for r in recover:
            ws_recover.append(ctrl.step(r))

        self.assertLess(ws_recover[-1], w_peak,
                        "w should decrease as rank recovers")


class TestClamp(unittest.TestCase):
    """w must stay within [w_min, w_max] under extreme inputs."""

    def test_clamp_upper(self):
        cfg = ControllerConfig(Kp=0.5, Ki=0.5, r_target=100.0, w_init=0.5,
                               w_min=0.1, w_max=0.9)
        ctrl = CollapseAwareController(cfg)

        for r in [100.0, 10.0, 1.0, 0.1, 0.01]:
            w = ctrl.step(r)
            self.assertLessEqual(w, cfg.w_max)

    def test_clamp_lower(self):
        cfg = ControllerConfig(Kp=0.5, Ki=0.5, r_target=10.0, w_init=0.5,
                               w_min=0.1, w_max=0.9)
        ctrl = CollapseAwareController(cfg)

        for r in [10.0, 100.0, 200.0, 500.0, 1000.0]:
            w = ctrl.step(r)
            self.assertGreaterEqual(w, cfg.w_min)

    def test_clamp_both_bounds(self):
        cfg = ControllerConfig(Kp=1.0, Ki=1.0, r_target=50.0, w_init=0.5,
                               w_min=0.2, w_max=0.8)
        ctrl = CollapseAwareController(cfg)

        for r in [50.0, 0.0, 0.0, 0.0]:
            w = ctrl.step(r)
        self.assertAlmostEqual(w, 0.8)

        ctrl.reset()
        for r in [50.0, 500.0, 500.0, 500.0]:
            w = ctrl.step(r)
        self.assertAlmostEqual(w, 0.2)


class TestReset(unittest.TestCase):
    """reset() restores initial state."""

    def test_reset_restores_state(self):
        cfg = ControllerConfig(r_target=50.0, w_init=0.6)
        ctrl = CollapseAwareController(cfg)

        for r in [50.0, 40.0, 30.0]:
            ctrl.step(r)

        self.assertNotEqual(ctrl.get_state()["w"], cfg.w_init)
        self.assertGreater(ctrl.get_state()["step_count"], 0)

        ctrl.reset()
        state = ctrl.get_state()
        self.assertEqual(state["w"], cfg.w_init)
        self.assertEqual(state["step_count"], 0)
        self.assertEqual(state["proportional_term"], 0.0)
        self.assertEqual(state["integral_term"], 0.0)
        self.assertEqual(state["r_history"], [])
        self.assertEqual(state["w_history"], [cfg.w_init])

    def test_reset_then_step(self):
        cfg = ControllerConfig(r_target=50.0, w_init=0.5)
        ctrl = CollapseAwareController(cfg)

        for r in [50.0, 30.0, 20.0]:
            ctrl.step(r)
        ctrl.reset()

        w = ctrl.step(50.0)
        self.assertEqual(w, 0.5)


class TestHistory(unittest.TestCase):
    """get_state() correctly records history."""

    def test_r_history(self):
        cfg = ControllerConfig(r_target=50.0)
        ctrl = CollapseAwareController(cfg)

        ranks = [50.0, 48.0, 46.0, 44.0]
        for r in ranks:
            ctrl.step(r)

        self.assertEqual(ctrl.get_state()["r_history"], ranks)

    def test_w_history_length(self):
        cfg = ControllerConfig(r_target=50.0, w_init=0.5)
        ctrl = CollapseAwareController(cfg)

        ranks = [50.0, 48.0, 46.0]
        for r in ranks:
            ctrl.step(r)

        state = ctrl.get_state()
        # w_history: [w_init] + one entry per update step (first step is init, no append)
        self.assertEqual(state["w_history"][0], 0.5)
        self.assertEqual(len(state["w_history"]), len(ranks))

    def test_step_count(self):
        cfg = ControllerConfig(r_target=50.0)
        ctrl = CollapseAwareController(cfg)

        for r in [50.0, 45.0, 40.0]:
            ctrl.step(r)

        # first step is initialization (no update), next 2 are real steps
        self.assertEqual(ctrl.get_state()["step_count"], 2)

    def test_proportional_and_integral_terms(self):
        cfg = ControllerConfig(Kp=0.01, Ki=0.005, r_target=50.0)
        ctrl = CollapseAwareController(cfg)

        ctrl.step(50.0)  # init
        ctrl.step(45.0)  # rank dropped by 5, error = -5

        state = ctrl.get_state()
        # proportional: -Kp * (45-50) = -0.01 * (-5) = 0.05
        self.assertAlmostEqual(state["proportional_term"], 0.05)
        # integral: -Ki * (45-50) = -0.005 * (-5) = 0.025
        self.assertAlmostEqual(state["integral_term"], 0.025)


if __name__ == "__main__":
    unittest.main()
