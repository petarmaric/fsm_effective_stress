__version__ = '1.0.1'


def compute_damage(omega, omega_d):
    return 1 - (omega_d/omega)**2

def compute_effective_stress(omega, omega_d, sigma_d):
    return sigma_d * (omega/omega_d)**2
