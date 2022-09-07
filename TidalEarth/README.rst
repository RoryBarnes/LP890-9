Thermal/Magnetic Evolution of LP 890-9 c's Interior
======================================================

===================   ============
**Date**              09/14/2022
**Modules**           RadHeat, ThermInt, EqTide
**Approx. runtime**   xx minutes
===================   ============

TODO:

1. Modify sun.in to match LP 890-9's properties
2. Modify tidalearth.in to match planet c's properties
3. Switch sTideModel to either CPL or CTL 
4. Try different cases with different tidal Q's and radiogenic inventories
5. Switch to stagnant lid and try planet b (maybe new subdir?)


To run this example
-------------------

.. code-block:: bash

   python makeplot.py <pdf | png>


Expected output
---------------

.. figure:: TidalEarth1.png
.. figure:: TidalEarth2.png
   :width: 600px
   :align: center

Caption
