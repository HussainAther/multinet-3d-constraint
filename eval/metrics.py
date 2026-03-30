def compute_metrics(success, violations, steps):
    return {
        "success": success,
        "violations": violations,
        "steps": steps
    }
