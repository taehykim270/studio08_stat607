"""Specify the simulation design in one place."""
import numpy as np

def make_scenarios():
    """Return {scenario_id: settings} for different n

    IDs are unique, stable, filename-safe strings. Each settings dictionary
    has EXACTLY n (int), p (int), and 
    error_distribution ('normal').
    The study supplies all generation, fitting, evaluation, and replication.
    """
    n = 200
    scenarios = {}
    
    n_reps = 1
    for gamma in 10**np.linspace(-1, 1, 5000):
        p = max(1, round(n * gamma)) # Ensure p is at least 1
        scenarios[f"nreps_{n_reps:03d}_gamma_{gamma:.3f}"] = {
            "experiment": "A", "n": n, "p": p, "rho": 0.0, 
            "error_distribution": "normal", "n_reps": n_reps, "SNR": 5
        }

    # Case n = 50:
    n_reps = 50
    for gamma in 10**np.linspace(-1, 1, 100):
        p = max(1, round(n * gamma))
        scenarios[f"nreps_{n_reps:03d}_gamma_{gamma:.3f}"] = {
            "experiment": "A", "n": n, "p": p, "rho": 0.0, 
            "error_distribution": "normal", "n_reps": n_reps, "SNR": 5
        }

    # Case n = 1000:
    n_reps = 1000
    for gamma in [0.2, 0.5, 0.8, 2, 5]:
        p = max(1, round(n * gamma))
        scenarios[f"nreps_{n_reps:03d}_gamma_{gamma:.3f}"] = {
            "experiment": "A", "n": n, "p": p, "rho": 0.0, 
            "error_distribution": "normal", "n_reps": n_reps, "SNR": 5
        }
        
    return scenarios