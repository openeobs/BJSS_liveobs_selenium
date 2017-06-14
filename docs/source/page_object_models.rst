Page Object Models
==================
Page Object Models provide methods to interact with the pages they represent
for instance using the Data Entry Page Object Model provides methods to fill
out the observation form.

All Mobile Page Object Models are subclasses of ``BaseMobilePage`` which
provides methods for going to the various mobile pages as well as common
interaction patterns such as clicking a button and waiting for a particular
element to become visible/invisible to verify the intended action has worked.

.. toctree::
   :maxdepth: 2
   :caption: Page Object Models:
   :glob:

   page_object_models/mobile/common
   page_object_models/desktop/common

Common Methods:
---------------

.. autoclass:: liveobs_ui.page_object_models.common.base_liveobs_page.BaseLiveObsPage
   :members:
