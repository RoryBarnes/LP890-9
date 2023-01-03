Thermal/Magnetic Evolution of LP 890-9 b/c's Interior
======================================================

===================   ============
**Date**              12/20/2022
**Modules**           RadHeat, ThermInt, EqTide
**Approx. runtime**   1 minute per trial
===================   ============


In this folder, we model the evolution of the interior and total heat budget
for the two known plants in the LP 890-9 system. We provide summary files of the
intergrations run in the folder /DataSummaryFiles, or the user can re-run the 
integrations and re-generate the files. The summary files are used in MakeFigures.ipynb
to make the figures included in the paper draft. 

To run one case
-------------------

.. code-block:: bash

   vplanet vpl.in

To run the full parameter sweep 
-------------------

.. code-block:: bash

   vspace VSPACE.in
   multiplanet -c 2 VSPACE.in &
   
Then use the Jupyter notebook to plot the results. Reading the files in may take a while. 
   
