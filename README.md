# CUED Part IA Flood Warning System

This is the Part IA Lent Term computing activity at the Department of
Engineering, University of Cambridge.

The activity is documented at
https://cued-partia-flood-warning.readthedocs.io/. Fork this repository
to start the activity.

Your team has been tasked with building the computational backend (library) to a new real-time flood warning system for England. The library should:

Fetch real-time river level data over the Internet from the Department for Environment Food and Rural Affairs data service.

Support specified data query types on river level monitoring stations.

Analyse monitoring station data in order to assess flood risks, and issue flood warnings for areas of the country.

The mandated development practices are listed in the Requirements section. The library is required to support specific query interfaces (API), as outlined in the Deliverables section, which form the public interface of the library. Another company has been contracted to build a user interface using the prescribed public interfaces to the library, hence they cannot be changed.

he system is to be built on the (near) real-time river level data at the nearly 2000 monitoring stations that is made available by the Department for Environment Food and Rural Affairs (DEFRA) at https://environment.data.gov.uk/. For most stations river level data is updated every 15 minutes. The data service is summarised at https://data.gov.uk/dataset/real-time-and-near-real-time-river-level-data1.

REST interface for data retrieval
Data is fetched from https://environment.data.gov.uk/ using a REST interface. With a suitably formed URL (a string), as defined in the service documentation, the server returns the requested data as a JSON object. JSON objects are represented in Python as data structures made up of dictionaries, lists and strings. JSON objects are straightforward to manipulate from Python. The interface to the DEFRA service is documented at https://environment.data.gov.uk/flood-monitoring/doc/reference.