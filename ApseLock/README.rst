Apsidal Locking in the LP 890-9 System
=========================================

===================   ============
**Date**              9/14/22
**Modules**           DistOrb
                      EqTide
                      STELLAR
**Approx. runtime**   xxx seconds
===================   ============

TODO:

1. Modify sun.in to match LP 890-9's properties
2. Modify TGb.in and TGc.in to match planets b and c
3. Consider a range of initial eccentricities and longitudes of pericenter

To run this example
-------------------

.. code-block:: bash

    python makeplot.py <pdf | png>

Expected output
---------------

.. figure:: ApseLock.png
   :width: 300px
   :align: center

Caption
