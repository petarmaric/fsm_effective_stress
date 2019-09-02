About
=====

Python library that uses the rheological-dynamical analogy (RDA) to compute
damage and effective buckling stress in prismatic shell structures.

This work is a part of the investigation within the research project
[ON174027]_, supported by the Ministry for Science and Technology, Republic of
Serbia. This support is gratefully acknowledged.

References
----------

.. [ON174027]
   "Computational Mechanics in Structural Engineering"

Installation
============

To install fsm_effective_stress run::

    $ pip install fsm_effective_stress

Usage examples
==============

Quick start::

    >>> from fsm_effective_stress import compute_damage, compute_effective_stress

    >>> omega =  103.9167 # [rad/s] natural frequency for undamaged state of structure
    >>> omega_d = 60.0179 # [rad/s] natural frequency for damaged state of structure
    >>> sigma_d = 19.4754 # [MPa] buckling stress for damaged state of structure

    # [no unit] damage variable
    >>> print "%.4f" % compute_damage(omega, omega_d)
    0.6664

    # [MPa] effective buckling stress
    >>> print "%.4f" % compute_effective_stress(omega, omega_d, sigma_d)
    58.3842

Please see the `fsm_damage_analysis`_ source code for more examples.

.. _`fsm_damage_analysis`: https://github.com/petarmaric/fsm_damage_analysis

Contribute
==========

If you find any bugs, or wish to propose new features `please let us know`_.

If you'd like to contribute, simply fork `the repository`_, commit your changes
and send a pull request. Make sure you add yourself to `AUTHORS`_.

.. _`please let us know`: https://github.com/petarmaric/fsm_effective_stress/issues/new
.. _`the repository`: https://github.com/petarmaric/fsm_effective_stress
.. _`AUTHORS`: https://github.com/petarmaric/fsm_effective_stress/blob/master/AUTHORS
